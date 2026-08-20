"""
High-Precision Vector SVG Renderer for Mathematical Diagrams.
"""

from __future__ import annotations
import math
import html
import re
import numpy as np
from typing import List, Tuple
from ..core.models import (
    DiagramIR,
    Point,
    Segment,
    ParabolaCurve,
    ParametricCurve,
    Polygon,
    RightAngleMarker,
    ArcAngleMarker,
    MathLabel,
    ArrowType,
    StrokeStyle,
)
from ..solver.geometry_solver import GeometrySolver


class SVGRenderer:
    """
    Renders DiagramIR directly into high-fidelity, resolution-independent pure SVG XML.
    """

    def __init__(self, ir: DiagramIR):
        self.ir = ir

    def _format_math_text(self, text: str) -> str:
        """
        Converts LaTeX-style superscripts/subscripts and basic math into SVG-compatible XML.
        """
        escaped = html.escape(text)
        # Superscript ^2 or ^{...}
        def replace_sup(match):
            content = match.group(1) or match.group(2)
            return f'<tspan baseline-shift="super" font-size="70%">{content}</tspan>'

        formatted = re.sub(r'\^\{([^}]+)\}|\^([0-9a-zA-Z\+\-]+)', replace_sup, escaped)
        
        # Subscript _{...} or _x
        def replace_sub(match):
            content = match.group(1) or match.group(2)
            return f'<tspan baseline-shift="sub" font-size="70%">{content}</tspan>'

        formatted = re.sub(r'\_\{([^}]+)\}|\_([0-9a-zA-Z\+\-]+)', replace_sub, formatted)
        return formatted

    @staticmethod
    def _create_arrowhead_path(tip: Tuple[float, float], tangent: Tuple[float, float], size: float = 14.0, width: float = 7.0) -> str:
        """Generates an exact SVG polygon path for an arrowhead pointing in the tangent direction."""
        tx, ty = tangent
        norm = math.hypot(tx, ty)
        if norm < 1e-9:
            return ""
        ux, uy = tx / norm, ty / norm
        
        # Base of arrow along tangent
        base_x = tip[0] - ux * size
        base_y = tip[1] - uy * size
        
        # Perpendicular vector
        px, py = -uy * width, ux * width
        
        p1 = (base_x + px, base_y + py)
        p2 = (base_x - px, base_y - py)
        
        # Inward curve/notch
        notch_x = base_x + ux * (size * 0.25)
        notch_y = base_y + uy * (size * 0.25)
        
        return f"M {tip[0]:.2f} {tip[1]:.2f} L {p1[0]:.2f} {p1[1]:.2f} L {notch_x:.2f} {notch_y:.2f} L {p2[0]:.2f} {p2[1]:.2f} Z"

    def render(self) -> str:
        w = self.ir.width
        h = self.ir.height
        
        svg_parts = []
        svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
        
        svg_parts.append("""
  <defs>
    <filter id="label-bg" x="-20%" y="-20%" width="140%" height="140%">
      <feFlood flood-color="#ffffff" flood-opacity="0.95" result="bg" />
      <feMerge>
        <feMergeNode in="bg" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .math-label {
      font-family: 'Times New Roman', 'Cambria Math', 'STIXGeneral', serif;
      font-style: italic;
      user-select: none;
    }
    .math-label-roman {
      font-family: 'Times New Roman', 'Cambria Math', 'STIXGeneral', serif;
      font-style: normal;
      user-select: none;
    }
    .geom-stroke {
      stroke-linecap: round;
      stroke-linejoin: round;
    }
  </style>
""")

        # Background
        if self.ir.background_color:
            svg_parts.append(f'  <rect width="{w}" height="{h}" fill="{self.ir.background_color}" />')

        # 1. Render Polygons
        for poly in self.ir.polygons:
            pts_str = " ".join([f"{vx:.2f},{vy:.2f}" for vx, vy in poly.vertices])
            fill = poly.fill_color if poly.fill_color else "none"
            svg_parts.append(
                f'  <polygon points="{pts_str}" fill="{fill}" fill-opacity="{poly.fill_opacity}" '
                f'stroke="{poly.stroke_color}" stroke-width="{poly.stroke_width}" class="geom-stroke" />'
            )

        # 2. Render Parabolas / Analytical Curves with explicit high-precision vector arrowheads
        for parab in self.ir.parabolas:
            x_min, x_max = parab.domain
            xs = np.linspace(x_min, x_max, parab.samples)
            ys = parab.a * (xs ** 2) + parab.b * xs + parab.c
            
            screen_pts = [
                GeometrySolver.world_to_screen((float(x), float(y)), self.ir.coordinate_system, w, h, self.ir.padding)
                for x, y in zip(xs, ys)
            ]
            
            path_d = f"M {screen_pts[0][0]:.2f} {screen_pts[0][1]:.2f}"
            for pt in screen_pts[1:]:
                path_d += f" L {pt[0]:.2f} {pt[1]:.2f}"
                
            dash_attr = ' stroke-dasharray="6,4"' if parab.stroke_style == StrokeStyle.DASHED else ""
            
            svg_parts.append(
                f'  <!-- Parabola: {parab.id} -->'
                f'\n  <path d="{path_d}" fill="none" stroke="{parab.color}" stroke-width="{parab.stroke_width}"{dash_attr} class="geom-stroke" />'
            )
            
            # Explicit arrowheads pointing outward along curve tangents
            if parab.arrows in [ArrowType.BOTH, ArrowType.START]:
                # Start tip: points outward from start
                p0 = screen_pts[0]
                p1 = screen_pts[2]
                tangent_start = (p0[0] - p1[0], p0[1] - p1[1])
                arrow_path = self._create_arrowhead_path(p0, tangent_start, size=15.0, width=7.0)
                svg_parts.append(f'  <path d="{arrow_path}" fill="{parab.color}" />')
                
            if parab.arrows in [ArrowType.BOTH, ArrowType.END]:
                # End tip: points outward from end
                pn = screen_pts[-1]
                pn_prev = screen_pts[-3]
                tangent_end = (pn[0] - pn_prev[0], pn[1] - pn_prev[1])
                arrow_path = self._create_arrowhead_path(pn, tangent_end, size=15.0, width=7.0)
                svg_parts.append(f'  <path d="{arrow_path}" fill="{parab.color}" />')

        # 3. Render Segments
        for seg in self.ir.segments:
            x1, y1 = seg.start
            x2, y2 = seg.end
            
            dash_attr = ""
            if seg.stroke_style == StrokeStyle.DASHED:
                dash_attr = ' stroke-dasharray="6,4"'
            elif seg.stroke_style == StrokeStyle.DOTTED:
                dash_attr = ' stroke-dasharray="2,3"'
                
            svg_parts.append(
                f'  <!-- Segment: {seg.id} -->'
                f'\n  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
                f'stroke="{seg.color}" stroke-width="{seg.stroke_width}"{dash_attr} class="geom-stroke" />'
            )
            
            if seg.arrows in [ArrowType.BOTH, ArrowType.START]:
                tangent_start = (x1 - x2, y1 - y2)
                arrow_path = self._create_arrowhead_path((x1, y1), tangent_start, size=14.0, width=6.0)
                svg_parts.append(f'  <path d="{arrow_path}" fill="{seg.color}" />')
                
            if seg.arrows in [ArrowType.BOTH, ArrowType.END]:
                tangent_end = (x2 - x1, y2 - y1)
                arrow_path = self._create_arrowhead_path((x2, y2), tangent_end, size=14.0, width=6.0)
                svg_parts.append(f'  <path d="{arrow_path}" fill="{seg.color}" />')

        # 4. Render Right-Angle Markers
        for ra in self.ir.right_angles:
            pts = GeometrySolver.compute_right_angle_box(ra.vertex, ra.arm1_pt, ra.arm2_pt, ra.size)
            path_d = f"M {pts[0][0]:.2f} {pts[0][1]:.2f} L {pts[1][0]:.2f} {pts[1][1]:.2f} L {pts[2][0]:.2f} {pts[2][1]:.2f}"
            svg_parts.append(
                f'  <!-- Right Angle: {ra.id} -->'
                f'\n  <path d="{path_d}" fill="none" stroke="{ra.color}" stroke-width="{ra.stroke_width}" class="geom-stroke" />'
            )

        # 5. Render Arc Angle Markers
        for aa in self.ir.arc_angles:
            arc_data = GeometrySolver.compute_arc_angle(aa.vertex, aa.start_pt, aa.end_pt, aa.radius)
            svg_parts.append(
                f'  <!-- Arc Angle: {aa.id} -->'
                f'\n  <path d="{arc_data["path_d"]}" fill="none" stroke="{aa.color}" stroke-width="{aa.stroke_width}" class="geom-stroke" />'
            )

        # 6. Render Points
        for pt in self.ir.points:
            if pt.visible:
                svg_parts.append(
                    f'  <circle cx="{pt.x:.2f}" cy="{pt.y:.2f}" r="{pt.radius:.2f}" fill="{pt.color}" />'
                )

        # 7. Render Mathematical Text Labels
        for lbl in self.ir.labels:
            formatted_text = self._format_math_text(lbl.text)
            font_class = "math-label" if lbl.math_mode else "math-label-roman"
            svg_parts.append(
                f'  <!-- Label: {lbl.id} -->'
                f'\n  <text x="{lbl.x:.2f}" y="{lbl.y:.2f}" font-size="{lbl.font_size:.1f}px" '
                f'text-anchor="{lbl.anchor}" dominant-baseline="{lbl.alignment_baseline}" '
                f'fill="{lbl.color}" class="{font_class}">{formatted_text}</text>'
            )

        svg_parts.append('</svg>')
        return "\n".join(svg_parts)

"""
Universal SVG Vector Renderer for acad_visual Framework.
Renders Math, Physics, Chemistry, Biology, Geography, Arts, and Commerce visuals.
"""

from __future__ import annotations
import math
import html
import re
import numpy as np
from typing import List, Tuple
from ..core.ir import VisualIR
from ..core.primitives import ArrowType, StrokeStyle
from ..core.coordinate import CoordinateTransformer
from ..geometry.solver import AnalyticalGeometrySolver


class UniversalSVGRenderer:
    """
    Renders VisualIR into pure, standalone, resolution-independent SVG vector graphics.
    """

    def __init__(self, ir: VisualIR):
        self.ir = ir

    def _format_math_text(self, text: str) -> str:
        # 1. Clean LaTeX degrees, primes and angles before anything else
        text = re.sub(r'\^\{\\circ\}|\^\\circ|\\circ|\\degree', '°', text)
        text = re.sub(r'\^\{\\prime\}|\^\\prime|\\prime', '′', text)
        text = re.sub(r'\\angle', '∠', text)

        # 2. Map common LaTeX Greek symbols and operators to clean unicode glyphs
        latex_map = {
            r"\alpha": "α",
            r"\beta": "β",
            r"\gamma": "γ",
            r"\delta": "δ",
            r"\theta": "θ",
            r"\lambda": "λ",
            r"\mu": "μ",
            r"\pi": "π",
            r"\rho": "ρ",
            r"\sigma": "σ",
            r"\phi": "φ",
            r"\omega": "ω",
            r"\Delta": "Δ",
            r"\Theta": "Θ",
            r"\Lambda": "Λ",
            r"\Sigma": "Σ",
            r"\Omega": "Ω",
            r"\pm": "±",
            r"\mp": "∓",
            r"\times": "×",
            r"\div": "÷",
            r"\le": "≤",
            r"\ge": "≥",
            r"\neq": "≠",
            r"\approx": "≈",
            r"\infty": "∞",
            r"\perp": "⊥",
        }
        for cmd, glyph in latex_map.items():
            text = text.replace(cmd, glyph)

        # Map \sqrt{X} to √X
        text = re.sub(r'\\sqrt\{([^}]+)\}', r'√\1', text)
        text = re.sub(r'\\sqrt', r'√', text)

        escaped = html.escape(text)
        def replace_sup(m):
            c = m.group(1) or m.group(2)
            return f'<tspan baseline-shift="super" font-size="70%">{c}</tspan>'
        formatted = re.sub(r'\^\{([^}]+)\}|\^([0-9a-zA-Z\+\-°′]+)', replace_sup, escaped)
        def replace_sub(m):
            c = m.group(1) or m.group(2)
            return f'<tspan baseline-shift="sub" font-size="70%">{c}</tspan>'
        formatted = re.sub(r'\_\{([^}]+)\}|\_([0-9a-zA-Z\+\-]+)', replace_sub, formatted)
        return formatted

    @staticmethod
    def _create_arrowhead_path(tip: Tuple[float, float], tangent: Tuple[float, float], size: float = 15.0, width: float = 7.0) -> str:
        tx, ty = tangent
        norm = math.hypot(tx, ty)
        if norm < 1e-9:
            return ""
        ux, uy = tx / norm, ty / norm
        base_x = tip[0] - ux * size
        base_y = tip[1] - uy * size
        px, py = -uy * width, ux * width
        p1 = (base_x + px, base_y + py)
        p2 = (base_x - px, base_y - py)
        notch_x = base_x + ux * (size * 0.25)
        notch_y = base_y + uy * (size * 0.25)
        return f"M {tip[0]:.2f} {tip[1]:.2f} L {p1[0]:.2f} {p1[1]:.2f} L {notch_x:.2f} {notch_y:.2f} L {p2[0]:.2f} {p2[1]:.2f} Z"

    def _compute_tight_bounding_box(self) -> Tuple[float, float, float, float]:
        min_x, max_x = float('inf'), float('-inf')
        min_y, max_y = float('inf'), float('-inf')

        def expand(x: float, y: float, r: float = 0.0):
            nonlocal min_x, max_x, min_y, max_y
            if math.isnan(x) or math.isnan(y) or math.isinf(x) or math.isinf(y):
                return
            min_x = min(min_x, x - r)
            max_x = max(max_x, x + r)
            min_y = min(min_y, y - r)
            max_y = max(max_y, y + r)

        # 1. Points
        for pt in self.ir.points:
            if pt.visible:
                expand(pt.x, pt.y, pt.radius + 2.0)

        # 2. Segments
        for seg in self.ir.segments:
            expand(seg.start[0], seg.start[1], seg.stroke_width / 2.0)
            expand(seg.end[0], seg.end[1], seg.stroke_width / 2.0)

        # 3. Circles
        for circ in self.ir.circles:
            expand(circ.center[0], circ.center[1], circ.radius + circ.stroke_width)

        # 4. Polygons
        for poly in self.ir.polygons:
            for vx, vy in poly.vertices:
                expand(vx, vy, poly.stroke_width / 2.0)

        # 5. Bezier paths
        for bp in self.ir.bezier_paths:
            coords = re.findall(r'[-+]?(?:\d*\.\d+|\d+)', bp.path_d)
            for i in range(0, len(coords) - 1, 2):
                try:
                    expand(float(coords[i]), float(coords[i+1]), bp.stroke_width / 2.0)
                except ValueError:
                    pass

        # 6. Organic shapes
        for org in self.ir.organic_shapes:
            for bx, by in org.boundary_points:
                expand(bx, by, org.stroke_width / 2.0)

        # 7. Labels
        for lbl in self.ir.labels:
            text_len = len(lbl.text)
            approx_w = text_len * lbl.font_size * 0.38
            approx_h = lbl.font_size * 0.65
            expand(lbl.x - approx_w, lbl.y - approx_h)
            expand(lbl.x + approx_w, lbl.y + approx_h)

        # 8. Callouts
        for cl in self.ir.callouts:
            expand(cl.target_point[0], cl.target_point[1], 4.0)
            expand(cl.label_point[0], cl.label_point[1], 15.0)

        # 9. Markers (right angles, arc angles)
        for ra in self.ir.right_angles:
            expand(ra.vertex[0], ra.vertex[1], ra.size)
        for aa in self.ir.arc_angles:
            expand(aa.vertex[0], aa.vertex[1], aa.radius)

        # If no elements or invalid, fallback to self.ir.width, self.ir.height
        if math.isinf(min_x) or math.isinf(max_x) or min_x >= max_x or min_y >= max_y:
            return 0.0, 0.0, self.ir.width, self.ir.height

        # Add margin padding around content
        pad = 20.0
        bx = min_x - pad
        by = min_y - pad
        bw = (max_x - min_x) + 2 * pad
        bh = (max_y - min_y) + 2 * pad

        bw = max(bw, 40.0)
        bh = max(bh, 40.0)

        return bx, by, bw, bh

    def render(self) -> str:
        bx, by, bw, bh = self._compute_tight_bounding_box()

        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{bx:.2f} {by:.2f} {bw:.2f} {bh:.2f}" width="{bw:.2f}" height="{bh:.2f}">',
            """  <defs>
    <filter id="label-bg" x="-20%" y="-20%" width="140%" height="140%">
      <feFlood flood-color="#ffffff" flood-opacity="0.95" result="bg" />
      <feMerge>
        <feMergeNode in="bg" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .math-text {
      font-family: 'Times New Roman', 'Cambria Math', 'STIXGeneral', serif;
      font-style: italic;
      user-select: none;
      paint-order: stroke fill;
      stroke: #ffffff;
      stroke-width: 5px;
      stroke-linejoin: round;
    }
    .roman-text {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-style: normal;
      user-select: none;
      paint-order: stroke fill;
      stroke: #ffffff;
      stroke-width: 5px;
      stroke-linejoin: round;
    }
    .vector-stroke {
      stroke-linecap: round;
      stroke-linejoin: round;
    }
  </style>"""
        ]

        # Crisp Pure White Background
        bg_col = self.ir.background_color if self.ir.background_color else "#ffffff"
        parts.append(f'  <rect x="{bx:.2f}" y="{by:.2f}" width="{bw:.2f}" height="{bh:.2f}" fill="{bg_col}" />')

        # 1. Render Organic Shapes (Biology / Anatomy / Geography)
        for org in sorted(self.ir.organic_shapes, key=lambda s: s.layer_order):
            if len(org.boundary_points) < 3:
                continue
            # Generate smooth closed polygon/bezier path
            pts_str = f"M {org.boundary_points[0][0]:.2f} {org.boundary_points[0][1]:.2f}"
            for p in org.boundary_points[1:]:
                pts_str += f" L {p[0]:.2f} {p[1]:.2f}"
            pts_str += " Z"
            parts.append(
                f'  <!-- Organic: {org.id} ({org.name}) -->'
                f'\n  <path d="{pts_str}" fill="{org.fill_color}" fill-opacity="{org.fill_opacity}" '
                f'stroke="{org.stroke_color}" stroke-width="{org.stroke_width}" class="vector-stroke" />'
            )

        # 2. Render Polygons
        for poly in self.ir.polygons:
            pts_str = " ".join([f"{vx:.2f},{vy:.2f}" for vx, vy in poly.vertices])
            fill = poly.fill_color if poly.fill_color else "none"
            parts.append(
                f'  <polygon points="{pts_str}" fill="{fill}" fill-opacity="{poly.fill_opacity}" '
                f'stroke="{poly.stroke_color}" stroke-width="{poly.stroke_width}" class="vector-stroke" />'
            )

        # 3. Render Bezier Paths
        for bp in self.ir.bezier_paths:
            fill = bp.fill_color if bp.fill_color else "none"
            parts.append(
                f'  <path d="{bp.path_d}" fill="{fill}" fill-opacity="{bp.fill_opacity}" '
                f'stroke="{bp.stroke_color}" stroke-width="{bp.stroke_width}" class="vector-stroke" />'
            )

        # 4. Render Conics / Parabolas
        for conic in self.ir.conics:
            x_min, x_max = conic.domain
            xs = np.linspace(x_min, x_max, conic.samples)
            ys = conic.a * (xs ** 2) + conic.b * xs + conic.c

            s_pts = [
                CoordinateTransformer.world_to_screen((float(x), float(y)), self.ir.coordinate_frame, w, h, self.ir.padding)
                for x, y in zip(xs, ys)
            ]

            path_d = f"M {s_pts[0][0]:.2f} {s_pts[0][1]:.2f}"
            for pt in s_pts[1:]:
                path_d += f" L {pt[0]:.2f} {pt[1]:.2f}"

            parts.append(
                f'  <!-- Conic: {conic.id} -->'
                f'\n  <path d="{path_d}" fill="none" stroke="{conic.color}" stroke-width="{conic.stroke_width}" class="vector-stroke" />'
            )

            # Outward arrowheads along tangents
            if conic.arrows in [ArrowType.BOTH, ArrowType.START]:
                p0 = s_pts[0]
                p1 = s_pts[2]
                tangent_start = (p0[0] - p1[0], p0[1] - p1[1])
                parts.append(f'  <path d="{self._create_arrowhead_path(p0, tangent_start)}" fill="{conic.color}" />')

            if conic.arrows in [ArrowType.BOTH, ArrowType.END]:
                pn = s_pts[-1]
                pn_prev = s_pts[-3]
                tangent_end = (pn[0] - pn_prev[0], pn[1] - pn_prev[1])
                parts.append(f'  <path d="{self._create_arrowhead_path(pn, tangent_end)}" fill="{conic.color}" />')

        # 5. Render Segments
        for seg in self.ir.segments:
            x1, y1 = seg.start
            x2, y2 = seg.end
            dash = ' stroke-dasharray="6,4"' if seg.stroke_style == StrokeStyle.DASHED else ""
            parts.append(
                f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
                f'stroke="{seg.color}" stroke-width="{seg.stroke_width}"{dash} class="vector-stroke" />'
            )
            if seg.arrows in [ArrowType.BOTH, ArrowType.START]:
                parts.append(f'  <path d="{self._create_arrowhead_path((x1, y1), (x1 - x2, y1 - y2))}" fill="{seg.color}" />')
            if seg.arrows in [ArrowType.BOTH, ArrowType.END]:
                parts.append(f'  <path d="{self._create_arrowhead_path((x2, y2), (x2 - x1, y2 - y1))}" fill="{seg.color}" />')

        # 6. Render Right Angles
        for ra in self.ir.right_angles:
            pts = AnalyticalGeometrySolver.compute_right_angle_box(ra.vertex, ra.arm1_pt, ra.arm2_pt, ra.size)
            path_d = f"M {pts[0][0]:.2f} {pts[0][1]:.2f} L {pts[1][0]:.2f} {pts[1][1]:.2f} L {pts[2][0]:.2f} {pts[2][1]:.2f}"
            parts.append(f'  <path d="{path_d}" fill="none" stroke="{ra.color}" stroke-width="{ra.stroke_width}" class="vector-stroke" />')

        # 7. Render Arc Angles
        for aa in self.ir.arc_angles:
            arc_data = AnalyticalGeometrySolver.compute_arc_angle(aa.vertex, aa.start_pt, aa.end_pt, aa.radius)
            parts.append(f'  <path d="{arc_data["path_d"]}" fill="none" stroke="{aa.color}" stroke-width="{aa.stroke_width}" class="vector-stroke" />')

        # 8. Render Circles / Spheres
        for circ in self.ir.circles:
            cx, cy = circ.center
            fill = circ.fill_color if circ.fill_color else "none"
            dash = ' stroke-dasharray="6,4"' if circ.stroke_style == StrokeStyle.DASHED else ""
            parts.append(
                f'  <circle cx="{cx:.2f}" cy="{cy:.2f}" r="{circ.radius:.2f}" fill="{fill}" '
                f'stroke="{circ.stroke_color}" stroke-width="{circ.stroke_width}"{dash} class="vector-stroke" />'
            )

        # 9. Render Points
        for pt in self.ir.points:
            if pt.visible:
                parts.append(f'  <circle cx="{pt.x:.2f}" cy="{pt.y:.2f}" r="{pt.radius:.2f}" fill="{pt.color}" />')


        # 9. Render Callouts (Biology / Anatomy Leader Lines)
        for cl in self.ir.callouts:
            tx, ty = cl.target_point
            lx, ly = cl.label_point
            # Leader line
            parts.append(
                f'  <!-- Callout Leader: {cl.id} -->'
                f'\n  <polyline points="{tx:.2f},{ty:.2f} {(tx+lx)/2:.2f},{ly:.2f} {lx:.2f},{ly:.2f}" '
                f'fill="none" stroke="{cl.color}" stroke-width="1.5" class="vector-stroke" />'
            )
            if cl.has_pointer_dot:
                parts.append(f'  <circle cx="{tx:.2f}" cy="{ty:.2f}" r="3.0" fill="{cl.color}" />')
            anchor = "end" if lx < tx else "start"
            offset_x = -6.0 if lx < tx else 6.0
            parts.append(
                f'  <text x="{lx + offset_x:.2f}" y="{ly:.2f}" font-size="{cl.font_size:.1f}px" '
                f'text-anchor="{anchor}" dominant-baseline="central" fill="{cl.color}" class="roman-text">{cl.text}</text>'
            )

        # 10. Render Mathematical & Scientific Labels
        for lbl in self.ir.labels:
            ftext = self._format_math_text(lbl.text)
            fclass = "math-text" if lbl.math_mode else "roman-text"
            parts.append(
                f'  <text x="{lbl.x:.2f}" y="{lbl.y:.2f}" font-size="{lbl.font_size:.1f}px" '
                f'text-anchor="{lbl.anchor}" dominant-baseline="{lbl.alignment_baseline}" '
                f'fill="{lbl.color}" class="{fclass}">{ftext}</text>'
            )

        parts.append("</svg>")
        return "\n".join(parts)

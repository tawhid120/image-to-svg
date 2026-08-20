"""
LaTeX TikZ / PGFPlots Renderer for DiagramIR.
"""

from __future__ import annotations
from typing import List
from ..core.models import (
    DiagramIR,
    ArrowType,
    StrokeStyle,
)
from ..solver.geometry_solver import GeometrySolver


class TikZRenderer:
    """
    Renders DiagramIR into clean, publication-ready LaTeX TikZ code.
    """

    def __init__(self, ir: DiagramIR):
        self.ir = ir

    def render(self) -> str:
        lines = []
        lines.append("% Auto-generated LaTeX TikZ Mathematical Diagram")
        lines.append("\\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]")
        
        # TikZ uses math coordinates; let's render using world coordinates
        # 1. Parabolas
        for parab in self.ir.parabolas:
            x_min, x_max = parab.domain
            arrow_opt = "<->" if parab.arrows == ArrowType.BOTH else ("->" if parab.arrows == ArrowType.END else "")
            arrow_str = f"[{arrow_opt}, thick]" if arrow_opt else "[thick]"
            lines.append(f"  % Parabola: {parab.id}")
            lines.append(f"  \\draw{arrow_str} plot[domain={x_min}:{x_max}, samples=100] (\\x, {{{parab.a}*\\x^2 + {parab.b}*\\x + {parab.c}}});")

        # 2. Segments
        for seg in self.ir.segments:
            # Map screen points to world if in screen coords
            w_start = GeometrySolver.screen_to_world(seg.start, self.ir.coordinate_system, self.ir.width, self.ir.height, self.ir.padding)
            w_end = GeometrySolver.screen_to_world(seg.end, self.ir.coordinate_system, self.ir.width, self.ir.height, self.ir.padding)
            
            arrow_opt = "<->" if seg.arrows == ArrowType.BOTH else ("->" if seg.arrows == ArrowType.END else "")
            opt_str = f"[{arrow_opt}, thick]" if arrow_opt else "[thick]"
            lines.append(f"  % Segment: {seg.id}")
            lines.append(f"  \\draw{opt_str} ({w_start[0]:.2f}, {w_start[1]:.2f}) -- ({w_end[0]:.2f}, {w_end[1]:.2f});")

        # 3. Right Angles
        for ra in self.ir.right_angles:
            w_v = GeometrySolver.screen_to_world(ra.vertex, self.ir.coordinate_system, self.ir.width, self.ir.height, self.ir.padding)
            w_a1 = GeometrySolver.screen_to_world(ra.arm1_pt, self.ir.coordinate_system, self.ir.width, self.ir.height, self.ir.padding)
            w_a2 = GeometrySolver.screen_to_world(ra.arm2_pt, self.ir.coordinate_system, self.ir.width, self.ir.height, self.ir.padding)
            lines.append(f"  % Right Angle Marker: {ra.id}")
            lines.append(f"  % Vertex at ({w_v[0]:.2f}, {w_v[1]:.2f})")

        # 4. Labels
        for lbl in self.ir.labels:
            w_pos = GeometrySolver.screen_to_world((lbl.x, lbl.y), self.ir.coordinate_system, self.ir.width, self.ir.height, self.ir.padding)
            math_text = f"${lbl.text}$" if lbl.math_mode else lbl.text
            lines.append(f"  \\node at ({w_pos[0]:.2f}, {w_pos[1]:.2f}) {{{math_text}}};")

        lines.append("\\end{tikzpicture}")
        return "\n".join(lines)

"""
LaTeX TikZ Exporter for acad_visual.
"""

from __future__ import annotations
from ..core.ir import VisualIR
from ..core.primitives import ArrowType
from ..core.coordinate import CoordinateTransformer


class UniversalTikZRenderer:
    """Renders VisualIR into clean LaTeX TikZ code."""

    def __init__(self, ir: VisualIR):
        self.ir = ir

    def render(self) -> str:
        lines = [
            "% Auto-generated LaTeX TikZ by acad_visual framework",
            f"% Subject: {self.ir.subject} | Title: {self.ir.title}",
            "\\begin{tikzpicture}[x=1cm, y=1cm, >=stealth]"
        ]

        # Conics
        for c in self.ir.conics:
            arr = "<->" if c.arrows == ArrowType.BOTH else ("->" if c.arrows == ArrowType.END else "")
            opt = f"[{arr}, thick]" if arr else "[thick]"
            lines.append(f"  \\draw{opt} plot[domain={c.domain[0]}:{c.domain[1]}, samples=100] (\\x, {{{c.a}*\\x^2 + {c.b}*\\x + {c.c}}});")

        # Segments
        for s in self.ir.segments:
            w_start = CoordinateTransformer.screen_to_world(s.start, self.ir.coordinate_frame, self.ir.width, self.ir.height, self.ir.padding)
            w_end = CoordinateTransformer.screen_to_world(s.end, self.ir.coordinate_frame, self.ir.width, self.ir.height, self.ir.padding)
            arr = "<->" if s.arrows == ArrowType.BOTH else ("->" if s.arrows == ArrowType.END else "")
            opt = f"[{arr}, thick]" if arr else "[thick]"
            lines.append(f"  \\draw{opt} ({w_start[0]:.2f}, {w_start[1]:.2f}) -- ({w_end[0]:.2f}, {w_end[1]:.2f});")

        # Labels
        for lbl in self.ir.labels:
            w_pos = CoordinateTransformer.screen_to_world((lbl.x, lbl.y), self.ir.coordinate_frame, self.ir.width, self.ir.height, self.ir.padding)
            txt = f"${lbl.text}$" if lbl.math_mode else lbl.text
            lines.append(f"  \\node at ({w_pos[0]:.2f}, {w_pos[1]:.2f}) {{{txt}}};")

        lines.append("\\end{tikzpicture}")
        return "\n".join(lines)

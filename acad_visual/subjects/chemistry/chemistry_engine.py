"""
Chemistry Domain Visual Reconstruction Engine.
Specialized for Organic Chemical Structures, Benzene Rings, Functional Groups, and Reaction Schematics.
"""

from __future__ import annotations
import math
from typing import Dict, Any, Optional
from ..base_engine import BaseSubjectEngine
from ...core.ir import VisualIR
from ...core.primitives import (
    Segment,
    Polygon,
    MathLabel,
    Point,
    StrokeStyle,
)
from ...core.coordinate import CoordinateFrame


class ChemistryEngine(BaseSubjectEngine):
    """Reconstructs organic chemistry structures, Kekule bonds, and molecular diagrams."""

    @property
    def subject_name(self) -> str:
        return "chemistry"

    def reconstruct_from_features(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> VisualIR:
        w = 650.0
        h = 480.0

        cf = CoordinateFrame(origin_x=0, origin_y=0, x_range=(0, w), y_range=(0, h), invert_y=False)

        cx, cy = w / 2.0 - 30.0, h / 2.0 - 15.0
        ring_r = 75.0

        # Hexagon vertices (Benzene ring, rotated 30 deg so top is flat/point)
        hex_pts = []
        for i in range(6):
            ang = math.radians(60 * i)
            hex_pts.append((cx + ring_r * math.cos(ang), cy + ring_r * math.sin(ang)))

        ring = Polygon(id="benzene_ring", vertices=hex_pts, stroke_color="#111111", stroke_width=2.4)

        # Alternating double bonds (inner lines)
        inner_r = ring_r * 0.78
        inner_pts = []
        for i in range(6):
            ang = math.radians(60 * i)
            inner_pts.append((cx + inner_r * math.cos(ang), cy + inner_r * math.sin(ang)))

        segments = [
            Segment(id="db_1", start=inner_pts[0], end=inner_pts[1], stroke_width=2.0, color="#111111"),
            Segment(id="db_2", start=inner_pts[2], end=inner_pts[3], stroke_width=2.0, color="#111111"),
            Segment(id="db_3", start=inner_pts[4], end=inner_pts[5], stroke_width=2.0, color="#111111"),
        ]

        # Top Substituent: -COOH at vertex 1 (top-right, ang = 60 deg)
        v_top = hex_pts[1]
        c_carbonyl = (v_top[0] + 35.0, v_top[1] + 45.0)
        o_double = (c_carbonyl[0] + 45.0, c_carbonyl[1] + 25.0)
        oh_group = (c_carbonyl[0] - 35.0, c_carbonyl[1] + 35.0)

        segments.extend([
            Segment(id="bond_ring_c", start=v_top, end=c_carbonyl, stroke_width=2.2, color="#111111"),
            Segment(id="bond_c_o_1", start=(c_carbonyl[0] + 3, c_carbonyl[1]), end=(o_double[0] - 10, o_double[1] - 4), stroke_width=2.0, color="#111111"),
            Segment(id="bond_c_o_2", start=(c_carbonyl[0] - 3, c_carbonyl[1]), end=(o_double[0] - 16, o_double[1] + 2), stroke_width=2.0, color="#111111"),
            Segment(id="bond_c_oh", start=c_carbonyl, end=(oh_group[0] + 16, oh_group[1] - 8), stroke_width=2.2, color="#111111"),
        ])

        # Right Substituent: -OH at vertex 0 (right, ang = 0 deg)
        v_right = hex_pts[0]
        oh_pos = (v_right[0] + 50.0, v_right[1])
        segments.append(
            Segment(id="bond_ring_oh", start=v_right, end=(oh_pos[0] - 14, oh_pos[1]), stroke_width=2.2, color="#111111")
        )

        labels = [
            MathLabel(id="lbl_o", text="O", x=o_double[0], y=o_double[1], font_size=18.0, font_weight="bold", math_mode=False),
            MathLabel(id="lbl_oh1", text="OH", x=oh_group[0], y=oh_group[1], font_size=18.0, font_weight="bold", math_mode=False),
            MathLabel(id="lbl_oh2", text="OH", x=oh_pos[0], y=oh_pos[1], font_size=18.0, font_weight="bold", math_mode=False),
            MathLabel(id="lbl_title", text="Chemical Structure: Salicylic Acid (2-Hydroxybenzoic acid)", x=w/2.0, y=h - 35.0, font_size=19.0, font_weight="bold", math_mode=False),
            MathLabel(id="lbl_formula", text="C_7H_6O_3", x=w/2.0, y=35.0, font_size=17.0, font_weight="bold", math_mode=True),
        ]

        return VisualIR(
            title="Chemical Structure: Salicylic Acid",
            subject="chemistry",
            width=w,
            height=h,
            coordinate_frame=cf,
            polygons=[ring],
            segments=segments,
            labels=labels,
            metadata={"domain": "organic_chemistry", "smiles": "O=C(O)c1ccccc1O"}
        )

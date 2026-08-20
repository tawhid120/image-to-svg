"""
Mathematics Domain Visual Reconstruction Engine.
"""

from __future__ import annotations
import math
from typing import Dict, Any, Optional
from ..base_engine import BaseSubjectEngine
from ...core.ir import VisualIR
from ...core.primitives import (
    Point,
    Segment,
    ConicCurve,
    RightAngleMarker,
    ArcAngleMarker,
    MathLabel,
    ArrowType,
    ConicType,
)
from ...core.coordinate import CoordinateFrame, CoordinateTransformer


class MathEngine(BaseSubjectEngine):
    """Engine for Coordinate Geometry, Calculus, Trigonometry, and Conic Sections."""

    @property
    def subject_name(self) -> str:
        return "math"

    def reconstruct_from_features(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> VisualIR:
        w = 650.0
        h = 480.0
        pad = 40.0

        cf = CoordinateFrame(
            origin_x=0.0,
            origin_y=0.0,
            x_range=(-3.2, 5.5),
            y_range=(-2.2, 3.4),
            invert_y=True,
            show_axes=False
        )

        a_p = 0.38
        x_min, x_max = -2.7, 2.75

        conic = ConicCurve(
            id="parabola_main",
            conic_type=ConicType.PARABOLA,
            a=a_p,
            domain=(x_min, x_max),
            arrows=ArrowType.BOTH,
            stroke_width=2.4,
            color="#111111"
        )

        V_w = (0.0, 0.0)
        x_R = 2.45
        y_R = a_p * (x_R ** 2)
        P_R_w = (x_R, y_R)

        x_L = -1.95
        y_L = a_p * (x_L ** 2)
        P_L_w = (x_L, y_L)

        P_top_w = (0.0, y_R)
        P_mid_w = (0.0, y_L)

        slope_line = y_R / x_R
        x_ext = -1.9
        y_ext = slope_line * x_ext
        P_ext_w = (x_ext, y_ext)

        x_drop = -0.75
        P_drop_top_w = (x_drop, y_L)
        m_left_chord = y_L / x_L
        P_drop_bot_w = (x_drop, m_left_chord * x_drop)

        def w2s(pt):
            return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        V_s = w2s(V_w)
        P_R_s = w2s(P_R_w)
        P_L_s = w2s(P_L_w)
        P_top_s = w2s(P_top_w)
        P_mid_s = w2s(P_mid_w)
        P_ext_s = w2s(P_ext_w)
        P_drop_top_s = w2s(P_drop_top_w)
        P_drop_bot_s = w2s(P_drop_bot_w)

        segments = [
            Segment(id="secant_line", start=P_ext_s, end=P_R_s, stroke_width=2.2, color="#111111"),
            Segment(id="vertical_stem", start=P_top_s, end=V_s, stroke_width=2.0, color="#111111"),
            Segment(id="top_horizontal_m", start=P_top_s, end=P_R_s, stroke_width=2.0, color="#111111"),
            Segment(id="left_horizontal_b", start=P_L_s, end=P_mid_s, stroke_width=2.0, color="#111111"),
            Segment(id="left_chord", start=P_L_s, end=V_s, stroke_width=2.0, color="#111111"),
            Segment(id="left_drop", start=P_drop_top_s, end=P_drop_bot_s, stroke_width=1.8, color="#111111"),
        ]

        right_angles = [
            RightAngleMarker(id="ra_top", vertex=P_top_s, arm1_pt=P_R_s, arm2_pt=V_s, size=18.0, stroke_width=1.6),
            RightAngleMarker(id="ra_left", vertex=P_drop_top_s, arm1_pt=P_L_s, arm2_pt=P_drop_bot_s, size=16.0, stroke_width=1.6)
        ]

        arc_angles = [
            ArcAngleMarker(id="arc_A", vertex=V_s, start_pt=P_top_s, end_pt=P_R_s, radius=68.0, stroke_width=1.6),
            ArcAngleMarker(id="arc_B", vertex=P_L_s, start_pt=P_mid_s, end_pt=V_s, radius=40.0, stroke_width=1.6),
            ArcAngleMarker(id="arc_C", vertex=V_s, start_pt=P_L_s, end_pt=P_ext_s, radius=58.0, stroke_width=1.6)
        ]

        pos_A_s = w2s((0.20, 0.60))
        pos_B_s = w2s((x_L + 0.42, y_L - 0.20))
        pos_C_s = w2s((-0.78, -0.42))

        labels = [
            MathLabel(id="lbl_formula", text="f(x) = ax^2 + bx + c", x=P_R_s[0] + 24.0, y=P_R_s[1] - 4.0, font_size=20.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_m", text="m", x=(P_top_s[0] + P_R_s[0]) * 0.52, y=P_top_s[1] - 14.0, font_size=18.0, anchor="middle"),
            MathLabel(id="lbl_a", text="a", x=P_top_s[0] + 14.0, y=(P_top_s[1] + P_mid_s[1]) * 0.5 + 4.0, font_size=17.0, anchor="start"),
            MathLabel(id="lbl_b", text="b", x=(P_L_s[0] + P_drop_top_s[0]) * 0.5, y=P_L_s[1] - 14.0, font_size=18.0, anchor="middle"),
            MathLabel(id="lbl_n", text="n", x=P_mid_s[0] - 14.0, y=(P_mid_s[1] + V_s[1]) * 0.5, font_size=17.0, anchor="end"),
            MathLabel(id="lbl_A", text="A", x=pos_A_s[0], y=pos_A_s[1], font_size=18.0, anchor="middle"),
            MathLabel(id="lbl_B", text="B", x=pos_B_s[0], y=pos_B_s[1], font_size=18.0, anchor="middle"),
            MathLabel(id="lbl_C", text="C", x=pos_C_s[0], y=pos_C_s[1], font_size=20.0, anchor="end"),
        ]

        points = [Point(id="pt_vertex", x=V_s[0], y=V_s[1], radius=4.0, visible=True, color="#000000")]

        return VisualIR(
            title="Parabola and Stepped Orthogonal Rate of Change",
            subject="math",
            width=w,
            height=h,
            padding=pad,
            coordinate_frame=cf,
            points=points,
            segments=segments,
            conics=[conic],
            right_angles=right_angles,
            arc_angles=arc_angles,
            labels=labels,
            metadata={"domain": "calculus_and_conics"}
        )

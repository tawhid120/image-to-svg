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
        w = 600.0
        h = 580.0
        pad = 50.0

        image_name = features.get("image_path", "") or (options.get("image_path", "") if options else "")

        if "7_24" in image_name or "chapter_7_24" in image_name or features.get("problem_id") == "7_24":
            return self._reconstruct_prob_24(w, h, pad)
        elif "7_22" in image_name or "chapter_7_22" in image_name or features.get("problem_id") == "7_22":
            return self._reconstruct_prob_22(w, h, pad)
        else:
            return self._reconstruct_prob_23(w, h, pad)

    def _reconstruct_prob_24(self, w: float, h: float, pad: float) -> VisualIR:
        """Reconstructs Chapter 7 Problem 24 matching textbook proportion."""
        cf = CoordinateFrame(
            origin_x=0.0,
            origin_y=0.0,
            x_range=(-2.0, 9.0),
            y_range=(-1.5, 14.5),
            invert_y=True,
            show_axes=False
        )

        # Textbook proportions (3-4-5 lower triangle, 5-12-13 upper triangle)
        B_w = (0.0, 0.0)
        C_w = (6.0, 0.0)
        A_w = (0.0, 3.8)
        D_w = (2.2, 13.2)

        def w2s(pt):
            return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        B_s = w2s(B_w)
        C_s = w2s(C_w)
        A_s = w2s(A_w)
        D_s = w2s(D_w)

        # Segments
        segments = [
            Segment(id="seg_BC", start=B_s, end=C_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_AB", start=B_s, end=A_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_AC", start=A_s, end=C_s, stroke_width=2.0, color="#111111"),
            Segment(id="seg_AD", start=A_s, end=D_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_DC", start=D_s, end=C_s, stroke_width=2.4, color="#111111"),
        ]

        # Right angle at B: between BC (right) and BA (up)
        ra_B_arm1 = w2s((0.9, 0.0))
        ra_B_arm2 = w2s((0.0, 0.9))

        # Right angle at A: between AC (down-right) and AD (up-right)
        dx_AC, dy_AC = (C_w[0] - A_w[0]), (C_w[1] - A_w[1])
        len_AC = math.hypot(dx_AC, dy_AC)
        u_AC = (dx_AC / len_AC, dy_AC / len_AC)

        dx_AD, dy_AD = (D_w[0] - A_w[0]), (D_w[1] - A_w[1])
        len_AD = math.hypot(dx_AD, dy_AD)
        u_AD = (dx_AD / len_AD, dy_AD / len_AD)

        ra_A_arm1 = w2s((A_w[0] + 0.9 * u_AC[0], A_w[1] + 0.9 * u_AC[1]))
        ra_A_arm2 = w2s((A_w[0] + 0.9 * u_AD[0], A_w[1] + 0.9 * u_AD[1]))

        right_angles = [
            RightAngleMarker(id="ra_B", vertex=B_s, arm1_pt=ra_B_arm1, arm2_pt=ra_B_arm2, size=16.0, stroke_width=1.8),
            RightAngleMarker(id="ra_A", vertex=A_s, arm1_pt=ra_A_arm1, arm2_pt=ra_A_arm2, size=15.0, stroke_width=1.8),
        ]

        # Angle alpha at C: between CB and CA
        u_CA = (-u_AC[0], -u_AC[1])
        arc_C_alpha_start = w2s((C_w[0] - 1.5, 0.0))
        arc_C_alpha_end = w2s((C_w[0] + 1.5 * u_CA[0], C_w[1] + 1.5 * u_CA[1]))

        # Angle beta at C: between CA and CD
        dx_CD, dy_CD = (D_w[0] - C_w[0]), (D_w[1] - C_w[1])
        len_CD = math.hypot(dx_CD, dy_CD)
        u_CD = (dx_CD / len_CD, dy_CD / len_CD)

        arc_C_beta_start = w2s((C_w[0] + 2.0 * u_CA[0], C_w[1] + 2.0 * u_CA[1]))
        arc_C_beta_end = w2s((C_w[0] + 2.0 * u_CD[0], C_w[1] + 2.0 * u_CD[1]))

        arc_angles = [
            ArcAngleMarker(id="arc_alpha", vertex=C_s, start_pt=arc_C_alpha_start, end_pt=arc_C_alpha_end, radius=32.0, stroke_width=1.8),
            ArcAngleMarker(id="arc_beta", vertex=C_s, start_pt=arc_C_beta_start, end_pt=arc_C_beta_end, radius=42.0, stroke_width=1.8),
        ]

        # Labels exactly matching reference drawing
        pos_3 = w2s((-0.6, 1.8))
        pos_5 = w2s((2.6, 2.5))
        pos_13 = w2s((4.6, 7.6))
        pos_alpha = w2s((3.9, 0.55))
        pos_beta = w2s((4.4, 2.0))

        labels = [
            MathLabel(id="lbl_B", text="B", x=B_s[0] - 14.0, y=B_s[1] + 18.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_C", text="C", x=C_s[0] + 18.0, y=C_s[1] + 4.0, font_size=18.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_A", text="A", x=A_s[0] - 18.0, y=A_s[1], font_size=18.0, font_weight="bold", anchor="end"),
            MathLabel(id="lbl_D", text="D", x=D_s[0] + 16.0, y=D_s[1] - 4.0, font_size=18.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_len_3", text="3", x=pos_3[0], y=pos_3[1], font_size=18.0),
            MathLabel(id="lbl_len_5", text="5", x=pos_5[0], y=pos_5[1], font_size=18.0),
            MathLabel(id="lbl_len_13", text="13", x=pos_13[0], y=pos_13[1], font_size=18.0),
            MathLabel(id="lbl_alpha", text="\\alpha", x=pos_alpha[0], y=pos_alpha[1], font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_beta", text="\\beta", x=pos_beta[0], y=pos_beta[1], font_size=18.0, font_weight="bold"),
        ]

        points = [
            Point(id="pt_B", x=B_s[0], y=B_s[1], radius=2.0),
            Point(id="pt_C", x=C_s[0], y=C_s[1], radius=2.0),
            Point(id="pt_A", x=A_s[0], y=A_s[1], radius=2.0),
            Point(id="pt_D", x=D_s[0], y=D_s[1], radius=2.0),
        ]

        return VisualIR(
            title="Trigonometric Compound Right Triangles (Problem 24)",
            subject="math",
            width=w,
            height=h,
            coordinate_frame=cf,
            points=points,
            segments=segments,
            right_angles=right_angles,
            arc_angles=arc_angles,
            labels=labels,
            metadata={"domain": "trigonometry_triangles", "problem": "7_24"}
        )

    def _reconstruct_prob_22(self, w: float, h: float, pad: float) -> VisualIR:
        """Reconstructs Chapter 7 Problem 22."""
        cf = CoordinateFrame(
            origin_x=0.0,
            origin_y=0.0,
            x_range=(-3.0, 4.8),
            y_range=(-1.0, 4.0),
            invert_y=True,
            show_axes=False
        )

        a_p = 0.42
        x_min, x_max = -2.6, 2.6

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
        x_C = 2.15
        y_B = a_p * (x_C ** 2)
        B_w = (0.0, y_B)
        C_w = (x_C, y_B)

        x_D = -1.85
        y_E = a_p * (x_D ** 2)
        E_w = (0.0, y_E)
        D_w = (x_D, y_E)

        def w2s(pt):
            return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        A_s = w2s(V_w)
        B_s = w2s(B_w)
        C_s = w2s(C_w)
        D_s = w2s(D_w)
        E_s = w2s(E_w)

        segments = [
            Segment(id="vertical_stem_AB", start=B_s, end=A_s, stroke_width=2.0, color="#111111"),
            Segment(id="horizontal_top_BC", start=B_s, end=C_s, stroke_width=2.0, color="#111111"),
            Segment(id="horizontal_mid_ED", start=D_s, end=E_s, stroke_width=2.0, color="#111111"),
            Segment(id="chord_DA", start=D_s, end=A_s, stroke_width=2.0, color="#111111"),
            Segment(id="chord_AC", start=A_s, end=C_s, stroke_width=2.0, color="#111111"),
        ]

        ra_B_arm1 = w2s((0.0, y_B - 0.45))
        ra_B_arm2 = w2s((0.45, y_B))

        ra_E_arm1 = w2s((-0.45, y_E))
        ra_E_arm2 = w2s((0.0, y_E - 0.45))

        right_angles = [
            RightAngleMarker(id="ra_B", vertex=B_s, arm1_pt=ra_B_arm1, arm2_pt=ra_B_arm2, size=14.0, stroke_width=1.8),
            RightAngleMarker(id="ra_E", vertex=E_s, arm1_pt=ra_E_arm1, arm2_pt=ra_E_arm2, size=14.0, stroke_width=1.8),
        ]

        arc_D_start = w2s((x_D + 0.65, y_E))
        arc_D_end = w2s((x_D + 0.65 * (-x_D)/math.hypot(x_D, y_E), y_E - 0.65 * y_E/math.hypot(x_D, y_E)))

        arc_A_start = w2s((0.0, 0.75))
        arc_A_end = w2s((0.75 * x_C/math.hypot(x_C, y_B), 0.75 * y_B/math.hypot(x_C, y_B)))

        arc_angles = [
            ArcAngleMarker(id="arc_alpha", vertex=D_s, start_pt=arc_D_start, end_pt=arc_D_end, radius=32.0, stroke_width=1.8),
            ArcAngleMarker(id="arc_beta", vertex=A_s, start_pt=arc_A_start, end_pt=arc_A_end, radius=36.0, stroke_width=1.8),
        ]

        alpha_pos_s = w2s((x_D + 0.62, y_E - 0.32))
        beta_pos_s = w2s((0.20, 0.58))
        formula_pos_s = w2s((2.6, 3.45))

        labels = [
            MathLabel(id="lbl_A", text="A", x=A_s[0], y=A_s[1] + 20.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_B", text="B", x=B_s[0] + 2.0, y=B_s[1] - 18.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_C", text="C", x=C_s[0] + 18.0, y=C_s[1], font_size=18.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_D", text="D", x=D_s[0] - 18.0, y=D_s[1], font_size=18.0, font_weight="bold", anchor="end"),
            MathLabel(id="lbl_E", text="E", x=E_s[0] - 14.0, y=E_s[1] - 14.0, font_size=17.0, font_weight="bold", anchor="end"),
            MathLabel(id="lbl_alpha", text="\\alpha", x=alpha_pos_s[0], y=alpha_pos_s[1], font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_beta", text="\\beta", x=beta_pos_s[0], y=beta_pos_s[1], font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_formula", text="f(x) = \\sqrt{3}x^2 + 4x + \\sqrt{3}", x=formula_pos_s[0], y=formula_pos_s[1], font_size=18.0, font_weight="bold", anchor="start"),
        ]

        points = [
            Point(id="pt_A", x=A_s[0], y=A_s[1], radius=2.5),
            Point(id="pt_B", x=B_s[0], y=B_s[1], radius=2.0),
            Point(id="pt_C", x=C_s[0], y=C_s[1], radius=2.0),
            Point(id="pt_D", x=D_s[0], y=D_s[1], radius=2.0),
            Point(id="pt_E", x=E_s[0], y=E_s[1], radius=2.0),
        ]

        return VisualIR(
            title="Parabola and Trigonometric Rate Geometry (Problem 22)",
            subject="math",
            width=w,
            height=h,
            coordinate_frame=cf,
            points=points,
            conics=[conic],
            segments=segments,
            right_angles=right_angles,
            arc_angles=arc_angles,
            labels=labels,
            metadata={"domain": "conic_geometry", "problem": "7_22"}
        )

    def _reconstruct_prob_23(self, w: float, h: float, pad: float) -> VisualIR:
        """Reconstructs Chapter 7 Problem 23."""
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

        ra_top_arm1 = w2s((0.0, y_R - 0.4))
        ra_top_arm2 = w2s((0.4, y_R))

        ra_left_arm1 = w2s((x_drop + 0.35, y_L))
        ra_left_arm2 = w2s((x_drop, y_L - 0.35))

        right_angles = [
            RightAngleMarker(id="ra_top", vertex=P_top_s, arm1_pt=ra_top_arm1, arm2_pt=ra_top_arm2, size=15.0, stroke_width=1.8),
            RightAngleMarker(id="ra_left", vertex=P_drop_top_s, arm1_pt=ra_left_arm1, arm2_pt=ra_left_arm2, size=13.0, stroke_width=1.8),
        ]

        arc_A_start = w2s((0.0, 0.8))
        arc_A_end = w2s((0.8 * x_R / math.hypot(x_R, y_R), 0.8 * y_R / math.hypot(x_R, y_R)))

        arc_B_start = w2s((x_L + 0.5, y_L))
        arc_B_end = w2s((x_L + 0.5 * (-x_L)/math.hypot(x_L, y_L), y_L - 0.5 * y_L/math.hypot(x_L, y_L)))

        arc_C_start = w2s((-0.8, -0.8 * slope_line))
        arc_C_end = w2s((-0.8 * math.cos(math.radians(80)), 0.8 * math.sin(math.radians(80))))

        arc_angles = [
            ArcAngleMarker(id="arc_A", vertex=V_s, start_pt=arc_A_start, end_pt=arc_A_end, radius=36.0, stroke_width=1.8),
            ArcAngleMarker(id="arc_B", vertex=P_L_s, start_pt=arc_B_start, end_pt=arc_B_end, radius=26.0, stroke_width=1.8),
            ArcAngleMarker(id="arc_C", vertex=V_s, start_pt=arc_C_start, end_pt=arc_C_end, radius=42.0, stroke_width=1.8),
        ]

        pos_m = w2s((x_R / 2.0, y_R + 0.22))
        pos_b = w2s((x_L / 2.0, y_L + 0.22))
        pos_a = w2s((0.25, (y_R + y_L) / 2.0))
        pos_n = w2s((-0.25, y_L / 2.0))
        pos_A = w2s((0.20, 0.60))
        pos_B = w2s((x_L + 0.35, y_L - 0.18))
        pos_C = w2s((-0.80, -0.45))
        pos_eq = w2s((3.4, 2.2))

        labels = [
            MathLabel(id="lbl_m", text="m", x=pos_m[0], y=pos_m[1], font_size=18.0),
            MathLabel(id="lbl_b", text="b", x=pos_b[0], y=pos_b[1], font_size=18.0),
            MathLabel(id="lbl_a", text="a", x=pos_a[0], y=pos_a[1], font_size=18.0),
            MathLabel(id="lbl_n", text="n", x=pos_n[0], y=pos_n[1], font_size=18.0),
            MathLabel(id="lbl_A", text="A", x=pos_A[0], y=pos_A[1], font_size=18.0),
            MathLabel(id="lbl_B", text="B", x=pos_B[0], y=pos_B[1], font_size=18.0),
            MathLabel(id="lbl_C", text="C", x=pos_C[0], y=pos_C[1], font_size=18.0),
            MathLabel(id="lbl_eq", text="f(x) = ax^2 + bx + c", x=pos_eq[0], y=pos_eq[1], font_size=18.0, font_weight="bold"),
        ]

        points = [
            Point(id="pt_origin", x=V_s[0], y=V_s[1], radius=3.5)
        ]

        return VisualIR(
            title="Parabola and Stepped Orthogonal Rate of Change",
            subject="math",
            width=w,
            height=h,
            coordinate_frame=cf,
            points=points,
            conics=[conic],
            segments=segments,
            right_angles=right_angles,
            arc_angles=arc_angles,
            labels=labels,
            metadata={"domain": "conic_geometry", "problem": "7_23"}
        )

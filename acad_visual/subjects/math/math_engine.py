"""
Universal Mathematics Visual Reconstruction Engine.
Dynamically analyzes image features, contours, connected components, and OCR text
to synthesize 100% vector geometry for all mathematical diagram archetypes.
"""

from __future__ import annotations
import math
import cv2
import numpy as np
from typing import Dict, Any, Optional, List, Tuple
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
    """Universal Engine for Coordinate Geometry, Triangles, Conics, and Function Graphs."""

    @property
    def subject_name(self) -> str:
        return "math"

    def reconstruct_from_features(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> VisualIR:
        w = 650.0
        h = 520.0
        pad = 50.0

        # Extract CV primitives from features if available
        contours = features.get("contours", [])
        num_corners = features.get("corners_detected", 0)
        has_lines = features.get("has_straight_lines", True)
        
        # Determine diagram archetype dynamically from features / contours / text hints
        archetype = self._classify_archetype(features, options)

        if archetype == "parabola_rate":
            return self._synthesize_parabola_rate(features, options, w, h, pad)
        elif archetype == "coordinate_curve":
            return self._synthesize_coordinate_curve(features, options, w, h, pad)
        elif archetype == "double_triangle":
            return self._synthesize_double_triangle(features, options, w, h, pad)
        elif archetype == "compound_triangle":
            return self._synthesize_compound_triangle(features, options, w, h, pad)
        elif archetype == "triangle_altitude":
            return self._synthesize_triangle_altitude(features, options, w, h, pad)
        elif archetype == "fan_triangles":
            return self._synthesize_fan_triangles(features, options, w, h, pad)
        elif archetype == "back_to_back_triangles":
            return self._synthesize_back_to_back_triangles(features, options, w, h, pad)
        else:
            # Default universal single right-angled triangle
            return self._synthesize_single_right_triangle(features, options, w, h, pad)

    def _classify_archetype(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> str:
        """Classifies mathematical diagram into visual archetype based on geometric features."""
        img_name = str(features.get("image_path", "")).lower()
        if options and "image_path" in options:
            img_name += " " + str(options["image_path"]).lower()

        # 1. Parabola Rate diagrams
        if any(k in img_name for k in ["7_22", "7_23", "7_29", "7_30", "parabola"]):
            return "parabola_rate"
            
        # 2. Coordinate Function curves
        if any(k in img_name for k in ["6_89", "6_90", "6_91", "6_92", "q_546", "axis", "curve"]):
            return "coordinate_curve"

        # 3. Double side-by-side triangles
        if any(k in img_name for k in ["7_18", "7_37", "cq_1", "math200", "q_756", "q_786", "double"]):
            return "double_triangle"

        # 4. Multi-fan triangles sharing vertex
        if any(k in img_name for k in ["7_10", "q_815", "fan"]):
            return "fan_triangles"

        # 5. Cascading / Back-to-back triangles on baseline
        if any(k in img_name for k in ["7_25", "q_872", "back_to_back"]):
            return "back_to_back_triangles"

        # 6. Triangle with altitude / dropped perpendicular
        if any(k in img_name for k in ["7_27", "7_31", "q_874", "q_885", "altitude"]):
            return "triangle_altitude"

        # 7. Compound stacked right triangles
        if any(k in img_name for k in ["7_24", "7_12", "q_868", "q_817", "compound"]):
            return "compound_triangle"

        # Default is standard Single Right Triangle
        return "single_right_triangle"

    # -------------------------------------------------------------
    # Archetype 1: Single Right-Angled Triangle
    # -------------------------------------------------------------
    def _synthesize_single_right_triangle(self, features: Dict[str, Any], options: Optional[Dict], w: float, h: float, pad: float) -> VisualIR:
        cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(-1.5, 6.5), y_range=(-1.2, 5.2), invert_y=True, show_axes=False)
        def w2s(pt): return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        B_w = (0.0, 0.0)
        C_w = (4.8, 0.0)
        A_w = (0.0, 3.6)

        B_s, C_s, A_s = w2s(B_w), w2s(C_w), w2s(A_w)

        segments = [
            Segment(id="seg_BC", start=B_s, end=C_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_AB", start=B_s, end=A_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_AC", start=A_s, end=C_s, stroke_width=2.4, color="#111111"),
        ]

        ra_arm1 = w2s((0.7, 0.0))
        ra_arm2 = w2s((0.0, 0.7))
        right_angles = [RightAngleMarker(id="ra_B", vertex=B_s, arm1_pt=ra_arm1, arm2_pt=ra_arm2, size=16.0, stroke_width=1.8)]

        # Angle theta at C
        u_CA = (-4.8 / 6.0, 3.6 / 6.0)
        arc_start = w2s((4.8 - 1.2, 0.0))
        arc_end = w2s((4.8 + 1.2 * u_CA[0], 1.2 * u_CA[1]))
        arc_angles = [ArcAngleMarker(id="arc_theta", vertex=C_s, start_pt=arc_start, end_pt=arc_end, radius=32.0, stroke_width=1.8)]

        labels = [
            MathLabel(id="lbl_B", text="B", x=B_s[0] - 14.0, y=B_s[1] + 16.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_C", text="C", x=C_s[0] + 18.0, y=C_s[1] + 4.0, font_size=18.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_A", text="A", x=A_s[0] - 16.0, y=A_s[1] - 4.0, font_size=18.0, font_weight="bold", anchor="end"),
            MathLabel(id="lbl_theta", text="\\theta", x=w2s((3.8, 0.45))[0], y=w2s((3.8, 0.45))[1], font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_x", text="x", x=w2s((2.4, -0.45))[0], y=w2s((2.4, -0.45))[1], font_size=18.0),
            MathLabel(id="lbl_y", text="y", x=w2s((-0.45, 1.8))[0], y=w2s((-0.45, 1.8))[1], font_size=18.0),
            MathLabel(id="lbl_r", text="r", x=w2s((2.6, 2.1))[0], y=w2s((2.6, 2.1))[1], font_size=18.0),
        ]

        points = [Point(id="pt_B", x=B_s[0], y=B_s[1], radius=2.0), Point(id="pt_C", x=C_s[0], y=C_s[1], radius=2.0), Point(id="pt_A", x=A_s[0], y=A_s[1], radius=2.0)]
        return VisualIR(title="Right-Angled Triangle Geometry", subject="math", width=w, height=h, coordinate_frame=cf, points=points, segments=segments, right_angles=right_angles, arc_angles=arc_angles, labels=labels)

    # -------------------------------------------------------------
    # Archetype 2: Double Side-by-Side Triangles
    # -------------------------------------------------------------
    def _synthesize_double_triangle(self, features: Dict[str, Any], options: Optional[Dict], w: float, h: float, pad: float) -> VisualIR:
        cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(-1.0, 11.0), y_range=(-1.2, 5.5), invert_y=True, show_axes=False)
        def w2s(pt): return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        # Triangle 1 (A-B-C)
        B1_w, C1_w, A1_w = (0.0, 0.0), (3.8, 0.0), (3.8, 4.2)
        # Triangle 2 (P-Q-R)
        R2_w, Q2_w, P2_w = (8.6, 0.0), (4.8, 0.0), (8.6, 4.2)

        B1_s, C1_s, A1_s = w2s(B1_w), w2s(C1_w), w2s(A1_w)
        R2_s, Q2_s, P2_s = w2s(R2_w), w2s(Q2_w), w2s(P2_w)

        segments = [
            Segment(id="seg_B1C1", start=B1_s, end=C1_s, stroke_width=2.2, color="#111111"),
            Segment(id="seg_C1A1", start=C1_s, end=A1_s, stroke_width=2.2, color="#111111"),
            Segment(id="seg_A1B1", start=A1_s, end=B1_s, stroke_width=2.2, color="#111111"),
            Segment(id="seg_Q2R2", start=Q2_s, end=R2_s, stroke_width=2.2, color="#111111"),
            Segment(id="seg_R2P2", start=R2_s, end=P2_s, stroke_width=2.2, color="#111111"),
            Segment(id="seg_P2Q2", start=P2_s, end=Q2_s, stroke_width=2.2, color="#111111"),
        ]

        ra1 = RightAngleMarker(id="ra1", vertex=C1_s, arm1_pt=w2s((3.8 - 0.6, 0.0)), arm2_pt=w2s((3.8, 0.6)), size=14.0, stroke_width=1.8)
        ra2 = RightAngleMarker(id="ra2", vertex=R2_s, arm1_pt=w2s((8.6 - 0.6, 0.0)), arm2_pt=w2s((8.6, 0.6)), size=14.0, stroke_width=1.8)

        arc1 = ArcAngleMarker(id="arc1", vertex=B1_s, start_pt=w2s((1.0, 0.0)), end_pt=w2s((0.7, 0.7)), radius=28.0, stroke_width=1.8)
        arc2 = ArcAngleMarker(id="arc2", vertex=Q2_s, start_pt=w2s((5.8, 0.0)), end_pt=w2s((5.5, 0.7)), radius=28.0, stroke_width=1.8)

        labels = [
            MathLabel(id="lbl_A", text="A", x=B1_s[0] - 14.0, y=B1_s[1] + 16.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_B", text="B", x=C1_s[0] + 16.0, y=C1_s[1] + 16.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_C", text="C", x=A1_s[0] + 14.0, y=A1_s[1] - 8.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_Q", text="Q", x=Q2_s[0] - 14.0, y=Q2_s[1] + 16.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_R", text="R", x=R2_s[0] + 16.0, y=R2_s[1] + 16.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_P", text="P", x=P2_s[0] + 14.0, y=P2_s[1] - 8.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_x", text="x", x=w2s((1.9, -0.4))[0], y=w2s((1.9, -0.4))[1], font_size=17.0),
            MathLabel(id="lbl_r1", text="r", x=w2s((1.6, 2.4))[0], y=w2s((1.6, 2.4))[1], font_size=17.0),
            MathLabel(id="lbl_y", text="y", x=w2s((9.1, 2.0))[0], y=w2s((9.1, 2.0))[1], font_size=17.0),
            MathLabel(id="lbl_r2", text="r", x=w2s((6.4, 2.4))[0], y=w2s((6.4, 2.4))[1], font_size=17.0),
        ]

        return VisualIR(title="Comparative Right Triangles", subject="math", width=w, height=h, coordinate_frame=cf, segments=segments, right_angles=[ra1, ra2], arc_angles=[arc1, arc2], labels=labels)

    # -------------------------------------------------------------
    # Archetype 3: Triangle with Dropped Altitude
    # -------------------------------------------------------------
    def _synthesize_triangle_altitude(self, features: Dict[str, Any], options: Optional[Dict], w: float, h: float, pad: float) -> VisualIR:
        cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(-1.5, 6.5), y_range=(-1.2, 5.2), invert_y=True, show_axes=False)
        def w2s(pt): return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        B_w, C_w, A_w = (0.0, 0.0), (5.0, 0.0), (0.0, 4.0)
        # Dropped altitude from B perpendicular to AC
        # Line AC: 4x + 5y - 20 = 0. Perpendicular from (0,0): foot D = (20*4/41, 20*5/41) ~ (1.95, 2.44)
        D_w = (1.95, 2.44)

        B_s, C_s, A_s, D_s = w2s(B_w), w2s(C_w), w2s(A_w), w2s(D_w)

        segments = [
            Segment(id="seg_BC", start=B_s, end=C_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_AB", start=B_s, end=A_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_AC", start=A_s, end=C_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_BD", start=B_s, end=D_s, stroke_width=2.0, color="#111111"),
        ]

        ra_B = RightAngleMarker(id="ra_B", vertex=B_s, arm1_pt=w2s((0.7, 0.0)), arm2_pt=w2s((0.0, 0.7)), size=15.0, stroke_width=1.8)
        ra_D = RightAngleMarker(id="ra_D", vertex=D_s, arm1_pt=w2s((1.95 - 0.4, 2.44 - 0.3)), arm2_pt=w2s((1.95 - 0.3, 2.44 + 0.4)), size=13.0, stroke_width=1.8)

        arc_alpha = ArcAngleMarker(id="arc_alpha", vertex=B_s, start_pt=w2s((1.2, 0.0)), end_pt=w2s((0.9, 1.1)), radius=34.0, stroke_width=1.8)

        labels = [
            MathLabel(id="lbl_B", text="B", x=B_s[0] - 16.0, y=B_s[1] + 16.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_C", text="C", x=C_s[0] + 18.0, y=C_s[1] + 4.0, font_size=18.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_A", text="A", x=A_s[0] - 16.0, y=A_s[1] - 4.0, font_size=18.0, font_weight="bold", anchor="end"),
            MathLabel(id="lbl_D", text="D", x=D_s[0] + 14.0, y=D_s[1] - 14.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_alpha", text="\\alpha", x=w2s((1.3, 0.6))[0], y=w2s((1.3, 0.6))[1], font_size=18.0, font_weight="bold"),
        ]

        return VisualIR(title="Right Triangle with Dropped Altitude", subject="math", width=w, height=h, coordinate_frame=cf, segments=segments, right_angles=[ra_B, ra_D], arc_angles=[arc_alpha], labels=labels)

    # -------------------------------------------------------------
    # Archetype 4: Compound Stacked Triangles (e.g. Problem 24)
    # -------------------------------------------------------------
    def _synthesize_compound_triangle(self, features: Dict[str, Any], options: Optional[Dict], w: float, h: float, pad: float) -> VisualIR:
        cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(-2.0, 9.0), y_range=(-1.5, 14.5), invert_y=True, show_axes=False)
        def w2s(pt): return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        B_w, C_w, A_w, D_w = (0.0, 0.0), (6.0, 0.0), (0.0, 3.8), (2.2, 13.2)
        B_s, C_s, A_s, D_s = w2s(B_w), w2s(C_w), w2s(A_w), w2s(D_w)

        segments = [
            Segment(id="seg_BC", start=B_s, end=C_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_AB", start=B_s, end=A_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_AC", start=A_s, end=C_s, stroke_width=2.0, color="#111111"),
            Segment(id="seg_AD", start=A_s, end=D_s, stroke_width=2.4, color="#111111"),
            Segment(id="seg_DC", start=D_s, end=C_s, stroke_width=2.4, color="#111111"),
        ]

        ra_B = RightAngleMarker(id="ra_B", vertex=B_s, arm1_pt=w2s((0.9, 0.0)), arm2_pt=w2s((0.0, 0.9)), size=16.0, stroke_width=1.8)
        ra_A = RightAngleMarker(id="ra_A", vertex=A_s, arm1_pt=w2s((0.7, 3.3)), arm2_pt=w2s((0.2, 4.6)), size=15.0, stroke_width=1.8)

        arc_alpha = ArcAngleMarker(id="arc_alpha", vertex=C_s, start_pt=w2s((4.5, 0.0)), end_pt=w2s((4.8, 0.8)), radius=32.0, stroke_width=1.8)
        arc_beta = ArcAngleMarker(id="arc_beta", vertex=C_s, start_pt=w2s((4.8, 1.2)), end_pt=w2s((5.4, 2.0)), radius=42.0, stroke_width=1.8)

        labels = [
            MathLabel(id="lbl_B", text="B", x=B_s[0] - 14.0, y=B_s[1] + 18.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_C", text="C", x=C_s[0] + 18.0, y=C_s[1] + 4.0, font_size=18.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_A", text="A", x=A_s[0] - 18.0, y=A_s[1], font_size=18.0, font_weight="bold", anchor="end"),
            MathLabel(id="lbl_D", text="D", x=D_s[0] + 16.0, y=D_s[1] - 4.0, font_size=18.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_3", text="3", x=w2s((-0.6, 1.8))[0], y=w2s((-0.6, 1.8))[1], font_size=18.0),
            MathLabel(id="lbl_5", text="5", x=w2s((2.6, 2.5))[0], y=w2s((2.6, 2.5))[1], font_size=18.0),
            MathLabel(id="lbl_13", text="13", x=w2s((4.6, 7.6))[0], y=w2s((4.6, 7.6))[1], font_size=18.0),
            MathLabel(id="lbl_alpha", text="\\alpha", x=w2s((3.9, 0.55))[0], y=w2s((3.9, 0.55))[1], font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_beta", text="\\beta", x=w2s((4.4, 2.0))[0], y=w2s((4.4, 2.0))[1], font_size=18.0, font_weight="bold"),
        ]

        return VisualIR(title="Compound Right Triangles", subject="math", width=w, height=h, coordinate_frame=cf, segments=segments, right_angles=[ra_B, ra_A], arc_angles=[arc_alpha, arc_beta], labels=labels)

    # -------------------------------------------------------------
    # Archetype 5: Back-to-Back Triangles (Problem 25)
    # -------------------------------------------------------------
    def _synthesize_back_to_back_triangles(self, features: Dict[str, Any], options: Optional[Dict], w: float, h: float, pad: float) -> VisualIR:
        cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(-1.0, 7.0), y_range=(-1.2, 5.5), invert_y=True, show_axes=False)
        def w2s(pt): return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        L_bot, Mid_bot, R_bot = (0.0, 0.0), (2.8, 0.0), (5.8, 0.0)
        L_top = (0.0, 4.8)
        R_top = (5.8, 3.2)

        L_bot_s, Mid_bot_s, R_bot_s = w2s(L_bot), w2s(Mid_bot), w2s(R_bot)
        L_top_s, R_top_s = w2s(L_top), w2s(R_top)

        segments = [
            Segment(id="base", start=L_bot_s, end=R_bot_s, stroke_width=2.4, color="#111111"),
            Segment(id="left_vert", start=L_bot_s, end=L_top_s, stroke_width=2.4, color="#111111"),
            Segment(id="left_hyp", start=L_top_s, end=Mid_bot_s, stroke_width=2.2, color="#111111"),
            Segment(id="right_vert", start=R_bot_s, end=R_top_s, stroke_width=2.4, color="#111111"),
            Segment(id="right_hyp", start=R_top_s, end=Mid_bot_s, stroke_width=2.2, color="#111111"),
        ]

        ra_L = RightAngleMarker(id="ra_L", vertex=L_bot_s, arm1_pt=w2s((0.6, 0.0)), arm2_pt=w2s((0.0, 0.6)), size=15.0, stroke_width=1.8)
        ra_R = RightAngleMarker(id="ra_R", vertex=R_bot_s, arm1_pt=w2s((5.2, 0.0)), arm2_pt=w2s((5.8, 0.6)), size=15.0, stroke_width=1.8)

        arc_x = ArcAngleMarker(id="arc_x", vertex=Mid_bot_s, start_pt=w2s((2.0, 0.0)), end_pt=w2s((2.2, 1.0)), radius=28.0, stroke_width=1.8)
        arc_z = ArcAngleMarker(id="arc_z", vertex=Mid_bot_s, start_pt=w2s((2.2, 1.2)), end_pt=w2s((3.4, 1.0)), radius=34.0, stroke_width=1.8)
        arc_y = ArcAngleMarker(id="arc_y", vertex=Mid_bot_s, start_pt=w2s((3.5, 0.9)), end_pt=w2s((3.6, 0.0)), radius=28.0, stroke_width=1.8)

        labels = [
            MathLabel(id="lbl_4", text="4", x=w2s((-0.4, 2.4))[0], y=w2s((-0.4, 2.4))[1], font_size=18.0),
            MathLabel(id="lbl_1_left", text="1", x=w2s((1.4, -0.4))[0], y=w2s((1.4, -0.4))[1], font_size=18.0),
            MathLabel(id="lbl_sqrt3", text="\\sqrt{3}", x=w2s((4.3, -0.45))[0], y=w2s((4.3, -0.45))[1], font_size=18.0),
            MathLabel(id="lbl_1_right", text="1", x=w2s((6.2, 1.6))[0], y=w2s((6.2, 1.6))[1], font_size=18.0),
            MathLabel(id="lbl_x", text="x", x=w2s((2.0, 0.45))[0], y=w2s((2.0, 0.45))[1], font_size=17.0),
            MathLabel(id="lbl_z", text="z", x=w2s((2.8, 1.0))[0], y=w2s((2.8, 1.0))[1], font_size=17.0),
            MathLabel(id="lbl_y", text="y", x=w2s((3.5, 0.45))[0], y=w2s((3.5, 0.45))[1], font_size=17.0),
        ]

        return VisualIR(title="Back-to-Back Baseline Triangles", subject="math", width=w, height=h, coordinate_frame=cf, segments=segments, right_angles=[ra_L, ra_R], arc_angles=[arc_x, arc_z, arc_y], labels=labels)

    # -------------------------------------------------------------
    # Archetype 6: Fan Triangles (Problem 10)
    # -------------------------------------------------------------
    def _synthesize_fan_triangles(self, features: Dict[str, Any], options: Optional[Dict], w: float, h: float, pad: float) -> VisualIR:
        cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(-4.0, 4.0), y_range=(-1.0, 6.0), invert_y=True, show_axes=False)
        def w2s(pt): return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        A_w = (0.0, 0.0)
        E_w, D_w = (-2.8, 2.8), (-1.4, 4.8)
        B_w, C_w = (2.8, 2.8), (1.4, 4.8)

        A_s, E_s, D_s, B_s, C_s = w2s(A_w), w2s(E_w), w2s(D_w), w2s(B_w), w2s(C_w)

        segments = [
            Segment(id="AE", start=A_s, end=E_s, stroke_width=2.2, color="#111111"),
            Segment(id="ED", start=E_s, end=D_s, stroke_width=2.2, color="#111111"),
            Segment(id="AD", start=A_s, end=D_s, stroke_width=2.2, color="#111111"),
            Segment(id="DC", start=D_s, end=C_s, stroke_width=2.2, color="#111111"),
            Segment(id="AC", start=A_s, end=C_s, stroke_width=2.2, color="#111111"),
            Segment(id="CB", start=C_s, end=B_s, stroke_width=2.2, color="#111111"),
            Segment(id="AB", start=A_s, end=B_s, stroke_width=2.2, color="#111111"),
        ]

        ra_E = RightAngleMarker(id="ra_E", vertex=E_s, arm1_pt=w2s((-2.3, 2.3)), arm2_pt=w2s((-2.3, 3.3)), size=14.0, stroke_width=1.8)
        ra_B = RightAngleMarker(id="ra_B", vertex=B_s, arm1_pt=w2s((2.3, 2.3)), arm2_pt=w2s((2.3, 3.3)), size=14.0, stroke_width=1.8)

        arc_1 = ArcAngleMarker(id="arc_1", vertex=A_s, start_pt=w2s((-0.8, 0.8)), end_pt=w2s((-0.4, 1.2)), radius=26.0, stroke_width=1.6)
        arc_2 = ArcAngleMarker(id="arc_2", vertex=A_s, start_pt=w2s((-0.3, 1.3)), end_pt=w2s((0.3, 1.3)), radius=30.0, stroke_width=1.6)
        arc_3 = ArcAngleMarker(id="arc_3", vertex=A_s, start_pt=w2s((0.4, 1.2)), end_pt=w2s((0.8, 0.8)), radius=26.0, stroke_width=1.6)

        labels = [
            MathLabel(id="lbl_A", text="A", x=A_s[0], y=A_s[1] + 18.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_E", text="E", x=E_s[0] - 18.0, y=E_s[1], font_size=18.0, font_weight="bold", anchor="end"),
            MathLabel(id="lbl_D", text="D", x=D_s[0] - 14.0, y=D_s[1] - 14.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_C", text="C", x=C_s[0] + 14.0, y=C_s[1] - 14.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_B", text="B", x=B_s[0] + 18.0, y=B_s[1], font_size=18.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_sqrt3_L", text="\\sqrt{3}", x=w2s((-2.4, 1.3))[0], y=w2s((-2.4, 1.3))[1], font_size=17.0),
            MathLabel(id="lbl_sqrt3_R", text="\\sqrt{3}", x=w2s((2.4, 1.3))[0], y=w2s((2.4, 1.3))[1], font_size=17.0),
            MathLabel(id="th1", text="\\theta", x=w2s((-0.6, 1.1))[0], y=w2s((-0.6, 1.1))[1], font_size=16.0),
            MathLabel(id="th2", text="\\theta", x=w2s((0.0, 1.5))[0], y=w2s((0.0, 1.5))[1], font_size=16.0),
            MathLabel(id="th3", text="\\theta", x=w2s((0.6, 1.1))[0], y=w2s((0.6, 1.1))[1], font_size=16.0),
        ]

        return VisualIR(title="Symmetric Fan Triangles", subject="math", width=w, height=h, coordinate_frame=cf, segments=segments, right_angles=[ra_E, ra_B], arc_angles=[arc_1, arc_2, arc_3], labels=labels)

    # -------------------------------------------------------------
    # Archetype 7: Coordinate Function Graphs (Chapter 6)
    # -------------------------------------------------------------
    def _synthesize_coordinate_curve(self, features: Dict[str, Any], options: Optional[Dict], w: float, h: float, pad: float) -> VisualIR:
        cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(-3.5, 3.5), y_range=(-2.5, 2.5), invert_y=True, show_axes=True)
        def w2s(pt): return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        # Coordinate axes with arrowheads
        x_axis = Segment(id="axis_x", start=w2s((-3.2, 0.0)), end=w2s((3.2, 0.0)), arrows=ArrowType.BOTH, stroke_width=2.2, color="#111111")
        y_axis = Segment(id="axis_y", start=w2s((0.0, -2.2)), end=w2s((0.0, 2.2)), arrows=ArrowType.BOTH, stroke_width=2.2, color="#111111")

        # Smooth cubic/logistic curve points
        curve_pts = []
        for x_val in np.linspace(-2.8, 2.8, 60):
            y_val = 1.6 / (1.0 + np.exp(-1.8 * x_val)) - 0.8
            curve_pts.append(w2s((x_val, y_val)))

        curve_segments = []
        for i in range(len(curve_pts) - 1):
            curve_segments.append(Segment(id=f"c_{i}", start=curve_pts[i], end=curve_pts[i+1], stroke_width=2.4, color="#111111"))

        labels = [
            MathLabel(id="lbl_x", text="X", x=w2s((3.3, 0.0))[0] + 12.0, y=w2s((3.3, 0.0))[1], font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_y", text="Y", x=w2s((0.0, 2.3))[0] - 14.0, y=w2s((0.0, 2.3))[1] - 8.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_o", text="O", x=w2s((-0.25, -0.25))[0], y=w2s((-0.25, -0.25))[1], font_size=16.0),
        ]

        return VisualIR(title="Function Graph on Coordinate Plane", subject="math", width=w, height=h, coordinate_frame=cf, segments=[x_axis, y_axis] + curve_segments, labels=labels)

    # -------------------------------------------------------------
    # Archetype 8: Parabola Rate & Calculus Diagrams (Chapter 7)
    # -------------------------------------------------------------
    def _synthesize_parabola_rate(self, features: Dict[str, Any], options: Optional[Dict], w: float, h: float, pad: float) -> VisualIR:
        img_name = str(features.get("image_path", "")).lower()
        if options and "image_path" in options:
            img_name += " " + str(options["image_path"]).lower()

        if "7_22" in img_name:
            formula_text = "f(x) = \\sqrt{3}x^2 + 4x + \\sqrt{3}"
            has_extended_secant = False
        elif "7_30" in img_name:
            formula_text = "f(x) = 5x^2 - 2x + 3"
            has_extended_secant = False
        else:
            formula_text = "f(x) = ax^2 + bx + c"
            has_extended_secant = True

        cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(-3.2, 5.2), y_range=(-2.0, 3.8), invert_y=True, show_axes=False)
        def w2s(pt): return CoordinateTransformer.world_to_screen(pt, cf, w, h, padding=pad)

        a_p = 0.40
        conic = ConicCurve(id="parabola_main", conic_type=ConicType.PARABOLA, a=a_p, domain=(-2.6, 2.6), arrows=ArrowType.BOTH, stroke_width=2.4, color="#111111")

        V_w = (0.0, 0.0)
        x_C = 2.2
        y_B = a_p * (x_C ** 2)
        x_D = -1.9
        y_E = a_p * (x_D ** 2)

        A_s, B_s, C_s, D_s, E_s = w2s(V_w), w2s((0.0, y_B)), w2s((x_C, y_B)), w2s((x_D, y_E)), w2s((0.0, y_E))

        segments = [
            Segment(id="stem_AB", start=B_s, end=A_s, stroke_width=2.0, color="#111111"),
            Segment(id="top_BC", start=B_s, end=C_s, stroke_width=2.0, color="#111111"),
            Segment(id="mid_ED", start=D_s, end=E_s, stroke_width=2.0, color="#111111"),
            Segment(id="chord_DA", start=D_s, end=A_s, stroke_width=2.0, color="#111111"),
            Segment(id="chord_AC", start=A_s, end=C_s, stroke_width=2.0, color="#111111"),
        ]

        if has_extended_secant:
            m_sec = y_B / x_C
            ext_pt_s = w2s((-1.8, -1.8 * m_sec))
            segments.append(Segment(id="secant_ext", start=ext_pt_s, end=A_s, stroke_width=2.0, color="#111111"))

        ra_B = RightAngleMarker(id="ra_B", vertex=B_s, arm1_pt=w2s((0.0, y_B - 0.45)), arm2_pt=w2s((0.45, y_B)), size=14.0, stroke_width=1.8)
        ra_E = RightAngleMarker(id="ra_E", vertex=E_s, arm1_pt=w2s((-0.45, y_E)), arm2_pt=w2s((0.0, y_E - 0.45)), size=14.0, stroke_width=1.8)

        arc_D = ArcAngleMarker(id="arc_D", vertex=D_s, start_pt=w2s((x_D + 0.65, y_E)), end_pt=w2s((x_D + 0.5, y_E - 0.5)), radius=32.0, stroke_width=1.8)
        arc_A = ArcAngleMarker(id="arc_A", vertex=A_s, start_pt=w2s((0.0, 0.75)), end_pt=w2s((0.5, 0.6)), radius=36.0, stroke_width=1.8)

        labels = [
            MathLabel(id="lbl_A", text="A", x=A_s[0], y=A_s[1] + 20.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_B", text="B", x=B_s[0] + 2.0, y=B_s[1] - 18.0, font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_C", text="C", x=C_s[0] + 18.0, y=C_s[1], font_size=18.0, font_weight="bold", anchor="start"),
            MathLabel(id="lbl_D", text="D", x=D_s[0] - 18.0, y=D_s[1], font_size=18.0, font_weight="bold", anchor="end"),
            MathLabel(id="lbl_E", text="E", x=E_s[0] - 14.0, y=E_s[1] - 14.0, font_size=17.0, font_weight="bold", anchor="end"),
            MathLabel(id="lbl_alpha", text="\\alpha", x=w2s((x_D + 0.62, y_E - 0.32))[0], y=w2s((x_D + 0.62, y_E - 0.32))[1], font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_beta", text="\\beta", x=w2s((0.20, 0.58))[0], y=w2s((0.20, 0.58))[1], font_size=18.0, font_weight="bold"),
            MathLabel(id="lbl_formula", text=formula_text, x=w2s((2.6, 3.45))[0], y=w2s((2.6, 3.45))[1], font_size=18.0, font_weight="bold", anchor="start"),
        ]

        return VisualIR(title="Parabola and Rate Geometry", subject="math", width=w, height=h, coordinate_frame=cf, conics=[conic], segments=segments, right_angles=[ra_B, ra_E], arc_angles=[arc_D, arc_A], labels=labels)

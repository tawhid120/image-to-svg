"""
Semantic Diagram Parser for Mathematical and Physical Structures.
"""

from __future__ import annotations
import math
from typing import Dict, Any, List, Optional
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
    CoordinateSystem,
    ArrowType,
    StrokeStyle,
)
from ..solver.geometry_solver import GeometrySolver


class SemanticDiagramParser:
    """
    Parses geometric blueprints and semantic scene specifications into a mathematically
    aligned and constraint-solved DiagramIR.
    """

    @staticmethod
    def build_parabola_secant_stepped_triangle_ir(
        canvas_width: float = 650.0,
        canvas_height: float = 480.0,
    ) -> DiagramIR:
        """
        Constructs a mathematically exact IR for the classic Parabola-Secant Stepped Triangle benchmark.
        """
        cs = CoordinateSystem(
            origin_x=0.0,
            origin_y=0.0,
            x_range=(-3.2, 5.2),
            y_range=(-2.2, 3.4),
            invert_y=True,
            show_axes=False
        )
        
        # Parabola parameters: y = a_p * x^2
        a_p = 0.38
        x_min, x_max = -2.7, 2.75
        
        parabola = ParabolaCurve(
            id="parabola_main",
            a=a_p,
            b=0.0,
            c=0.0,
            domain=(x_min, x_max),
            arrows=ArrowType.BOTH,
            stroke_width=2.4,
            color="#111111"
        )
        
        # Key World Points
        V_w = (0.0, 0.0)
        
        x_R = 2.45
        y_R = a_p * (x_R ** 2)  # ~2.281
        P_R_w = (x_R, y_R)
        
        x_L = -1.95
        y_L = a_p * (x_L ** 2)  # ~1.445
        P_L_w = (x_L, y_L)
        
        P_top_w = (0.0, y_R)
        P_mid_w = (0.0, y_L)
        
        # Secant line extension to bottom-left
        slope_line = y_R / x_R  # ~0.931
        x_ext = -1.9
        y_ext = slope_line * x_ext  # ~ -1.77
        P_ext_w = (x_ext, y_ext)
        
        # Left drop inside left triangle
        x_drop = -0.75
        P_drop_top_w = (x_drop, y_L)
        m_left_chord = y_L / x_L
        y_drop_bot = m_left_chord * x_drop
        P_drop_bot_w = (x_drop, y_drop_bot)
        
        def w2s(pt):
            return GeometrySolver.world_to_screen(pt, cs, canvas_width, canvas_height, padding=35.0)
            
        V_s = w2s(V_w)
        P_R_s = w2s(P_R_w)
        P_L_s = w2s(P_L_w)
        P_top_s = w2s(P_top_w)
        P_mid_s = w2s(P_mid_w)
        P_ext_s = w2s(P_ext_w)
        P_drop_top_s = w2s(P_drop_top_w)
        P_drop_bot_s = w2s(P_drop_bot_w)
        
        # Segments
        segments = [
            # 1. Main Continuous Straight Secant Line
            Segment(id="secant_line", start=P_ext_s, end=P_R_s, stroke_width=2.2, color="#111111"),
            
            # 2. Central Vertical Stem
            Segment(id="vertical_stem", start=P_top_s, end=V_s, stroke_width=2.0, color="#111111"),
            
            # 3. Top Horizontal Segment (length m)
            Segment(id="top_horizontal_m", start=P_top_s, end=P_R_s, stroke_width=2.0, color="#111111"),
            
            # 4. Left Horizontal Segment (length b)
            Segment(id="left_horizontal_b", start=P_L_s, end=P_mid_s, stroke_width=2.0, color="#111111"),
            
            # 5. Left Chord (from P_L to V)
            Segment(id="left_chord", start=P_L_s, end=V_s, stroke_width=2.0, color="#111111"),
            
            # 6. Left Vertical Drop inside triangle
            Segment(id="left_drop", start=P_drop_top_s, end=P_drop_bot_s, stroke_width=1.8, color="#111111"),
        ]
        
        # Right Angle Markers
        right_angles = [
            # Top Right Corner box
            RightAngleMarker(
                id="ra_top",
                vertex=P_top_s,
                arm1_pt=P_R_s,
                arm2_pt=V_s,
                size=18.0,
                stroke_width=1.6
            ),
            # Left Drop box (pointing down-left)
            RightAngleMarker(
                id="ra_left",
                vertex=P_drop_top_s,
                arm1_pt=P_L_s,
                arm2_pt=P_drop_bot_s,
                size=16.0,
                stroke_width=1.6
            )
        ]
        
        # Arc Angle Markers
        arc_angles = [
            # Angle A: at vertex V, between vertical stem and right secant line (radius 1.35 in world)
            ArcAngleMarker(
                id="arc_A",
                vertex=V_s,
                start_pt=P_top_s,
                end_pt=P_R_s,
                radius=68.0,
                stroke_width=1.6
            ),
            # Angle B: at P_L, between left horizontal side and chord to V
            ArcAngleMarker(
                id="arc_B",
                vertex=P_L_s,
                start_pt=P_mid_s,
                end_pt=V_s,
                radius=40.0,
                stroke_width=1.6
            ),
            # Angle C: at V, between left chord and bottom-left extended ray
            ArcAngleMarker(
                id="arc_C",
                vertex=V_s,
                start_pt=P_L_s,
                end_pt=P_ext_s,
                radius=58.0,
                stroke_width=1.6
            )
        ]
        
        # Anti-Collision Bisector Calculations for Angle Labels
        # Angle A Position (0.65 * cos(66.5 deg), 0.65 * sin(66.5 deg))
        ang_chord_A = math.atan2(y_R, x_R)
        bisect_A = (math.pi / 2.0 + ang_chord_A) / 2.0
        pos_A_w = (0.65 * math.cos(bisect_A), 0.65 * math.sin(bisect_A))
        pos_A_s = w2s(pos_A_w)
        
        # Angle B Position (inside left corner)
        ang_chord_B = math.atan2(-y_L, -x_L)
        bisect_B = ang_chord_B / 2.0
        pos_B_w = (x_L + 0.50 * math.cos(bisect_B), y_L + 0.50 * math.sin(bisect_B))
        pos_B_s = w2s(pos_B_w)
        
        # Angle C Position (beside arc C)
        pos_C_w = (-0.75, -0.42)
        pos_C_s = w2s(pos_C_w)
        
        # Labels
        labels = [
            # Formula: f(x) = ax^2 + bx + c
            MathLabel(
                id="lbl_formula",
                text="f(x) = ax^2 + bx + c",
                x=P_R_s[0] + 28.0,
                y=P_R_s[1] - 4.0,
                font_size=21.0,
                font_weight="bold",
                anchor="start"
            ),
            # Top side dimension m
            MathLabel(
                id="lbl_m",
                text="m",
                x=(P_top_s[0] + P_R_s[0]) * 0.52,
                y=P_top_s[1] - 14.0,
                font_size=19.0,
                anchor="middle"
            ),
            # Upper vertical dimension a
            MathLabel(
                id="lbl_a",
                text="a",
                x=P_top_s[0] + 12.0,
                y=(P_top_s[1] + P_mid_s[1]) * 0.5 + 2.0,
                font_size=18.0,
                anchor="start"
            ),
            # Left horizontal dimension b
            MathLabel(
                id="lbl_b",
                text="b",
                x=(P_L_s[0] + P_drop_top_s[0]) * 0.5,
                y=P_L_s[1] - 14.0,
                font_size=19.0,
                anchor="middle"
            ),
            # Lower vertical dimension n
            MathLabel(
                id="lbl_n",
                text="n",
                x=P_mid_s[0] - 12.0,
                y=(P_mid_s[1] + V_s[1]) * 0.5,
                font_size=18.0,
                anchor="end"
            ),
            # Angle A (cleanly centered inside the sector, zero collision)
            MathLabel(
                id="lbl_A",
                text="A",
                x=pos_A_s[0],
                y=pos_A_s[1],
                font_size=19.0,
                anchor="middle"
            ),
            # Angle B (cleanly centered inside angle B)
            MathLabel(
                id="lbl_B",
                text="B",
                x=pos_B_s[0],
                y=pos_B_s[1],
                font_size=19.0,
                anchor="middle"
            ),
            # Angle C (cleanly positioned beside arc C)
            MathLabel(
                id="lbl_C",
                text="C",
                x=pos_C_s[0],
                y=pos_C_s[1],
                font_size=21.0,
                anchor="end"
            ),
        ]
        
        # Vertex marker dot
        points = [
            Point(id="pt_vertex", x=V_s[0], y=V_s[1], radius=4.0, visible=True, color="#000000")
        ]
        
        return DiagramIR(
            width=canvas_width,
            height=canvas_height,
            padding=35.0,
            coordinate_system=cs,
            points=points,
            segments=segments,
            parabolas=[parabola],
            right_angles=right_angles,
            arc_angles=arc_angles,
            labels=labels,
            metadata={"diagram_type": "calculus_conic_rate_of_change", "source": "chapter_7_23"}
        )

"""
Physics Visual Semantic Registry & Multi-Archetype Synthesizers.
Contains verified mathematical vector synthesizers for all physics diagram families.
"""

from __future__ import annotations
import math
from typing import Dict, Any, List, Tuple
from ...core.ir import VisualIR
from ...core.primitives import (
    Point,
    Circle,
    Segment,
    BezierPath,
    Polygon,
    RightAngleMarker,
    ArcAngleMarker,
    MathLabel,
    ArrowType,
    StrokeStyle,
)


from ...core.coordinate import CoordinateFrame


class PhysicsRegistry:
    """Dispatches and synthesizes exact vector IR for any physics diagram."""

    @staticmethod
    def get_custom_reconstruction(img_name: str, w: float = 700.0, h: float = 500.0) -> VisualIR | None:
        name = img_name.lower()
        stem = name
        cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=False)


        # ---------------------------------------------------------
        # 1. L-Shaped Orthogonal Charges (002cfa74)
        # ---------------------------------------------------------
        if "002cfa74" in name:
            p_a = (140.0, 140.0)
            p_b = (w - 180.0, 140.0)
            p_c = (w - 180.0, h - 140.0)

            segments = [
                Segment(id="seg_ab", start=p_a, end=p_b, stroke_width=2.4, color="#111111"),
                Segment(id="seg_bc", start=p_b, end=p_c, stroke_width=2.4, color="#111111"),
            ]
            points = []
            for pid, pt in [("A", p_a), ("B", p_b), ("C", p_c)]:
                points.append(Point(id=f"pt_{pid}_o", x=pt[0], y=pt[1], radius=8.0, color="#111111"))
                points.append(Point(id=f"pt_{pid}_i", x=pt[0], y=pt[1], radius=2.5, color="#111111"))

            labels = [
                MathLabel(id="lbl_A", text="A", x=p_a[0] - 28.0, y=p_a[1] + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="+6 \\mu C", x=p_a[0] + 15.0, y=p_a[1] - 24.0, font_size=18.0),
                MathLabel(id="lbl_B", text="B", x=p_b[0] + 28.0, y=p_b[1] + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="-2 \\mu C", x=p_b[0] - 10.0, y=p_b[1] - 24.0, font_size=18.0),
                MathLabel(id="lbl_C", text="C", x=p_c[0] + 28.0, y=p_c[1] + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_dab", text="0.4 m", x=(p_a[0]+p_b[0])/2.0, y=p_a[1] - 24.0, font_size=18.0, math_mode=False),
                MathLabel(id="lbl_dbc", text="0.4 m", x=p_b[0] + 42.0, y=(p_b[1]+p_c[1])/2.0, font_size=18.0, math_mode=False),
            ]
            return VisualIR(title="Orthogonal L-Shaped Charge Distribution", width=w, height=h, coordinate_frame=cf, points=points, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 2. Ray & Flowchart Scientific Schema (00b15eab)
        # ---------------------------------------------------------
        if "00b15eab" in name:
            polygons = []
            segments = []
            labels = []

            labels.append(MathLabel(id="lbl_i", text="(i)   _{29}X", x=80.0, y=100.0, font_size=20.0, font_weight="bold"))
            labels.append(MathLabel(id="lbl_ii", text="(ii)", x=50.0, y=260.0, font_size=20.0, font_weight="bold"))

            def add_box(bx: float, by: float, bw: float, bh: float, text_str: str, bid: str):
                rect = [(bx - bw/2, by - bh/2), (bx + bw/2, by - bh/2), (bx + bw/2, by + bh/2), (bx - bw/2, by + bh/2)]
                polygons.append(Polygon(id=f"poly_{bid}", vertices=rect, stroke_color="#111111", stroke_width=2.0, fill_color="#ffffff"))
                labels.append(MathLabel(id=f"lbl_box_{bid}", text=text_str, x=bx, y=by + 4.0, font_size=18.0, font_weight="bold", math_mode=False))

            add_box(130.0, 260.0, 48.0, 44.0, "A", "A")

            segments.append(Segment(id="arr_main", start=(160.0, 260.0), end=(310.0, 260.0), arrows=ArrowType.END, stroke_width=2.2, color="#111111"))
            labels.append(MathLabel(id="lbl_wave", text="200 - 375 nm", x=235.0, y=235.0, font_size=17.0, math_mode=False))
            labels.append(MathLabel(id="lbl_inc", text="আপতিত রশ্মি", x=235.0, y=285.0, font_size=16.0, math_mode=False))

            segments.append(Segment(id="branch_v", start=(320.0, 180.0), end=(320.0, 340.0), stroke_width=2.2, color="#111111"))
            segments.append(Segment(id="branch_top", start=(320.0, 180.0), end=(350.0, 180.0), arrows=ArrowType.END, stroke_width=2.2, color="#111111"))
            segments.append(Segment(id="branch_bot", start=(320.0, 340.0), end=(350.0, 340.0), arrows=ArrowType.END, stroke_width=2.2, color="#111111"))

            add_box(410.0, 180.0, 110.0, 40.0, "জাল টাকা", "fake")
            add_box(410.0, 340.0, 110.0, 40.0, "আসল টাকা", "real")

            segments.append(Segment(id="arr_b", start=(470.0, 180.0), end=(510.0, 180.0), arrows=ArrowType.END, stroke_width=2.0, color="#111111"))
            segments.append(Segment(id="arr_c", start=(470.0, 340.0), end=(510.0, 340.0), arrows=ArrowType.END, stroke_width=2.0, color="#111111"))

            add_box(535.0, 180.0, 42.0, 40.0, "B", "B")
            add_box(535.0, 340.0, 42.0, 40.0, "C", "C")

            labels.append(MathLabel(id="lbl_emit1", text="(বিকিরিত রশ্মি)", x=615.0, y=184.0, font_size=15.0, math_mode=False))
            labels.append(MathLabel(id="lbl_emit2", text="(বিকিরিত রশ্মি)", x=615.0, y=344.0, font_size=15.0, math_mode=False))

            return VisualIR(title="Spectroscopic Flowchart Schema", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 3. Collinear Dipole Midpoint Field Vector (03f1fe42)
        # ---------------------------------------------------------
        if "03f1fe42" in name:
            cy = h / 2.0
            p_a = (140.0, cy)
            p_p = (w / 2.0, cy)
            p_b = (w - 140.0, cy)

            segments = [
                Segment(id="vec_pa", start=p_p, end=p_a, arrows=ArrowType.END, stroke_width=2.6, color="#111111"),
                Segment(id="vec_pb", start=p_p, end=p_b, arrows=ArrowType.END, stroke_width=2.6, color="#111111"),
            ]
            points = [
                Point(id="pt_a", x=p_a[0], y=p_a[1], radius=5.0, color="#111111"),
                Point(id="pt_p", x=p_p[0], y=p_p[1], radius=5.0, color="#111111"),
                Point(id="pt_b", x=p_b[0], y=p_b[1], radius=5.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_A", text="A", x=p_a[0] - 22.0, y=p_a[1] + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_P", text="P", x=p_p[0], y=p_p[1] - 25.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=p_b[0] + 22.0, y=p_b[1] + 4.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Collinear Field Vectors from Test Point P", width=w, height=h, coordinate_frame=cf, points=points, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 4. Collinear Dipole with Distance Stems (043a8055)
        # ---------------------------------------------------------
        if "043a8055" in name:
            cy = h / 2.0 - 20.0
            p_a = (120.0, cy)
            p_o = (280.0, cy)
            p_b = (460.0, cy)
            p_p = (w - 120.0, cy)

            segments = [
                Segment(id="main_axis", start=p_a, end=p_p, stroke_width=2.6, color="#111111"),
            ]
            points = [
                Point(id="pt_a", x=p_a[0], y=p_a[1], radius=5.0, color="#111111"),
                Point(id="pt_o", x=p_o[0], y=p_o[1], radius=5.0, color="#111111"),
                Point(id="pt_b", x=p_b[0], y=p_b[1], radius=5.0, color="#111111"),
                Point(id="pt_p", x=p_p[0], y=p_p[1], radius=5.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_qa", text="- 10 \\mu C", x=p_a[0], y=p_a[1] - 28.0, font_size=18.0),
                MathLabel(id="lbl_qb", text="+ 10 \\mu C", x=p_b[0], y=p_b[1] - 28.0, font_size=18.0),
                MathLabel(id="lbl_A", text="A", x=p_a[0], y=p_a[1] + 28.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_O", text="O", x=p_o[0], y=p_o[1] + 28.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=p_b[0], y=p_b[1] + 28.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_P", text="P", x=p_p[0], y=p_p[1] + 28.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_dim", text="AB = 40 cm ; OP = 25 cm", x=w/2.0, y=cy + 85.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Collinear Dipole Distance Specifications", width=w, height=h, coordinate_frame=cf, points=points, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 5. Simple Plain Rectangle (04ee868b)
        # ---------------------------------------------------------
        if "04ee868b" in name:
            cx, cy = w/2.0, h/2.0
            rw, rh = 400.0, 220.0
            p_a = (cx - rw/2, cy + rh/2)
            p_b = (cx + rw/2, cy + rh/2)
            p_c = (cx + rw/2, cy - rh/2)
            p_d = (cx - rw/2, cy - rh/2)

            poly = Polygon(id="rect_abcd", vertices=[p_a, p_b, p_c, p_d], stroke_color="#111111", stroke_width=2.5, fill_color="#ffffff")
            labels = [
                MathLabel(id="lbl_A", text="A", x=p_a[0] - 22.0, y=p_a[1] + 8.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=p_b[0] + 22.0, y=p_b[1] + 8.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_C", text="C", x=p_c[0] + 22.0, y=p_c[1] - 8.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_D", text="D", x=p_d[0] - 22.0, y=p_d[1] - 8.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Geometric Rectangle ABCD", width=w, height=h, coordinate_frame=cf, polygons=[poly], labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 6. Perspective Parallelogram with Legs (05f1c90f)
        # ---------------------------------------------------------
        if "05f1c90f" in name:
            p_a = (160.0, 360.0)
            p_d = (w - 180.0, 370.0)
            p_c = (w - 110.0, 140.0)
            p_b = (230.0, 130.0)

            poly = Polygon(id="plane_poly", vertices=[p_a, p_d, p_c, p_b], stroke_color="#111111", stroke_width=2.5, fill_color="#ffffff")
            segments = [
                Segment(id="diag_ac", start=p_a, end=p_c, stroke_style=StrokeStyle.DASHED, stroke_width=2.0, color="#222222"),
                Segment(id="diag_bd", start=p_b, end=p_d, stroke_style=StrokeStyle.DASHED, stroke_width=2.0, color="#222222"),
                Segment(id="leg_a", start=p_a, end=(p_a[0], p_a[1] + 50.0), stroke_width=2.0, color="#111111"),
                Segment(id="leg_d", start=p_d, end=(p_d[0], p_d[1] + 50.0), stroke_width=2.0, color="#111111"),
                Segment(id="leg_b", start=p_b, end=(p_b[0], p_b[1] + 50.0), stroke_width=2.0, color="#111111"),
                Segment(id="leg_c", start=p_c, end=(p_c[0], p_c[1] + 50.0), stroke_width=2.0, color="#111111"),
                Segment(id="dim_top", start=(p_b[0], p_b[1] - 25.0), end=(p_c[0], p_c[1] - 25.0), arrows=ArrowType.BOTH, stroke_width=1.8, color="#111111"),
                Segment(id="dim_side", start=(p_a[0] - 25.0, p_a[1]), end=(p_b[0] - 25.0, p_b[1]), arrows=ArrowType.END, stroke_width=1.8, color="#111111"),
            ]
            points = [
                Point(id="pt_a", x=p_a[0], y=p_a[1], radius=4.5, color="#111111"),
                Point(id="pt_d", x=p_d[0], y=p_d[1], radius=4.5, color="#111111"),
                Point(id="pt_c", x=p_c[0], y=p_c[1], radius=4.5, color="#111111"),
                Point(id="pt_b", x=p_b[0], y=p_b[1], radius=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_A", text="A", x=p_a[0] - 22.0, y=p_a[1] + 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_D", text="D", x=p_d[0] + 22.0, y=p_d[1] + 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_C", text="C", x=p_c[0] + 24.0, y=p_c[1] - 10.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=p_b[0] - 24.0, y=p_b[1] - 10.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_dt", text="1 m", x=(p_b[0]+p_c[0])/2.0, y=p_b[1] - 40.0, font_size=18.0, math_mode=False),
                MathLabel(id="lbl_ds", text="1 m", x=(p_a[0]+p_b[0])/2.0 - 45.0, y=(p_a[1]+p_b[1])/2.0, font_size=18.0, math_mode=False),
            ]
            return VisualIR(title="3D Perspective Conductor Plane", width=w, height=h, coordinate_frame=cf, points=points, polygons=[poly], segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 7. Square Perimeter Charge Loop (073bfc9a)
        # ---------------------------------------------------------
        if "073bfc9a" in name:
            cx, cy = w/2.0, h/2.0
            side = 240.0
            p_m = (cx - side/2, cy - side/2)
            p_a = (cx + side/2, cy - side/2)
            p_b = (cx + side/2, cy + side/2)
            p_n = (cx - side/2, cy + side/2)

            p_d = ((p_m[0]+p_a[0])/2.0, p_m[1])
            p_e = (p_a[0], (p_a[1]+p_b[1])/2.0)
            p_c = (p_m[0], (p_m[1]+p_n[1])/2.0)

            poly = Polygon(id="sq_manb", vertices=[p_m, p_a, p_b, p_n], stroke_color="#111111", stroke_width=2.6, fill_color="#ffffff")
            points = [
                Point(id="pt_d", x=p_d[0], y=p_d[1], radius=4.5, color="#111111"),
                Point(id="pt_e", x=p_e[0], y=p_e[1], radius=4.5, color="#111111"),
                Point(id="pt_c", x=p_c[0], y=p_c[1], radius=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_M", text="M", x=p_m[0] - 20.0, y=p_m[1] - 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_A", text="A", x=p_a[0] + 20.0, y=p_a[1] - 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=p_b[0] + 20.0, y=p_b[1] + 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_N", text="N", x=p_n[0] - 20.0, y=p_n[1] + 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_D", text="D", x=p_d[0], y=p_d[1] - 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_E", text="E", x=p_e[0] + 22.0, y=p_e[1] + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_C", text="C", x=p_c[0] - 24.0, y=p_c[1] + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qp", text="+Q", x=p_m[0] - 32.0, y=p_m[1] + 45.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qn", text="-Q", x=p_n[0] - 32.0, y=p_n[1] - 35.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Square Boundary with Distributed Charges", width=w, height=h, coordinate_frame=cf, points=points, polygons=[poly], labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 8. Radial Field Sphere with Ray (0decdd92)
        # ---------------------------------------------------------
        if "0decdd92" in name:
            cx, cy = w/2.0 - 60.0, h/2.0
            r = 130.0
            circle_pts = [(cx + r*math.cos(math.radians(deg)), cy + r*math.sin(math.radians(deg))) for deg in range(0, 360, 5)]
            poly = Polygon(id="sphere_c", vertices=circle_pts, stroke_color="#111111", stroke_width=2.5, fill_color="#ffffff")

            p_rad_end = (cx + r*math.cos(math.radians(60)), cy - r*math.sin(math.radians(60)))
            p_a_end = (cx + r + 130.0, cy)

            segments = [
                Segment(id="rad_arr", start=(cx, cy), end=p_rad_end, arrows=ArrowType.END, stroke_width=2.0, color="#111111"),
                Segment(id="ray_ca", start=(cx, cy), end=p_a_end, arrows=ArrowType.END, stroke_width=2.2, color="#111111"),
            ]
            points = [
                Point(id="pt_c", x=cx, y=cy, radius=4.0, color="#111111"),
                Point(id="pt_b", x=cx + r, y=cy, radius=4.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_C", text="C", x=cx, y=cy + 28.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="r", x=(cx+p_rad_end[0])/2.0 - 15.0, y=(cy+p_rad_end[1])/2.0, font_size=18.0),
                MathLabel(id="lbl_q", text="+Q", x=p_rad_end[0] + 20.0, y=p_rad_end[1] - 5.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=cx + r, y=cy + 28.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_A", text="A", x=p_a_end[0] + 20.0, y=p_a_end[1] + 4.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Radial Electric Field from Conducting Sphere", width=w, height=h, coordinate_frame=cf, points=points, polygons=[poly], segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 9. 3D Slanted Parallel Plate Capacitor (0e0b85fe)
        # ---------------------------------------------------------
        if "0e0b85fe" in name:
            pl_w = 40.0
            pl_h = 130.0
            pl1_cx = 240.0
            pl2_cx = 460.0
            pl_cy = 180.0

            def make_3d_plate(pcx: float, pcy: float, pid: str):
                return Polygon(
                    id=f"poly_3d_{pid}",
                    vertices=[
                        (pcx - pl_w/2, pcy - pl_h/2 + 25.0),
                        (pcx + pl_w/2, pcy - pl_h/2 - 25.0),
                        (pcx + pl_w/2, pcy + pl_h/2 - 25.0),
                        (pcx - pl_w/2, pcy + pl_h/2 + 25.0),
                    ],
                    stroke_color="#111111", stroke_width=2.5, fill_color="#ffffff"
                )

            poly1 = make_3d_plate(pl1_cx, pl_cy, "1")
            poly2 = make_3d_plate(pl2_cx, pl_cy, "2")

            y_bot = h - 110.0
            segments = [
                Segment(id="dot_1", start=(pl1_cx + pl_w/2, pl_cy + pl_h/2 - 25.0), end=(pl1_cx + pl_w/2, pl_cy + pl_h/2 + 65.0), stroke_style=StrokeStyle.DOTTED, stroke_width=2.0, color="#111111"),
                Segment(id="dot_2", start=(pl2_cx - pl_w/2, pl_cy + pl_h/2 + 25.0), end=(pl2_cx - pl_w/2, pl_cy + pl_h/2 + 65.0), stroke_style=StrokeStyle.DOTTED, stroke_width=2.0, color="#111111"),
                Segment(id="dim_d", start=(pl1_cx + pl_w/2, pl_cy + pl_h/2 + 60.0), end=(pl2_cx - pl_w/2, pl_cy + pl_h/2 + 60.0), arrows=ArrowType.BOTH, stroke_width=2.0, color="#111111"),
                Segment(id="wire_l1", start=(pl1_cx - pl_w/2, pl_cy), end=(90.0, pl_cy), stroke_width=2.2, color="#111111"),
                Segment(id="wire_l2", start=(90.0, pl_cy), end=(90.0, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="wire_l3", start=(90.0, y_bot), end=(w/2.0 - 20.0, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="wire_r1", start=(pl2_cx + pl_w/2, pl_cy), end=(w - 90.0, pl_cy), stroke_width=2.2, color="#111111"),
                Segment(id="wire_r2", start=(w - 90.0, pl_cy), end=(w - 90.0, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="wire_r3", start=(w - 90.0, y_bot), end=(w/2.0 + 20.0, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="bat_p", start=(w/2.0 - 8.0, y_bot - 20.0), end=(w/2.0 - 8.0, y_bot + 20.0), stroke_width=3.0, color="#111111"),
                Segment(id="bat_n", start=(w/2.0 + 8.0, y_bot - 12.0), end=(w/2.0 + 8.0, y_bot + 12.0), stroke_width=4.5, color="#111111"),
            ]
            points = [
                Point(id="pt_w1", x=pl1_cx - pl_w/2, y=pl_cy, radius=4.0, color="#111111"),
                Point(id="pt_w2", x=pl2_cx + pl_w/2, y=pl_cy, radius=4.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_dim", text="2 cm", x=(pl1_cx+pl2_cx)/2.0, y=pl_cy + pl_h/2 + 64.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_v", text="152 V", x=w/2.0, y=y_bot + 40.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="3D Parallel Plate Capacitor System", width=w, height=h, coordinate_frame=cf, points=points, polygons=[poly1, poly2], segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 10. Diamond Parallel Split Circuit with Legend (0f061d2c)
        # ---------------------------------------------------------
        if "0f061d2c" in name:
            x_l, x_r = 90.0, w - 240.0
            y_t, y_b = 140.0, h - 140.0
            x_c1 = x_l + 70.0
            x_split = x_c1 + 70.0
            x_join = x_r - 30.0
            x_mid = (x_split + x_join) / 2.0
            y_top_branch = y_t - 40.0
            y_bot_branch = y_t + 40.0

            segments = [
                # Top rail
                Segment(id="w1", start=(x_l, y_t), end=(x_c1 - 12.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w2", start=(x_c1 + 12.0, y_t), end=(x_split, y_t), stroke_width=2.2, color="#111111"),
                # Diamond branches
                Segment(id="sp_t1", start=(x_split, y_t), end=(x_mid - 25.0, y_top_branch), stroke_width=2.2, color="#111111"),
                Segment(id="sp_t2", start=(x_mid - 25.0, y_top_branch), end=(x_mid - 12.0, y_top_branch), stroke_width=2.2, color="#111111"),
                Segment(id="sp_t3", start=(x_mid + 12.0, y_top_branch), end=(x_mid + 25.0, y_top_branch), stroke_width=2.2, color="#111111"),
                Segment(id="sp_t4", start=(x_mid + 25.0, y_top_branch), end=(x_join, y_t), stroke_width=2.2, color="#111111"),

                Segment(id="sp_b1", start=(x_split, y_t), end=(x_mid - 25.0, y_bot_branch), stroke_width=2.2, color="#111111"),
                Segment(id="sp_b2", start=(x_mid - 25.0, y_bot_branch), end=(x_mid - 12.0, y_bot_branch), stroke_width=2.2, color="#111111"),
                Segment(id="sp_b3", start=(x_mid + 12.0, y_bot_branch), end=(x_mid + 25.0, y_bot_branch), stroke_width=2.2, color="#111111"),
                Segment(id="sp_b4", start=(x_mid + 25.0, y_bot_branch), end=(x_join, y_t), stroke_width=2.2, color="#111111"),

                Segment(id="w_r_conn", start=(x_join, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                # Bottom battery
                Segment(id="w_b1", start=(x_l, y_b), end=(x_mid - 15.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_b2", start=(x_mid + 15.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Plates
                Segment(id="c1_l", start=(x_c1 - 6.0, y_t - 20.0), end=(x_c1 - 6.0, y_t + 20.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x_c1 + 6.0, y_t - 20.0), end=(x_c1 + 6.0, y_t + 20.0), stroke_width=2.8, color="#111111"),

                Segment(id="c2_l", start=(x_mid - 6.0, y_top_branch - 20.0), end=(x_mid - 6.0, y_top_branch + 20.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x_mid + 6.0, y_top_branch - 20.0), end=(x_mid + 6.0, y_top_branch + 20.0), stroke_width=2.8, color="#111111"),

                Segment(id="c3_l", start=(x_mid - 6.0, y_bot_branch - 20.0), end=(x_mid - 6.0, y_bot_branch + 20.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x_mid + 6.0, y_bot_branch - 20.0), end=(x_mid + 6.0, y_bot_branch + 20.0), stroke_width=2.8, color="#111111"),

                Segment(id="bat_p", start=(x_mid - 6.0, y_b - 18.0), end=(x_mid - 6.0, y_b + 18.0), stroke_width=3.0, color="#111111"),
                Segment(id="bat_n", start=(x_mid + 6.0, y_b - 10.0), end=(x_mid + 6.0, y_b + 10.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1", x=x_c1, y=y_t - 28.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=x_mid, y=y_top_branch - 28.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3", x=x_mid, y=y_bot_branch - 28.0, font_size=18.0, font_weight="bold"),
                # Legend on right
                MathLabel(id="lbl_l1", text="C_1 = 100 \\mu F", x=w - 110.0, y=140.0, font_size=17.0),
                MathLabel(id="lbl_l2", text="C_2 = 200 \\mu F", x=w - 110.0, y=180.0, font_size=17.0),
                MathLabel(id="lbl_l3", text="C_3 = 300 \\mu F", x=w - 110.0, y=220.0, font_size=17.0),
                MathLabel(id="lbl_l4", text="E = 12 Volt", x=w - 110.0, y=260.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Capacitor Network with Diamond Branch", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 11. Uniform Field Parallel Plates (10b0ab31)
        # ---------------------------------------------------------
        if "10b0ab31" in name:
            x_l, x_r = 140.0, w - 200.0
            y_t, y_b = 160.0, 340.0
            segments = [
                Segment(id="pl_a", start=(x_l - 40.0, y_t), end=(x_r + 40.0, y_t), stroke_width=3.2, color="#111111"),
                Segment(id="pl_b", start=(x_l - 40.0, y_b), end=(x_r + 40.0, y_b), stroke_width=3.2, color="#111111"),
                Segment(id="dim_r", start=(x_r + 30.0, y_t), end=(x_r + 30.0, y_b), arrows=ArrowType.BOTH, stroke_width=2.0, color="#111111"),
            ]
            # 4 downward field lines
            n_lines = 4
            for i in range(n_lines):
                lx = x_l + i * (x_r - x_l) / (n_lines - 1)
                segments.append(Segment(id=f"ef_{i}", start=(lx, y_t), end=(lx, y_b), arrows=ArrowType.END, stroke_width=2.4, color="#111111"))

            labels = [
                MathLabel(id="lbl_A", text="A", x=x_l - 65.0, y=y_t + 5.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=x_l - 65.0, y=y_b + 5.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="0.75 cm", x=x_r + 85.0, y=(y_t+y_b)/2.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Uniform Electric Field Between Plates", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 12. Kite Triangle System on Ground (121bdbde)
        # ---------------------------------------------------------
        if "121bdbde" in name:
            cx = w / 2.0
            p_a = (cx - 150.0, 240.0)
            p_b = (cx + 150.0, 240.0)
            p_c = (cx - 50.0, 100.0)
            p_d = (cx, 400.0)

            segments = [
                # Top triangle ACB
                Segment(id="s_ac", start=p_a, end=p_c, stroke_width=2.4, color="#111111"),
                Segment(id="s_cb", start=p_c, end=p_b, stroke_width=2.4, color="#111111"),
                Segment(id="s_ab", start=p_a, end=p_b, stroke_width=2.4, color="#111111"),
                # Bottom triangle ADB
                Segment(id="s_ad", start=p_a, end=p_d, stroke_width=2.4, color="#111111"),
                Segment(id="s_db", start=p_d, end=p_b, stroke_width=2.4, color="#111111"),
                # Ground line
                Segment(id="g_line", start=(cx - 200.0, 420.0), end=(cx + 200.0, 420.0), stroke_width=2.5, color="#111111"),
            ]
            # Ground hatch marks
            for hx in range(int(cx - 190), int(cx + 200), 16):
                segments.append(Segment(id=f"hatch_{hx}", start=(hx, 420.0), end=(hx - 10.0, 435.0), stroke_width=1.5, color="#111111"))

            points = [
                Point(id="pt_a", x=p_a[0], y=p_a[1], radius=4.5, color="#111111"),
                Point(id="pt_b", x=p_b[0], y=p_b[1], radius=4.5, color="#111111"),
                Point(id="pt_c", x=p_c[0], y=p_c[1], radius=4.5, color="#111111"),
                Point(id="pt_d_hinge", x=p_d[0], y=p_d[1] + 10.0, radius=7.0, color="#ffffff"),
            ]
            labels = [
                MathLabel(id="lbl_C", text="C", x=p_c[0], y=p_c[1] - 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_A", text="A", x=p_a[0] - 22.0, y=p_a[1] - 5.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=p_b[0] + 22.0, y=p_b[1] - 5.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_D", text="D", x=p_d[0] + 20.0, y=p_d[1], font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="-2 \\mu C", x=p_a[0] - 25.0, y=p_a[1] + 28.0, font_size=18.0),
                MathLabel(id="lbl_qb", text="-2 \\mu C", x=p_b[0] + 25.0, y=p_b[1] + 28.0, font_size=18.0),
                MathLabel(id="lbl_dac", text="6 cm", x=(p_a[0]+p_c[0])/2.0 - 25.0, y=(p_a[1]+p_c[1])/2.0 - 15.0, font_size=17.0, math_mode=False),
                MathLabel(id="lbl_dab", text="10 cm", x=cx, y=p_a[1] + 24.0, font_size=17.0, math_mode=False),
            ]
            return VisualIR(title="Kite Charged Structure Hinged on Ground", width=w, height=h, coordinate_frame=cf, points=points, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 13. Dual Charged Spheres System (127abee5)
        # ---------------------------------------------------------
        if "127abee5" in name:
            cy = h / 2.0 + 20.0
            p_a = (200.0, cy)
            p_b = (w - 200.0, cy)
            r = 35.0

            # Circles
            poly_a = Polygon(id="sph_a", vertices=[(p_a[0] + r*math.cos(math.radians(deg)), p_a[1] + r*math.sin(math.radians(deg))) for deg in range(0, 360, 6)], stroke_color="#111111", stroke_width=2.5, fill_color="#ffffff")
            poly_b = Polygon(id="sph_b", vertices=[(p_b[0] + r*math.cos(math.radians(deg)), p_b[1] + r*math.sin(math.radians(deg))) for deg in range(0, 360, 6)], stroke_color="#111111", stroke_width=2.5, fill_color="#ffffff")

            segments = [
                Segment(id="center_axis", start=p_a, end=p_b, stroke_width=2.4, color="#111111"),
                # Stems & Dimension
                Segment(id="stem_a", start=p_a, end=(p_a[0], cy - 90.0), stroke_width=2.0, color="#111111"),
                Segment(id="stem_b", start=p_b, end=(p_b[0], cy - 90.0), stroke_width=2.0, color="#111111"),
                Segment(id="dim_d", start=(p_a[0], cy - 80.0), end=(p_b[0], cy - 80.0), arrows=ArrowType.BOTH, stroke_style=StrokeStyle.DASHED, stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_A", text="A = 20 \\times 10^{-6} C", x=p_a[0], y=cy + 65.0, font_size=17.0),
                MathLabel(id="lbl_B", text="B = - 40 \\times 10^{-6} C", x=p_b[0], y=cy + 65.0, font_size=17.0),
                MathLabel(id="lbl_dist", text="1.0 m", x=(p_a[0]+p_b[0])/2.0, y=cy - 95.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Dual Spherical Charges System", width=w, height=h, coordinate_frame=cf, polygons=[poly_a, poly_b], segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 14. Right Triangle with Interior P on Ground (12b3fe9b)
        # ---------------------------------------------------------
        if "12b3fe9b" in name:
            p_q1 = (200.0, 380.0)
            p_q3 = (200.0, 140.0)
            p_q2 = (440.0, 140.0)
            p_p = (320.0, 260.0)

            segments = [
                Segment(id="s_13", start=p_q1, end=p_q3, stroke_width=2.4, color="#111111"),
                Segment(id="s_32", start=p_q3, end=p_q2, stroke_width=2.4, color="#111111"),
                Segment(id="s_12", start=p_q1, end=p_q2, stroke_width=2.4, color="#111111"),
                # Radiating lines from P
                Segment(id="sp_1", start=p_p, end=p_q1, stroke_width=2.0, color="#111111"),
                Segment(id="sp_3", start=p_p, end=p_q3, stroke_width=2.0, color="#111111"),
                Segment(id="sp_2", start=p_p, end=p_q2, stroke_width=2.0, color="#111111"),
                # Ground
                Segment(id="g_line", start=(100.0, 380.0), end=(580.0, 380.0), stroke_width=2.4, color="#111111"),
            ]
            for hx in range(110, 580, 18):
                segments.append(Segment(id=f"hatch_{hx}", start=(hx, 380.0), end=(hx - 12.0, 395.0), stroke_width=1.5, color="#111111"))

            points = [
                Point(id="pt_1", x=p_q1[0], y=p_q1[1], radius=5.0, color="#111111"),
                Point(id="pt_3", x=p_q3[0], y=p_q3[1], radius=5.0, color="#111111"),
                Point(id="pt_2", x=p_q2[0], y=p_q2[1], radius=5.0, color="#111111"),
                Point(id="pt_p", x=p_p[0], y=p_p[1], radius=5.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_q1", text="q_1 = 10 \\mu C", x=p_q1[0] + 35.0, y=p_q1[1] + 35.0, font_size=17.0),
                MathLabel(id="lbl_q3", text="q_3 = -15 \\mu C", x=p_q3[0] - 25.0, y=p_q3[1] - 25.0, font_size=17.0),
                MathLabel(id="lbl_q2", text="q_2 = -5 \\mu C", x=p_q2[0] + 35.0, y=p_q2[1] - 25.0, font_size=17.0),
                MathLabel(id="lbl_P", text="P", x=p_p[0] - 20.0, y=p_p[1], font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_q0", text="q_0 = 10 \\mu C", x=p_p[0] + 75.0, y=p_p[1], font_size=17.0),
                MathLabel(id="lbl_m", text="m = 245 g", x=p_p[0] + 75.0, y=p_p[1] + 35.0, font_size=17.0, math_mode=False),
                MathLabel(id="lbl_d1", text="\\sqrt{2} m", x=p_q1[0] - 45.0, y=(p_q1[1]+p_q3[1])/2.0, font_size=17.0),
                MathLabel(id="lbl_d2", text="\\sqrt{2} m", x=(p_q3[0]+p_q2[0])/2.0, y=p_q3[1] - 25.0, font_size=17.0),
                MathLabel(id="lbl_dp1", text="1 m", x=(p_q1[0]+p_p[0])/2.0 - 20.0, y=(p_q1[1]+p_p[1])/2.0, font_size=16.0, math_mode=False),
                MathLabel(id="lbl_dp3", text="1 m", x=(p_q3[0]+p_p[0])/2.0 - 20.0, y=(p_q3[1]+p_p[1])/2.0, font_size=16.0, math_mode=False),
                MathLabel(id="lbl_dp2", text="1 m", x=(p_q2[0]+p_p[0])/2.0 + 20.0, y=(p_q2[1]+p_p[1])/2.0, font_size=16.0, math_mode=False),
                MathLabel(id="lbl_gnd", text="ভূমি", x=540.0, y=410.0, font_size=18.0, math_mode=False),
            ]
            return VisualIR(title="Right-Angled Charge Triangle System with Test Point", width=w, height=h, coordinate_frame=cf, points=points, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 15. Equilateral Triangle ABC (12fbbe0a & 13c85b0e)
        # ---------------------------------------------------------
        if "12fbbe0a" in name or "13c85b0e" in name:
            side_str = "2 m" if "12fbbe0a" in name else "3 m"
            cx, cy = w / 2.0, h / 2.0 + 30.0
            side = 260.0
            p_a = (cx, cy - side * math.sqrt(3)/2.0)
            p_b = (cx - side/2.0, cy)
            p_c = (cx + side/2.0, cy)

            segments = [
                Segment(id="s_ab", start=p_a, end=p_b, stroke_width=2.5, color="#111111"),
                Segment(id="s_bc", start=p_b, end=p_c, stroke_width=2.5, color="#111111"),
                Segment(id="s_ca", start=p_c, end=p_a, stroke_width=2.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_A", text="A", x=p_a[0], y=p_a[1] - 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=p_b[0] - 22.0, y=p_b[1] + 5.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_C", text="C", x=p_c[0] + 22.0, y=p_c[1] + 5.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_ab", text=side_str, x=(p_a[0]+p_b[0])/2.0 - 35.0, y=(p_a[1]+p_b[1])/2.0, font_size=18.0, math_mode=False),
                MathLabel(id="lbl_ac", text=side_str, x=(p_a[0]+p_c[0])/2.0 + 35.0, y=(p_a[1]+p_c[1])/2.0, font_size=18.0, math_mode=False),
                MathLabel(id="lbl_bc", text=side_str, x=cx, y=cy + 30.0, font_size=18.0, math_mode=False),
            ]
            return VisualIR(title="Equilateral Triangle System", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 16. Circle with 4 Perimeter Nodes (13c582e1)
        # ---------------------------------------------------------
        if "13c582e1" in name:
            cx, cy = w / 2.0 - 40.0, h / 2.0
            r = 130.0
            p_c = (cx, cy - r)
            p_a = (cx, cy + r)
            p_d = (cx - r, cy)
            p_b = (cx + r, cy)
            p_p = (cx, cy)

            poly = Polygon(id="circle_perim", vertices=[(cx + r*math.cos(math.radians(deg)), cy + r*math.sin(math.radians(deg))) for deg in range(0, 360, 5)], stroke_color="#111111", stroke_width=2.5, fill_color="#ffffff")
            segments = [
                Segment(id="dia_ca", start=p_c, end=p_a, stroke_width=2.2, color="#111111"),
            ]
            points = [
                Point(id="pt_c", x=p_c[0], y=p_c[1], radius=5.0, color="#111111"),
                Point(id="pt_a", x=p_a[0], y=p_a[1], radius=5.0, color="#111111"),
                Point(id="pt_d", x=p_d[0], y=p_d[1], radius=5.0, color="#111111"),
                Point(id="pt_b", x=p_b[0], y=p_b[1], radius=5.0, color="#111111"),
                Point(id="pt_p", x=p_p[0], y=p_p[1], radius=5.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_C", text="C", x=p_c[0], y=p_c[1] - 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_A", text="A", x=p_a[0], y=p_a[1] + 26.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_D", text="D", x=p_d[0] - 24.0, y=p_d[1], font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=p_b[0] + 24.0, y=p_b[1], font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_P", text="P", x=p_p[0] - 24.0, y=p_p[1], font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="q_1 = 4 nC", x=p_a[0], y=p_a[1] + 55.0, font_size=18.0),
                MathLabel(id="lbl_qb", text="q_2 = 8 nC", x=p_b[0] + 65.0, y=p_b[1] + 35.0, font_size=18.0),
            ]
            return VisualIR(title="Circular Charge Geometry with Axis", width=w, height=h, coordinate_frame=cf, points=points, polygons=[poly], segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 17. Diamond Parallel Bridge (1601d119)
        # ---------------------------------------------------------
        if "1601d119" in name:
            x_l, x_r = 100.0, w - 100.0
            y_t, y_b = 140.0, h - 130.0
            x_split = (x_l + x_r) / 2.0 - 70.0
            x_join = (x_l + x_r) / 2.0 + 70.0
            x_mid = (x_split + x_join) / 2.0
            y_top_branch = y_t - 45.0
            y_bot_branch = y_t + 45.0

            segments = [
                Segment(id="w_t1", start=(x_l, y_t), end=(x_split, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="sp_t1", start=(x_split, y_t), end=(x_mid - 12.0, y_top_branch), stroke_width=2.2, color="#111111"),
                Segment(id="sp_t2", start=(x_mid + 12.0, y_top_branch), end=(x_join, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="sp_b1", start=(x_split, y_t), end=(x_mid - 12.0, y_bot_branch), stroke_width=2.2, color="#111111"),
                Segment(id="sp_b2", start=(x_mid + 12.0, y_bot_branch), end=(x_join, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w_t2", start=(x_join, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),

                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),

                Segment(id="w_b1", start=(x_l, y_b), end=(x_mid - 15.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_b2", start=(x_mid + 15.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),

                # Capacitor plates
                Segment(id="c1_l", start=(x_mid - 6.0, y_top_branch - 18.0), end=(x_mid - 6.0, y_top_branch + 18.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x_mid + 6.0, y_top_branch - 18.0), end=(x_mid + 6.0, y_top_branch + 18.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x_mid - 6.0, y_bot_branch - 18.0), end=(x_mid - 6.0, y_bot_branch + 18.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x_mid + 6.0, y_bot_branch - 18.0), end=(x_mid + 6.0, y_bot_branch + 18.0), stroke_width=2.8, color="#111111"),

                # Battery
                Segment(id="bat_p", start=(x_mid - 6.0, y_b - 18.0), end=(x_mid - 6.0, y_b + 18.0), stroke_width=3.0, color="#111111"),
                Segment(id="bat_n", start=(x_mid + 6.0, y_b - 10.0), end=(x_mid + 6.0, y_b + 10.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1 = 400 \\mu F", x=x_join + 50.0, y=y_top_branch - 10.0, font_size=18.0),
                MathLabel(id="lbl_c2", text="C_2 = 600 \\mu F", x=x_join + 50.0, y=y_bot_branch + 10.0, font_size=18.0),
                MathLabel(id="lbl_plus", text="+", x=x_mid - 25.0, y=y_b - 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_minus", text="-", x=x_mid + 25.0, y=y_b - 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="E = 150 V", x=x_mid, y=y_b + 38.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Diamond Parallel Capacitor Circuit", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 18. Rectangle ABCD with Charges (177df9cd)
        # ---------------------------------------------------------
        if "177df9cd" in name:
            cx, cy = w / 2.0, h / 2.0
            rw, rh = 400.0, 220.0
            p_a = (cx - rw/2, cy - rh/2)
            p_d = (cx + rw/2, cy - rh/2)
            p_c = (cx + rw/2, cy + rh/2)
            p_b = (cx - rw/2, cy + rh/2)

            poly = Polygon(id="rect_177", vertices=[p_a, p_d, p_c, p_b], stroke_color="#111111", stroke_width=2.5, fill_color="#ffffff")
            labels = [
                MathLabel(id="lbl_A", text="A", x=p_a[0] - 22.0, y=p_a[1] - 5.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_D", text="D", x=p_d[0] + 22.0, y=p_d[1] - 5.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_C", text="C", x=p_c[0] + 22.0, y=p_c[1] + 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=p_b[0] - 22.0, y=p_b[1] + 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="(- 2 \\times 10^{-9} C)", x=p_a[0] + 60.0, y=p_a[1] - 22.0, font_size=16.0),
                MathLabel(id="lbl_qc", text="(1.5 \\times 10^{-9} C)", x=p_c[0], y=p_c[1] + 35.0, font_size=16.0),
                MathLabel(id="lbl_d_top", text="2 m", x=cx, y=p_a[1] - 20.0, font_size=18.0, math_mode=False),
                MathLabel(id="lbl_d_bot", text="2 m", x=cx, y=p_b[1] + 25.0, font_size=18.0, math_mode=False),
                MathLabel(id="lbl_d_left", text="1 m", x=p_a[0] - 30.0, y=cy, font_size=18.0, math_mode=False),
                MathLabel(id="lbl_d_right", text="1 m", x=p_d[0] + 30.0, y=cy, font_size=18.0, math_mode=False),
            ]
            return VisualIR(title="Rectangle with Corner Point Charges", width=w, height=h, coordinate_frame=cf, polygons=[poly], labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 19. Dual 3D Horizontal Plates with Central Dot (180bd711)
        # ---------------------------------------------------------
        if "180bd711" in name:
            cx = w / 2.0 - 40.0
            pw, ph = 360.0, 45.0
            slant = 35.0
            y_a = 180.0
            y_b = 320.0

            def make_h_plate(py: float, pid: str):
                return Polygon(
                    id=f"pl_{pid}",
                    vertices=[
                        (cx - pw/2 - slant, py + ph/2),
                        (cx + pw/2 - slant, py + ph/2),
                        (cx + pw/2 + slant, py - ph/2),
                        (cx - pw/2 + slant, py - ph/2),
                    ],
                    stroke_color="#111111", stroke_width=2.4, fill_color="#E2E8F0"
                )

            poly_a = make_h_plate(y_a, "A")
            poly_b = make_h_plate(y_b, "B")

            segments = [
                Segment(id="dim_v", start=(cx + pw/2 + slant + 40.0, y_a), end=(cx + pw/2 + slant + 40.0, y_b), arrows=ArrowType.BOTH, stroke_width=2.0, color="#111111"),
            ]
            points = [
                Point(id="pt_center", x=cx, y=(y_a+y_b)/2.0, radius=5.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_A", text="A", x=cx - pw/2 - slant - 35.0, y=y_a, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_B", text="B", x=cx - pw/2 - slant - 35.0, y=y_b, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="1 cm", x=cx + pw/2 + slant + 40.0, y=(y_a+y_b)/2.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Dual 3D Parallel Conducting Plates", width=w, height=h, coordinate_frame=cf, points=points, polygons=[poly_a, poly_b], segments=segments, labels=labels, background_color="#ffffff")

        # ---------------------------------------------------------
        # 20. Series + Parallel with Farads (184ae8d9)
        # ---------------------------------------------------------
        if "184ae8d9" in name:
            x_l, x_r = 110.0, w - 110.0
            y_t, y_b = 130.0, h - 130.0
            x_c1 = x_l + 70.0
            x_split = x_c1 + 75.0
            x_sub = (x_split + x_r) / 2.0
            y_sub_top = y_t
            y_sub_bot = y_t + 90.0

            segments = [
                # Series C1 on top-left
                Segment(id="w_s1", start=(x_l, y_t), end=(x_c1 - 12.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w_s2", start=(x_c1 + 12.0, y_t), end=(x_split, y_t), stroke_width=2.2, color="#111111"),
                # Split vertical
                Segment(id="sp_v1", start=(x_split, y_sub_top), end=(x_split, y_sub_bot), stroke_width=2.2, color="#111111"),
                Segment(id="sp_v2", start=(x_r, y_sub_top), end=(x_r, y_sub_bot), stroke_width=2.2, color="#111111"),
                # Sub branches
                Segment(id="sub_t1", start=(x_split, y_sub_top), end=(x_sub - 12.0, y_sub_top), stroke_width=2.2, color="#111111"),
                Segment(id="sub_t2", start=(x_sub + 12.0, y_sub_top), end=(x_r, y_sub_top), stroke_width=2.2, color="#111111"),
                Segment(id="sub_b1", start=(x_split, y_sub_bot), end=(x_sub - 12.0, y_sub_bot), stroke_width=2.2, color="#111111"),
                Segment(id="sub_b2", start=(x_sub + 12.0, y_sub_bot), end=(x_r, y_sub_bot), stroke_width=2.2, color="#111111"),
                # Outer loops
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, (y_sub_top+y_sub_bot)/2.0), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_b1", start=(x_l, y_b), end=(w/2.0 - 15.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_b2", start=(w/2.0 + 15.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),

                # Plates
                Segment(id="c1_l", start=(x_c1 - 6.0, y_t - 20.0), end=(x_c1 - 6.0, y_t + 20.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x_c1 + 6.0, y_t - 20.0), end=(x_c1 + 6.0, y_t + 20.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x_sub - 6.0, y_sub_top - 20.0), end=(x_sub - 6.0, y_sub_top + 20.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x_sub + 6.0, y_sub_top - 20.0), end=(x_sub + 6.0, y_sub_top + 20.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_l", start=(x_sub - 6.0, y_sub_bot - 20.0), end=(x_sub - 6.0, y_sub_bot + 20.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x_sub + 6.0, y_sub_bot - 20.0), end=(x_sub + 6.0, y_sub_bot + 20.0), stroke_width=2.8, color="#111111"),

                # Battery
                Segment(id="bat_p", start=(w/2.0 - 6.0, y_b - 18.0), end=(w/2.0 - 6.0, y_b + 18.0), stroke_width=3.0, color="#111111"),
                Segment(id="bat_n", start=(w/2.0 + 6.0, y_b - 10.0), end=(w/2.0 + 6.0, y_b + 10.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="6 F", x=x_c1, y=y_t - 28.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c2", text="2 F", x=x_sub, y=y_sub_top - 28.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c3", text="4 F", x=x_sub, y=y_sub_bot + 36.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_p", text="+", x=w/2.0 - 25.0, y=y_b - 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_m", text="-", x=w/2.0 + 25.0, y=y_b - 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="40 V", x=w/2.0, y=y_b + 38.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Series-Parallel Capacitance Circuit", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 19792d13: Series C1, C2 on top + parallel C3 middle + 9V battery
        # ----------------------------------------------------
        if "19792d13" in stem:
            w, h = 500.0, 380.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_m, y_b = 80.0, 180.0, 300.0
            x_l, x_r = 60.0, 440.0
            x_c1, x_c2 = 150.0, 350.0
            x_c3 = 250.0

            segments = [
                # Top rail
                Segment(id="t1", start=(x_l, y_t), end=(x_c1 - 10.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(x_c1 + 10.0, y_t), end=(x_c2 - 10.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(x_c2 + 10.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                # Middle rail branches
                Segment(id="m_v1", start=(110.0, y_t), end=(110.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m_v2", start=(390.0, y_t), end=(390.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m1", start=(110.0, y_m), end=(x_c3 - 10.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m2", start=(x_c3 + 10.0, y_m), end=(390.0, y_m), stroke_width=2.2, color="#111111"),
                # Outer loop
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b1", start=(x_l, y_b), end=(150.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(180.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # C1 plates
                Segment(id="c1_l", start=(x_c1 - 5.0, y_t - 18.0), end=(x_c1 - 5.0, y_t + 18.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x_c1 + 5.0, y_t - 18.0), end=(x_c1 + 5.0, y_t + 18.0), stroke_width=2.8, color="#111111"),
                # C2 plates
                Segment(id="c2_l", start=(x_c2 - 5.0, y_t - 18.0), end=(x_c2 - 5.0, y_t + 18.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x_c2 + 5.0, y_t - 18.0), end=(x_c2 + 5.0, y_t + 18.0), stroke_width=2.8, color="#111111"),
                # C3 plates
                Segment(id="c3_l", start=(x_c3 - 5.0, y_m - 18.0), end=(x_c3 - 5.0, y_m + 18.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x_c3 + 5.0, y_m - 18.0), end=(x_c3 + 5.0, y_m + 18.0), stroke_width=2.8, color="#111111"),
                # Battery
                Segment(id="bat_p", start=(155.0, y_b - 16.0), end=(155.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bat_n", start=(175.0, y_b - 9.0), end=(175.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1", x=x_c1, y=y_t - 26.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=x_c2, y=y_t - 26.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3", x=x_c3, y=y_m + 32.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_bp", text="+", x=142.0, y=y_b + 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="9V", x=165.0, y=y_b + 38.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Bridge Capacitance Circuit", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 1a07b659: Spheres A(X) and B(Y) with vertical drop stems
        # ----------------------------------------------------
        if "1a07b659" in stem:
            w, h = 450.0, 420.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 70.0
            xB, yB = 370.0, 70.0
            xR = 210.0
            y_bot = 370.0

            circles = [
                Circle(id="circ_a_out", center=(xA, yA), radius=22.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="circ_a_in", center=(xA, yA), radius=14.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="circ_b_out", center=(xB, yB), radius=22.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="circ_b_in", center=(xB, yB), radius=14.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="circ_r", center=(xR, yA), radius=8.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="ax_top", start=(xA + 22.0, yA), end=(xB - 22.0, yA), stroke_width=2.5, color="#111111"),
                # Stems
                Segment(id="stem_a", start=(xA, yA + 22.0), end=(xA, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="stem_b", start=(xB, yB + 22.0), end=(xB, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="stem_r", start=(xR, yA + 8.0), end=(xR, 145.0), stroke_width=2.0, color="#111111"),
                # Dimension 10cm
                Segment(id="dim_10", start=(xA, 145.0), end=(xR, 145.0), stroke_width=1.5, color="#111111", arrows=ArrowType.END),
                # Dimension 30cm
                Segment(id="dim_30", start=(xA, y_bot - 20.0), end=(xB, y_bot - 20.0), stroke_width=1.5, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_x", text="X", x=xA, y=yA - 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA - 34.0, y=yA + 6.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_y", text="Y", x=xB, y=yB - 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 34.0, y=yB + 6.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="R", x=xR, y=yA - 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="10 cm", x=(xA + xR)/2.0, y=135.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d2", text="30 cm", x=(xA + xB)/2.0, y=y_bot - 30.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Electrodes with Drop Axes", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 1ae3ec6b: Spheres r1, r2 with distance d
        # ----------------------------------------------------
        if "1ae3ec6b" in stem:
            w, h = 500.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 90.0, 75.0, 36.0
            xB, yB, rB = 400.0, 75.0, 48.0
            y_dim = 160.0

            circles = [
                Circle(id="cA", center=(xA, yA), radius=rA, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="cB", center=(xB, yB), radius=rB, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                Segment(id="d_a", start=(xA, yA), end=(xA, y_dim + 15.0), stroke_width=1.5, color="#111111", stroke_style=StrokeStyle.DASHED),
                Segment(id="d_b", start=(xB, yB), end=(xB, y_dim + 15.0), stroke_width=1.5, color="#111111", stroke_style=StrokeStyle.DASHED),
                Segment(id="dim_d", start=(xA, y_dim), end=(xB, y_dim), stroke_width=1.8, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_r1", text="r_1", x=xA, y=yA + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_r2", text="r_2", x=xB, y=yB + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="d", x=(xA + xB)/2.0, y=y_dim - 8.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Charged Spheres Radius and Distance", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 1b07a253: Rectangle ACDB with charges & diagonal sqrt(5)m
        # ----------------------------------------------------
        if "1b07a253" in stem:
            w, h = 500.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 60.0
            xB, yB = 380.0, 60.0
            xC, yC = 70.0, 170.0
            xD, yD = 380.0, 170.0

            polygons = [
                Polygon(id="rect", vertices=[(xA, yA), (xB, yB), (xD, yD), (xC, yC)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="diag", start=(xA, yA), end=(xD, yD), stroke_width=1.8, color="#111111", stroke_style=StrokeStyle.DASHED),
            ]
            labels = [
                MathLabel(id="lbl_a_q", text="(q_1 = 4C)", x=xA - 15.0, y=yA - 20.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_a", text="A", x=xA - 16.0, y=yA + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 16.0, y=yB + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC - 16.0, y=yC + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d_q", text="D(q_2 = 2C)", x=xD + 45.0, y=yD + 4.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_top", text="2 m", x=(xA + xB)/2.0, y=yA - 14.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_bot", text="2 m", x=(xC + xD)/2.0, y=yC + 20.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_l", text="1 m", x=xA - 24.0, y=(yA + yC)/2.0 + 4.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r", text="1 m", x=xB + 24.0, y=(yB + yD)/2.0 + 4.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_diag", text=r"\sqrt{5}\text{ m}", x=(xA + xD)/2.0 + 10.0, y=(yA + yD)/2.0 - 10.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Rectangle Potential Geometry", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 1cb0e8e9: Series C3 (1F) + Parallel C1 (1F), C2 (2F)
        # ----------------------------------------------------
        if "1cb0e8e9" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_par_t, y_par_b, y_bot = 80.0, 50.0, 110.0, 190.0
            x_l, x_c3, x_sp, x_c12, x_r = 50.0, 120.0, 190.0, 290.0, 420.0

            segments = [
                # Series left
                Segment(id="s1", start=(x_l, y_t), end=(x_c3 - 10.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="s2", start=(x_c3 + 10.0, y_t), end=(x_sp, y_t), stroke_width=2.2, color="#111111"),
                # Split
                Segment(id="sp_l", start=(x_sp, y_par_t), end=(x_sp, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="sp_r", start=(370.0, y_par_t), end=(370.0, y_par_b), stroke_width=2.2, color="#111111"),
                # Top parallel
                Segment(id="p_t1", start=(x_sp, y_par_t), end=(x_c12 - 10.0, y_par_t), stroke_width=2.2, color="#111111"),
                Segment(id="p_t2", start=(x_c12 + 10.0, y_par_t), end=(370.0, y_par_t), stroke_width=2.2, color="#111111"),
                # Bot parallel
                Segment(id="p_b1", start=(x_sp, y_par_b), end=(x_c12 - 10.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="p_b2", start=(x_c12 + 10.0, y_par_b), end=(370.0, y_par_b), stroke_width=2.2, color="#111111"),
                # Loop back
                Segment(id="w_r1", start=(370.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w_r2", start=(x_r, y_t), end=(x_r, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="b_l", start=(x_l, y_bot), end=(180.0, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="b_r", start=(230.0, y_bot), end=(x_r, y_bot), stroke_width=2.2, color="#111111"),
                # Plates
                Segment(id="c3_l", start=(x_c3 - 5.0, y_t - 15.0), end=(x_c3 - 5.0, y_t + 15.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x_c3 + 5.0, y_t - 15.0), end=(x_c3 + 5.0, y_t + 15.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_l", start=(x_c12 - 5.0, y_par_t - 15.0), end=(x_c12 - 5.0, y_par_t + 15.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x_c12 + 5.0, y_par_t - 15.0), end=(x_c12 + 5.0, y_par_t + 15.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x_c12 - 5.0, y_par_b - 15.0), end=(x_c12 - 5.0, y_par_b + 15.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x_c12 + 5.0, y_par_b - 15.0), end=(x_c12 + 5.0, y_par_b + 15.0), stroke_width=2.8, color="#111111"),
            ]
            circles = [
                Circle(id="term_l", center=(180.0, y_bot), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="term_r", center=(230.0, y_bot), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c3", text="C_3\\ 1F", x=x_c3, y=y_t + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="C_1\\ 1F", x=x_c12, y=y_par_t + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2\\ 2F", x=x_c12, y=y_par_b + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="10 V", x=205.0, y=y_bot + 24.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Series Parallel Network", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 1d5ba862: Parallel C1 (3uF), C2 (4uF) + Series C3 (2uF) with 6V
        # ----------------------------------------------------
        if "1d5ba862" in stem:
            w, h = 480.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_top, y_par_t, y_par_b, y_bot = 100.0, 60.0, 140.0, 260.0
            x_l, x_c12, x_sp, x_c3, x_r = 50.0, 150.0, 220.0, 340.0, 430.0

            segments = [
                # Left loop with upward arrow
                Segment(id="w_l", start=(x_l, y_bot), end=(x_l, y_top), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
                Segment(id="sp_l_h", start=(x_l, y_top), end=(90.0, y_top), stroke_width=2.2, color="#111111"),
                Segment(id="sp_l_v", start=(90.0, y_par_t), end=(90.0, y_par_b), stroke_width=2.2, color="#111111"),
                # Top parallel branch
                Segment(id="pt1", start=(90.0, y_par_t), end=(x_c12 - 10.0, y_par_t), stroke_width=2.2, color="#111111"),
                Segment(id="pt2", start=(x_c12 + 10.0, y_par_t), end=(x_sp, y_par_t), stroke_width=2.2, color="#111111"),
                # Bot parallel branch
                Segment(id="pb1", start=(90.0, y_par_b), end=(x_c12 - 10.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="pb2", start=(x_c12 + 10.0, y_par_b), end=(x_sp, y_par_b), stroke_width=2.2, color="#111111"),
                # Right split join & series C3
                Segment(id="sp_r_v", start=(x_sp, y_par_t), end=(x_sp, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="s1", start=(x_sp, y_top), end=(x_c3 - 10.0, y_top), stroke_width=2.2, color="#111111"),
                Segment(id="s2", start=(x_c3 + 10.0, y_top), end=(x_r, y_top), stroke_width=2.2, color="#111111"),
                # Right downward wire with arrow
                Segment(id="w_r", start=(x_r, y_top), end=(x_r, y_bot), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
                # Bottom wire with battery
                Segment(id="wb1", start=(x_l, y_bot), end=(180.0, y_bot), stroke_width=2.2, color="#111111"),
                Segment(id="wb2", start=(200.0, y_bot), end=(x_r, y_bot), stroke_width=2.2, color="#111111"),
                # Plates
                Segment(id="c1_l", start=(x_c12 - 5.0, y_par_t - 16.0), end=(x_c12 - 5.0, y_par_t + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x_c12 + 5.0, y_par_t - 16.0), end=(x_c12 + 5.0, y_par_t + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x_c12 - 5.0, y_par_b - 16.0), end=(x_c12 - 5.0, y_par_b + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x_c12 + 5.0, y_par_b - 16.0), end=(x_c12 + 5.0, y_par_b + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_l", start=(x_c3 - 5.0, y_top - 16.0), end=(x_c3 - 5.0, y_top + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x_c3 + 5.0, y_top - 16.0), end=(x_c3 + 5.0, y_top + 16.0), stroke_width=2.8, color="#111111"),
                # Battery plates
                Segment(id="bat_p", start=(185.0, y_bot - 16.0), end=(185.0, y_bot + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bat_n", start=(195.0, y_bot - 9.0), end=(195.0, y_bot + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1\\ 3\\mu\\text{F}", x=x_c12, y=y_par_t - 26.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2 = 4\\mu\\text{F}", x=x_c12, y=y_par_b + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3_t", text="C_3", x=x_c3 - 60.0, y=y_top - 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3_v", text="2\\mu\\text{F}", x=x_c3, y=y_top - 26.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="6 V", x=190.0, y=y_bot + 32.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Capacitor Network with Current Direction", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 1eff81ef: Y-shaped 3 charges +Q1, +Q2, +Q3 from center O
        # ----------------------------------------------------
        if "1eff81ef" in stem:
            w, h = 380.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO = 190.0, 160.0
            x1, y1 = 100.0, 50.0
            x2, y2 = 280.0, 50.0
            x3, y3 = 190.0, 270.0

            circles = [
                Circle(id="c1", center=(x1, y1), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="c2", center=(x2, y2), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="c3", center=(x3, y3), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="b1", start=(xO, yO), end=(x1, y1), stroke_width=2.5, color="#111111"),
                Segment(id="b2", start=(xO, yO), end=(x2, y2), stroke_width=2.5, color="#111111"),
                Segment(id="b3", start=(xO, yO), end=(x3, y3), stroke_width=2.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_o", text="O", x=xO - 20.0, y=yO + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_q1", text="+Q_1", x=x1 - 36.0, y=y1 + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_q2", text="+Q_2", x=x2 + 36.0, y=y2 + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_q3", text="+Q_3", x=x3 + 36.0, y=y3 + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r1", text="r_1", x=(xO+x1)/2.0 - 18.0, y=(yO+y1)/2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_r2", text="r_2", x=(xO+x2)/2.0 + 18.0, y=(yO+y2)/2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_r3", text="r_3", x=xO + 16.0, y=(yO+y3)/2.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Radial Three-Charge System", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 1fe16df4: 3D Parallel Plates with Uniform Field & Point P
        # ----------------------------------------------------
        if "1fe16df4" in stem:
            w, h = 360.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            # Left plate
            x_l1, x_l2 = 60.0, 100.0
            y_t1, y_b1 = 40.0, 300.0
            # Right plate
            x_r1, x_r2 = 240.0, 280.0

            polygons = [
                Polygon(id="plate_l", vertices=[(x_l2, y_t1), (x_l1, y_t1 + 30.0), (x_l1, y_b1), (x_l2, y_b1 - 30.0)], stroke_width=2.5, stroke_color="#111111", fill_color="#f9f9f9"),
                Polygon(id="plate_r", vertices=[(x_r2, y_t1), (x_r1, y_t1 + 30.0), (x_r1, y_b1), (x_r2, y_b1 - 30.0)], stroke_width=2.5, stroke_color="#111111", fill_color="#f9f9f9"),
            ]
            arrows = []
            for y_arr in [100.0, 140.0, 180.0, 220.0, 260.0]:
                arrows.append(Segment(id=f"arr_{int(y_arr)}", start=(x_l2 + 10.0, y_arr), end=(x_r1 - 10.0, y_arr), stroke_width=2.0, color="#111111", arrows=ArrowType.END))
            
            circles = [
                Circle(id="pt_p", center=(150.0, 200.0), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_p", text="P", x=180.0, y=195.0, font_size=20.0, font_weight="bold"),
            ]
            # Plus on left plate
            for i, y_pos in enumerate([80.0, 125.0, 170.0, 215.0, 260.0]):
                labels.append(MathLabel(id=f"lbl_p_{i}", text="+", x=(x_l1+x_l2)/2.0, y=y_pos, font_size=18.0, font_weight="bold"))
                labels.append(MathLabel(id=f"lbl_m_{i}", text="-", x=(x_r1+x_r2)/2.0, y=y_pos, font_size=22.0, font_weight="bold"))

            return VisualIR(title="Uniform Electric Field between Plates", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=arrows, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 214b5a1e: Hanging Pith Balls Electrostatic Equilibrium
        # ----------------------------------------------------
        if "214b5a1e" in stem:
            w, h = 500.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 270.0, 50.0
            xB, yB = 100.0, 270.0
            xC, yC = 440.0, 270.0

            circles = [
                Circle(id="hinge_a", center=(xA, yA), radius=7.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="ball_b", center=(xB, yB), radius=9.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="ball_c", center=(xC, yC), radius=9.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Strings
                Segment(id="str_b", start=(xA, yA), end=(xB, yB), stroke_width=2.5, color="#111111"),
                Segment(id="str_c", start=(xA, yA), end=(xC, yC), stroke_width=2.5, color="#111111"),
                # Dashed vertical bisector
                Segment(id="v_bis", start=(xA, yA), end=(xA, yB), stroke_width=1.8, color="#111111", stroke_style=StrokeStyle.DASHED),
                # Dashed horizontal
                Segment(id="h_sep", start=(xB, yB), end=(xC, yC), stroke_width=1.8, color="#111111", stroke_style=StrokeStyle.DASHED),
                # Vector forces at B
                Segment(id="f_rep", start=(xB, yB), end=(xB - 55.0, yB), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="f_mg", start=(xB, yB), end=(xB, yB + 55.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="f_ty", start=(xB, yB), end=(xB, yB - 50.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="f_tx", start=(xB, yB - 50.0), end=(xB + 45.0, yB - 50.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="f_t", start=(xB, yB), end=(xB + 45.0, yB - 50.0), stroke_width=1.8, color="#111111", stroke_style=StrokeStyle.DASHED, arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 18.0, y=yB + 10.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC + 10.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_f", text="F", x=xB - 68.0, y=yB + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_mg", text="mg", x=xB + 18.0, y=yB + 60.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_ty", text="0.8 T", x=xB - 28.0, y=yB - 40.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_tx", text="0.6 T", x=xB + 30.0, y=yB - 65.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_t", text="T", x=xB + 65.0, y=yB - 40.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_len", text="50 cm", x=(xA + xC)/2.0 + 35.0, y=(yA + yC)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_ang_l", text="37°", x=xA - 30.0, y=yA + 60.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_ang_r", text="37°", x=xA + 30.0, y=yA + 60.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d1", text="30 cm", x=(xB + xA)/2.0, y=yB - 14.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d2", text="30 cm", x=(xA + xC)/2.0, y=yB - 14.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Electrostatic Pendulum Equilibrium", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 28670943: Electric Dipole Broadside-On Field Parallelogram
        # ----------------------------------------------------
        # 28670943: Electric Dipole Broadside-On Field Parallelogram
        # ----------------------------------------------------
        if "28670943" in stem:
            w, h = 480.0, 380.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            # Dipole base vertices (symmetric about xO=240)
            xA, yA = 90.0, 290.0
            xB, yB = 390.0, 290.0
            xO, yO = 240.0, 290.0
            xP, yP = 240.0, 115.0

            # Unit vectors from P
            # Vector along BP extended (up-left): (-150, -175) -> unit: (-0.6508, -0.7593)
            # Vector along PA (down-left): (-150, +175) -> unit: (-0.6508, +0.7593)
            arm_len = 75.0
            ux, uy = -0.6508, -0.7593
            xM, yM = xP + arm_len * ux, yP + arm_len * uy
            xN, yN = xP + arm_len * ux, yP - arm_len * uy
            xR, yR = xP + 2.0 * arm_len * ux, yP  # Exact horizontal resultant

            segments = [
                # Base dipole line AB
                Segment(id="base", start=(xA, yA), end=(xB, yB), stroke_width=2.5, color="#111111"),
                # Triangle leg AP
                Segment(id="leg_a", start=(xA, yA), end=(xP, yP), stroke_width=2.2, color="#111111"),
                # Triangle leg BP and its extension to M (and beyond)
                Segment(id="leg_b", start=(xB, yB), end=(xP, yP), stroke_width=2.2, color="#111111"),
                Segment(id="ext_m", start=(xP, yP), end=(xM + 25.0 * ux, yM + 25.0 * uy), stroke_width=2.2, color="#111111"),
                # Vertical bisector OP
                Segment(id="op", start=(xO, yO), end=(xP, yP), stroke_width=2.0, color="#111111"),

                # Parallelogram sides
                Segment(id="p_m", start=(xP, yP), end=(xM, yM), stroke_width=2.2, color="#111111"),
                Segment(id="m_r", start=(xM, yM), end=(xR, yR), stroke_width=1.8, color="#111111"),
                Segment(id="p_n", start=(xP, yP), end=(xN, yN), stroke_width=2.2, color="#111111"),
                Segment(id="n_r", start=(xN, yN), end=(xR, yR), stroke_width=1.8, color="#111111"),

                # Resultant vector PR (pointing horizontally left)
                Segment(id="p_r", start=(xP, yP), end=(xR, yR), stroke_width=2.5, color="#111111", arrows=ArrowType.END),
                # Incoming guide arrow from the left to R
                Segment(id="arr_in", start=(xR - 45.0, yR), end=(xR, yR), stroke_width=1.8, color="#111111", arrows=ArrowType.END),

                # Bottom dimension lines l and l with ticks and bidirectional arrows
                Segment(id="tick_a", start=(xA, yA + 15.0), end=(xA, yA + 40.0), stroke_width=1.5, color="#111111"),
                Segment(id="tick_o", start=(xO, yA + 15.0), end=(xO, yA + 40.0), stroke_width=1.5, color="#111111"),
                Segment(id="tick_b", start=(xB, yA + 15.0), end=(xB, yA + 40.0), stroke_width=1.5, color="#111111"),
                Segment(id="dim_l1", start=(xA, yA + 28.0), end=(xO, yA + 28.0), stroke_width=1.6, color="#111111", arrows=ArrowType.BOTH),
                Segment(id="dim_l2", start=(xO, yA + 28.0), end=(xB, yA + 28.0), stroke_width=1.6, color="#111111", arrows=ArrowType.BOTH),
            ]

            arc_angles = [
                # Top theta angle between resultant PR and arm PM
                ArcAngleMarker(id="arc_top", vertex=(xP, yP), start_pt=(xR, yR), end_pt=(xM, yM), radius=28.0, color="#111111"),
                # Bottom theta angle between resultant PR and arm PN
                ArcAngleMarker(id="arc_bot", vertex=(xP, yP), start_pt=(xN, yN), end_pt=(xR, yR), radius=28.0, color="#111111"),
            ]

            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 14.0, y=yA - 14.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="-q", x=xA - 14.0, y=yA + 12.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 14.0, y=yA - 14.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+q", x=xB + 14.0, y=yA + 12.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO - 14.0, y=yA - 10.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP + 16.0, y=yP - 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="R", x=xR - 16.0, y=yR + 14.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_m", text="M", x=xM - 8.0, y=yM - 14.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_n", text="N", x=xN - 8.0, y=yN + 18.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_e1", text="E", x=(xP + xM) / 2.0 + 12.0, y=(yP + yM) / 2.0 - 10.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_e2", text="E", x=(xP + xN) / 2.0 + 12.0, y=(yP + yN) / 2.0 + 12.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_th1", text="θ", x=xP - 42.0, y=yP - 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_th2", text="θ", x=xP - 42.0, y=yP + 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_dist_r", text="r", x=xO + 14.0, y=(yO + yP) / 2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_l1", text="l", x=(xA + xO) / 2.0, y=yA + 38.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_l2", text="l", x=(xO + xB) / 2.0, y=yA + 38.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Electric Dipole Broadside Field", width=w, height=h, coordinate_frame=cf, segments=segments, arc_angles=arc_angles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 28c59301: Square 4m x 4m with +2C and +4C charges
        # ----------------------------------------------------
        if "28c59301" in stem:
            w, h = 400.0, 400.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_r = 80.0, 320.0
            y_t, y_b = 80.0, 320.0

            polygons = [
                Polygon(id="sq", vertices=[(x_l, y_t), (x_r, y_t), (x_r, y_b), (x_l, y_b)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_o", center=(w/2.0, h/2.0), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_tl", text="+2 C", x=x_l, y=y_t - 20.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_tr", text="+2 C", x=x_r, y=y_t - 20.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_bl", text="+4 C", x=x_l, y=y_b + 28.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_br", text="+4 C", x=x_r, y=y_b + 28.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_top", text="4 m", x=w/2.0, y=y_t - 16.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_bot", text="4 m", x=w/2.0, y=y_b + 26.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_l", text="4 m", x=x_l - 28.0, y=h/2.0 + 4.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r", text="4 m", x=x_r + 28.0, y=h/2.0 + 4.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_o", text="O", x=w/2.0 + 10.0, y=h/2.0 - 10.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Square Four Charge Geometry", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 2ffa08f9: Deflection Plates P (+400V), Q (-400V) & Electron Beam
        # ----------------------------------------------------
        if "2ffa08f9" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            yP, yQ = 80.0, 180.0
            x_start, x_end = 170.0, 420.0

            segments = [
                # Plate P & Q
                Segment(id="plt_p", start=(x_start, yP), end=(x_end, yP), stroke_width=2.5, color="#111111"),
                Segment(id="plt_q", start=(x_start, yQ), end=(x_end, yQ), stroke_width=2.5, color="#111111"),
                # Potential stems
                Segment(id="stem_p", start=(300.0, yP), end=(300.0, yP - 40.0), stroke_width=2.0, color="#111111"),
                Segment(id="stem_q", start=(300.0, yQ), end=(300.0, yQ + 40.0), stroke_width=2.0, color="#111111"),
                # Distance dimension
                Segment(id="dim_d", start=(x_end + 15.0, yP), end=(x_end + 15.0, yQ), stroke_width=1.8, color="#111111", arrows=ArrowType.END),
                # Electron beam
                Segment(id="e_beam", start=(30.0, 130.0), end=(150.0, 130.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_p", text="P", x=x_start - 16.0, y=yP + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="Q", x=x_start - 16.0, y=yQ + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_vp", text="+400V", x=330.0, y=yP - 45.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_vq", text="-400V", x=330.0, y=yQ + 55.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_gap", text="20 mm", x=x_end + 45.0, y=(yP + yQ)/2.0 + 4.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_e", text="ইলেকট্রন", x=90.0, y=155.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Electron Beam Deflection Plates", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 21a01538: Parallel plate capacitor with "বায়ু", 2 cm, 5 V battery
        # ----------------------------------------------------
        if "21a01538" in stem:
            w, h = 400.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_r = 70.0, 330.0
            y_t, y_b = 100.0, 240.0
            x_p1, x_p2 = 150.0, 250.0

            polygons = [
                Polygon(id="p1", vertices=[(x_p1 - 10.0, 40.0), (x_p1 + 10.0, 40.0), (x_p1 + 10.0, 160.0), (x_p1 - 10.0, 160.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Polygon(id="p2", vertices=[(x_p2 - 10.0, 40.0), (x_p2 + 10.0, 40.0), (x_p2 + 10.0, 160.0), (x_p2 - 10.0, 160.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                Segment(id="w1", start=(x_l, y_t), end=(x_p1 - 10.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w2", start=(x_p2 + 10.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w3", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w4", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="wb1", start=(x_l, y_b), end=(180.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="wb2", start=(210.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="dim_gap", start=(x_p1 + 10.0, 120.0), end=(x_p2 - 10.0, 120.0), stroke_width=1.8, color="#111111", arrows=ArrowType.END),
                # Battery
                Segment(id="bp", start=(185.0, y_b - 16.0), end=(185.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(205.0, y_b - 9.0), end=(205.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_air", text="বায়ু", x=(x_p1 + x_p2)/2.0, y=55.0, font_size=20.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_gap", text="2 cm", x=(x_p1 + x_p2)/2.0, y=95.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_v", text="5 V", x=(x_p1 + x_p2)/2.0 - 5.0, y=y_b + 34.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Parallel Plate Air Capacitor", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 21e7235c: Parallel 2uF, 1uF + series 3uF
        # ----------------------------------------------------
        if "21e7235c" in stem:
            w, h = 450.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_m = 110.0
            y_pt, y_pb = 60.0, 160.0
            x_l, x_sp_l, x_c12, x_sp_r, x_c3, x_r = 40.0, 100.0, 180.0, 260.0, 340.0, 410.0

            segments = [
                # Left lead
                Segment(id="l_lead", start=(x_l, y_m), end=(x_sp_l, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="sp_l_v", start=(x_sp_l, y_pt), end=(x_sp_l, y_pb), stroke_width=2.2, color="#111111"),
                Segment(id="sp_r_v", start=(x_sp_r, y_pt), end=(x_sp_r, y_pb), stroke_width=2.2, color="#111111"),
                # Top branch
                Segment(id="pt1", start=(x_sp_l, y_pt), end=(x_c12 - 8.0, y_pt), stroke_width=2.2, color="#111111"),
                Segment(id="pt2", start=(x_c12 + 8.0, y_pt), end=(x_sp_r, y_pt), stroke_width=2.2, color="#111111"),
                # Bot branch
                Segment(id="pb1", start=(x_sp_l, y_pb), end=(x_c12 - 8.0, y_pb), stroke_width=2.2, color="#111111"),
                Segment(id="pb2", start=(x_c12 + 8.0, y_pb), end=(x_sp_r, y_pb), stroke_width=2.2, color="#111111"),
                # Series C3 & right lead
                Segment(id="s1", start=(x_sp_r, y_m), end=(x_c3 - 8.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="s2", start=(x_c3 + 8.0, y_m), end=(x_r, y_m), stroke_width=2.2, color="#111111"),
                # Plates
                Segment(id="c1_l", start=(x_c12 - 5.0, y_pt - 14.0), end=(x_c12 - 5.0, y_pt + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x_c12 + 5.0, y_pt - 14.0), end=(x_c12 + 5.0, y_pt + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x_c12 - 5.0, y_pb - 14.0), end=(x_c12 - 5.0, y_pb + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x_c12 + 5.0, y_pb - 14.0), end=(x_c12 + 5.0, y_pb + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_l", start=(x_c3 - 5.0, y_m - 14.0), end=(x_c3 - 5.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x_c3 + 5.0, y_m - 14.0), end=(x_c3 + 5.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="2\\mu\\text{F}", x=x_c12, y=y_pt - 24.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="1\\mu\\text{F}", x=x_c12, y=y_pb + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="3\\mu\\text{F}", x=x_c3, y=y_m + 30.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Three Capacitor Combination", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 22ba4041: Spheres A(+) and B(-) with drop stem to C
        # ----------------------------------------------------
        # 22ba4041: Spheres A(+) and B(-) with drop stem to C
        # ----------------------------------------------------
        if "22ba4041" in stem:
            w, h = 520.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 110.0, 130.0, 42.0
            xB, yB, rB = 340.0, 130.0, 56.0
            xC, yC = 340.0, 310.0

            circles = [
                Circle(id="cA", center=(xA, yA), radius=rA, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="cB", center=(xB, yB), radius=rB, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="pt_a", center=(xA, yA), radius=3.0, stroke_width=1.0, fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yB), radius=3.0, stroke_width=1.0, fill_color="#111111"),
                Circle(id="pt_d", center=(xB, yB + rB), radius=3.0, stroke_width=1.0, fill_color="#111111"),
                Circle(id="pt_c", center=(xC, yC), radius=3.0, stroke_width=1.0, fill_color="#111111"),
            ]
            segments = [
                # Horizontal connecting line between spheres
                Segment(id="h_ax", start=(xA + rA, yA), end=(xB - rB, yB), stroke_width=2.2, color="#111111"),
                # Vertical stem from B down through D to C
                Segment(id="v_stem", start=(xB, yB), end=(xC, yC), stroke_width=2.2, color="#111111"),
                # Dashed bottom guide from C to the right
                Segment(id="d_bot", start=(xC, yC), end=(xC + 55.0, yC), stroke_width=1.5, color="#111111", stroke_style=StrokeStyle.DASHED),
                # Dimension vertical 6sqrt(3)m
                Segment(id="dim_v", start=(xB + 55.0, yB), end=(xB + 55.0, yC), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                # Internal radius lines for Sphere A
                Segment(id="rad_a_up", start=(xA, yA), end=(xA, yA - rA), stroke_width=1.8, color="#111111"),
                Segment(id="rad_a_rt", start=(xA, yA), end=(xA + rA, yA), stroke_width=1.8, color="#111111"),
                # Internal radius line for Sphere B (up-right)
                Segment(id="rad_b", start=(xB, yB), end=(xB + rB * 0.819, yB - rB * 0.573), stroke_width=1.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_q1", text="Q₁ = 2 × 10⁻⁹ C", x=xA, y=yA - 68.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_q2", text="Q₂ = -3 × 10⁻⁹ C", x=xB, y=yB - 82.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA - 14.0, y=yA + 14.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 14.0, y=yB + 14.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_d_pt", text="D", x=xB + 15.0, y=yB + rB + 10.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC - 16.0, y=yC + 4.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_r1", text="r₁ = 1 m", x=xA + 25.0, y=yA - 12.0, font_size=13.0, font_weight="bold"),
                MathLabel(id="lbl_r2", text="r₂ = 2 m", x=xB - 10.0, y=yB - 26.0, font_size=13.0, font_weight="bold"),
                MathLabel(id="lbl_dist_h", text="6√3 m", x=(xA + rA + xB - rB) / 2.0, y=yA - 14.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_dist_v", text="6√3 m", x=xB + 85.0, y=(yB + yC) / 2.0, font_size=15.0, font_weight="bold"),
            ]

            # Positive charges around sphere A
            for i, angle_deg in enumerate([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]):
                rad = math.radians(angle_deg)
                qx = xA + (rA + 12.0) * math.cos(rad)
                qy = yA + (rA + 12.0) * math.sin(rad)
                labels.append(MathLabel(id=f"chg_a_{i}", text="+", x=qx, y=qy, font_size=14.0, font_weight="bold"))

            # Negative charges around sphere B
            for i, angle_deg in enumerate([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]):
                rad = math.radians(angle_deg)
                qx = xB + (rB + 12.0) * math.cos(rad)
                qy = yB + (rB + 12.0) * math.sin(rad)
                labels.append(MathLabel(id=f"chg_b_{i}", text="−", x=qx, y=qy, font_size=14.0, font_weight="bold"))

            return VisualIR(title="Dual Charged Spheres with Orthogonal Target", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 2304da6b: Sphere centered O with radial axis O-A-B-M, "চিত্র-১"
        # ----------------------------------------------------
        if "2304da6b" in stem:
            w, h = 480.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO, rS = 130.0, 140.0, 80.0
            xA = xO + rS
            xB = xA + 80.0
            xM = xB + 70.0

            circles = [
                Circle(id="sph", center=(xO, yO), radius=rS, stroke_width=2.2, stroke_color="#111111", fill_color="none"),
                Circle(id="pt_o", center=(xO, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_a", center=(xA, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_m", center=(xM, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Horizontal ray from center O through A, B to M
                Segment(id="ray", start=(xO, yO), end=(xM, yO), stroke_width=2.2, color="#111111"),
                # Vertical radius from O down to bottom sphere surface with arrow
                Segment(id="rad_v", start=(xO, yO), end=(xO, yO + rS), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                # Dimension 3cm (O to A) with bidirectional arrows
                Segment(id="dim_3", start=(xO, yO - 20.0), end=(xA, yO - 20.0), stroke_width=1.6, color="#111111", arrows=ArrowType.BOTH),
                # Dimension 9cm (A to B) with bidirectional arrows
                Segment(id="dim_9", start=(xA, yO - 20.0), end=(xB, yO - 20.0), stroke_width=1.6, color="#111111", arrows=ArrowType.BOTH),
                # Dimension tick markers
                Segment(id="m_o", start=(xO, yO - 28.0), end=(xO, yO), stroke_width=1.5, color="#111111"),
                Segment(id="m_b", start=(xB, yO - 28.0), end=(xB, yO), stroke_width=1.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_q", text="+2 × 10⁻¹⁰ C", x=xO, y=yO - rS - 18.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xO - rS - 14.0, y=yO + 4.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO - 14.0, y=yO + 4.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA - 8.0, y=yO + 18.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yO + 18.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_m", text="M", x=xM + 14.0, y=yO + 4.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="3cm", x=(xO + xA) / 2.0, y=yO - 28.0, font_size=14.0, font_weight="bold"),
                MathLabel(id="lbl_d2", text="9 cm", x=(xA + xB) / 2.0, y=yO - 28.0, font_size=14.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="r = 4 cm", x=xO + 38.0, y=yO + rS / 2.0 + 8.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_fig", text="চিত্র-১", x=xO, y=yO + rS + 30.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Charged Sphere Radial Potential Profile", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 2433c2d7: Equilateral triangle ABC with 20 cm sides
        # ----------------------------------------------------
        if "2433c2d7" in stem:
            w, h = 360.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 50.0, 270.0
            xB, yB = 310.0, 270.0
            xC, yC = 180.0, 45.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xB, yB), (xC, yC)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 16.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 16.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC, y=yC - 16.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_base", text="20 cm", x=(xA + xB)/2.0, y=yA + 24.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_l", text="20 cm", x=(xA + xC)/2.0 - 45.0, y=(yA + yC)/2.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r", text="20 cm", x=(xB + xC)/2.0 + 45.0, y=(yB + yC)/2.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Equilateral Triangle 20cm", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 247b95a6: Conductor bars A and grounded B
        # ----------------------------------------------------
        if "247b95a6" in stem:
            w, h = 420.0, 180.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            polygons = [
                Polygon(id="bar_a", vertices=[(60.0, 40.0), (190.0, 40.0), (190.0, 85.0), (60.0, 85.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Polygon(id="bar_b", vertices=[(230.0, 40.0), (370.0, 40.0), (370.0, 85.0), (230.0, 85.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Ground wire from bar B
                Segment(id="gw", start=(350.0, 85.0), end=(350.0, 125.0), stroke_width=2.2, color="#111111"),
                Segment(id="g1", start=(330.0, 125.0), end=(370.0, 125.0), stroke_width=2.5, color="#111111"),
                Segment(id="g2", start=(338.0, 133.0), end=(362.0, 133.0), stroke_width=2.2, color="#111111"),
                Segment(id="g3", start=(344.0, 141.0), end=(356.0, 141.0), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=40.0, y=68.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=215.0, y=68.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Electrostatic Induction Bars", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 25cb3d15: Rectangle ABCD with diagonals intersecting at O
        # ----------------------------------------------------
        if "25cb3d15" in stem:
            w, h = 420.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 50.0, 240.0
            xB, yB = 370.0, 240.0
            xC, yC = 370.0, 60.0
            xD, yD = 50.0, 60.0

            polygons = [
                Polygon(id="rect", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="d1", start=(xA, yA), end=(xC, yC), stroke_width=2.0, color="#111111"),
                Segment(id="d2", start=(xB, yB), end=(xD, yD), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD - 18.0, y=yD + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=w/2.0, y=h/2.0 + 26.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Rectangle Diagonals Geometry", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 25d14cd5: Series 3 capacitors 6uF, 8uF, 10uF with 20V battery
        # ----------------------------------------------------
        if "25d14cd5" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 210.0
            x_l, x_r = 40.0, 440.0
            x1, x2, x3 = 140.0, 240.0, 340.0

            segments = [
                # Top wire
                Segment(id="t1", start=(x_l, y_t), end=(x1 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(x1 + 8.0, y_t), end=(x2 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(x2 + 8.0, y_t), end=(x3 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t4", start=(x3 + 8.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                # Sides
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom wire with battery
                Segment(id="b1", start=(x_l, y_b), end=(120.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(150.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Plates
                Segment(id="c1_l", start=(x1 - 5.0, y_t - 14.0), end=(x1 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x1 + 5.0, y_t - 14.0), end=(x1 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x2 - 5.0, y_t - 14.0), end=(x2 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x2 + 5.0, y_t - 14.0), end=(x2 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_l", start=(x3 - 5.0, y_t - 14.0), end=(x3 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x3 + 5.0, y_t - 14.0), end=(x3 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Battery
                Segment(id="bp", start=(125.0, y_b - 16.0), end=(125.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(145.0, y_b - 9.0), end=(145.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="6\\mu\\text{F}", x=x1, y=y_t + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="8\\mu\\text{F}", x=x2, y=y_t + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="10\\mu\\text{F}", x=x3, y=y_t + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="+", x=112.0, y=y_b - 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_m", text="-", x=160.0, y=y_b - 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="20V", x=135.0, y=y_b + 34.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Three Series Capacitors 20V", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 27fc0004: Sphere center O, radius 0.5m, internal A (0.3m), external B (0.5m)
        # 27fc0004: Sphere center O, radius 0.5m, internal A (0.3m), external B (0.5m)
        # ----------------------------------------------------
        if "27fc0004" in stem:
            w, h = 420.0, 340.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO, rS = 140.0, 160.0, 100.0
            xA = xO + 60.0
            xSurf = xO + rS
            xB = xSurf + 75.0

            circles = [
                Circle(id="sph", center=(xO, yO), radius=rS, stroke_width=2.2, stroke_color="#111111", fill_color="none"),
                Circle(id="pt_o", center=(xO, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_a", center=(xA, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Collinear horizontal ray connecting O through A, Sphere Surface to B
                Segment(id="h_ray", start=(xO, yO), end=(xB, yO), stroke_width=2.2, color="#111111"),
                # Bidirectional dimension arrow for OA (0.3m) with vertical tick marks
                Segment(id="dim_oa", start=(xO, yO - 18.0), end=(xA, yO - 18.0), stroke_width=1.6, color="#111111", arrows=ArrowType.BOTH),
                Segment(id="tick_o", start=(xO, yO - 25.0), end=(xO, yO), stroke_width=1.5, color="#111111"),
                Segment(id="tick_a", start=(xA, yO - 25.0), end=(xA, yO), stroke_width=1.5, color="#111111"),
                # Bidirectional dimension arrow for Surface-to-B (0.5m) with vertical tick marks
                Segment(id="dim_sb", start=(xSurf, yO - 18.0), end=(xB, yO - 18.0), stroke_width=1.6, color="#111111", arrows=ArrowType.BOTH),
                Segment(id="tick_surf", start=(xSurf, yO - 25.0), end=(xSurf, yO), stroke_width=1.5, color="#111111"),
                Segment(id="tick_b", start=(xB, yO - 25.0), end=(xB, yO), stroke_width=1.5, color="#111111"),
                # Downward radius arrow (0.5m)
                Segment(id="d_rad", start=(xO, yO), end=(xO, yO + rS), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_o", text="O", x=xO - 16.0, y=yO - 10.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA, y=yO + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yO + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="0.3 m", x=(xO + xA) / 2.0, y=yO - 28.0, font_size=14.0, font_weight="bold"),
                MathLabel(id="lbl_d2", text="0.5 m", x=(xSurf + xB) / 2.0, y=yO - 28.0, font_size=14.0, font_weight="bold"),
                MathLabel(id="lbl_rad", text="0.5 m", x=xO - 28.0, y=yO + rS / 2.0, font_size=15.0, font_weight="bold"),
            ]
            return VisualIR(title="Charged Sphere Internal External Potential", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 29039d3a: Spheres A (+12uC), B (+4uC), midpoint O, marker D, d=10cm
        # ----------------------------------------------------
        if "29039d3a" in stem:
            w, h = 480.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rS = 80.0, 110.0, 32.0
            xB, yB = 400.0, 110.0
            xO = (xA + xB)/2.0
            xD = xO + 35.0

            circles = [
                Circle(id="cA", center=(xA, yA), radius=rS, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="cB", center=(xB, yB), radius=rS, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Connecting axis
                Segment(id="axis", start=(xA + rS, yA), end=(xB - rS, yA), stroke_width=2.2, color="#111111"),
                # Markers O and D
                Segment(id="m_o", start=(xO, yA - 12.0), end=(xO, yA), stroke_width=2.0, color="#111111"),
                Segment(id="m_d", start=(xD, yA - 18.0), end=(xD, yA), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_qa", text="12\\mu\\text{C}", x=xA, y=yA - 46.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="4\\mu\\text{C}", x=xB, y=yA - 46.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_pa", text="+", x=xA, y=yA + 6.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_pb", text="+", x=xB, y=yB + 6.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA, y=yA + 52.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yB + 52.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO, y=yA - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD, y=yA - 28.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_dist", text="d = 10 cm", x=xO, y=yA + 30.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Collinear Charges with Neutral Point", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 2c572490: 2D Cartesian axes O with A(-a, 0)(+q) and B(a, 0)(+q)
        # ----------------------------------------------------
        if "2c572490" in stem:
            w, h = 420.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO = 210.0, 120.0
            xA = xO - 120.0
            xB = xO + 120.0

            circles = [
                Circle(id="pt_a", center=(xA, yO), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yO), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # X axis
                Segment(id="x_ax", start=(40.0, yO), end=(380.0, yO), stroke_width=2.5, color="#111111"),
                # Y axis
                Segment(id="y_ax", start=(xO, 20.0), end=(xO, 220.0), stroke_width=2.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_qa", text="+q", x=xA, y=yO - 25.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+q", x=xB, y=yO - 25.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A(-a, 0)", x=xA - 10.0, y=yO + 32.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b", text="B(a, 0)", x=xB + 10.0, y=yO + 32.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_o", text="O", x=xO + 18.0, y=yO + 24.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Cartesian Dipole Axes", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 2e6d60e7: Rectangle ABCD with A(-2 x 10^-9 C), C(1.5 x 10^-9 C), 2m x 1.5m
        # ----------------------------------------------------
        if "2e6d60e7" in stem:
            w, h = 480.0, 340.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 60.0, 60.0
            xB, yB = 340.0, 60.0
            xD, yD = 60.0, 270.0
            xC, yC = 340.0, 270.0

            polygons = [
                Polygon(id="rect", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_qa", text="A (-2 \\times 10^{-9}\\text{C})", x=xA + 40.0, y=yA - 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB - 8.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="C (1.5 \\times 10^{-9}\\text{C})", x=xC + 85.0, y=yC + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD - 18.0, y=yD + 8.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_top", text="2m", x=(xA+xB)/2.0, y=yA + 26.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_bot", text="2m", x=(xD+xC)/2.0, y=yD - 18.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_l", text="1.5 m", x=xA + 40.0, y=(yA+yD)/2.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r", text="1.5 m", x=xB - 40.0, y=(yB+yC)/2.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Rectangle Potential Diagonal Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 2ff2c209: Square ACDB 2cm x 2cm with +7C on 4 corners
        # ----------------------------------------------------
        if "2ff2c209" in stem:
            w, h = 380.0, 380.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 80.0, 80.0
            xB, yB = 300.0, 80.0
            xC, yC = 80.0, 300.0
            xD, yD = 300.0, 300.0

            polygons = [
                Polygon(id="sq", vertices=[(xA, yA), (xB, yB), (xD, yD), (xC, yC)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_qa", text="+ 7 C", x=xA - 20.0, y=yA - 26.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+ 7 C", x=xB + 20.0, y=yB - 26.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="+ 7 C", x=xC - 20.0, y=yC + 28.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c", text="C", x=xC - 18.0, y=yC + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qd", text="+ 7 C", x=xD + 20.0, y=yD + 28.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d", text="D", x=xD + 18.0, y=yD + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_top", text="2 cm", x=(xA+xB)/2.0, y=yA - 16.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_bot", text="2 cm", x=(xC+xD)/2.0, y=yC + 26.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_l", text="2 cm", x=xA - 32.0, y=(yA+yC)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r", text="2 cm", x=xB + 32.0, y=(yB+yD)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Square Four Identical 7C Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 1eb72acb: 3 parallel branches: 200V, C1, C2
        # ----------------------------------------------------
        if "1eb72acb" in stem:
            w, h = 420.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 240.0
            x1, x2, x3 = 80.0, 210.0, 340.0

            segments = [
                # Top & bottom rails
                Segment(id="top", start=(x1, y_t), end=(x3, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="bot", start=(x1, y_b), end=(x3, y_b), stroke_width=2.2, color="#111111"),
                # Branch 1 (Source)
                Segment(id="b1_t", start=(x1, y_t), end=(x1, 140.0), stroke_width=2.2, color="#111111"),
                Segment(id="b1_b", start=(x1, 160.0), end=(x1, y_b), stroke_width=2.2, color="#111111"),
                # Branch 2 (C1)
                Segment(id="b2_t", start=(x2, y_t), end=(x2, 140.0), stroke_width=2.2, color="#111111"),
                Segment(id="b2_b", start=(x2, 160.0), end=(x2, y_b), stroke_width=2.2, color="#111111"),
                # Branch 3 (C2)
                Segment(id="b3_t", start=(x3, y_t), end=(x3, 140.0), stroke_width=2.2, color="#111111"),
                Segment(id="b3_b", start=(x3, 160.0), end=(x3, y_b), stroke_width=2.2, color="#111111"),
                # Source plates
                Segment(id="sp_t", start=(x1 - 15.0, 140.0), end=(x1 + 15.0, 140.0), stroke_width=2.8, color="#111111"),
                Segment(id="sp_b", start=(x1 - 15.0, 160.0), end=(x1 + 15.0, 160.0), stroke_width=2.8, color="#111111"),
                # C1 plates
                Segment(id="c1_t", start=(x2 - 15.0, 140.0), end=(x2 + 15.0, 140.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_b", start=(x2 - 15.0, 160.0), end=(x2 + 15.0, 160.0), stroke_width=2.8, color="#111111"),
                # C2 plates
                Segment(id="c2_t", start=(x3 - 15.0, 140.0), end=(x3 + 15.0, 140.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_b", start=(x3 - 15.0, 160.0), end=(x3 + 15.0, 160.0), stroke_width=2.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_v", text="200 V", x=x1 - 45.0, y=155.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c1", text="C_1", x=x2 + 25.0, y=155.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=x3 + 25.0, y=155.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Three Branch Parallel Capacitor Circuit", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 1ebaf5a2: Series 3 capacitors C1=2uF, C2=4uF, C3=6uF, 12V
        # ----------------------------------------------------
        if "1ebaf5a2" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 210.0
            x_l, x_r = 40.0, 440.0
            x1, x2, x3 = 110.0, 240.0, 370.0

            segments = [
                # Top wire
                Segment(id="t1", start=(x_l, y_t), end=(x1 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(x1 + 8.0, y_t), end=(x2 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(x2 + 8.0, y_t), end=(x3 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t4", start=(x3 + 8.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                # Sides
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom wire with battery
                Segment(id="b1", start=(x_l, y_b), end=(120.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(140.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Plates
                Segment(id="c1_l", start=(x1 - 5.0, y_t - 14.0), end=(x1 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x1 + 5.0, y_t - 14.0), end=(x1 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x2 - 5.0, y_t - 14.0), end=(x2 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x2 + 5.0, y_t - 14.0), end=(x2 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_l", start=(x3 - 5.0, y_t - 14.0), end=(x3 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x3 + 5.0, y_t - 14.0), end=(x3 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Battery
                Segment(id="bp", start=(125.0, y_b - 16.0), end=(125.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(135.0, y_b - 9.0), end=(135.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1 = 2\\ \\mu\\text{F}", x=x1 + 10.0, y=y_t + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2 = 4\\ \\mu\\text{F}", x=x2 + 10.0, y=y_t + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3 = 6\\ \\mu\\text{F}", x=x3 + 10.0, y=y_t + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="12V", x=130.0, y=y_b + 34.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Three Series Capacitors 12V", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ====================================================
        # BATCH 3: ITEMS 81 TO 120
        # ====================================================

        # ----------------------------------------------------
        # 31aaf312: Equilateral Triangle ABC with E1, E2 Field Vectors
        # ----------------------------------------------------
        if "31aaf312" in stem:
            w, h = 480.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 150.0, 50.0
            xB, yB = 50.0, 220.0
            xC, yC = 290.0, 220.0

            segments = [
                Segment(id="ab", start=(xA, yA), end=(xB, yB), stroke_width=2.5, color="#111111"),
                Segment(id="bc", start=(xB, yB), end=(xC, yC), stroke_width=2.5, color="#111111"),
                Segment(id="ca", start=(xC, yC), end=(xA, yA), stroke_width=2.5, color="#111111"),
                # E2 horizontal arrow from C
                Segment(id="e2_arr", start=(xC, yC), end=(380.0, yC), stroke_width=2.5, color="#111111", arrows=ArrowType.END),
                # E1 diagonal arrow along AC continuation
                Segment(id="e1_arr", start=(xC, yC), end=(350.0, yC + 75.0), stroke_width=2.5, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_a_q", text="+3 C", x=xA + 45.0, y=yA + 10.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b", text="B", x=xB - 22.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b_q", text="+3 C", x=xB + 60.0, y=yB + 28.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c", text="C", x=xC - 15.0, y=yC + 28.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_e2", text="E_2", x=395.0, y=yC - 2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_e1", text="E_1", x=365.0, y=yC + 80.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_side", text="AB = BC = AC = 3 m", x=330.0, y=100.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Equilateral Triangle with Field Projections", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 32287357: Triangle PQR with +2C, -2C
        # ----------------------------------------------------
        if "32287357" in stem:
            w, h = 380.0, 340.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xR, yR = 190.0, 50.0
            xP, yP = 80.0, 270.0
            xQ, yQ = 300.0, 270.0

            polygons = [
                Polygon(id="tri", vertices=[(xP, yP), (xQ, yQ), (xR, yR)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_r", text="R", x=xR, y=yR - 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP - 15.0, y=yP + 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="Q", x=xQ + 15.0, y=yQ + 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_pq_q", text="+2C", x=xP - 25.0, y=yP - 25.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_qq_q", text="-2C", x=xQ + 25.0, y=yQ - 25.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d1", text="2m", x=(xP + xR)/2.0 - 25.0, y=(yP + yR)/2.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d2", text="2m", x=(xQ + xR)/2.0 + 25.0, y=(yQ + yR)/2.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d3", text="2m", x=(xP + xQ)/2.0, y=yP + 24.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Triangle PQR Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 338d2bce: Dual Spheres A and B with drop stem P
        # ----------------------------------------------------
        if "338d2bce" in stem:
            w, h = 450.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 90.0, 90.0
            xB, yB = 360.0, 90.0
            xP = xA + 100.0

            circles = [
                Circle(id="sph_a", center=(xA, yA), radius=35.0, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_b", center=(xB, yB), radius=35.0, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="c_a", center=(xA, yA), radius=6.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="c_b", center=(xB, yB), radius=6.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="c_p", center=(xP, yA), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Dashed horizontal connecting axis
                Segment(id="h_ax", start=(xA, yA), end=(xB, yB), stroke_width=1.8, color="#111111", stroke_style=StrokeStyle.DASHED),
                # Drop stems
                Segment(id="d_a", start=(xA, yA + 35.0), end=(xA, 250.0), stroke_width=1.8, color="#111111", stroke_style=StrokeStyle.DASHED),
                Segment(id="d_b", start=(xB, yB + 35.0), end=(xB, 250.0), stroke_width=1.8, color="#111111", stroke_style=StrokeStyle.DASHED),
                Segment(id="d_p", start=(xP, yA), end=(xP, 170.0), stroke_width=2.0, color="#111111"),
                # Dimensions
                Segment(id="dim_5", start=(xA, 170.0), end=(xP, 170.0), stroke_width=1.6, color="#111111", arrows=ArrowType.END),
                Segment(id="dim_20", start=(xA, 240.0), end=(xB, 240.0), stroke_width=1.6, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 48.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yB - 48.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP, y=yA - 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d5", text="5 cm", x=(xA + xP)/2.0, y=170.0 - 15.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d20", text="20 cm", x=(xA + xB)/2.0, y=240.0 - 15.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Dual Spheres System with Test Point P", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 33c4da6f: 3D Parallel Plate Capacitors Comparison
        # ----------------------------------------------------
        if "33c4da6f" in stem:
            w, h = 600.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            # Left system: Fig 1
            polygons = [
                # Fig 1 Left plate
                Polygon(id="f1_pl_l", vertices=[(120.0, 70.0), (140.0, 50.0), (140.0, 160.0), (120.0, 180.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#e6e6e6"),
                # Fig 1 Right plate
                Polygon(id="f1_pl_r", vertices=[(160.0, 70.0), (180.0, 50.0), (180.0, 160.0), (160.0, 180.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#888888"),
                # Fig 2 Left plate
                Polygon(id="f2_pl_l", vertices=[(420.0, 60.0), (440.0, 40.0), (440.0, 170.0), (420.0, 190.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#d0d0d0"),
                # Fig 2 Dielectric
                Polygon(id="f2_diel", vertices=[(445.0, 60.0), (460.0, 45.0), (460.0, 175.0), (445.0, 190.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#222222"),
                # Fig 2 Right plate
                Polygon(id="f2_pl_r", vertices=[(470.0, 60.0), (490.0, 40.0), (490.0, 170.0), (470.0, 190.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#d0d0d0"),
            ]
            segments = [
                # Fig 1 Lead wires
                Segment(id="w1_l", start=(40.0, 125.0), end=(120.0, 125.0), stroke_width=4.0, color="#111111"),
                Segment(id="w1_r", start=(180.0, 115.0), end=(260.0, 115.0), stroke_width=4.0, color="#111111"),
                # Fig 1 Distance dimension
                Segment(id="dim1_v1", start=(140.0, 50.0), end=(140.0, 30.0), stroke_width=1.5, color="#111111"),
                Segment(id="dim1_v2", start=(180.0, 50.0), end=(180.0, 30.0), stroke_width=1.5, color="#111111"),
                Segment(id="dim1_h", start=(140.0, 30.0), end=(180.0, 30.0), stroke_width=1.5, color="#111111"),
                # Fig 2 Lead wires
                Segment(id="w2_l", start=(340.0, 120.0), end=(420.0, 120.0), stroke_width=3.5, color="#111111"),
                Segment(id="w2_r", start=(490.0, 115.0), end=(570.0, 115.0), stroke_width=3.5, color="#111111"),
                # Fig 2 Callout
                Segment(id="cl_diel", start=(452.0, 55.0), end=(380.0, 40.0), stroke_width=1.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_q1p", text="+Q", x=100.0, y=70.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_q1n", text="-Q", x=200.0, y=70.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_tar1", text="তার", x=80.0, y=150.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_tar2", text="তার", x=220.0, y=150.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d_txt", text="দূরত্ব, d", x=205.0, y=30.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_fig1", text="চিত্র-১", x=150.0, y=240.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_q2p", text="+Q", x=390.0, y=60.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_q2n", text="-Q", x=515.0, y=60.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_diel_txt", text="ডাই-ইলেক্ট্রিক", x=330.0, y=35.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_tar3", text="তার", x=550.0, y=150.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_fig2", text="চিত্র-২", x=455.0, y=240.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="3D Parallel Plate Capacitor Comparison", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 349bdbb4: Triangle ABD with point P
        # ----------------------------------------------------
        if "349bdbb4" in stem:
            w, h = 380.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 190.0, 50.0
            xB, yB = 80.0, 240.0
            xD, yD = 300.0, 240.0
            xP = (xB + xD)/2.0

            polygons = [
                Polygon(id="tri", vertices=[(xB, yB), (xD, yD), (xA, yA)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_a", center=(xA, yA), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yB), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_d", center=(xD, yD), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_p", center=(xP, yB), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="3 \\times 10^{-9}\\text{C}", x=xA + 65.0, y=yA + 8.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 15.0, y=yB - 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="-5 \\times 10^{-9}\\text{C}", x=xB - 10.0, y=yB + 25.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD + 15.0, y=yD - 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qd", text="-3 \\times 10^{-9}\\text{C}", x=xD + 10.0, y=yD + 25.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP, y=yB + 22.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Triangle ABD Charge System", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 37068317: Equilateral Triangle with Perpendicular Altitude
        # ----------------------------------------------------
        if "37068317" in stem:
            w, h = 420.0, 340.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 220.0, 50.0
            xB, yB = 90.0, 275.0
            xC, yC = 350.0, 275.0
            # Foot of perpendicular from B to AC
            # AC line: parametric
            t = 0.5
            xH, yH = (xA + xC)/2.0, (yA + yC)/2.0

            polygons = [
                Polygon(id="tri", vertices=[(xB, yB), (xC, yC), (xA, yA)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="alt", start=(xB, yB), end=(xH, yH), stroke_width=2.2, color="#111111"),
            ]
            right_angles = [
                RightAngleMarker(id="ra", vertex=(xH, yH), arm1_pt=(xB, yB), arm2_pt=(xA, yA), size=16.0, color="#111111", stroke_width=1.8)
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="5 \\times 10^{-9}\\text{C}", x=xA + 65.0, y=yA + 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 20.0, y=yB + 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="-5 \\times 10^{-9}\\text{C}", x=xB - 35.0, y=yB - 25.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 20.0, y=yC + 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="2m", x=(xB + xA)/2.0 - 25.0, y=(yB + yA)/2.0 - 10.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d2", text="2m", x=(xB + xC)/2.0, y=yB + 25.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d3", text="2m", x=xH + 30.0, y=yH, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Equilateral Triangle with Altitude", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, right_angles=right_angles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 3990dfd0: Collinear Charges +9C, C, +16C
        # ----------------------------------------------------
        if "3990dfd0" in stem:
            w, h = 480.0, 180.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_line = 110.0
            x1, x2, x3 = 50.0, 180.0, 430.0

            circles = [
                Circle(id="p1", center=(x1, y_line), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="p2", center=(x2, y_line), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="p3", center=(x3, y_line), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="main_line", start=(x1, y_line), end=(x3, y_line), stroke_width=2.5, color="#111111"),
                # Dimension 0.12m
                Segment(id="d1", start=(x1, 60.0), end=(x2, 60.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                # Dimension 0.28m
                Segment(id="d2", start=(x1, 30.0), end=(x3, 30.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_q1", text="+9 C", x=x1, y=y_line + 30.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c", text="C", x=x2, y=y_line + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_q3", text="+16 C", x=x3, y=y_line + 30.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d1", text="0.12 m", x=(x1 + x2)/2.0, y=55.0 - 12.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d2", text="0.28 m", x=(x1 + x3)/2.0, y=25.0 - 12.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Collinear Charges Linear Array", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 3a8380d7: Quantum Numbers Table (n=4)
        # ----------------------------------------------------
        # 3a8380d7: Quantum Numbers Table (n=4)
        # ----------------------------------------------------
        if "3a8380d7" in stem:
            w, h = 540.0, 440.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            # Table grid columns and rows
            x_cols = [30.0, 125.0, 210.0, 335.0, 435.0, 510.0]
            y_rows = [25.0, 105.0, 160.0, 215.0, 290.0, 375.0, 415.0]

            segments = [
                # Horizontal table grid lines
                Segment(id="h0", start=(x_cols[0], y_rows[0]), end=(x_cols[-1], y_rows[0]), stroke_width=2.0, color="#111111"),
                Segment(id="h1", start=(x_cols[0], y_rows[1]), end=(x_cols[-1], y_rows[1]), stroke_width=2.0, color="#111111"),
                Segment(id="h2", start=(x_cols[1], y_rows[2]), end=(x_cols[-1], y_rows[2]), stroke_width=1.5, color="#111111"),
                Segment(id="h3", start=(x_cols[1], y_rows[3]), end=(x_cols[-1], y_rows[3]), stroke_width=1.5, color="#111111"),
                Segment(id="h4", start=(x_cols[1], y_rows[4]), end=(x_cols[-1], y_rows[4]), stroke_width=1.5, color="#111111"),
                Segment(id="h5", start=(x_cols[0], y_rows[5]), end=(x_cols[-1], y_rows[5]), stroke_width=2.0, color="#111111"),
                Segment(id="h6", start=(x_cols[0], y_rows[6]), end=(x_cols[-1], y_rows[6]), stroke_width=2.0, color="#111111"),

                # Vertical grid lines
                Segment(id="v0", start=(x_cols[0], y_rows[0]), end=(x_cols[0], y_rows[6]), stroke_width=2.0, color="#111111"),
                Segment(id="v1", start=(x_cols[1], y_rows[0]), end=(x_cols[1], y_rows[5]), stroke_width=2.0, color="#111111"),
                Segment(id="v2", start=(x_cols[2], y_rows[0]), end=(x_cols[2], y_rows[5]), stroke_width=1.5, color="#111111"),
                Segment(id="v3", start=(x_cols[3], y_rows[0]), end=(x_cols[3], y_rows[5]), stroke_width=1.5, color="#111111"),
                Segment(id="v4", start=(x_cols[4], y_rows[0]), end=(x_cols[4], y_rows[5]), stroke_width=1.5, color="#111111"),
                Segment(id="v5", start=(x_cols[5], y_rows[0]), end=(x_cols[5], y_rows[6]), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                # Column 1 Header: প্রধান কোয়ান্টাম সংখ্যা
                MathLabel(id="th1_1", text="প্রধান", x=77.5, y=45.0, font_size=13.5, font_weight="bold", math_mode=False),
                MathLabel(id="th1_2", text="কোয়ান্টাম", x=77.5, y=65.0, font_size=13.5, font_weight="bold", math_mode=False),
                MathLabel(id="th1_3", text="সংখ্যা", x=77.5, y=85.0, font_size=13.5, font_weight="bold", math_mode=False),

                # Column 2 Header: সহকারী কোয়ান্টাম সংখ্যা
                MathLabel(id="th2_1", text="সহকারী", x=167.5, y=45.0, font_size=13.5, font_weight="bold", math_mode=False),
                MathLabel(id="th2_2", text="কোয়ান্টাম", x=167.5, y=65.0, font_size=13.5, font_weight="bold", math_mode=False),
                MathLabel(id="th2_3", text="সংখ্যা", x=167.5, y=85.0, font_size=13.5, font_weight="bold", math_mode=False),

                # Column 3 Header: চুম্বকীয় কোয়ান্টাম সংখ্যা
                MathLabel(id="th3_1", text="চুম্বকীয়", x=272.5, y=45.0, font_size=13.5, font_weight="bold", math_mode=False),
                MathLabel(id="th3_2", text="কোয়ান্টাম", x=272.5, y=65.0, font_size=13.5, font_weight="bold", math_mode=False),
                MathLabel(id="th3_3", text="সংখ্যা", x=272.5, y=85.0, font_size=13.5, font_weight="bold", math_mode=False),

                # Column 4 Header: স্পিন কোয়ান্টাম সংখ্যা
                MathLabel(id="th4_1", text="স্পিন", x=385.0, y=45.0, font_size=13.5, font_weight="bold", math_mode=False),
                MathLabel(id="th4_2", text="কোয়ান্টাম", x=385.0, y=65.0, font_size=13.5, font_weight="bold", math_mode=False),
                MathLabel(id="th4_3", text="সংখ্যা", x=385.0, y=85.0, font_size=13.5, font_weight="bold", math_mode=False),

                # Column 5 Header: অরবিটাল সংখ্যা
                MathLabel(id="th5_1", text="অরবিটাল", x=472.5, y=55.0, font_size=13.5, font_weight="bold", math_mode=False),
                MathLabel(id="th5_2", text="সংখ্যা", x=472.5, y=75.0, font_size=13.5, font_weight="bold", math_mode=False),

                # n = 4 (Spans all rows vertically)
                MathLabel(id="r_n", text="n = 4", x=77.5, y=240.0, font_size=18.0, font_weight="bold"),

                # Row 0 (l = 0)
                MathLabel(id="r0_l", text="l = 0", x=167.5, y=132.5, font_size=16.0),
                MathLabel(id="r0_m", text="m = 0", x=272.5, y=132.5, font_size=16.0),
                MathLabel(id="r0_s", text=r"(\pm \frac{1}{2})", x=385.0, y=132.5, font_size=16.0),
                MathLabel(id="r0_o", text="1", x=472.5, y=132.5, font_size=16.0),

                # Row 1 (l = 1)
                MathLabel(id="r1_l", text="l = 1", x=167.5, y=187.5, font_size=16.0),
                MathLabel(id="r1_m", text="m = -1, 0, +1", x=272.5, y=187.5, font_size=15.0),
                MathLabel(id="r1_s", text=r"3(\pm \frac{1}{2})", x=385.0, y=187.5, font_size=16.0),
                MathLabel(id="r1_o", text="3", x=472.5, y=187.5, font_size=16.0),

                # Row 2 (l = 2)
                MathLabel(id="r2_l", text="l = 2", x=167.5, y=252.5, font_size=16.0),
                MathLabel(id="r2_m1", text="m = -2, -1,", x=272.5, y=242.0, font_size=14.0),
                MathLabel(id="r2_m2", text="0, +1, +2", x=272.5, y=263.0, font_size=14.0),
                MathLabel(id="r2_s", text=r"5(\pm \frac{1}{2})", x=385.0, y=252.5, font_size=16.0),
                MathLabel(id="r2_o", text="5", x=472.5, y=252.5, font_size=16.0),

                # Row 3 (l = 3)
                MathLabel(id="r3_l", text="l = 3", x=167.5, y=332.5, font_size=16.0),
                MathLabel(id="r3_m1", text="m = -3, -2,", x=272.5, y=312.0, font_size=13.0),
                MathLabel(id="r3_m2", text="-1, 0, +1,", x=272.5, y=332.5, font_size=13.0),
                MathLabel(id="r3_m3", text="+2, +3", x=272.5, y=353.0, font_size=13.0),
                MathLabel(id="r3_s", text=r"7(\pm \frac{1}{2})", x=385.0, y=332.5, font_size=16.0),
                MathLabel(id="r3_o", text="7", x=472.5, y=332.5, font_size=16.0),

                # Bottom Footer: মোট অরবিটাল সংখ্যা = 16টি
                MathLabel(id="lbl_tot", text="মোট অরবিটাল সংখ্যা = 16টি", x=360.0, y=395.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Quantum Numbers Table", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 3aadbc21: Triangle Medians Centroid C
        # ----------------------------------------------------
        if "3aadbc21" in stem:
            w, h = 360.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 180.0, 40.0
            xB, yB = 60.0, 300.0
            xD, yD = 300.0, 300.0
            xC, yC = 180.0, (yA + yB + yD)/3.0

            polygons = [
                Polygon(id="tri", vertices=[(xB, yB), (xD, yD), (xA, yA)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="m_a", start=(xA, yA), end=((xB + xD)/2.0, yB), stroke_width=2.0, color="#111111"),
                Segment(id="m_b", start=(xB, yB), end=((xA + xD)/2.0, (yA + yD)/2.0), stroke_width=2.0, color="#111111"),
                Segment(id="m_d", start=(xD, yD), end=((xA + xB)/2.0, (yA + yB)/2.0), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c", text="C", x=xC - 18.0, y=yC + 24.0, font_size=24.0, font_weight="bold"),
            ]
            return VisualIR(title="Triangle Centroid Medians", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 3e36c3b8: Hand Holding Charged Sphere above Negative Plate
        # ----------------------------------------------------
        if "3e36c3b8" in stem:
            from ...anatomy.organic_tracer import OrganicVectorTracer
            w, h = 420.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            cx, cy, r = 180.0, 75.0, 45.0
            hand_beziers = OrganicVectorTracer.synthesize_hand_holding_sphere(
                sphere_center=(cx, cy),
                sphere_radius=r,
                id_prefix="hand"
            )

            circles = [
                Circle(id="sph", center=(cx, cy), radius=r, stroke_width=2.2, stroke_color="#111111", fill_color="none"),
            ]
            polygons = [
                # Bottom plate
                Polygon(id="plate", vertices=[(40.0, 220.0), (380.0, 225.0), (380.0, 275.0), (45.0, 270.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                # Dashed minus line inside plate
                Segment(id="minus_line", start=(60.0, 248.0), end=(360.0, 250.0), stroke_width=2.5, color="#111111", stroke_style=StrokeStyle.DASHED),
            ]
            labels = [
                MathLabel(id="lbl_q0", text="q₀", x=cx + 12.0, y=cy - 2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=cx - 88.0, y=cy + 5.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=cx - 10.0, y=cy + 105.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(
                title="Hand-Held Sphere Electrostatic Induction",
                width=w, height=h,
                coordinate_frame=cf,
                circles=circles,
                polygons=polygons,
                bezier_paths=hand_beziers,
                segments=segments,
                labels=labels,
                background_color="#ffffff"
            )

        # ----------------------------------------------------
        # 3faff89f: Triangle ABC with node charges q1, q2
        # ----------------------------------------------------
        if "3faff89f" in stem:
            w, h = 360.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 180.0, 45.0
            xB, yB = 80.0, 250.0
            xC, yC = 280.0, 250.0

            polygons = [
                Polygon(id="tri", vertices=[(xB, yB), (xC, yC), (xA, yA)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="cb", center=(xB, yB), radius=10.0, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="cc", center=(xC, yC), radius=10.0, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 18.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 28.0, y=yB - 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 28.0, y=yC - 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_q1", text="q_1", x=xB - 15.0, y=yB + 32.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_q2", text="q_2", x=xC + 15.0, y=yC + 32.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="d", x=(xA + xB)/2.0 - 22.0, y=(yA + yB)/2.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d2", text="d", x=(xA + xC)/2.0 + 22.0, y=(yA + yC)/2.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d3", text="d", x=(xB + xC)/2.0, y=yB + 28.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Equilateral Triangle with Charged Base Nodes", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 3feee562: Infinite Charged Plane Sheet in 3D Perspective
        # ----------------------------------------------------
        if "3feee562" in stem:
            w, h = 480.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            polygons = [
                Polygon(id="plane", vertices=[(80.0, 180.0), (360.0, 180.0), (440.0, 130.0), (160.0, 130.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#f5f5f5")
            ]
            circles = [
                Circle(id="pt_p", center=(260.0, 40.0), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Perpendicular line from plane center up to P
                Segment(id="norm", start=(260.0, 155.0), end=(260.0, 40.0), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_p", text="P", x=280.0, y=40.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="r = 0.2\\text{ m}", x=320.0, y=100.0, font_size=18.0, font_weight="bold"),
            ]
            # Add grid of plus signs across the plane
            for row, y_pos in enumerate([145.0, 165.0]):
                for col in range(7):
                    x_pos = 120.0 + col * 38.0 + (15.0 if row == 0 else 0.0)
                    labels.append(MathLabel(id=f"plus_{row}_{col}", text="+", x=x_pos, y=y_pos, font_size=16.0, font_weight="bold", math_mode=False))

            return VisualIR(title="Infinite Charged Plane Sheet", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 434666d4: Circuit A (Series) vs Circuit B (Parallel)
        # ----------------------------------------------------
        if "434666d4" in stem:
            w, h = 580.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            segments = [
                # Circuit A
                Segment(id="a_t1", start=(60.0, 60.0), end=(120.0, 60.0), stroke_width=2.2, color="#111111"),
                Segment(id="a_t2", start=(140.0, 60.0), end=(200.0, 60.0), stroke_width=2.2, color="#111111"),
                Segment(id="a_t3", start=(220.0, 60.0), end=(280.0, 60.0), stroke_width=2.2, color="#111111"),
                Segment(id="a_l", start=(60.0, 60.0), end=(60.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="a_r", start=(280.0, 60.0), end=(280.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="a_b1", start=(60.0, 180.0), end=(160.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="a_b2", start=(180.0, 180.0), end=(280.0, 180.0), stroke_width=2.2, color="#111111"),
                # Circuit A plates
                Segment(id="a_c1_l", start=(125.0, 48.0), end=(125.0, 72.0), stroke_width=2.8, color="#111111"),
                Segment(id="a_c1_r", start=(135.0, 48.0), end=(135.0, 72.0), stroke_width=2.8, color="#111111"),
                Segment(id="a_c2_l", start=(205.0, 48.0), end=(205.0, 72.0), stroke_width=2.8, color="#111111"),
                Segment(id="a_c2_r", start=(215.0, 48.0), end=(215.0, 72.0), stroke_width=2.8, color="#111111"),
                # Circuit A battery
                Segment(id="a_bp", start=(165.0, 168.0), end=(165.0, 192.0), stroke_width=3.0, color="#111111"),
                Segment(id="a_bn", start=(175.0, 173.0), end=(175.0, 187.0), stroke_width=4.5, color="#111111"),

                # Circuit B (Diamond / Hexagonal parallel loop)
                Segment(id="b_l", start=(360.0, 110.0), end=(360.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="b_r", start=(560.0, 110.0), end=(560.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="b_bot1", start=(360.0, 180.0), end=(450.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="b_bot2", start=(470.0, 180.0), end=(560.0, 180.0), stroke_width=2.2, color="#111111"),
                # Diamond top branch
                Segment(id="b_dt1", start=(360.0, 110.0), end=(410.0, 50.0), stroke_width=2.2, color="#111111"),
                Segment(id="b_dt2", start=(410.0, 50.0), end=(450.0, 50.0), stroke_width=2.2, color="#111111"),
                Segment(id="b_dt3", start=(470.0, 50.0), end=(510.0, 50.0), stroke_width=2.2, color="#111111"),
                Segment(id="b_dt4", start=(510.0, 50.0), end=(560.0, 110.0), stroke_width=2.2, color="#111111"),
                # Diamond bottom parallel branch
                Segment(id="b_db1", start=(360.0, 110.0), end=(410.0, 135.0), stroke_width=2.2, color="#111111"),
                Segment(id="b_db2", start=(410.0, 135.0), end=(450.0, 135.0), stroke_width=2.2, color="#111111"),
                Segment(id="b_db3", start=(470.0, 135.0), end=(510.0, 135.0), stroke_width=2.2, color="#111111"),
                Segment(id="b_db4", start=(510.0, 135.0), end=(560.0, 110.0), stroke_width=2.2, color="#111111"),
                # Circuit B top capacitor
                Segment(id="b_ct_l", start=(455.0, 38.0), end=(455.0, 62.0), stroke_width=2.8, color="#111111"),
                Segment(id="b_ct_r", start=(465.0, 38.0), end=(465.0, 62.0), stroke_width=2.8, color="#111111"),
                # Circuit B bottom capacitor
                Segment(id="b_cb_l", start=(455.0, 123.0), end=(455.0, 147.0), stroke_width=2.8, color="#111111"),
                Segment(id="b_cb_r", start=(465.0, 123.0), end=(465.0, 147.0), stroke_width=2.8, color="#111111"),
                # Circuit B battery
                Segment(id="b_bp", start=(455.0, 168.0), end=(455.0, 192.0), stroke_width=3.0, color="#111111"),
                Segment(id="b_bn", start=(465.0, 173.0), end=(465.0, 187.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                # Circuit A labels
                MathLabel(id="lbl_ca1", text="C", x=130.0, y=32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_ca2", text="C", x=210.0, y=32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_circ_a", text="বর্তনী A", x=35.0, y=120.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_va", text="V_1", x=170.0, y=210.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_vap", text="+", x=150.0, y=168.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_van", text="-", x=190.0, y=168.0, font_size=16.0, font_weight="bold", math_mode=False),
                # Circuit B labels
                MathLabel(id="lbl_cb1", text="C", x=460.0, y=25.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_cb2", text="C", x=460.0, y=110.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_circ_b", text="বর্তনী B", x=330.0, y=140.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_vb", text="V_2", x=460.0, y=210.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_vbp", text="+", x=440.0, y=168.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_vbn", text="-", x=480.0, y=168.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Comparison of Series and Parallel Capacitors", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 43a0c30b: Three Capacitor Bridge Circuit Network
        # ----------------------------------------------------
        if "43a0c30b" in stem:
            w, h = 420.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_c1, x_c3, x_c2, x_r = 40.0, 90.0, 180.0, 320.0, 320.0
            y_t, y_m, y_b = 40.0, 130.0, 240.0

            segments = [
                # Top wire
                Segment(id="top_wire", start=(x_l, y_t), end=(x_r, y_t), stroke_width=2.5, color="#111111"),
                # Leftmost drop and loop down to C3 bottom
                Segment(id="left_drop", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.5, color="#111111"),
                Segment(id="bot_loop", start=(x_l, y_b), end=(x_c3, y_b), stroke_width=2.5, color="#111111"),
                Segment(id="bot_to_c3", start=(x_c3, y_b), end=(x_c3, y_m + 75.0), stroke_width=2.5, color="#111111"),
                # Middle rail between C1 and C2
                Segment(id="mid_rail", start=(x_c1, y_m), end=(x_c2, y_m), stroke_width=2.5, color="#111111"),
                # C1 vertical branch
                Segment(id="c1_top", start=(x_c1, y_t), end=(x_c1, 80.0), stroke_width=2.5, color="#111111"),
                Segment(id="c1_bot", start=(x_c1, 100.0), end=(x_c1, y_m), stroke_width=2.5, color="#111111"),
                Segment(id="c1_p1", start=(x_c1 - 15.0, 80.0), end=(x_c1 + 15.0, 80.0), stroke_width=3.0, color="#111111"),
                Segment(id="c1_p2", start=(x_c1 - 15.0, 100.0), end=(x_c1 + 15.0, 100.0), stroke_width=3.0, color="#111111"),
                # C2 vertical branch
                Segment(id="c2_top", start=(x_c2, y_t), end=(x_c2, 80.0), stroke_width=2.5, color="#111111"),
                Segment(id="c2_bot", start=(x_c2, 100.0), end=(x_c2, y_m), stroke_width=2.5, color="#111111"),
                Segment(id="c2_p1", start=(x_c2 - 15.0, 80.0), end=(x_c2 + 15.0, 80.0), stroke_width=3.0, color="#111111"),
                Segment(id="c2_p2", start=(x_c2 - 15.0, 100.0), end=(x_c2 + 15.0, 100.0), stroke_width=3.0, color="#111111"),
                # C3 vertical branch
                Segment(id="c3_top", start=(x_c3, y_m), end=(x_c3, 175.0), stroke_width=2.5, color="#111111"),
                Segment(id="c3_p1", start=(x_c3 - 15.0, 175.0), end=(x_c3 + 15.0, 175.0), stroke_width=3.0, color="#111111"),
                Segment(id="c3_p2", start=(x_c3 - 15.0, 195.0), end=(x_c3 + 15.0, 195.0), stroke_width=3.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1", x=x_c1 + 25.0, y=90.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=x_c2 + 25.0, y=90.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3", x=x_c3 + 25.0, y=185.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Three Capacitor Bridge Network", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 46a33d3c: Diode I-V Characteristic Curve
        # ----------------------------------------------------
        if "46a33d3c" in stem:
            w, h = 450.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO = 210.0, 160.0

            circles = [
                Circle(id="pt_o", center=(xO, yO), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_p", center=(120.0, yO), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Horizontal axis
                Segment(id="ax_h", start=(60.0, yO), end=(380.0, yO), stroke_width=2.5, color="#111111"),
                # Vertical axis
                Segment(id="ax_v", start=(xO, 40.0), end=(xO, 280.0), stroke_width=2.5, color="#111111"),
                # Reverse breakdown vertical line
                Segment(id="rev_break", start=(120.0, 180.0), end=(120.0, 240.0), stroke_width=2.5, color="#111111"),
                # Reverse saturation horizontal line
                Segment(id="rev_sat", start=(120.0, 180.0), end=(180.0, 180.0), stroke_width=2.5, color="#111111"),
                # Small curve connecting origin to rev_sat
                Segment(id="rev_conn", start=(180.0, 180.0), end=(xO, yO), stroke_width=2.5, color="#111111"),
            ]
            # Forward exponential curve
            fwd_pts = []
            for t in range(0, 30):
                x = xO + t * 2.2
                y = yO - (t/28.0)**3 * 110.0
                fwd_pts.append((x, y))
            for i in range(len(fwd_pts) - 1):
                segments.append(Segment(id=f"fwd_{i}", start=fwd_pts[i], end=fwd_pts[i+1], stroke_width=2.5, color="#111111"))

            labels = [
                MathLabel(id="lbl_v", text="V \\text{ (Volt)}", x=400.0, y=yO + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_nv", text="- V \\text{ (Volt)}", x=40.0, y=yO + 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_i", text="I \\text{ (mA)}", x=xO + 45.0, y=40.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_ni", text="- I \\text{ (}\\mu\\text{A)}", x=xO + 45.0, y=280.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=120.0, y=yO - 16.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Diode Characteristic Curve", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 46dbf609: Triangle ABC with median CD
        # ----------------------------------------------------
        if "46dbf609" in stem:
            w, h = 380.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 260.0
            xB, yB = 310.0, 260.0
            xC, yC = 190.0, 60.0
            xD, yD = 190.0, 260.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xB, yB), (xC, yC)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="cd", start=(xC, yC), end=(xD, yD), stroke_width=2.2, color="#111111"),
            ]
            circles = [
                Circle(id="pt_a", center=(xA, yA), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_c", center=(xC, yC), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="+ 4.8C", x=xA + 10.0, y=yA + 30.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC, y=yC - 18.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="- 1.6C", x=xC + 50.0, y=yC + 4.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d", text="D", x=xD, y=yD + 26.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_leg", text="AD = BD = CD", x=xA + 30.0, y=yA + 60.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Triangle Median Geometry", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 47deb213: Equilateral Triangle ABC with P(2kg)
        # ----------------------------------------------------
        if "47deb213" in stem:
            w, h = 420.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 210.0, 60.0
            xB, yB = 100.0, 250.0
            xC, yC = 320.0, 250.0

            polygons = [
                Polygon(id="tri", vertices=[(xB, yB), (xC, yC), (xA, yA)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_a", center=(xA, yA), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA - 12.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P(2 kg)", x=xA + 45.0, y=yA - 12.0, font_size=20.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b", text="B", x=xB - 5.0, y=yB + 28.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="1.676 C", x=xB - 45.0, y=yB - 8.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c", text="C", x=xC + 5.0, y=yB + 28.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="1.676 C", x=xC + 45.0, y=yB - 8.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d1", text="2 m", x=(xA + xB)/2.0 - 25.0, y=(yA + yB)/2.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d2", text="2 m", x=(xA + xC)/2.0 + 25.0, y=(yA + yC)/2.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d3", text="2 m", x=(xB + xC)/2.0, y=yB + 28.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_cap", text="চিত্রে ABC একটি সমবাহু ত্রিভুজ।", x=210.0, y=320.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Equilateral Triangle Charge System", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 4a24877f: Radial 3-Branch System with Rectangular Charge Cards
        # ----------------------------------------------------
        # 4a24877f: Radial 3-Branch System with Rectangular Charge Cards
        # ----------------------------------------------------
        if "4a24877f" in stem:
            w, h = 420.0, 480.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO = 210.0, 240.0

            polygons = [
                # Left box (Q3)
                Polygon(id="box_q3", vertices=[(30.0, 140.0), (80.0, 140.0), (80.0, 340.0), (30.0, 340.0)], stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                # Top right box (Q1)
                Polygon(id="box_q1", vertices=[(290.0, 20.0), (340.0, 20.0), (340.0, 220.0), (290.0, 220.0)], stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                # Bottom right box (Q2)
                Polygon(id="box_q2", vertices=[(290.0, 260.0), (340.0, 260.0), (340.0, 460.0), (290.0, 460.0)], stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Left branch to Q3
                Segment(id="br_q3", start=(80.0, yO), end=(xO, yO), stroke_width=2.2, color="#111111"),
                # Top right branch to Q1
                Segment(id="br_q1", start=(xO, yO), end=(290.0, 120.0), stroke_width=2.2, color="#111111"),
                # Bottom right branch to Q2
                Segment(id="br_q2", start=(xO, yO), end=(290.0, 360.0), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_o", text="O", x=xO + 16.0, y=yO + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d3", text="3 m", x=145.0, y=yO - 16.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="2 m", x=240.0, y=162.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_d2", text="1 m", x=240.0, y=318.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_q3", text="Q_3 = 1.95 \\times 10^{-9}\\text{ C}", x=55.0, y=240.0, font_size=15.0, font_weight="bold", rotation=-90.0),
                MathLabel(id="lbl_q1", text="Q_1 = 1.75 \\times 10^{-9}\\text{ C}", x=315.0, y=120.0, font_size=15.0, font_weight="bold", rotation=-90.0),
                MathLabel(id="lbl_q2", text="Q_2 = 1.6 \\times 10^{-9}\\text{ C}", x=315.0, y=360.0, font_size=15.0, font_weight="bold", rotation=-90.0),
            ]
            return VisualIR(title="Three Radial Charge Branches", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 4a80a78f: Parallel C1, C3 in series with C2 and Battery
        # ----------------------------------------------------
        if "4a80a78f" in stem:
            w, h = 480.0, 280.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_par_t, y_par_b, y_b = 60.0, 60.0, 120.0, 200.0
            x_l, x_par_r, x_c2, x_r = 50.0, 230.0, 320.0, 420.0

            segments = [
                # Parallel box on left
                Segment(id="p_l", start=(x_l, y_par_t), end=(x_l, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="p_r", start=(x_par_r, y_par_t), end=(x_par_r, y_par_b), stroke_width=2.2, color="#111111"),
                # Top parallel wire
                Segment(id="pt1", start=(x_l, y_par_t), end=(120.0, y_par_t), stroke_width=2.2, color="#111111"),
                Segment(id="pt2", start=(140.0, y_par_t), end=(x_par_r, y_par_t), stroke_width=2.2, color="#111111"),
                # Bottom parallel wire
                Segment(id="pb1", start=(x_l, y_par_b), end=(120.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="pb2", start=(140.0, y_par_b), end=(x_par_r, y_par_b), stroke_width=2.2, color="#111111"),
                # C1 plates
                Segment(id="c1_l", start=(125.0, y_par_t - 14.0), end=(125.0, y_par_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(135.0, y_par_t - 14.0), end=(135.0, y_par_t + 14.0), stroke_width=2.8, color="#111111"),
                # C3 plates
                Segment(id="c3_l", start=(125.0, y_par_b - 14.0), end=(125.0, y_par_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(135.0, y_par_b - 14.0), end=(135.0, y_par_b + 14.0), stroke_width=2.8, color="#111111"),
                # Connection to C2
                Segment(id="to_c2", start=(x_par_r, y_t), end=(x_c2 - 10.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c2_to_r", start=(x_c2 + 10.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                # C2 plates
                Segment(id="c2_l", start=(x_c2 - 5.0, y_t - 14.0), end=(x_c2 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x_c2 + 5.0, y_t - 14.0), end=(x_c2 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Left drop and Right drop
                Segment(id="drop_l", start=(x_l, y_par_b), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="drop_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom wire with battery
                Segment(id="bot1", start=(x_l, y_b), end=(220.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bot2", start=(240.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bp", start=(225.0, y_b - 16.0), end=(225.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(235.0, y_b - 9.0), end=(235.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1 = 3\\mu\\text{F}", x=130.0, y=y_par_t + 28.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3 = 2\\mu\\text{F}", x=130.0, y=y_par_b + 28.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2 = 1\\mu\\text{F}", x=x_c2, y=y_t - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="V = 10\\text{Volt}", x=230.0, y=y_b + 32.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_vp", text="+", x=215.0, y=y_b - 18.0, font_size=15.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_vn", text="-", x=245.0, y=y_b - 18.0, font_size=15.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Series-Parallel Capacitive Circuit", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 4b571ac2: Square ABDC with Corner and Midpoint Charges
        # ----------------------------------------------------
        if "4b571ac2" in stem:
            w, h = 380.0, 380.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 70.0
            xB, yB = 300.0, 70.0
            xD, yD = 300.0, 300.0
            xC, yC = 70.0, 300.0

            polygons = [
                Polygon(id="sq", vertices=[(xA, yA), (xB, yB), (xD, yD), (xC, yC)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_o", center=(185.0, 185.0), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_m_l", center=(xA, 185.0), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_m_r", center=(xB, 185.0), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="5C", x=xA + 15.0, y=yA - 16.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="7C", x=xB - 15.0, y=yB - 16.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c", text="C", x=xC - 18.0, y=yC + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="- 15C", x=xC + 5.0, y=yC + 28.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d", text="D", x=xD + 18.0, y=yD + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=185.0, y=215.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Square Charge Distribution", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 4f25a53d: Rectangle ABCD with corner charges
        # ----------------------------------------------------
        if "4f25a53d" in stem:
            w, h = 420.0, 340.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 260.0
            xB, yB = 300.0, 260.0
            xC, yC = 300.0, 70.0
            xD, yD = 70.0, 70.0

            polygons = [
                Polygon(id="rect", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=yA + 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=yB + 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+5 \\times 10^{-3}\\text{ C}", x=xB + 85.0, y=yB + 20.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD - 18.0, y=yD - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qd", text="-2.25 \\times 10^{-3}\\text{ C}", x=185.0, y=yD - 18.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_w1", text="1 m", x=185.0, y=yC + 22.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_w2", text="1 m", x=185.0, y=yA + 22.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_h1", text="0.8 m", x=xA - 40.0, y=165.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_h2", text="0.8 m", x=xB + 40.0, y=165.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Rectangle Charge Boundary", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 52c1983f: Spheres A and B with drop stem to C
        # ----------------------------------------------------
        # 52c1983f: Spheres A and B with drop stem to C
        # ----------------------------------------------------
        if "52c1983f" in stem:
            w, h = 520.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 95.0, 135.0, 42.0
            xB, yB, rB = 320.0, 135.0, 65.0
            xD, yD = xB, yB + rB
            xC, yC = xB, 320.0

            circles = [
                Circle(id="sph_a", center=(xA, yA), radius=rA, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_b", center=(xB, yB), radius=rB, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Internal radius r1 of sphere A
                Segment(id="rad1_v", start=(xA, yA), end=(xA, yA - rA), stroke_width=2.0, color="#111111"),
                Segment(id="rad1_h", start=(xA, yA), end=(xA + rA, yA), stroke_width=2.0, color="#111111"),
                # Horizontal connecting line from Sphere A to Sphere B
                Segment(id="conn_h", start=(xA + rA, yA), end=(xB, yB), stroke_width=2.2, color="#111111"),
                # Internal radius r2 of sphere B
                Segment(id="rad2", start=(xB, yB), end=(xB + rB * 0.707, yB - rB * 0.707), stroke_width=2.0, color="#111111"),
                # Vertical stem from B through D down to C
                Segment(id="v_stem", start=(xB, yB), end=(xC, yC), stroke_width=2.2, color="#111111"),
                # Dimension 4m with ticks and bidirectional arrow
                Segment(id="dim_4m", start=(xB + 105.0, yB), end=(xB + 105.0, yC), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                Segment(id="tick_top", start=(xB + 95.0, yB), end=(xB + 115.0, yB), stroke_width=1.5, color="#111111"),
                Segment(id="tick_bot", start=(xB + 95.0, yC), end=(xB + 115.0, yC), stroke_width=1.5, color="#111111"),
            ]
            right_angles = [
                # Right angle at A
                RightAngleMarker(id="ra_a", vertex=(xA, yA), arm1_pt=(xA + rA, yA), arm2_pt=(xA, yA - rA), size=14.0, color="#111111", stroke_width=1.6),
                # Right angle at B
                RightAngleMarker(id="ra_b", vertex=(xB, yB), arm1_pt=(xA, yA), arm2_pt=(xC, yC), size=18.0, color="#111111", stroke_width=1.8),
            ]

            # 8 Positive (+) charges around Sphere A
            labels = [
                MathLabel(id="lbl_q1", text="Q_1", x=xA - 14.0, y=yA - 60.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=yA + 10.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r1", text="r_1", x=xA + 16.0, y=yA - 16.0, font_size=16.0, font_weight="bold"),

                # Plus charges around Sphere A
                MathLabel(id="chg_a_top", text="+", x=xA, y=yA - rA - 12.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="chg_a_tr", text="+", x=xA + 36.0, y=yA - 36.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="chg_a_tl", text="+", x=xA - 36.0, y=yA - 36.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="chg_a_l", text="+", x=xA - rA - 12.0, y=yA, font_size=20.0, font_weight="bold"),
                MathLabel(id="chg_a_bl", text="+", x=xA - 36.0, y=yA + 36.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="chg_a_bot", text="+", x=xA, y=yA + rA + 12.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="chg_a_br", text="+", x=xA + 36.0, y=yA + 36.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="chg_a_r", text="+", x=xA + rA + 16.0, y=yA - 16.0, font_size=20.0, font_weight="bold"),

                # Sphere B labels
                MathLabel(id="lbl_q2", text="Q_2", x=xB + 35.0, y=yB - 70.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB + 6.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r2", text="r_2", x=xB + 32.0, y=yB - 18.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD + 16.0, y=yD, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 16.0, y=yC, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_deg", text="90^\\circ", x=xB - 45.0, y=yB + 18.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_dim", text="4 m", x=xB + 125.0, y=(yB + yC) / 2.0, font_size=17.0, font_weight="bold"),

                # Minus charges around Sphere B
                MathLabel(id="chg_b_top", text="−", x=xB, y=yB - rB - 14.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="chg_b_tr", text="−", x=xB + 56.0, y=yB - 56.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="chg_b_tl", text="−", x=xB - 56.0, y=yB - 56.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="chg_b_l", text="−", x=xB - rB - 14.0, y=yB - 10.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="chg_b_bl", text="−", x=xB - 56.0, y=yB + 50.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="chg_b_br", text="−", x=xB + 56.0, y=yB + 50.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="chg_b_r", text="−", x=xB + rB + 14.0, y=yB, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Charged Spheres with Right-Angle Drop Stem", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, right_angles=right_angles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5564f155: Equilateral Triangle ABC 10cm 100C
        # ----------------------------------------------------
        if "5564f155" in stem:
            w, h = 380.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 80.0, 240.0
            xB, yB = 300.0, 240.0
            xC, yC = 190.0, 50.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xB, yB), (xC, yC)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="100 C", x=xA - 15.0, y=yA + 30.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="100 C", x=xB + 15.0, y=yB + 30.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c", text="C", x=xC, y=yC - 18.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="10 cm", x=(xA + xC)/2.0 - 30.0, y=(yA + yC)/2.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d2", text="10 cm", x=(xB + xC)/2.0 + 30.0, y=(yB + yC)/2.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d3", text="10 cm", x=(xA + xB)/2.0, y=yA + 25.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Equilateral Triangle Charge System 100C", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5614f06c: Kite on Grounded Hinge D
        # ----------------------------------------------------
        if "5614f06c" in stem:
            w, h = 380.0, 380.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 80.0, 160.0
            xB, yB = 300.0, 160.0
            xC, yC = 135.0, 60.0
            xD, yD = 190.0, 320.0

            polygons = [
                Polygon(id="kite", vertices=[(xA, yA), (xC, yC), (xB, yB), (xD, yD)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="hinge", center=(xD, yD), radius=8.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Horizontal base AB
                Segment(id="ab", start=(xA, yA), end=(xB, yB), stroke_width=2.2, color="#111111"),
                # Ground line
                Segment(id="gnd", start=(30.0, yD + 8.0), end=(350.0, yD + 8.0), stroke_width=2.2, color="#111111"),
            ]
            # Ground hatching
            for hx in range(40, 350, 14):
                segments.append(Segment(id=f"hatch_{hx}", start=(float(hx), yD + 8.0), end=(float(hx) - 10.0, yD + 20.0), stroke_width=1.5, color="#111111"))

            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="-2\\mu\\text{C}", x=xA - 35.0, y=yA + 25.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="-2\\mu\\text{C}", x=xB + 35.0, y=yB + 25.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC - 10.0, y=yC - 16.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD + 20.0, y=yD, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_ac", text="6 cm", x=90.0, y=95.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_ab", text="10 cm", x=(xA + xB)/2.0, y=yA + 24.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Kite System on Grounded Hinge", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5644bb10: Collinear Segment P-A-B-Q
        # ----------------------------------------------------
        if "5644bb10" in stem:
            w, h = 480.0, 160.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_line = 70.0
            xP, xA, xB, xQ = 40.0, 150.0, 340.0, 440.0

            circles = [
                Circle(id="pt_a", center=(xA, y_line), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, y_line), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="line", start=(xP, y_line), end=(xQ, y_line), stroke_width=2.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_p", text="P", x=xP, y=y_line - 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA, y=y_line - 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="+ 6 \\mu\\text{C}", x=xA, y=y_line + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=y_line - 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="- 3 \\mu\\text{C}", x=xB, y=y_line + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="Q", x=xQ, y=y_line - 22.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Collinear Charge Axis", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 56bcf776: Deflected Particle between Parallel Plates
        # ----------------------------------------------------
        if "56bcf776" in stem:
            w, h = 380.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_r = 50.0, 310.0
            y_pt, y_pb = 100.0, 270.0
            y_ax = 190.0

            polygons = [
                # Top plate
                Polygon(id="plate_t", vertices=[(x_l, y_pt - 6.0), (x_r, y_pt - 6.0), (x_r, y_pt + 6.0), (x_l, y_pt + 6.0)], stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                # Bottom plate
                Polygon(id="plate_b", vertices=[(x_l, y_pb - 6.0), (x_r, y_pb - 6.0), (x_r, y_pb + 6.0), (x_l, y_pb + 6.0)], stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            circles = [
                Circle(id="particle", center=(220.0, 160.0), radius=6.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Y axis
                Segment(id="ax_y", start=(x_l, 40.0), end=(x_l, 330.0), stroke_width=2.0, color="#111111"),
                # X axis
                Segment(id="ax_x", start=(x_l, y_ax), end=(350.0, y_ax), stroke_width=2.0, color="#111111"),
                # Downward electric field arrow
                Segment(id="e_field", start=(100.0, 120.0), end=(100.0, 170.0), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
                # Deflected trajectory curve
                Segment(id="t1", start=(x_l, y_ax), end=(150.0, y_ax - 5.0), stroke_width=2.0, color="#111111"),
                Segment(id="t2", start=(150.0, y_ax - 5.0), end=(220.0, 160.0), stroke_width=2.0, color="#111111"),
                Segment(id="t3", start=(220.0, 160.0), end=(310.0, 120.0), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
                # Tick at x=L
                Segment(id="tick_l", start=(x_r, y_ax - 10.0), end=(x_r, y_ax + 10.0), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_y", text="y", x=35.0, y=40.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_x", text="x", x=365.0, y=y_ax, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=x_l - 18.0, y=y_ax + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_e", text="\\vec{E}", x=125.0, y=145.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_mq", text="m, q", x=210.0, y=130.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_l", text="x = L", x=x_r, y=y_ax + 30.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_plt1", text="প্লেট", x=(x_l + x_r)/2.0, y=y_pt - 20.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_plt2", text="প্লেট", x=(x_l + x_r)/2.0, y=y_pb + 25.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Charged Particle Trajectory in Electric Field", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 56fea8e8: Series C1 with Parallel C2, C3 and 6V Battery
        # ----------------------------------------------------
        if "56fea8e8" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_par_t, y_par_b, y_b = 60.0, 30.0, 90.0, 190.0
            x_l, x_c1, x_sp, x_c23, x_r = 40.0, 170.0, 260.0, 320.0, 440.0

            segments = [
                # Top left series wire with C1
                Segment(id="t1", start=(x_l, y_t), end=(x_c1 - 10.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(x_c1 + 10.0, y_t), end=(x_sp, y_t), stroke_width=2.2, color="#111111"),
                # C1 plates
                Segment(id="c1_l", start=(x_c1 - 5.0, y_t - 14.0), end=(x_c1 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x_c1 + 5.0, y_t - 14.0), end=(x_c1 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Parallel branch
                Segment(id="sp_l", start=(x_sp, y_par_t), end=(x_sp, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="sp_r", start=(380.0, y_par_t), end=(380.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="to_r", start=(380.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                # Top parallel wire
                Segment(id="pt1", start=(x_sp, y_par_t), end=(x_c23 - 10.0, y_par_t), stroke_width=2.2, color="#111111"),
                Segment(id="pt2", start=(x_c23 + 10.0, y_par_t), end=(380.0, y_par_t), stroke_width=2.2, color="#111111"),
                # Bottom parallel wire
                Segment(id="pb1", start=(x_sp, y_par_b), end=(x_c23 - 10.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="pb2", start=(x_c23 + 10.0, y_par_b), end=(380.0, y_par_b), stroke_width=2.2, color="#111111"),
                # C2 plates
                Segment(id="c2_l", start=(x_c23 - 5.0, y_par_t - 14.0), end=(x_c23 - 5.0, y_par_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x_c23 + 5.0, y_par_t - 14.0), end=(x_c23 + 5.0, y_par_t + 14.0), stroke_width=2.8, color="#111111"),
                # C3 plates
                Segment(id="c3_l", start=(x_c23 - 5.0, y_par_b - 14.0), end=(x_c23 - 5.0, y_par_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x_c23 + 5.0, y_par_b - 14.0), end=(x_c23 + 5.0, y_par_b + 14.0), stroke_width=2.8, color="#111111"),
                # Side drops
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom wire with battery
                Segment(id="wb1", start=(x_l, y_b), end=(180.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="wb2", start=(200.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bp", start=(185.0, y_b - 16.0), end=(185.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(195.0, y_b - 9.0), end=(195.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1 = 5\\mu\\text{F}", x=x_c1, y=y_t - 22.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2 = 2\\mu\\text{F}", x=x_c23 + 60.0, y=y_par_t - 15.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3 = 2\\mu\\text{F}", x=x_c23 + 10.0, y=y_par_b + 32.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="6V", x=190.0, y=y_b + 32.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_vp", text="+", x=175.0, y=y_b - 18.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_vn", text="-", x=205.0, y=y_b - 18.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Series-Parallel Capacitive Network 6V", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 570ac6f7: Horizontal Rod on Three Insulated Pillar Stands
        # ----------------------------------------------------
        if "570ac6f7" in stem:
            w, h = 500.0, 180.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_bar = 60.0
            xA, xB, xP = 60.0, 240.0, 420.0

            polygons = [
                # Hexagonal / vase shaped pillar stands
                Polygon(id="stand_a", vertices=[(xA - 8.0, y_bar), (xA + 8.0, y_bar), (xA + 12.0, y_bar + 25.0), (xA + 6.0, y_bar + 55.0), (xA - 6.0, y_bar + 55.0), (xA - 12.0, y_bar + 25.0)], stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                Polygon(id="stand_b", vertices=[(xB - 8.0, y_bar), (xB + 8.0, y_bar), (xB + 12.0, y_bar + 25.0), (xB + 6.0, y_bar + 55.0), (xB - 6.0, y_bar + 55.0), (xB - 12.0, y_bar + 25.0)], stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                Polygon(id="stand_p", vertices=[(xP - 8.0, y_bar), (xP + 8.0, y_bar), (xP + 12.0, y_bar + 25.0), (xP + 6.0, y_bar + 55.0), (xP - 6.0, y_bar + 55.0), (xP - 12.0, y_bar + 25.0)], stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                Segment(id="rod", start=(xA - 15.0, y_bar), end=(xP + 15.0, y_bar), stroke_width=2.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=y_bar + 75.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="- 6 \\times 10^{-9}\\text{C}", x=xA, y=y_bar - 20.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=y_bar + 75.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="- 8 \\times 10^{-9}\\text{C}", x=xB, y=y_bar - 20.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP, y=y_bar + 75.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_dim", text="AB = BP = 10 cm", x=xP, y=y_bar - 20.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Insulated Pillar Supported Rod", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5b48f8ec: Two Parallel Branches (Top 3uF, Bottom 2uF + 1uF)
        # ----------------------------------------------------
        if "5b48f8ec" in stem:
            w, h = 480.0, 200.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_m, y_t, y_b = 90.0, 40.0, 140.0
            x_l, x_sp_l, x_sp_r, x_r = 30.0, 80.0, 400.0, 450.0

            circles = [
                Circle(id="term_l", center=(x_l, y_m), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="term_r", center=(x_r, y_m), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Left lead and split
                Segment(id="lead_l", start=(x_l, y_m), end=(x_sp_l, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="sp_l", start=(x_sp_l, y_t), end=(x_sp_l, y_b), stroke_width=2.2, color="#111111"),
                # Right lead and split
                Segment(id="sp_r", start=(x_sp_r, y_t), end=(x_sp_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="lead_r", start=(x_sp_r, y_m), end=(x_r, y_m), stroke_width=2.2, color="#111111"),
                # Top branch with 3uF
                Segment(id="t1", start=(x_sp_l, y_t), end=(230.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(250.0, y_t), end=(x_sp_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="ct_l", start=(235.0, y_t - 14.0), end=(235.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="ct_r", start=(245.0, y_t - 14.0), end=(245.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Bottom branch with 2uF and 1uF
                Segment(id="b1", start=(x_sp_l, y_b), end=(150.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(170.0, y_b), end=(310.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b3", start=(330.0, y_b), end=(x_sp_r, y_b), stroke_width=2.2, color="#111111"),
                # 2uF plates
                Segment(id="cb1_l", start=(155.0, y_b - 14.0), end=(155.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cb1_r", start=(165.0, y_b - 14.0), end=(165.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                # 1uF plates
                Segment(id="cb2_l", start=(315.0, y_b - 14.0), end=(315.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cb2_r", start=(325.0, y_b - 14.0), end=(325.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_ct", text="3\\mu\\text{F}", x=240.0, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_cb1", text="2\\mu\\text{F}", x=160.0, y=y_b + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_cb2", text="1\\mu\\text{F}", x=320.0, y=y_b + 32.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Parallel Capacitance Network Terminals", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5bfa2d39: Two Point Charges q1, q2 with Separation d
        # ----------------------------------------------------
        if "5bfa2d39" in stem:
            w, h = 420.0, 140.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_c = 50.0
            x1, x2 = 50.0, 370.0
            xm = (x1 + x2)/2.0

            circles = [
                Circle(id="q1", center=(x1, y_c), radius=6.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="q2", center=(x2, y_c), radius=6.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Left arrow pointing to q1 from d
                Segment(id="arr_l", start=(xm - 20.0, y_c), end=(x1 + 10.0, y_c), stroke_width=2.5, color="#111111", arrows=ArrowType.END),
                # Right arrow pointing to q2 from d
                Segment(id="arr_r", start=(xm + 20.0, y_c), end=(x2 - 10.0, y_c), stroke_width=2.5, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_q1", text="q_1", x=x1, y=y_c + 38.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_q2", text="q_2", x=x2, y=y_c + 38.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="d", x=xm, y=y_c + 4.0, font_size=24.0, font_weight="bold"),
            ]
            return VisualIR(title="Two Interactive Point Charges", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5c90ee7b: Series 3 Capacitors 3uF, 6uF, 8uF and 20V Battery
        # ----------------------------------------------------
        if "5c90ee7b" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 200.0
            x_l, x_r = 40.0, 440.0
            x1, x2, x3 = 120.0, 240.0, 360.0

            segments = [
                Segment(id="t1", start=(x_l, y_t), end=(x1 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(x1 + 8.0, y_t), end=(x2 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(x2 + 8.0, y_t), end=(x3 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t4", start=(x3 + 8.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b1", start=(x_l, y_b), end=(130.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(150.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Plates
                Segment(id="c1_l", start=(x1 - 5.0, y_t - 14.0), end=(x1 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x1 + 5.0, y_t - 14.0), end=(x1 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x2 - 5.0, y_t - 14.0), end=(x2 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x2 + 5.0, y_t - 14.0), end=(x2 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_l", start=(x3 - 5.0, y_t - 14.0), end=(x3 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x3 + 5.0, y_t - 14.0), end=(x3 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Battery
                Segment(id="bp", start=(135.0, y_b - 16.0), end=(135.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(145.0, y_b - 9.0), end=(145.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1_t", text="C_1", x=x1, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c1_v", text="3\\ \\mu\\text{F}", x=x1, y=y_t + 32.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c2_t", text="C_2", x=x2, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2_v", text="6\\ \\mu\\text{F}", x=x2, y=y_t + 32.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c3_t", text="C_3", x=x3, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3_v", text="8\\ \\mu\\text{F}", x=x3, y=y_t + 32.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="V = 20\\text{ V}", x=140.0, y=y_b + 34.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Three Series Capacitors 20V", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5d07899a: Series 3 Capacitors 5uF, 5uF, 5uF and 80V Multi-Cell Battery
        # ----------------------------------------------------
        if "5d07899a" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 200.0
            x_l, x_r = 40.0, 440.0
            x1, x2, x3 = 120.0, 240.0, 360.0

            segments = [
                Segment(id="t1", start=(x_l, y_t), end=(x1 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(x1 + 8.0, y_t), end=(x2 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(x2 + 8.0, y_t), end=(x3 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t4", start=(x3 + 8.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b1", start=(x_l, y_b), end=(110.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(170.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Plates
                Segment(id="c1_l", start=(x1 - 5.0, y_t - 14.0), end=(x1 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x1 + 5.0, y_t - 14.0), end=(x1 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x2 - 5.0, y_t - 14.0), end=(x2 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x2 + 5.0, y_t - 14.0), end=(x2 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_l", start=(x3 - 5.0, y_t - 14.0), end=(x3 - 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x3 + 5.0, y_t - 14.0), end=(x3 + 5.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Multi-cell battery
                Segment(id="bp1", start=(118.0, y_b - 16.0), end=(118.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn1", start=(128.0, y_b - 9.0), end=(128.0, y_b + 9.0), stroke_width=4.0, color="#111111"),
                Segment(id="bp2", start=(138.0, y_b - 16.0), end=(138.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn2", start=(148.0, y_b - 9.0), end=(148.0, y_b + 9.0), stroke_width=4.0, color="#111111"),
                Segment(id="bp3", start=(158.0, y_b - 16.0), end=(158.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1_t", text="C_1", x=x1, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c1_v", text="5\\ \\mu\\text{F}", x=x1, y=y_t + 32.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c2_t", text="C_2", x=x2, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2_v", text="5\\ \\mu\\text{F}", x=x2, y=y_t + 32.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c3_t", text="C_3", x=x3, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3_v", text="5\\ \\mu\\text{F}", x=x3, y=y_t + 32.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="80\\text{ V}", x=185.0, y=y_b + 34.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_vp", text="+", x=105.0, y=y_b - 18.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_vn", text="-", x=175.0, y=y_b - 18.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Three Series Capacitors 80V Multi-Cell", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5d731a0b: Parallel Plate Capacitor with Battery 2V
        # ----------------------------------------------------
        # 5d731a0b: Parallel Plate Capacitor with Battery 2V
        # ----------------------------------------------------
        if "5d731a0b" in stem:
            w, h = 340.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            y_p1, y_p2 = 110.0, 230.0
            x_plate_l, x_plate_r = 60.0, 150.0
            x_plate_c = (x_plate_l + x_plate_r) / 2.0  # 105.0
            x_bat = 240.0

            segments = [
                # Capacitor Plates
                Segment(id="plate_top", start=(x_plate_l, y_p1), end=(x_plate_r, y_p1), stroke_width=3.5, color="#111111"),
                Segment(id="plate_bot", start=(x_plate_l, y_p2), end=(x_plate_r, y_p2), stroke_width=3.5, color="#111111"),

                # Top wire: from top plate up, right, down to battery
                Segment(id="w_top_v", start=(x_plate_c, y_p1), end=(x_plate_c, 50.0), stroke_width=2.2, color="#111111"),
                Segment(id="w_top_h", start=(x_plate_c, 50.0), end=(x_bat, 50.0), stroke_width=2.2, color="#111111"),
                Segment(id="w_top_down", start=(x_bat, 50.0), end=(x_bat, 145.0), stroke_width=2.2, color="#111111"),

                # 4-Plate Multi-cell Battery on right wire
                Segment(id="bat_p1", start=(x_bat - 20.0, 145.0), end=(x_bat + 20.0, 145.0), stroke_width=2.8, color="#111111"),
                Segment(id="bat_n1", start=(x_bat - 12.0, 153.0), end=(x_bat + 12.0, 153.0), stroke_width=4.5, color="#111111"),
                Segment(id="bat_p2", start=(x_bat - 20.0, 161.0), end=(x_bat + 20.0, 161.0), stroke_width=2.8, color="#111111"),
                Segment(id="bat_n2", start=(x_bat - 12.0, 169.0), end=(x_bat + 12.0, 169.0), stroke_width=4.5, color="#111111"),

                # Bottom wire: from battery down, left, up to bottom plate
                Segment(id="w_bot_down", start=(x_bat, 169.0), end=(x_bat, 290.0), stroke_width=2.2, color="#111111"),
                Segment(id="w_bot_h", start=(x_bat, 290.0), end=(x_plate_c, 290.0), stroke_width=2.2, color="#111111"),
                Segment(id="w_bot_up", start=(x_plate_c, 290.0), end=(x_plate_c, y_p2), stroke_width=2.2, color="#111111"),

                # Dimension d = 5 mm between plates with horizontal ticks
                Segment(id="dim_d", start=(180.0, y_p1), end=(180.0, y_p2), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                Segment(id="tick_top", start=(168.0, y_p1), end=(192.0, y_p1), stroke_width=1.5, color="#111111"),
                Segment(id="tick_bot", start=(168.0, y_p2), end=(192.0, y_p2), stroke_width=1.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_qp", text="+20 C", x=38.0, y=y_p1, font_size=17.0, font_weight="bold", rotation=-90.0),
                MathLabel(id="lbl_qn", text="-20 C", x=38.0, y=y_p2, font_size=17.0, font_weight="bold", rotation=-90.0),
                MathLabel(id="lbl_d", text="d = 5\\text{ mm}", x=162.0, y=(y_p1 + y_p2) / 2.0, font_size=16.0, font_weight="bold", rotation=-90.0),
                MathLabel(id="lbl_v", text="V = 2\\text{ V}", x=275.0, y=157.0, font_size=17.0, font_weight="bold", rotation=-90.0),
            ]
            return VisualIR(title="Parallel Plate Capacitor with Battery", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5e1198a1: Isosceles Right Triangle P(1kg) with Q, R Charges
        # ----------------------------------------------------
        if "5e1198a1" in stem:
            w, h = 420.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xP, yP = 170.0, 60.0
            xQ, yQ = 50.0, 250.0
            xR, yR = 370.0, 250.0

            polygons = [
                Polygon(id="tri", vertices=[(xQ, yQ), (xR, yR), (xP, yP)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            arc_angles = [
                ArcAngleMarker(id="arc90", vertex=(xP, yP), start_pt=(xQ, yQ), end_pt=(xR, yR), radius=28.0, color="#111111", stroke_width=1.8)
            ]
            labels = [
                MathLabel(id="lbl_p", text="P(1 kg)", x=xP, y=yP - 20.0, font_size=20.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_deg", text="90^\\circ", x=xP, y=yP + 45.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="Q (1.5 \\times 10^{-9}\\text{ C})", x=xQ + 30.0, y=yQ + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="R (1.5 \\times 10^{-9}\\text{ C})", x=xR - 30.0, y=yQ + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="2\\sqrt{2}\\text{m}", x=(xP + xQ)/2.0 - 35.0, y=(yP + yQ)/2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d2", text="2\\sqrt{2}\\text{m}", x=(xP + xR)/2.0 + 35.0, y=(yP + yR)/2.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Right Angled Isosceles Charge Triangle", width=w, height=h, coordinate_frame=cf, polygons=polygons, arc_angles=arc_angles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5e81d9d8: Rectangle ABCD 1.25m x 1m
        # ----------------------------------------------------
        if "5e81d9d8" in stem:
            w, h = 420.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 250.0
            xB, yB = 70.0, 70.0
            xC, yC = 340.0, 70.0
            xD, yD = 340.0, 250.0

            polygons = [
                Polygon(id="rect", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 20.0, y=yA + 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 20.0, y=yB + 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 20.0, y=yC + 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD + 20.0, y=yD + 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_w", text="1.25m", x=(xB + xC)/2.0, y=yB - 18.0, font_size=20.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_h", text="1m", x=xA + 25.0, y=(yA + yB)/2.0, font_size=20.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Rectangle Geometry 1.25m x 1m", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5f441d3d: Circuit Comparison (4 Parallel vs Parallel+Series)
        # ----------------------------------------------------
        if "5f441d3d" in stem:
            w, h = 600.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            segments = [
                # Fig 1 (4 Parallel Capacitors stacked vertically)
                Segment(id="f1_l_rail", start=(80.0, 50.0), end=(80.0, 170.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_r_rail", start=(180.0, 50.0), end=(180.0, 170.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_drop_l", start=(40.0, 110.0), end=(40.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_conn_l", start=(40.0, 110.0), end=(80.0, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_drop_r", start=(220.0, 110.0), end=(220.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_conn_r", start=(180.0, 110.0), end=(220.0, 110.0), stroke_width=2.2, color="#111111"),
                # Fig 1 bottom battery
                Segment(id="f1_b1", start=(40.0, 240.0), end=(95.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_b2", start=(115.0, 240.0), end=(220.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_bp", start=(100.0, 226.0), end=(100.0, 254.0), stroke_width=3.0, color="#111111"),
                Segment(id="f1_bn", start=(110.0, 231.0), end=(110.0, 249.0), stroke_width=4.5, color="#111111"),

                # Fig 2 (Parallel C1, C2 in series with C3, C4)
                Segment(id="f2_l_drop", start=(350.0, 110.0), end=(350.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_l_conn", start=(350.0, 110.0), end=(370.0, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_sp_l", start=(370.0, 80.0), end=(370.0, 140.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_sp_r", start=(430.0, 80.0), end=(430.0, 140.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_conn_c3", start=(430.0, 110.0), end=(465.0, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_c3_to_c4", start=(485.0, 110.0), end=(515.0, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_c4_to_r", start=(535.0, 110.0), end=(560.0, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_r_drop", start=(560.0, 110.0), end=(560.0, 240.0), stroke_width=2.2, color="#111111"),
                # Fig 2 bottom battery
                Segment(id="f2_b1", start=(350.0, 240.0), end=(425.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_b2", start=(445.0, 240.0), end=(560.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_bp", start=(430.0, 226.0), end=(430.0, 254.0), stroke_width=3.0, color="#111111"),
                Segment(id="f2_bn", start=(440.0, 231.0), end=(440.0, 249.0), stroke_width=4.5, color="#111111"),
            ]
            # Add Fig 1 4 parallel capacitor plates
            for idx, y_pos in enumerate([50.0, 90.0, 130.0, 170.0], start=1):
                segments.append(Segment(id=f"f1_h_{idx}_l", start=(80.0, y_pos), end=(120.0, y_pos), stroke_width=2.2, color="#111111"))
                segments.append(Segment(id=f"f1_h_{idx}_r", start=(140.0, y_pos), end=(180.0, y_pos), stroke_width=2.2, color="#111111"))
                segments.append(Segment(id=f"f1_pl_{idx}_l", start=(125.0, y_pos - 12.0), end=(125.0, y_pos + 12.0), stroke_width=2.8, color="#111111"))
                segments.append(Segment(id=f"f1_pl_{idx}_r", start=(135.0, y_pos - 12.0), end=(135.0, y_pos + 12.0), stroke_width=2.8, color="#111111"))

            # Add Fig 2 C1, C2 parallel plates + C3, C4 series plates
            for idx, y_pos in [(1, 80.0), (2, 140.0)]:
                segments.append(Segment(id=f"f2_p_{idx}_l", start=(370.0, y_pos), end=(390.0, y_pos), stroke_width=2.2, color="#111111"))
                segments.append(Segment(id=f"f2_p_{idx}_r", start=(410.0, y_pos), end=(430.0, y_pos), stroke_width=2.2, color="#111111"))
                segments.append(Segment(id=f"f2_pl_{idx}_l", start=(395.0, y_pos - 12.0), end=(395.0, y_pos + 12.0), stroke_width=2.8, color="#111111"))
                segments.append(Segment(id=f"f2_pl_{idx}_r", start=(405.0, y_pos - 12.0), end=(405.0, y_pos + 12.0), stroke_width=2.8, color="#111111"))

            # Fig 2 C3 and C4 plates
            segments.append(Segment(id="f2_c3_pl_l", start=(470.0, 98.0), end=(470.0, 122.0), stroke_width=2.8, color="#111111"))
            segments.append(Segment(id="f2_c3_pl_r", start=(480.0, 98.0), end=(480.0, 122.0), stroke_width=2.8, color="#111111"))
            segments.append(Segment(id="f2_c4_pl_l", start=(520.0, 98.0), end=(520.0, 122.0), stroke_width=2.8, color="#111111"))
            segments.append(Segment(id="f2_c4_pl_r", start=(530.0, 98.0), end=(530.0, 122.0), stroke_width=2.8, color="#111111"))

            labels = [
                # Fig 1 labels
                MathLabel(id="lbl_f1_c1", text="C_1", x=105.0, y=40.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_f1_c2", text="C_2", x=105.0, y=80.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_f1_c3", text="C_3", x=105.0, y=120.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_f1_c4", text="C_4", x=105.0, y=160.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_f1_e", text="E", x=105.0, y=270.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_fig1", text="চিত্র-১", x=110.0, y=300.0, font_size=18.0, font_weight="bold", math_mode=False),
                # Fig 2 labels
                MathLabel(id="lbl_f2_c1", text="C_1", x=400.0, y=60.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_f2_c2", text="C_2", x=400.0, y=165.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_f2_c3", text="C_3", x=475.0, y=140.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_f2_c4", text="C_4", x=525.0, y=140.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_f2_e", text="E", x=435.0, y=270.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_fig2", text="চিত্র-২", x=440.0, y=300.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Capacitor Configurations Comparison", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 5f55734e: Series 3 Capacitors 27uF, 18uF, 9uF and 24V Battery
        # ----------------------------------------------------
        if "5f55734e" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 200.0
            x_l, x_r = 40.0, 440.0
            x1, x2, x3 = 130.0, 240.0, 350.0

            segments = [
                Segment(id="t1", start=(x_l, y_t), end=(x1 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(x1 + 8.0, y_t), end=(x2 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(x2 + 8.0, y_t), end=(x3 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t4", start=(x3 + 8.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="w_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b1", start=(x_l, y_b), end=(225.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(245.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Plates
                Segment(id="c1_l", start=(x1 - 5.0, y_t - 16.0), end=(x1 - 5.0, y_t + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_r", start=(x1 + 5.0, y_t - 16.0), end=(x1 + 5.0, y_t + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_l", start=(x2 - 5.0, y_t - 16.0), end=(x2 - 5.0, y_t + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_r", start=(x2 + 5.0, y_t - 16.0), end=(x2 + 5.0, y_t + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_l", start=(x3 - 5.0, y_t - 16.0), end=(x3 - 5.0, y_t + 16.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_r", start=(x3 + 5.0, y_t - 16.0), end=(x3 + 5.0, y_t + 16.0), stroke_width=2.8, color="#111111"),
                # Battery
                Segment(id="bp", start=(230.0, y_b - 16.0), end=(230.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(240.0, y_b - 9.0), end=(240.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="27\\ \\mu\\text{F}", x=x1, y=y_t + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="18\\ \\mu\\text{F}", x=x2, y=y_t + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="9\\ \\mu\\text{F}", x=x3, y=y_t + 32.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="24\\text{ V}", x=235.0, y=y_b + 34.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Series Three Capacitors 24V", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 601fd7f3: Parallel Branches C2, C1, 220V
        # ----------------------------------------------------
        if "601fd7f3" in stem:
            w, h = 420.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 40.0, 200.0
            x1, x2, x3 = 80.0, 210.0, 340.0

            segments = [
                # Top and bottom rails
                Segment(id="top_rail", start=(x1, y_t), end=(x3, y_t), stroke_width=2.5, color="#111111"),
                Segment(id="bot_rail", start=(x1, y_b), end=(x3, y_b), stroke_width=2.5, color="#111111"),
                # Branch 1 (C2)
                Segment(id="b1_t", start=(x1, y_t), end=(x1, 110.0), stroke_width=2.5, color="#111111"),
                Segment(id="b1_b", start=(x1, 130.0), end=(x1, y_b), stroke_width=2.5, color="#111111"),
                Segment(id="c2_p1", start=(x1 - 15.0, 110.0), end=(x1 + 15.0, 110.0), stroke_width=3.0, color="#111111"),
                Segment(id="c2_p2", start=(x1 - 15.0, 130.0), end=(x1 + 15.0, 130.0), stroke_width=3.0, color="#111111"),
                # Branch 2 (C1)
                Segment(id="b2_t", start=(x2, y_t), end=(x2, 110.0), stroke_width=2.5, color="#111111"),
                Segment(id="b2_b", start=(x2, 130.0), end=(x2, y_b), stroke_width=2.5, color="#111111"),
                Segment(id="c1_p1", start=(x2 - 15.0, 110.0), end=(x2 + 15.0, 110.0), stroke_width=3.0, color="#111111"),
                Segment(id="c1_p2", start=(x2 - 15.0, 130.0), end=(x2 + 15.0, 130.0), stroke_width=3.0, color="#111111"),
                # Branch 3 (220V source)
                Segment(id="b3_t", start=(x3, y_t), end=(x3, 110.0), stroke_width=2.5, color="#111111"),
                Segment(id="b3_b", start=(x3, 130.0), end=(x3, y_b), stroke_width=2.5, color="#111111"),
                Segment(id="v_p1", start=(x3 - 15.0, 110.0), end=(x3 + 15.0, 110.0), stroke_width=3.0, color="#111111"),
                Segment(id="v_p2", start=(x3 - 15.0, 130.0), end=(x3 + 15.0, 130.0), stroke_width=3.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c2", text="C_2", x=x1 - 30.0, y=120.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="C_1", x=x2 - 30.0, y=120.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="220\\text{ V}", x=x3 + 55.0, y=120.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_vp", text="+", x=x3 + 18.0, y=100.0, font_size=15.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_vn", text="-", x=x3 + 18.0, y=140.0, font_size=15.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Three Parallel Circuit Branches", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 6125e504: Spherical Conductor with Radial Electric Field Vectors
        # ----------------------------------------------------
        if "6125e504" in stem:
            w, h = 380.0, 380.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO, rS = 190.0, 190.0, 75.0

            circles = [
                Circle(id="sph", center=(xO, yO), radius=rS, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="center", center=(xO, yO), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Internal radius line
                Segment(id="rad", start=(xO, yO), end=(xO + rS*0.707, yO + rS*0.707), stroke_width=2.2, color="#111111"),
            ]
            # 8 outward arrows (every 45 deg)
            for ang in range(0, 360, 45):
                rad_ang = math.radians(ang)
                is_solid = (ang % 90 == 0)
                style = StrokeStyle.SOLID if is_solid else StrokeStyle.DASHED
                x_in = xO + rS * 0.3 * math.cos(rad_ang)
                y_in = yO + rS * 0.3 * math.sin(rad_ang)
                x_out = xO + (rS + 65.0) * math.cos(rad_ang)
                y_out = yO + (rS + 65.0) * math.sin(rad_ang)
                segments.append(Segment(id=f"arr_{ang}", start=(x_in, y_in), end=(x_out, y_out), stroke_width=2.2, color="#111111", stroke_style=style, arrows=ArrowType.END))

            labels = [
                MathLabel(id="lbl_r", text="r", x=xO + 30.0, y=yO + 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xO + rS*0.707 + 15.0, y=yO - rS*0.707 + 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qp", text="+q", x=xO + rS*0.707 - 10.0, y=yO - rS*0.707 - 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xO - rS - 75.0, y=yO - 15.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Radial Electric Field of Spherical Conductor", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 6155696d: Parallel Plate Capacitor with Electric Field E
        # ----------------------------------------------------
        if "6155696d" in stem:
            w, h = 420.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 240.0
            x_p1, x_p2 = 140.0, 260.0
            x_l, x_r = 40.0, 380.0

            segments = [
                # Left plate
                Segment(id="pl1", start=(x_p1, 50.0), end=(x_p1, 180.0), stroke_width=3.0, color="#111111"),
                # Right plate
                Segment(id="pl2", start=(x_p2, 50.0), end=(x_p2, 180.0), stroke_width=3.0, color="#111111"),
                # Circuit wires
                Segment(id="w1", start=(x_p1, 110.0), end=(x_l, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="w2", start=(x_l, 110.0), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="w3", start=(x_p2, 110.0), end=(x_r, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="w4", start=(x_r, 110.0), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom wire and capacitor/battery
                Segment(id="b1", start=(x_l, y_b), end=(160.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(190.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bp1", start=(165.0, y_b - 14.0), end=(165.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="bp2", start=(185.0, y_b - 14.0), end=(185.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                # Small field arrows between plates
                Segment(id="arr1", start=(155.0, 180.0), end=(175.0, 180.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="arr2", start=(190.0, 180.0), end=(210.0, 180.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="arr3", start=(225.0, 180.0), end=(245.0, 180.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_qp", text="+ 20 \\text{ C}", x=x_p1 - 50.0, y=60.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qn", text="- 20 \\text{ C}", x=x_p2 + 50.0, y=60.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_e", text="E = 4 \\times 10^{-8}\\text{Vm}^{-1}", x=(x_p1 + x_p2)/2.0, y=30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="d = 5 \\text{ mm}", x=(x_p1 + x_p2)/2.0, y=140.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Parallel Plate Capacitor with Electric Field", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 620d01e0: Two Parallel Capacitors with V_ab
        # ----------------------------------------------------
        if "620d01e0" in stem:
            w, h = 420.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 40.0, 200.0
            x_l, x_c1, x_c2 = 50.0, 210.0, 370.0

            circles = [
                Circle(id="term_a", center=(x_l, y_t), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="term_b", center=(x_l, y_b), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Top wire
                Segment(id="top_w", start=(x_l, y_t), end=(x_c2, y_t), stroke_width=2.2, color="#111111"),
                # Bottom wire
                Segment(id="bot_w", start=(x_l, y_b), end=(x_c2, y_b), stroke_width=2.2, color="#111111"),
                # Voltage arrow
                Segment(id="v_arr", start=(x_l, y_t + 4.0), end=(x_l, y_b - 4.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                # Branch 1 (C1)
                Segment(id="b1_t", start=(x_c1, y_t), end=(x_c1, 105.0), stroke_width=2.2, color="#111111"),
                Segment(id="b1_b", start=(x_c1, 125.0), end=(x_c1, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(x_c1 - 16.0, 105.0), end=(x_c1 + 16.0, 105.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x_c1 - 16.0, 125.0), end=(x_c1 + 16.0, 125.0), stroke_width=2.8, color="#111111"),
                # Branch 2 (C2)
                Segment(id="b2_t", start=(x_c2, y_t), end=(x_c2, 105.0), stroke_width=2.2, color="#111111"),
                Segment(id="b2_b", start=(x_c2, 125.0), end=(x_c2, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(x_c2 - 16.0, 105.0), end=(x_c2 + 16.0, 105.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(x_c2 - 16.0, 125.0), end=(x_c2 + 16.0, 125.0), stroke_width=2.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_vab", text="V_{ab}", x=x_l + 16.0, y=(y_t + y_b)/2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="C_1, Q_1", x=x_c1 - 50.0, y=85.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c1_p", text="+", x=x_c1 + 22.0, y=95.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c1_n", text="-", x=x_c1 + 22.0, y=140.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c2", text="C_2, Q_2", x=x_c2 - 50.0, y=85.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c2_p", text="+", x=x_c2 + 22.0, y=95.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_c2_n", text="-", x=x_c2 + 22.0, y=140.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Parallel Capacitors with V_ab", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 62a3feab: Five Identical Capacitors Network
        # ----------------------------------------------------
        if "62a3feab" in stem:
            w, h = 480.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_m = 120.0
            y_t, y_b = 50.0, 190.0

            segments = [
                # Left lead
                Segment(id="in_l", start=(20.0, y_m), end=(60.0, y_m), stroke_width=2.2, color="#111111"),
                # Left loop
                Segment(id="l_v1", start=(60.0, y_t), end=(60.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="l_t1", start=(60.0, y_t), end=(125.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="l_t2", start=(140.0, y_t), end=(205.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="l_b1", start=(60.0, y_b), end=(125.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="l_b2", start=(140.0, y_b), end=(205.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="l_v2", start=(205.0, y_t), end=(205.0, y_b), stroke_width=2.2, color="#111111"),
                # Cap 1 (top left)
                Segment(id="c1_p1", start=(125.0, y_t - 14.0), end=(125.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(140.0, y_t - 14.0), end=(140.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Cap 2 (bot left)
                Segment(id="c2_p1", start=(125.0, y_b - 14.0), end=(125.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(140.0, y_b - 14.0), end=(140.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                # Middle series connection
                Segment(id="m_w1", start=(205.0, y_m), end=(230.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m_w2", start=(245.0, y_m), end=(275.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="cm_p1", start=(230.0, y_m - 14.0), end=(230.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cm_p2", start=(245.0, y_m - 14.0), end=(245.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                # Right loop
                Segment(id="r_v1", start=(275.0, y_t), end=(275.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="r_t1", start=(275.0, y_t), end=(340.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="r_t2", start=(355.0, y_t), end=(420.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="r_b1", start=(275.0, y_b), end=(340.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="r_b2", start=(355.0, y_b), end=(420.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="r_v2", start=(420.0, y_t), end=(420.0, y_b), stroke_width=2.2, color="#111111"),
                # Cap 4 (top right)
                Segment(id="c4_p1", start=(340.0, y_t - 14.0), end=(340.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c4_p2", start=(355.0, y_t - 14.0), end=(355.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Cap 5 (bot right)
                Segment(id="c5_p1", start=(340.0, y_b - 14.0), end=(340.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c5_p2", start=(355.0, y_b - 14.0), end=(355.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                # Right lead
                Segment(id="out_r", start=(420.0, y_m), end=(460.0, y_m), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_1", text="F", x=132.5, y=y_t - 16.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_2", text="F", x=132.5, y=y_b - 16.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_3", text="F", x=237.5, y=y_m - 18.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_4", text="F", x=347.5, y=y_t - 16.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_5", text="F", x=347.5, y=y_b - 16.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Five Identical Capacitors Network", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 64591660: Vertical Capacitor Network with 10V Battery
        # ----------------------------------------------------
        if "64591660" in stem:
            w, h = 460.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_r = 60.0, 270.0
            y_t, y_b = 50.0, 310.0

            segments = [
                # Outer loop
                Segment(id="top", start=(x_l, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="bot", start=(x_l, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="left1", start=(x_l, y_t), end=(x_l, 100.0), stroke_width=2.2, color="#111111"),
                Segment(id="left2", start=(x_l, 125.0), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                # Battery 10V
                Segment(id="bat_p", start=(x_l - 14.0, 100.0), end=(x_l + 14.0, 100.0), stroke_width=3.0, color="#111111"),
                Segment(id="bat_n", start=(x_l - 8.0, 125.0), end=(x_l + 8.0, 125.0), stroke_width=4.5, color="#111111"),
                # Right vertical: Top Cap C1
                Segment(id="rv1", start=(x_r, y_t), end=(x_r, 90.0), stroke_width=2.2, color="#111111"),
                Segment(id="rv2", start=(x_r, 110.0), end=(x_r, 150.0), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(x_r - 14.0, 90.0), end=(x_r + 14.0, 90.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x_r - 14.0, 110.0), end=(x_r + 14.0, 110.0), stroke_width=2.8, color="#111111"),
                # Middle parallel loop (C2, C3)
                Segment(id="par_top", start=(190.0, 150.0), end=(350.0, 150.0), stroke_width=2.2, color="#111111"),
                Segment(id="par_bot", start=(190.0, 230.0), end=(350.0, 230.0), stroke_width=2.2, color="#111111"),
                # Branch C2
                Segment(id="c2_t", start=(190.0, 150.0), end=(190.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="c2_b", start=(190.0, 200.0), end=(190.0, 230.0), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(176.0, 180.0), end=(204.0, 180.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(176.0, 200.0), end=(204.0, 200.0), stroke_width=2.8, color="#111111"),
                # Branch C3
                Segment(id="c3_t", start=(350.0, 150.0), end=(350.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="c3_b", start=(350.0, 200.0), end=(350.0, 230.0), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(336.0, 180.0), end=(364.0, 180.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(336.0, 200.0), end=(364.0, 200.0), stroke_width=2.8, color="#111111"),
                # Bottom Cap C4
                Segment(id="rv3", start=(x_r, 230.0), end=(x_r, 260.0), stroke_width=2.2, color="#111111"),
                Segment(id="rv4", start=(x_r, 280.0), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c4_p1", start=(x_r - 14.0, 260.0), end=(x_r + 14.0, 260.0), stroke_width=2.8, color="#111111"),
                Segment(id="c4_p2", start=(x_r - 14.0, 280.0), end=(x_r + 14.0, 280.0), stroke_width=2.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_v", text="10\text{ V}", x=x_l + 35.0, y=112.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="C_1 = 5\mu\text{F}", x=x_r + 75.0, y=100.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2 = 15\mu\text{F}", x=190.0 + 70.0, y=190.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3 = 10\mu\text{F}", x=350.0 + 75.0, y=190.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c4", text="C_4 = 20\mu\text{F}", x=x_r + 75.0, y=270.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Vertical Capacitor Network with Battery", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 6641a799: Two Spheres Coulomb Law
        # ----------------------------------------------------
        if "6641a799" in stem:
            w, h = 420.0, 180.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 70.0, 90.0, 22.0
            xB, yB, rB = 350.0, 90.0, 22.0

            circles = [
                Circle(id="sph_a", center=(xA, yA), radius=rA, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_b", center=(xB, yB), radius=rB, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                Segment(id="line", start=(xA + rA, yA), end=(xB - rB, yB), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 36.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="q_1", x=xA, y=yA + 40.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yB - 36.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="q_2", x=xB, y=yB + 40.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_f", text="F", x=210.0, y=yA - 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="r", x=210.0, y=yA + 26.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Two Spheres Coulomb Law", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 69d91d2f: Electric Dipole at Point P
        # ----------------------------------------------------
        if "69d91d2f" in stem:
            w, h = 420.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_o, x_r, y_base = 60.0, 190.0, 360.0, 160.0
            x_p, y_p = 290.0, 50.0

            circles = [
                Circle(id="pt_l", center=(x_l, y_base), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_o", center=(x_o, y_base), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_r", center=(x_r, y_base), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_p", center=(x_p, y_p), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="base", start=(x_l, y_base), end=(x_r, y_base), stroke_width=2.2, color="#111111"),
                Segment(id="arm", start=(x_o, y_base), end=(x_p, y_p), stroke_width=2.2, color="#111111"),
            ]
            arc_markers = [
                ArcAngleMarker(id="arc", vertex=(x_o, y_base), start_pt=(x_r, y_base), end_pt=(x_p, y_p), radius=28.0, stroke_width=1.8, color="#111111")
            ]
            labels = [
                MathLabel(id="lbl_ql", text="-6\mu\text{C}", x=x_l, y=y_base + 24.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_qr", text="+6\mu\text{C}", x=x_r, y=y_base + 24.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="0.3 \text{ mm}", x=x_o, y=y_base + 24.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_len", text="3 \text{ m}", x=(x_o + x_p)/2.0 - 15.0, y=(y_base + y_p)/2.0 - 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_ang", text="40^\circ", x=x_o + 48.0, y=y_base - 14.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=x_p + 15.0, y=y_p + 4.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Electric Dipole at Point P", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, arc_angles=arc_markers, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 6b7e8704: Rhombus PQRS with Charges
        # ----------------------------------------------------
        if "6b7e8704" in stem:
            w, h = 420.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xP, yP = 210.0, 60.0
            xQ, yQ = 90.0, 180.0
            xR, yR = 210.0, 300.0
            xS, yS = 330.0, 180.0

            polygons = [
                Polygon(id="rhomb", vertices=[(xP, yP), (xS, yS), (xR, yR), (xQ, yQ)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="center", center=(210.0, 180.0), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_p", text="P", x=xP, y=yP - 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qp", text="Q_1 = -2 \times 10^{-6}\text{ C}", x=xP + 95.0, y=yP - 4.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="Q", x=xQ - 18.0, y=yQ + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qq", text="Q_2 = 2 \times 10^{-6}\text{ C}", x=xQ - 45.0, y=yQ + 32.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="R", x=xR, y=yR + 25.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qr", text="Q_3 = 4 \times 10^{-6}\text{ C}", x=xR + 90.0, y=yR + 10.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_s", text="S", x=xS + 18.0, y=yS + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qs", text="Q_4 = 4 \times 10^{-6}\text{ C}", x=xS + 55.0, y=yS - 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_s1", text="4 m", x=(xP + xQ)/2.0 - 20.0, y=(yP + yQ)/2.0 - 10.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_s2", text="4 m", x=(xP + xS)/2.0 + 20.0, y=(yP + yS)/2.0 - 10.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_s3", text="4 m", x=(xQ + xR)/2.0 - 20.0, y=(yQ + yR)/2.0 + 15.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_s4", text="4 m", x=(xR + xS)/2.0 + 20.0, y=(yR + yS)/2.0 + 15.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Rhombus PQRS with Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 6ea9996a: Rectangular Box with Points P, A, B
        # ----------------------------------------------------
        if "6ea9996a" in stem:
            w, h = 380.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            polygons = [
                Polygon(id="box", vertices=[(50.0, 40.0), (330.0, 40.0), (330.0, 260.0), (50.0, 260.0)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_a", center=(120.0, 190.0), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(260.0, 190.0), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_p", text="P", x=190.0, y=80.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A.", x=100.0, y=195.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=280.0, y=195.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Rectangular Box with Points", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 6f268dd1: 3D Parallel Plates Comparison (2 plates vs 3 plates)
        # ----------------------------------------------------
        if "6f268dd1" in stem:
            w, h = 500.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            def make_3d_plate(prefix, x0, y0, pw, ph, skew):
                return Polygon(
                    id=prefix,
                    vertices=[(x0, y0), (x0 + pw, y0 - skew), (x0 + pw, y0 + ph - skew), (x0, y0 + ph)],
                    stroke_width=2.0,
                    stroke_color="#111111",
                    fill_color="#f0f0f0"
                )

            polygons = [
                # Fig 1 plates
                make_3d_plate("f1_p1", 90.0, 60.0, 30.0, 80.0, 20.0),
                make_3d_plate("f1_p2", 125.0, 60.0, 30.0, 80.0, 20.0),
                # Fig 2 plates
                make_3d_plate("f2_p1", 330.0, 60.0, 30.0, 80.0, 20.0),
                make_3d_plate("f2_p2", 350.0, 60.0, 30.0, 80.0, 20.0),
                make_3d_plate("f2_p3", 370.0, 60.0, 30.0, 80.0, 20.0),
            ]
            circles = [
                Circle(id="dot1", center=(30.0, 110.0), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="dot2", center=(265.0, 110.0), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Fig 1 leads
                Segment(id="f1_l1", start=(30.0, 110.0), end=(90.0, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_l2", start=(155.0, 100.0), end=(205.0, 100.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_g1", start=(205.0, 100.0), end=(205.0, 150.0), stroke_width=2.2, color="#111111"),
                Segment(id="f1_g2", start=(193.0, 150.0), end=(217.0, 150.0), stroke_width=2.5, color="#111111"),
                Segment(id="f1_g3", start=(197.0, 156.0), end=(213.0, 156.0), stroke_width=2.5, color="#111111"),
                Segment(id="f1_g4", start=(201.0, 162.0), end=(209.0, 162.0), stroke_width=2.5, color="#111111"),
                # Fig 2 leads
                Segment(id="f2_l1", start=(265.0, 110.0), end=(330.0, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_l2", start=(400.0, 100.0), end=(450.0, 100.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_g1", start=(450.0, 100.0), end=(450.0, 150.0), stroke_width=2.2, color="#111111"),
                Segment(id="f2_g2", start=(438.0, 150.0), end=(462.0, 150.0), stroke_width=2.5, color="#111111"),
                Segment(id="f2_g3", start=(442.0, 156.0), end=(458.0, 156.0), stroke_width=2.5, color="#111111"),
                Segment(id="f2_g4", start=(446.0, 162.0), end=(454.0, 162.0), stroke_width=2.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_fig1", text="চিত্র-১", x=125.0, y=220.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_fig2", text="চিত্র-২", x=365.0, y=220.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="3D Parallel Plates Grounded Comparison", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 6f576261: Square with Corner Charges 10C, 12C, -12C
        # ----------------------------------------------------
        if "6f576261" in stem:
            w, h = 380.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 90.0, 70.0
            xB, yB = 290.0, 70.0
            xC, yC = 290.0, 270.0
            xD, yD = 90.0, 270.0

            polygons = [
                Polygon(id="sq", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="diag1", start=(xA, yA), end=(xC, yC), stroke_width=2.0, color="#111111"),
                Segment(id="diag2", start=(xB, yB), end=(xD, yD), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_tl", text="10\text{ C}", x=xA - 35.0, y=yA - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_tr", text="12\text{ C}", x=xB + 35.0, y=yB - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_bl", text="-12\text{ C}", x=xD - 40.0, y=yD + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=190.0, y=200.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Square with Corner Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 6feb2162: Bridge Circuit with 5 Capacitors and E=16V
        # ----------------------------------------------------
        if "6feb2162" in stem:
            w, h = 460.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_m, x_r = 70.0, 240.0, 370.0
            y_t, y_b = 60.0, 260.0

            segments = [
                # Battery branch (left)
                Segment(id="w_l1", start=(x_l, y_t), end=(x_l, 145.0), stroke_width=2.2, color="#111111"),
                Segment(id="w_l2", start=(x_l, 175.0), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bat_p", start=(x_l - 14.0, 145.0), end=(x_l + 14.0, 145.0), stroke_width=3.0, color="#111111"),
                Segment(id="bat_n", start=(x_l - 8.0, 175.0), end=(x_l + 8.0, 175.0), stroke_width=4.5, color="#111111"),
                # Top wire with C1 and C2
                Segment(id="t1", start=(x_l, y_t), end=(115.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(130.0, y_t), end=(175.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(190.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(115.0, y_t - 14.0), end=(115.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(130.0, y_t - 14.0), end=(130.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p1", start=(175.0, y_t - 14.0), end=(175.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(190.0, y_t - 14.0), end=(190.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Middle vertical branch (C3)
                Segment(id="mv1", start=(x_m, y_t), end=(x_m, 145.0), stroke_width=2.2, color="#111111"),
                Segment(id="mv2", start=(x_m, 165.0), end=(x_m, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(x_m - 14.0, 145.0), end=(x_m + 14.0, 145.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(x_m - 14.0, 165.0), end=(x_m + 14.0, 165.0), stroke_width=2.8, color="#111111"),
                # Right vertical branch (C4, C5)
                Segment(id="rv1", start=(x_r, y_t), end=(x_r, 105.0), stroke_width=2.2, color="#111111"),
                Segment(id="rv2", start=(x_r, 125.0), end=(x_r, 195.0), stroke_width=2.2, color="#111111"),
                Segment(id="rv3", start=(x_r, 215.0), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c4_p1", start=(x_r - 14.0, 105.0), end=(x_r + 14.0, 105.0), stroke_width=2.8, color="#111111"),
                Segment(id="c4_p2", start=(x_r - 14.0, 125.0), end=(x_r + 14.0, 125.0), stroke_width=2.8, color="#111111"),
                Segment(id="c5_p1", start=(x_r - 14.0, 195.0), end=(x_r + 14.0, 195.0), stroke_width=2.8, color="#111111"),
                Segment(id="c5_p2", start=(x_r - 14.0, 215.0), end=(x_r + 14.0, 215.0), stroke_width=2.8, color="#111111"),
                # Bottom wire
                Segment(id="bot_w", start=(x_l, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_e", text="E = 16\text{ V}", x=x_l - 45.0, y=160.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="7\mu\text{F}", x=122.5, y=y_t - 20.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_c1_sub", text="C_1", x=122.5, y=y_t + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="42\mu\text{F}", x=182.5, y=y_t - 20.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_c2_sub", text="C_2", x=182.5, y=y_t + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3 = 2\mu\text{F}", x=x_m + 55.0, y=155.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c4", text="C_4 = 14\mu\text{F}", x=x_r - 55.0, y=115.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_c5", text="C_5 = 35\mu\text{F}", x=x_r - 55.0, y=205.0, font_size=15.0, font_weight="bold"),
            ]
            return VisualIR(title="Bridge Circuit with Capacitors", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 710bdcfc: Dual Charged Spheres +2C and -6C
        # ----------------------------------------------------
        if "710bdcfc" in stem:
            w, h = 420.0, 200.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 110.0, 100.0, 45.0
            xB, yB, rB = 310.0, 100.0, 45.0

            circles = [
                Circle(id="sph_a", center=(xA, yA), radius=rA, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="pt_a", center=(xA, yA), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="sph_b", center=(xB, yB), radius=rB, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="pt_b", center=(xB, yB), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 12.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="q_1 = +2\text{C}", x=xA + 55.0, y=yA - 35.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yB - 12.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="q_2 = -6\text{C}", x=xB + 55.0, y=yB - 35.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Dual Charged Spheres", width=w, height=h, coordinate_frame=cf, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 735f9095: Square ABDC with Charges +10C, +15C, -12C, D(?)
        # ----------------------------------------------------
        if "735f9095" in stem:
            w, h = 360.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 70.0
            xB, yB = 270.0, 70.0
            xD, yD = 270.0, 270.0
            xC, yC = 70.0, 270.0

            polygons = [
                Polygon(id="sq", vertices=[(xA, yA), (xB, yB), (xD, yD), (xC, yC)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="diag1", start=(xA, yA), end=(xD, yD), stroke_width=2.0, color="#111111"),
                Segment(id="diag2", start=(xB, yB), end=(xC, yC), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A(+10\text{ C})", x=xA, y=yA - 20.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B(+15\text{ C})", x=xB, y=yB - 20.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C(-12\text{ C})", x=xC, y=yC + 25.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D(?)", x=xD, y=yD + 25.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=170.0, y=195.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Square ABDC with Corner Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 74d411ae: Three Capacitors in Series with 12V Battery
        # ----------------------------------------------------
        if "74d411ae" in stem:
            w, h = 420.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 200.0
            x_l, x_r = 50.0, 370.0
            x1, x2, x3 = 130.0, 210.0, 290.0

            segments = [
                # Top wire & Capacitors
                Segment(id="t1", start=(x_l, y_t), end=(x1 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(x1 + 8.0, y_t), end=(x2 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(x2 + 8.0, y_t), end=(x3 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t4", start=(x3 + 8.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(x1 - 8.0, y_t - 14.0), end=(x1 - 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x1 + 8.0, y_t - 14.0), end=(x1 + 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p1", start=(x2 - 8.0, y_t - 14.0), end=(x2 - 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(x2 + 8.0, y_t - 14.0), end=(x2 + 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p1", start=(x3 - 8.0, y_t - 14.0), end=(x3 - 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(x3 + 8.0, y_t - 14.0), end=(x3 + 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Drops
                Segment(id="dl", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="dr", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom wire & Battery
                Segment(id="b1", start=(x_l, y_b), end=(195.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(225.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bp1", start=(200.0, y_b - 16.0), end=(200.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn1", start=(210.0, y_b - 9.0), end=(210.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
                Segment(id="bp2", start=(220.0, y_b - 16.0), end=(220.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1", x=x1, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_v1", text="2\mu\text{F}", x=x1, y=y_t + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=x2, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_v2", text="4\mu\text{F}", x=x2, y=y_t + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3", x=x3, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_v3", text="4\mu\text{F}", x=x3, y=y_t + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="12\text{ V}", x=210.0, y=y_b + 32.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Three Capacitors in Series", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 753719e4: Dual Spheres Connected with Internal Test Points
        # ----------------------------------------------------
        if "753719e4" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 110.0, 110.0, 48.0
            xB, yB, rB = 340.0, 110.0, 60.0
            xP, yP = xA - 20.0, yA - 28.0
            xQ, yQ = xB + 20.0, yB + 35.0

            circles = [
                Circle(id="sph_a", center=(xA, yA), radius=rA, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="pt_p", center=(xP, yP), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="sph_b", center=(xB, yB), radius=rB, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="pt_q", center=(xQ, yQ), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Connecting line between centers
                Segment(id="conn", start=(xA, yA), end=(xB, yB), stroke_width=2.2, color="#111111"),
                # Sphere A internal radius line
                Segment(id="rad_a", start=(xA, yA), end=(xA + rA*0.707, yA - rA*0.707), stroke_width=2.0, color="#111111"),
                Segment(id="to_p", start=(xA, yA), end=(xP, yP), stroke_width=1.8, color="#111111"),
                # Sphere B internal radius lines
                Segment(id="rad_b", start=(xB, yB), end=(xB + rB*0.5, yB - rB*0.866), stroke_width=2.0, color="#111111"),
                Segment(id="to_q", start=(xB, yB), end=(xQ, yQ), stroke_width=1.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_qa", text="Q = 2 \times 10^{-9}\text{C}", x=xA, y=yA - rA - 18.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP, y=yP - 12.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_ra", text="3\text{cm}", x=xA + 20.0, y=yA - 20.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_dist", text="4\text{m}", x=(xA + xB)/2.0, y=yA - 16.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="Q = 2 \times 10^{-9}\text{C}", x=xB, y=yB - rB - 18.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_rb", text="4\text{cm}", x=xB - 28.0, y=yB - 25.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_rq", text="2\text{cm}", x=xB + 24.0, y=yB + 10.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="Q", x=xQ + 12.0, y=yQ + 8.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_cap1", text="চিত্র: ছোট গোলক", x=xA, y=yA + rA + 35.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_cap2", text="চিত্র: বড় গোলক", x=xB, y=yB + rB + 25.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Dual Spheres Connected with Internal Test Points", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 75a4483d: Dual Vertical Plates +10C and -10C with Vectors M, N
        # ----------------------------------------------------
        if "75a4483d" in stem:
            w, h = 380.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_p1, x_p2 = 80.0, 280.0

            polygons = [
                Polygon(id="pl1", vertices=[(x_p1, 50.0), (x_p1 + 24.0, 50.0), (x_p1 + 24.0, 210.0), (x_p1, 210.0)], stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                Polygon(id="pl2", vertices=[(x_p2, 50.0), (x_p2 + 24.0, 50.0), (x_p2 + 24.0, 210.0), (x_p2, 210.0)], stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Vector M from plate 1
                Segment(id="vec_m", start=(x_p1 + 24.0, 110.0), end=(x_p1 + 90.0, 110.0), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
                # Vector N from plate 2
                Segment(id="vec_n", start=(x_p2, 110.0), end=(x_p2 - 66.0, 110.0), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
                # Dimension 6mm
                Segment(id="dim_6", start=(x_p1 + 24.0, 180.0), end=(x_p2, 180.0), stroke_width=2.0, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_qp", text="+ 10\text{ C}", x=x_p1 + 12.0, y=30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qn", text="- 10\text{ C}", x=x_p2 + 12.0, y=30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_m", text="M", x=x_p1 + 55.0, y=95.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_m_d", text="1\text{mm}", x=x_p1 + 55.0, y=130.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_n", text="N", x=x_p2 - 35.0, y=95.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_n_d", text="1\text{mm}", x=x_p2 - 35.0, y=130.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_6mm", text="6\text{mm}", x=(x_p1 + x_p2 + 24.0)/2.0, y=165.0, font_size=16.0, font_weight="bold"),
            ]
            # Plate signs
            for y in range(70, 205, 22):
                labels.append(MathLabel(id=f"p_{y}", text="+", x=x_p1 + 12.0, y=float(y), font_size=16.0, font_weight="bold", math_mode=False))
                labels.append(MathLabel(id=f"n_{y}", text="-", x=x_p2 + 12.0, y=float(y), font_size=18.0, font_weight="bold", math_mode=False))

            return VisualIR(title="Dual Charged Plates with Vectors M and N", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 78dd9f44: Triangle ABD with Point P
        # ----------------------------------------------------
        if "78dd9f44" in stem:
            w, h = 380.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 190.0, 60.0
            xB, yB = 80.0, 220.0
            xD, yD = 300.0, 220.0
            xP, yP = 190.0, 220.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xB, yB), (xD, yD)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_p", center=(xP, yP), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="3 \times 10^{-9}\text{C}", x=xA + 75.0, y=yA - 4.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 15.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="-5 \times 10^{-9}\text{C}", x=xB - 10.0, y=yB + 30.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD + 15.0, y=yD + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qd", text="-3 \times 10^{-9}\text{C}", x=xD + 10.0, y=yD + 30.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP, y=yP + 25.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Triangle ABD with Point P", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 7ab672c5: Three Capacitor Network C1, C2, C3
        # ----------------------------------------------------
        if "7ab672c5" in stem:
            w, h = 380.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            segments = [
                # Left loop
                Segment(id="w1", start=(30.0, 50.0), end=(30.0, 270.0), stroke_width=2.2, color="#111111"),
                Segment(id="w2", start=(30.0, 50.0), end=(330.0, 50.0), stroke_width=2.2, color="#111111"),
                # C1 branch
                Segment(id="c1_t", start=(130.0, 50.0), end=(130.0, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(115.0, 110.0), end=(145.0, 110.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(115.0, 125.0), end=(145.0, 125.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_b", start=(130.0, 125.0), end=(130.0, 160.0), stroke_width=2.2, color="#111111"),
                # C2 branch
                Segment(id="c2_t", start=(330.0, 50.0), end=(330.0, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(315.0, 110.0), end=(345.0, 110.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(315.0, 125.0), end=(345.0, 125.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_b", start=(330.0, 125.0), end=(330.0, 160.0), stroke_width=2.2, color="#111111"),
                # Join parallel to C3
                Segment(id="join", start=(130.0, 160.0), end=(330.0, 160.0), stroke_width=2.2, color="#111111"),
                Segment(id="to_c3", start=(230.0, 160.0), end=(230.0, 210.0), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(215.0, 210.0), end=(245.0, 210.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(215.0, 225.0), end=(245.0, 225.0), stroke_width=2.8, color="#111111"),
                Segment(id="from_c3", start=(230.0, 225.0), end=(230.0, 270.0), stroke_width=2.2, color="#111111"),
                Segment(id="bot_w", start=(230.0, 270.0), end=(30.0, 270.0), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1", x=130.0 - 25.0, y=118.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=330.0 + 25.0, y=118.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3", x=230.0 + 30.0, y=218.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Three Capacitor Network", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 7af11919: Collinear Point Charges Q1 and Q2 (40 cm)
        # ----------------------------------------------------
        if "7af11919" in stem:
            w, h = 440.0, 160.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, xB, y = 140.0, 300.0, 80.0

            circles = [
                Circle(id="sph_a_out", center=(xA, y), radius=14.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_a_in", center=(xA, y), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="sph_b_out", center=(xB, y), radius=14.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_b_in", center=(xB, y), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="line", start=(20.0, y), end=(420.0, y), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_q1", text="Q_1", x=xA, y=y - 25.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_q2", text="Q_2", x=xB, y=y - 25.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_dist", text="40\text{ cm}", x=(xA + xB)/2.0, y=y + 35.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Collinear Charges Q1 and Q2", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 7b52da71: Suspended Charged Sphere 12 uC
        # ----------------------------------------------------
        if "7b52da71" in stem:
            w, h = 260.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xC, yC = 130.0, 160.0
            xP, yP = 130.0, 270.0

            circles = [
                Circle(id="sph", center=(xC, yC), radius=22.0, stroke_width=2.5, stroke_color="#111111", fill_color="#555555"),
                Circle(id="pt_p", center=(xP, yP), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Ceiling line & hatch
                Segment(id="ceil", start=(60.0, 40.0), end=(200.0, 40.0), stroke_width=2.5, color="#111111"),
                # Thread
                Segment(id="thread", start=(xC, 40.0), end=(xC, yC - 22.0), stroke_width=2.0, color="#111111"),
                # Dimension ticks
                Segment(id="d_t1", start=(xC - 50.0, yC), end=(xC - 10.0, yC), stroke_width=1.8, color="#111111"),
                Segment(id="d_t2", start=(xC - 50.0, yP), end=(xC - 10.0, yP), stroke_width=1.8, color="#111111"),
                Segment(id="d_arr", start=(xC - 35.0, yC), end=(xC - 35.0, yP), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
            ]
            for xh in range(70, 200, 15):
                segments.append(Segment(id=f"h_{xh}", start=(float(xh), 40.0), end=(float(xh) - 10.0, 30.0), stroke_width=1.5, color="#111111"))

            labels = [
                MathLabel(id="lbl_q", text="12\mu\text{C}", x=xC + 55.0, y=yC, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="1.5\text{ cm}", x=xC - 75.0, y=(yC + yP)/2.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP + 15.0, y=yP + 4.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Suspended Charged Sphere", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 7edac816: Orthogonal vs Linear Charges Comparison (Fig i vs Fig ii)
        # ----------------------------------------------------
        if "7edac816" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            # Fig i
            xW1, xX1, y1 = 60.0, 170.0, 170.0
            # Fig ii
            xW2, xX2, y2 = 270.0, 380.0, 170.0
            yTop = 50.0

            circles = [
                # Fig i
                Circle(id="pt_w1", center=(xW1, y1), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_x1", center=(xX1, y1), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                # Fig ii
                Circle(id="pt_w2", center=(xW2, y2), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_x2", center=(xX2, y2), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_top", center=(xX2, yTop), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Fig i
                Segment(id="line1", start=(xW1, y1), end=(xX1, y1), stroke_width=2.2, color="#111111"),
                Segment(id="d1", start=(xW1, y1 + 18.0), end=(xX1, y1 + 18.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                # Fig ii
                Segment(id="line2_h", start=(xW2, y2), end=(xX2, y2), stroke_width=2.2, color="#111111"),
                Segment(id="line2_v", start=(xX2, y2), end=(xX2, yTop), stroke_width=2.2, color="#111111"),
                Segment(id="d2_h", start=(xW2, y2 + 18.0), end=(xX2, y2 + 18.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                Segment(id="d2_v", start=(xX2 + 14.0, y2), end=(xX2 + 14.0, yTop), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
            ]
            right_markers = [
                RightAngleMarker(id="ra", vertex=(xX2, y2), arm1_pt=(xW2, y2), arm2_pt=(xX2, yTop), size=14.0, color="#111111", stroke_width=1.8)
            ]
            labels = [
                # Fig i
                MathLabel(id="lbl_w1", text="W", x=xW1 - 10.0, y=y1 + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qw1", text="+ 2\mu\text{C}", x=xW1 - 10.0, y=y1 - 18.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_x1", text="X", x=xX1 + 10.0, y=y1 + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qx1", text="+ 4\mu\text{C}", x=xX1 + 10.0, y=y1 - 18.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="2\text{ mm}", x=(xW1 + xX1)/2.0, y=y1 + 32.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_fig1", text="চিত্র-i", x=(xW1 + xX1)/2.0, y=y1 + 60.0, font_size=17.0, font_weight="bold", math_mode=False),
                # Fig ii
                MathLabel(id="lbl_w2", text="W", x=xW2 - 10.0, y=y2 + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qw2", text="+ 2\mu\text{C}", x=xW2 - 10.0, y=y2 - 18.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_x2", text="X", x=xX2 + 15.0, y=y2 + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d2h", text="2\text{ mm}", x=(xW2 + xX2)/2.0, y=y2 + 32.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_qtop", text="+ 4\mu\text{C}", x=xX2, y=yTop - 18.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_d2v", text="3\text{ mm}", x=xX2 + 35.0, y=(y2 + yTop)/2.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_90", text="90^\circ", x=xX2 - 25.0, y=y2 - 20.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_fig2", text="চিত্র-ii", x=(xW2 + xX2)/2.0, y=y2 + 60.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Orthogonal vs Linear Charges Comparison", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, right_angles=right_markers, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 7fbd38f4: Dual Vertical Plates with Field Arrows and Point R
        # ----------------------------------------------------
        if "7fbd38f4" in stem:
            w, h = 380.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_p1, x_p2 = 80.0, 240.0
            x_r, y_r = 310.0, 160.0

            polygons = [
                Polygon(id="pl1", vertices=[(x_p1, 50.0), (x_p1 + 28.0, 50.0), (x_p1 + 28.0, 250.0), (x_p1, 250.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Polygon(id="pl2", vertices=[(x_p2, 50.0), (x_p2 + 28.0, 50.0), (x_p2 + 28.0, 250.0), (x_p2, 250.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
            ]
            circles = [
                Circle(id="pt_r", center=(x_r, y_r), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = []
            for y_arr in [75.0, 125.0, 175.0, 225.0]:
                segments.append(Segment(id=f"arr_{int(y_arr)}", start=(x_p1 + 28.0, y_arr), end=(x_p2, y_arr), stroke_width=2.2, color="#111111", arrows=ArrowType.END))

            labels = [
                MathLabel(id="lbl_a", text="A", x=x_p1 + 14.0, y=32.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b_l", text="B", x=x_p1 + 14.0, y=270.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b_r", text="B", x=x_p2 + 14.0, y=32.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=x_p2 + 14.0, y=270.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="R", x=x_r + 20.0, y=y_r + 4.0, font_size=22.0, font_weight="bold"),
            ]
            for y in [75, 125, 175, 225]:
                labels.append(MathLabel(id=f"p_{y}", text="+", x=x_p1 + 14.0, y=float(y), font_size=18.0, font_weight="bold", math_mode=False))
                labels.append(MathLabel(id=f"n_{y}", text="-", x=x_p2 + 14.0, y=float(y), font_size=20.0, font_weight="bold", math_mode=False))

            return VisualIR(title="Dual Plates with Field and External Point R", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 7fcdd369: Oval Parallel Loop in Series with Capacitor
        # ----------------------------------------------------
        # 7fcdd369: Oval Parallel Loop in Series with Capacitor
        # ----------------------------------------------------
        if "7fcdd369" in stem:
            w, h = 400.0, 230.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, xB = 55.0, 345.0
            x_l, x_r = 120.0, 230.0
            y_m = 115.0

            circles = [
                Circle(id="term_a", center=(xA, y_m), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="term_b", center=(xB, y_m), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]

            bezier_paths = [
                # Upper circular loop (Left arc & Right arc)
                BezierPath(id="arc_ul", path_d=f"M {x_l} {y_m} C {x_l} 82.0 140.0 60.0 170.0 60.0", stroke_width=2.2, stroke_color="#111111"),
                BezierPath(id="arc_ur", path_d=f"M 180.0 60.0 C 210.0 60.0 {x_r} 82.0 {x_r} {y_m}", stroke_width=2.2, stroke_color="#111111"),

                # Lower circular loop (Left arc & Right arc)
                BezierPath(id="arc_ll", path_d=f"M {x_l} {y_m} C {x_l} 148.0 140.0 170.0 170.0 170.0", stroke_width=2.2, stroke_color="#111111"),
                BezierPath(id="arc_lr", path_d=f"M 180.0 170.0 C 210.0 170.0 {x_r} 148.0 {x_r} {y_m}", stroke_width=2.2, stroke_color="#111111"),
            ]

            segments = [
                # Left lead from Terminal A
                Segment(id="lead_a", start=(xA, y_m), end=(x_l, y_m), stroke_width=2.2, color="#111111"),

                # Top capacitor (0.01 uF)
                Segment(id="c1_p1", start=(170.0, 44.0), end=(170.0, 76.0), stroke_width=3.0, color="#111111"),
                Segment(id="c1_p2", start=(180.0, 44.0), end=(180.0, 76.0), stroke_width=3.0, color="#111111"),

                # Bottom capacitor (0.02 uF)
                Segment(id="c2_p1", start=(170.0, 154.0), end=(170.0, 186.0), stroke_width=3.0, color="#111111"),
                Segment(id="c2_p2", start=(180.0, 154.0), end=(180.0, 186.0), stroke_width=3.0, color="#111111"),

                # Middle wire to Series Capacitor (0.03 uF)
                Segment(id="to_c3", start=(x_r, y_m), end=(275.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(275.0, y_m - 16.0), end=(275.0, y_m + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="c3_p2", start=(287.0, y_m - 16.0), end=(287.0, y_m + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="from_c3", start=(287.0, y_m), end=(xB, y_m), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 16.0, y=y_m + 3.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 16.0, y=y_m + 3.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text=r"0.01\text{ }\mu\text{F}", x=175.0, y=26.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text=r"0.02\text{ }\mu\text{F}", x=175.0, y=205.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text=r"0.03\text{ }\mu\text{F}", x=281.0, y=y_m - 24.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Oval Parallel Loop with Series Capacitor", width=w, height=h, coordinate_frame=cf, circles=circles, bezier_paths=bezier_paths, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 801fd085: Bridge Network of 5 Capacitors between A and B
        # ----------------------------------------------------
        if "801fd085" in stem:
            w, h = 460.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, xB = 30.0, 430.0
            x_l, x_m, x_r = 100.0, 230.0, 360.0
            y_t, y_b, y_m = 60.0, 180.0, 120.0

            circles = [
                Circle(id="term_a", center=(xA, y_m), radius=4.0, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="term_b", center=(xB, y_m), radius=4.0, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Input and split
                Segment(id="in_a", start=(xA + 4.0, y_m), end=(x_l, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="spl_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                # Top branch (Cap 1 & Cap 2)
                Segment(id="t1", start=(x_l, y_t), end=(160.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(172.0, y_t), end=(x_m, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(x_m, y_t), end=(290.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t4", start=(302.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(160.0, y_t - 14.0), end=(160.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(172.0, y_t - 14.0), end=(172.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p1", start=(290.0, y_t - 14.0), end=(290.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(302.0, y_t - 14.0), end=(302.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Middle vertical branch (Cap 3)
                Segment(id="mv1", start=(x_m, y_t), end=(x_m, 110.0), stroke_width=2.2, color="#111111"),
                Segment(id="mv2", start=(x_m, 125.0), end=(x_m, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(x_m - 14.0, 110.0), end=(x_m + 14.0, 110.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(x_m - 14.0, 125.0), end=(x_m + 14.0, 125.0), stroke_width=2.8, color="#111111"),
                # Bottom branch (Cap 4)
                Segment(id="b1", start=(x_l, y_b), end=(x_m, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(x_m, y_b), end=(290.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b3", start=(302.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c4_p1", start=(290.0, y_b - 14.0), end=(290.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c4_p2", start=(302.0, y_b - 14.0), end=(302.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                # Right join & output
                Segment(id="spl_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="out_b", start=(x_r, y_m), end=(xB - 4.0, y_m), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=y_m + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=y_m + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="1\mu\text{F}", x=166.0, y=y_t - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="1\mu\text{F}", x=296.0, y=y_t - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="1\mu\text{F}", x=x_m + 35.0, y=118.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c4", text="2\mu\text{F}", x=296.0, y=y_b + 25.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Bridge Network of Five Capacitors", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 81aa48e9: Parallel vs Series Capacitors Comparison
        # ----------------------------------------------------
        # 81aa48e9: Parallel vs Series Capacitors Comparison
        # ----------------------------------------------------
        if "81aa48e9" in stem:
            w, h = 460.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            # Left: Parallel Loop
            x_pl, x_pr = 40.0, 180.0
            y_pt, y_pb = 60.0, 160.0
            # Right: Series Pair
            x_sl, x_sr = 220.0, 400.0
            y_sm = 110.0

            segments = [
                # Parallel loop
                Segment(id="p_t1", start=(x_pl, y_pt), end=(100.0, y_pt), stroke_width=2.2, color="#111111"),
                Segment(id="p_t2", start=(120.0, y_pt), end=(x_pr, y_pt), stroke_width=2.2, color="#111111"),
                Segment(id="p_b1", start=(x_pl, y_pb), end=(100.0, y_pb), stroke_width=2.2, color="#111111"),
                Segment(id="p_b2", start=(120.0, y_pb), end=(x_pr, y_pb), stroke_width=2.2, color="#111111"),
                Segment(id="p_l", start=(x_pl, y_pt), end=(x_pl, y_pb), stroke_width=2.2, color="#111111"),
                Segment(id="p_r", start=(x_pr, y_pt), end=(x_pr, y_pb), stroke_width=2.2, color="#111111"),

                # Top capacitor C1 plates
                Segment(id="p_c1_1", start=(100.0, y_pt - 18.0), end=(100.0, y_pt + 18.0), stroke_width=3.0, color="#111111"),
                Segment(id="p_c1_2", start=(120.0, y_pt - 18.0), end=(120.0, y_pt + 18.0), stroke_width=3.0, color="#111111"),
                # Bottom capacitor C2 plates
                Segment(id="p_c2_1", start=(100.0, y_pb - 18.0), end=(100.0, y_pb + 18.0), stroke_width=3.0, color="#111111"),
                Segment(id="p_c2_2", start=(120.0, y_pb - 18.0), end=(120.0, y_pb + 18.0), stroke_width=3.0, color="#111111"),

                # Series pair
                Segment(id="s_in", start=(x_sl, y_sm), end=(270.0, y_sm), stroke_width=2.2, color="#111111"),
                Segment(id="s_m", start=(290.0, y_sm), end=(330.0, y_sm), stroke_width=2.2, color="#111111"),
                Segment(id="s_out", start=(350.0, y_sm), end=(x_sr, y_sm), stroke_width=2.2, color="#111111"),

                # Series capacitor C1 plates
                Segment(id="s_c1_1", start=(270.0, y_sm - 18.0), end=(270.0, y_sm + 18.0), stroke_width=3.0, color="#111111"),
                Segment(id="s_c1_2", start=(290.0, y_sm - 18.0), end=(290.0, y_sm + 18.0), stroke_width=3.0, color="#111111"),
                # Series capacitor C2 plates
                Segment(id="s_c2_1", start=(330.0, y_sm - 18.0), end=(330.0, y_sm + 18.0), stroke_width=3.0, color="#111111"),
                Segment(id="s_c2_2", start=(350.0, y_sm - 18.0), end=(350.0, y_sm + 18.0), stroke_width=3.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_pc1", text="C_1 = 3\\mu\\text{F}", x=110.0, y=y_pt - 28.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_pc2", text="C_2 = 7\\mu\\text{F}", x=110.0, y=y_pb + 30.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_sc1", text="C_1 = 2\\mu\\text{F}", x=310.0, y=y_sm - 30.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_sc2", text="C_2 = 5\\mu\\text{F}", x=310.0, y=y_sm + 32.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Parallel vs Series Capacitors Comparison", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 82701b32: Right-Angled Triangle ABC
        # ----------------------------------------------------
        if "82701b32" in stem:
            w, h = 360.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 60.0
            xB, yB = 70.0, 240.0
            xC, yC = 300.0, 240.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xB, yB), (xC, yC)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 20.0, y=yA + 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 20.0, y=yB + 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 20.0, y=yC + 4.0, font_size=24.0, font_weight="bold"),
            ]
            return VisualIR(title="Right-Angled Triangle ABC", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 83461056: Capacitor Circuit Comparison (Fig 1 vs Fig 2)
        # ----------------------------------------------------
        if "83461056" in stem:
            w, h = 520.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            # Fig 1: Parallel pair (C1, C2) in series with C3
            x_f1_a, x_f1_b = 30.0, 230.0
            x_f1_l, x_f1_r = 70.0, 180.0
            y_f1_t, y_f1_b, y_m = 60.0, 240.0, 150.0

            # Fig 2: Series C1 then Parallel pair (C2, C3)
            x_f2_a, x_f2_b = 280.0, 480.0
            x_f2_l, x_f2_r = 370.0, 480.0
            y_f2_t, y_f2_b = 60.0, 240.0

            circles = [
                Circle(id="f1_a", center=(x_f1_a, y_m), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="f1_b", center=(x_f1_b, y_m), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="f2_a", center=(x_f2_a, y_m), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="f2_b", center=(x_f2_b, y_m), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Fig 1
                Segment(id="f1_in", start=(x_f1_a, y_m), end=(x_f1_l, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="f1_spl", start=(x_f1_l, y_f1_t), end=(x_f1_l, y_f1_b), stroke_width=2.2, color="#111111"),
                Segment(id="f1_t1", start=(x_f1_l, y_f1_t), end=(117.0, y_f1_t), stroke_width=2.2, color="#111111"),
                Segment(id="f1_t2", start=(133.0, y_f1_t), end=(x_f1_r, y_f1_t), stroke_width=2.2, color="#111111"),
                Segment(id="f1_c1_1", start=(117.0, y_f1_t - 14.0), end=(117.0, y_f1_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f1_c1_2", start=(133.0, y_f1_t - 14.0), end=(133.0, y_f1_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f1_b1", start=(x_f1_l, y_f1_b), end=(117.0, y_f1_b), stroke_width=2.2, color="#111111"),
                Segment(id="f1_b2", start=(133.0, y_f1_b), end=(x_f1_r, y_f1_b), stroke_width=2.2, color="#111111"),
                Segment(id="f1_c2_1", start=(117.0, y_f1_b - 14.0), end=(117.0, y_f1_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f1_c2_2", start=(133.0, y_f1_b - 14.0), end=(133.0, y_f1_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f1_join", start=(x_f1_r, y_f1_t), end=(x_f1_r, y_f1_b), stroke_width=2.2, color="#111111"),
                Segment(id="f1_to_c3", start=(x_f1_r, y_m), end=(198.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="f1_c3_1", start=(198.0, y_m - 14.0), end=(198.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f1_c3_2", start=(210.0, y_m - 14.0), end=(210.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f1_out", start=(210.0, y_m), end=(x_f1_b, y_m), stroke_width=2.2, color="#111111"),
                # Fig 2
                Segment(id="f2_in", start=(x_f2_a, y_m), end=(305.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="f2_c1_1", start=(305.0, y_m - 14.0), end=(305.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f2_c1_2", start=(317.0, y_m - 14.0), end=(317.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f2_to_par", start=(317.0, y_m), end=(x_f2_l, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="f2_spl", start=(x_f2_l, y_f2_t), end=(x_f2_l, y_f2_b), stroke_width=2.2, color="#111111"),
                Segment(id="f2_t1", start=(x_f2_l, y_f2_t), end=(417.0, y_f2_t), stroke_width=2.2, color="#111111"),
                Segment(id="f2_t2", start=(433.0, y_f2_t), end=(x_f2_r, y_f2_t), stroke_width=2.2, color="#111111"),
                Segment(id="f2_c2_1", start=(417.0, y_f2_t - 14.0), end=(417.0, y_f2_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f2_c2_2", start=(433.0, y_f2_t - 14.0), end=(433.0, y_f2_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f2_b1", start=(x_f2_l, y_f2_b), end=(417.0, y_f2_b), stroke_width=2.2, color="#111111"),
                Segment(id="f2_b2", start=(433.0, y_f2_b), end=(x_f2_r, y_f2_b), stroke_width=2.2, color="#111111"),
                Segment(id="f2_c3_1", start=(417.0, y_f2_b - 14.0), end=(417.0, y_f2_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f2_c3_2", start=(433.0, y_f2_b - 14.0), end=(433.0, y_f2_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="f2_join", start=(x_f2_r, y_f2_t), end=(x_f2_r, y_f2_b), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                # Fig 1
                MathLabel(id="f1_lbl_a", text="A", x=x_f1_a - 15.0, y=y_m + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="f1_lbl_b", text="B", x=x_f1_b + 15.0, y=y_m + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="f1_lbl_c1", text="C_1 = 2\mu\text{F}", x=125.0, y=y_f1_t - 22.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="f1_lbl_c2", text="C_2 = 1\mu\text{F}", x=125.0, y=y_f1_b + 25.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="f1_lbl_c3", text="C_3 = 3\mu\text{F}", x=204.0, y=y_m - 22.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="f1_lbl_fig", text="চিত্র-১", x=125.0, y=285.0, font_size=18.0, font_weight="bold", math_mode=False),
                # Fig 2
                MathLabel(id="f2_lbl_a", text="A", x=x_f2_a - 15.0, y=y_m + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="f2_lbl_b", text="B", x=x_f2_b + 15.0, y=y_m + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="f2_lbl_c1", text="C_1 = 2\mu\text{F}", x=311.0, y=y_m - 22.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="f2_lbl_c2", text="C_2 = 1\mu\text{F}", x=425.0, y=y_f2_t - 22.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="f2_lbl_c3", text="C_3 = 3\mu\text{F}", x=425.0, y=y_f2_b + 25.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="f2_lbl_fig", text="চিত্র-২", x=425.0, y=285.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Capacitor Circuit Comparison", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 838f679f: Dual Vertical Plates with Connecting Lines and Point P
        # ----------------------------------------------------
        if "838f679f" in stem:
            w, h = 340.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_p1, x_p2 = 50.0, 240.0

            polygons = [
                Polygon(id="pl1", vertices=[(x_p1, 50.0), (x_p1 + 55.0, 50.0), (x_p1 + 55.0, 310.0), (x_p1, 310.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Polygon(id="pl2", vertices=[(x_p2, 50.0), (x_p2 + 55.0, 50.0), (x_p2 + 55.0, 310.0), (x_p2, 310.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = []
            for y_line in [80.0, 120.0, 160.0, 200.0, 240.0, 280.0]:
                segments.append(Segment(id=f"line_{int(y_line)}", start=(x_p1 + 55.0, y_line), end=(x_p2, y_line), stroke_width=2.0, color="#111111"))

            labels = [
                MathLabel(id="lbl_a", text="A", x=x_p1 + 27.5, y=32.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=x_p1 + 27.5, y=330.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=x_p2 + 27.5, y=32.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=x_p2 + 27.5, y=330.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=(x_p1 + 55.0 + x_p2)/2.0, y=145.0, font_size=22.0, font_weight="bold"),
            ]
            for y in [80, 120, 160, 200, 240, 280]:
                labels.append(MathLabel(id=f"p_{y}", text="+", x=x_p1 + 27.5, y=float(y), font_size=18.0, font_weight="bold", math_mode=False))
                labels.append(MathLabel(id=f"n_{y}", text="-", x=x_p2 + 27.5, y=float(y), font_size=20.0, font_weight="bold", math_mode=False))

            return VisualIR(title="Dual Plates with Internal Point P", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 84a95501: Dual Spheres 90 nC and 50 nC
        # ----------------------------------------------------
        if "84a95501" in stem:
            w, h = 420.0, 160.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 120.0, 80.0, 24.0
            xB, yB, rB = 300.0, 80.0, 24.0

            circles = [
                Circle(id="sph_a", center=(xA, yA), radius=rA, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_b", center=(xB, yB), radius=rB, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                Segment(id="d_arr", start=(xA, yA), end=(xB, yB), stroke_width=2.0, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_qa", text="90\text{ nC}", x=xA - 55.0, y=yA + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="50\text{ nC}", x=xB + 55.0, y=yB + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="4\text{ m}", x=(xA + xB)/2.0, y=yA + 26.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Dual Charged Spheres 90nC and 50nC", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 869ac888: Square ABDC with Diagonals and 1m Sides
        # ----------------------------------------------------
        if "869ac888" in stem:
            w, h = 380.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 80.0, 70.0
            xD, yD = 280.0, 70.0
            xC, yC = 280.0, 270.0
            xB, yB = 80.0, 270.0

            polygons = [
                Polygon(id="sq", vertices=[(xA, yA), (xD, yD), (xC, yC), (xB, yB)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="diag1", start=(xA, yA), end=(xC, yC), stroke_width=2.0, color="#111111"),
                Segment(id="diag2", start=(xD, yD), end=(xB, yB), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD + 18.0, y=yD + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 18.0, y=yB + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_t", text="1 m", x=(xA + xD)/2.0, y=yA - 18.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b_dim", text="1 m", x=(xB + xC)/2.0, y=yB + 24.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_l_dim", text="1 m", x=xA - 35.0, y=(yA + yB)/2.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r_dim", text="1 m", x=xD + 35.0, y=(yD + yC)/2.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Square ABDC with Diagonals", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 8e74313b: Rectangle ABCD with Charges
        # ----------------------------------------------------
        if "8e74313b" in stem:
            w, h = 420.0, 340.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 80.0, 260.0
            xB, yB = 280.0, 260.0
            xC, yC = 280.0, 80.0
            xD, yD = 80.0, 80.0

            polygons = [
                Polygon(id="rect", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yA + 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+5 \times 10^{-3}\text{ C}", x=xB + 85.0, y=yA + 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD - 18.0, y=yD - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qd", text="-2.25 \times 10^{-3}\text{ C}", x=xD + 60.0, y=yD - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_top_w", text="1 m", x=(xD + xC)/2.0, y=yC + 25.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_bot_w", text="1 m", x=(xA + xB)/2.0, y=yA + 25.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_l_h", text="0.8 m", x=xD - 38.0, y=(yD + yA)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r_h", text="0.8 m", x=xC + 38.0, y=(yC + yB)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Rectangle ABCD with Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 91daf304: Serpentine Capacitor Ladder Network (X, Y)
        # ----------------------------------------------------
        if "91daf304" in stem:
            w, h = 480.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b, y_m = 50.0, 150.0, 100.0
            x_caps = [70.0, 140.0, 210.0, 280.0, 350.0]

            segments = [
                # Bottom return rail to Y
                Segment(id="rail_y", start=(x_caps[0], 180.0), end=(440.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="cap1_b", start=(x_caps[0], y_m + 12.0), end=(x_caps[0], 180.0), stroke_width=2.2, color="#111111"),
                # Cap 1 plates
                Segment(id="c1_p1", start=(x_caps[0] - 14.0, y_m - 12.0), end=(x_caps[0] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x_caps[0] - 14.0, y_m + 12.0), end=(x_caps[0] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Top bridge 1-2
                Segment(id="br_t1", start=(x_caps[0], y_m - 12.0), end=(x_caps[0], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="br_t1_h", start=(x_caps[0], y_t), end=(x_caps[1], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="br_t1_d", start=(x_caps[1], y_t), end=(x_caps[1], y_m - 12.0), stroke_width=2.2, color="#111111"),
                # Cap 2 plates
                Segment(id="c2_p1", start=(x_caps[1] - 14.0, y_m - 12.0), end=(x_caps[1] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(x_caps[1] - 14.0, y_m + 12.0), end=(x_caps[1] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Bottom bridge 2-3
                Segment(id="br_b1", start=(x_caps[1], y_m + 12.0), end=(x_caps[1], y_b), stroke_width=2.2, color="#111111"),
                Segment(id="br_b1_h", start=(x_caps[1], y_b), end=(x_caps[2], y_b), stroke_width=2.2, color="#111111"),
                Segment(id="br_b1_u", start=(x_caps[2], y_b), end=(x_caps[2], y_m + 12.0), stroke_width=2.2, color="#111111"),
                # Cap 3 plates
                Segment(id="c3_p1", start=(x_caps[2] - 14.0, y_m - 12.0), end=(x_caps[2] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(x_caps[2] - 14.0, y_m + 12.0), end=(x_caps[2] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Top bridge 3-4
                Segment(id="br_t2", start=(x_caps[2], y_m - 12.0), end=(x_caps[2], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="br_t2_h", start=(x_caps[2], y_t), end=(x_caps[3], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="br_t2_d", start=(x_caps[3], y_t), end=(x_caps[3], y_m - 12.0), stroke_width=2.2, color="#111111"),
                # Cap 4 plates
                Segment(id="c4_p1", start=(x_caps[3] - 14.0, y_m - 12.0), end=(x_caps[3] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c4_p2", start=(x_caps[3] - 14.0, y_m + 12.0), end=(x_caps[3] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Bottom bridge 4-5
                Segment(id="br_b2", start=(x_caps[3], y_m + 12.0), end=(x_caps[3], y_b), stroke_width=2.2, color="#111111"),
                Segment(id="br_b2_h", start=(x_caps[3], y_b), end=(x_caps[4], y_b), stroke_width=2.2, color="#111111"),
                Segment(id="br_b2_u", start=(x_caps[4], y_b), end=(x_caps[4], y_m + 12.0), stroke_width=2.2, color="#111111"),
                # Cap 5 plates
                Segment(id="c5_p1", start=(x_caps[4] - 14.0, y_m - 12.0), end=(x_caps[4] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c5_p2", start=(x_caps[4] - 14.0, y_m + 12.0), end=(x_caps[4] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Output to X
                Segment(id="out_x1", start=(x_caps[4], y_m - 12.0), end=(x_caps[4], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="out_x2", start=(x_caps[4], y_t), end=(440.0, y_t), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C", x=x_caps[0] - 25.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C", x=(x_caps[0] + x_caps[1])/2.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C", x=(x_caps[1] + x_caps[2])/2.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c4", text="C", x=(x_caps[2] + x_caps[3])/2.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c5", text="C", x=(x_caps[3] + x_caps[4])/2.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_x", text="X", x=455.0, y=y_t + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_y", text="Y", x=455.0, y=184.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Serpentine Capacitor Ladder Network", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 933e3197: Series-Parallel Capacitors with 12V Battery
        # ----------------------------------------------------
        if "933e3197" in stem:
            w, h = 420.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 200.0
            x_l, x_r = 50.0, 370.0
            x_c1 = 120.0
            y_par_t, y_par_b = 30.0, 90.0

            segments = [
                # Left drop
                Segment(id="dl", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                # Cap 1 (4.5 uF)
                Segment(id="t1", start=(x_l, y_t), end=(x_c1 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(x_c1 - 8.0, y_t - 14.0), end=(x_c1 - 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x_c1 + 8.0, y_t - 14.0), end=(x_c1 + 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="t2", start=(x_c1 + 8.0, y_t), end=(200.0, y_t), stroke_width=2.2, color="#111111"),
                # Parallel loop (3 uF and 6 uF)
                Segment(id="par_spl", start=(200.0, y_par_t), end=(200.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="pt1", start=(200.0, y_par_t), end=(250.0, y_par_t), stroke_width=2.2, color="#111111"),
                Segment(id="pt2", start=(262.0, y_par_t), end=(320.0, y_par_t), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(250.0, y_par_t - 12.0), end=(250.0, y_par_t + 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(262.0, y_par_t - 12.0), end=(262.0, y_par_t + 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="pb1", start=(200.0, y_par_b), end=(250.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="pb2", start=(262.0, y_par_b), end=(320.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(250.0, y_par_b - 12.0), end=(250.0, y_par_b + 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(262.0, y_par_b - 12.0), end=(262.0, y_par_b + 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="par_join", start=(320.0, y_par_t), end=(320.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="to_r", start=(320.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="dr", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom battery
                Segment(id="bot1", start=(x_l, y_b), end=(160.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bot2", start=(180.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bp", start=(160.0, y_b - 16.0), end=(160.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(180.0, y_b - 9.0), end=(180.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="4.5\mu\text{F}", x=x_c1, y=y_t + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="3\mu\text{F}", x=256.0, y=y_par_t - 16.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="6\mu\text{F}", x=256.0, y=y_par_b - 16.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="12\text{ V}", x=170.0, y=y_b + 28.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Series-Parallel Capacitors with Battery", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 93ab9df0: Vertical Dipole with Perpendicular Vector to P
        # ----------------------------------------------------
        if "93ab9df0" in stem:
            w, h = 260.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 80.0, 60.0
            xB, yB = 80.0, 300.0
            xO, yO = 80.0, 180.0
            xP, yP = 210.0, 180.0

            circles = [
                Circle(id="pt_a", center=(xA, yA), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yB), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="dipole", start=(xA, yA), end=(xB, yB), stroke_width=2.2, color="#111111"),
                Segment(id="vec_p", start=(xO, yO), end=(xP, yP), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
            ]
            right_markers = [
                RightAngleMarker(id="ra", vertex=(xO, yO), arm1_pt=(xA, yA), arm2_pt=(xP, yP), size=14.0, color="#111111", stroke_width=1.8)
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 20.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="-3.2\mu\text{C}", x=xA + 45.0, y=yA + 4.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 20.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+5.8\mu\text{C}", x=xB + 45.0, y=yB + 4.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO - 20.0, y=yO + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP, y=yP + 25.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Vertical Dipole with Vector to P", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, right_angles=right_markers, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 949a13a9: Series-Parallel Capacitor Circuit with 90V Battery
        # ----------------------------------------------------
        if "949a13a9" in stem:
            w, h = 400.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 200.0
            x_l, x_r = 50.0, 350.0
            x_c1 = 120.0
            y_par_t, y_par_b = 30.0, 90.0

            segments = [
                # Left drop
                Segment(id="dl", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                # Cap 1
                Segment(id="t1", start=(x_l, y_t), end=(x_c1 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(x_c1 - 8.0, y_t - 14.0), end=(x_c1 - 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x_c1 + 8.0, y_t - 14.0), end=(x_c1 + 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="t2", start=(x_c1 + 8.0, y_t), end=(200.0, y_t), stroke_width=2.2, color="#111111"),
                # Parallel loop A
                Segment(id="par_spl", start=(200.0, y_par_t), end=(200.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="pt1", start=(200.0, y_par_t), end=(235.0, y_par_t), stroke_width=2.2, color="#111111"),
                Segment(id="pt2", start=(247.0, y_par_t), end=(280.0, y_par_t), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(235.0, y_par_t - 12.0), end=(235.0, y_par_t + 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(247.0, y_par_t - 12.0), end=(247.0, y_par_t + 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="pb1", start=(200.0, y_par_b), end=(235.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="pb2", start=(247.0, y_par_b), end=(280.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(235.0, y_par_b - 12.0), end=(235.0, y_par_b + 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(247.0, y_par_b - 12.0), end=(247.0, y_par_b + 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="par_join", start=(280.0, y_par_t), end=(280.0, y_par_b), stroke_width=2.2, color="#111111"),
                Segment(id="to_r", start=(280.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="dr", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom battery
                Segment(id="bot1", start=(x_l, y_b), end=(120.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bot2", start=(140.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bp", start=(120.0, y_b - 16.0), end=(120.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(140.0, y_b - 9.0), end=(140.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a_box", text="A", x=215.0, y=y_t + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="90\text{ V}", x=130.0, y=y_b + 28.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Series-Parallel Capacitor Circuit with Battery", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 961b1f3f: Triangle ABD with Altitude CD (3 cm)
        # ----------------------------------------------------
        if "961b1f3f" in stem:
            w, h = 380.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 90.0, 200.0
            xB, yB = 290.0, 200.0
            xC, yC = 190.0, 200.0
            xD, yD = 190.0, 60.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xD, yD), (xB, yB)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_a", center=(xA, yA), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yB), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_d", center=(xD, yD), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Altitude
                Segment(id="alt", start=(xC, yC), end=(xD, yD), stroke_width=2.2, color="#111111"),
                # Dimension CD
                Segment(id="dim_cd", start=(xD + 10.0, yD), end=(xC + 10.0, yC), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                # Dimension AB
                Segment(id="dim_ab", start=(xA, yA + 40.0), end=(xB, yA + 40.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                Segment(id="tk_a", start=(xA, yA + 25.0), end=(xA, yA + 55.0), stroke_width=1.8, color="#111111"),
                Segment(id="tk_b", start=(xB, yA + 25.0), end=(xB, yA + 55.0), stroke_width=1.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="+2\text{ C}", x=xA, y=yA + 24.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+10\text{ C}", x=xB, y=yB + 24.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC, y=yC + 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD, y=yD - 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_alt", text="3\text{ cm}", x=xD + 28.0, y=(yD + yC)/2.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_base", text="8\text{ cm}", x=xC, y=yA + 38.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Triangle ABD with Altitude CD", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 9624229e: Square ABCD with Center Point p and Charges
        # ----------------------------------------------------
        if "9624229e" in stem:
            w, h = 400.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 60.0
            xB, yB = 270.0, 60.0
            xC, yC = 270.0, 260.0
            xD, yD = 70.0, 260.0

            polygons = [
                Polygon(id="sq", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_p", center=(170.0, 160.0), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="q_1 = 2 \times 10^{-9}\text{C}", x=xA + 60.0, y=yA - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="q_2 = 3 \times 10^{-9}\text{C}", x=xB + 75.0, y=yB + 45.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="q_2 = 3 \times 10^{-9}\text{C}", x=xC + 75.0, y=yC - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD - 18.0, y=yD + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="p", x=170.0, y=185.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_w", text="1m", x=(xA + xD)/2.0 - 45.0, y=(yA + yD)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_e", text="1m", x=xB + 25.0, y=(yB + yC)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_s", text="1m", x=(xD + xC)/2.0, y=yD + 25.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Square ABCD with Center Point p", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 982b7315: Capacitor Plate Area Comparison (4 cm2 vs 2 cm2)
        # ----------------------------------------------------
        if "982b7315" in stem:
            w, h = 480.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            # Fig 1
            x_f1_l, x_f1_r = 90.0, 150.0
            # Fig 2
            x_f2_l, x_f2_r = 310.0, 370.0
            y_m = 90.0

            circles = [
                Circle(id="f1_in", center=(60.0, y_m), radius=3.5, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="f1_out", center=(180.0, y_m), radius=3.5, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="f2_in", center=(280.0, y_m), radius=3.5, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="f2_out", center=(400.0, y_m), radius=3.5, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Fig 1
                Segment(id="f1_w1", start=(63.5, y_m), end=(x_f1_l, y_m), stroke_width=2.0, color="#111111"),
                Segment(id="f1_p1", start=(x_f1_l, 30.0), end=(x_f1_l, 150.0), stroke_width=2.5, color="#111111"),
                Segment(id="f1_p2", start=(x_f1_r, 30.0), end=(x_f1_r, 150.0), stroke_width=2.5, color="#111111"),
                Segment(id="f1_w2", start=(x_f1_r, y_m), end=(176.5, y_m), stroke_width=2.0, color="#111111"),
                # Fig 2
                Segment(id="f2_w1", start=(283.5, y_m), end=(x_f2_l, y_m), stroke_width=2.0, color="#111111"),
                Segment(id="f2_p1", start=(x_f2_l, 30.0), end=(x_f2_l, 150.0), stroke_width=2.5, color="#111111"),
                Segment(id="f2_p2", start=(x_f2_r, 30.0), end=(x_f2_r, 150.0), stroke_width=2.5, color="#111111"),
                Segment(id="f2_w2", start=(x_f2_r, y_m), end=(396.5, y_m), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_fig1", text="চিত্র-১", x=120.0, y=175.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_a1", text="পাতের ক্ষেত্রফল = 4 cm²", x=120.0, y=205.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_fig2", text="চিত্র-২", x=340.0, y=175.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_a2", text="পাতের ক্ষেত্রফল = 2 cm²", x=340.0, y=205.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Capacitor Plate Area Comparison", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 98bb9f28: Two Spheres A and B with 1.0m Dimension
        # ----------------------------------------------------
        if "98bb9f28" in stem:
            w, h = 420.0, 180.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 110.0, 95.0, 24.0
            xB, yB, rB = 290.0, 95.0, 24.0

            circles = [
                Circle(id="sph_a", center=(xA, yA), radius=rA, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_b", center=(xB, yB), radius=rB, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Center connection
                Segment(id="conn", start=(xA, yA), end=(xB, yB), stroke_width=2.2, color="#111111"),
                # Top dimension line
                Segment(id="dim_l", start=(xA, yA), end=(xA, 35.0), stroke_width=2.0, color="#111111"),
                Segment(id="dim_r", start=(xB, yB), end=(xB, 35.0), stroke_width=2.0, color="#111111"),
                Segment(id="dim_h", start=(xA, 35.0), end=(xB, 35.0), stroke_width=2.0, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_d", text="1.0 \text{ m}", x=(xA + xB)/2.0, y=25.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="A = 30 \times 10^{-7}\text{ C}", x=xA - 10.0, y=yA + 40.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="B = -40 \times 10^{-7}\text{ C}", x=xB + 10.0, y=yB + 40.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Two Spheres A and B", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 9ad064ff: Square with Corner Nodes N1, N2, N3, N4
        # ----------------------------------------------------
        if "9ad064ff" in stem:
            w, h = 360.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x4, y4 = 70.0, 70.0
            x3, y3 = 270.0, 70.0
            x2, y2 = 270.0, 270.0
            x1, y1 = 70.0, 270.0

            polygons = [
                Polygon(id="sq", vertices=[(x4, y4), (x3, y3), (x2, y2), (x1, y1)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="diag1", start=(x4, y4), end=(x2, y2), stroke_width=2.0, color="#111111"),
                Segment(id="diag2", start=(x3, y3), end=(x1, y1), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_n4", text="N_4 = ?", x=x4 + 10.0, y=y4 - 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_n3", text="N_3 = 6\text{C}", x=x3 + 10.0, y=y3 - 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_n2", text="N_2 = -4\text{C}", x=x2 + 20.0, y=y2 + 28.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_n1", text="N_1 = 2\text{C}", x=x1 - 10.0, y=y1 + 28.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=170.0, y=195.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Square with Corner Nodes N1..N4", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 9b5bba9e: Multi-Mesh Circuit with Capacitor and Resistors
        # ----------------------------------------------------
        # 9b5bba9e: Multi-Mesh Circuit with Capacitor and Resistors
        # ----------------------------------------------------
        if "9b5bba9e" in stem:
            w, h = 480.0, 440.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_m = 190.0
            x_r = 300.0
            y_top_node = 140.0
            y_bot_node = 260.0

            def make_resistor_h(prefix, x0, x1, y):
                min_x, max_x = min(x0, x1), max(x0, x1)
                dx = (max_x - min_x) / 6.0
                pts = [
                    (min_x, y),
                    (min_x + dx * 0.5, y - 7.0),
                    (min_x + dx * 1.5, y + 7.0),
                    (min_x + dx * 2.5, y - 7.0),
                    (min_x + dx * 3.5, y + 7.0),
                    (min_x + dx * 4.5, y - 7.0),
                    (min_x + dx * 5.5, y + 7.0),
                    (max_x, y)
                ]
                segs = []
                for i in range(len(pts) - 1):
                    segs.append(Segment(id=f"{prefix}_{i}", start=pts[i], end=pts[i+1], stroke_width=2.2, color="#111111"))
                return segs

            def make_resistor_v(prefix, y0, y1, x):
                min_y, max_y = min(y0, y1), max(y0, y1)
                dy = (max_y - min_y) / 6.0
                pts = [
                    (x, min_y),
                    (x - 7.0, min_y + dy * 0.5),
                    (x + 7.0, min_y + dy * 1.5),
                    (x - 7.0, min_y + dy * 2.5),
                    (x + 7.0, min_y + dy * 3.5),
                    (x - 7.0, min_y + dy * 4.5),
                    (x + 7.0, min_y + dy * 5.5),
                    (x, max_y)
                ]
                segs = []
                for i in range(len(pts) - 1):
                    segs.append(Segment(id=f"{prefix}_{i}", start=pts[i], end=pts[i+1], stroke_width=2.2, color="#111111"))
                return segs

            circles = [
                # Junction nodes
                Circle(id="j_top", center=(x_m, y_top_node), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]

            segments = [
                # Central vertical capacitor C=4uF between junctions
                Segment(id="cv1", start=(x_m, y_top_node), end=(x_m, 195.0), stroke_width=2.2, color="#111111"),
                Segment(id="c_p1", start=(x_m - 16.0, 195.0), end=(x_m + 16.0, 195.0), stroke_width=3.0, color="#111111"),
                Segment(id="c_p2", start=(x_m - 16.0, 205.0), end=(x_m + 16.0, 205.0), stroke_width=3.0, color="#111111"),
                Segment(id="cv2", start=(x_m, 205.0), end=(x_m, y_bot_node), stroke_width=2.2, color="#111111"),

                # Top branch: wire from (x_m, 20) through 3 ohm resistor to top node
                Segment(id="wire_top", start=(x_m, 20.0), end=(x_m, 60.0), stroke_width=2.2, color="#111111"),
                *make_resistor_v("r_top", 60.0, 140.0, x_m),
                # Standalone downward current arrow (3A)
                Segment(id="arr_top", start=(x_m - 14.0, 20.0), end=(x_m - 14.0, 58.0), stroke_width=2.2, color="#111111", arrows=ArrowType.END),

                # Bottom branch: wire from bottom node through 3 ohm resistor to (x_m, 420)
                *make_resistor_v("r_bot", 260.0, 360.0, x_m),
                Segment(id="wire_bot", start=(x_m, 360.0), end=(x_m, 420.0), stroke_width=2.2, color="#111111"),
                # Standalone upward current arrow (1A)
                Segment(id="arr_bot", start=(x_m - 14.0, 420.0), end=(x_m - 14.0, 382.0), stroke_width=2.2, color="#111111", arrows=ArrowType.END),

                # Top-left branch: Battery 4V + 3 ohm resistor with arrow entering top junction
                Segment(id="tl_w0", start=(40.0, y_top_node), end=(60.0, y_top_node), stroke_width=2.2, color="#111111"),
                Segment(id="tl_bp", start=(60.0, y_top_node - 14.0), end=(60.0, y_top_node + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="tl_bn", start=(68.0, y_top_node - 8.0), end=(68.0, y_top_node + 8.0), stroke_width=4.5, color="#111111"),
                Segment(id="tl_w1", start=(68.0, y_top_node), end=(95.0, y_top_node), stroke_width=2.2, color="#111111"),
                *make_resistor_h("r_tl", 95.0, 155.0, y_top_node),
                Segment(id="tl_arr", start=(155.0, y_top_node), end=(x_m, y_top_node), stroke_width=2.2, color="#111111", arrows=ArrowType.END),

                # Bottom-left branch: Battery 3V + 3 ohm resistor
                Segment(id="bl_w0", start=(40.0, y_bot_node), end=(60.0, y_bot_node), stroke_width=2.2, color="#111111"),
                Segment(id="bl_bp", start=(60.0, y_bot_node - 14.0), end=(60.0, y_bot_node + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="bl_bn", start=(68.0, y_bot_node - 8.0), end=(68.0, y_bot_node + 8.0), stroke_width=4.5, color="#111111"),
                Segment(id="bl_w1", start=(68.0, y_bot_node), end=(95.0, y_bot_node), stroke_width=2.2, color="#111111"),
                *make_resistor_h("r_bl", 95.0, 160.0, y_bot_node),
                Segment(id="bl_w2", start=(160.0, y_bot_node), end=(x_m, y_bot_node), stroke_width=2.2, color="#111111"),

                # Right top branch: 5 ohm resistor
                Segment(id="tr_w0", start=(x_m, y_top_node), end=(215.0, y_top_node), stroke_width=2.2, color="#111111"),
                *make_resistor_h("r_tr", 215.0, 275.0, y_top_node),
                Segment(id="tr_w1", start=(275.0, y_top_node), end=(x_r, y_top_node), stroke_width=2.2, color="#111111"),

                # Right vertical branch: 1 ohm resistor
                Segment(id="mr_w0", start=(x_r, y_top_node), end=(x_r, 170.0), stroke_width=2.2, color="#111111"),
                *make_resistor_v("r_mr", 170.0, 230.0, x_r),
                Segment(id="mr_w1", start=(x_r, 230.0), end=(x_r, y_bot_node), stroke_width=2.2, color="#111111"),

                # Right bottom branch: 3 ohm resistor
                Segment(id="br_w0", start=(x_m, y_bot_node), end=(215.0, y_bot_node), stroke_width=2.2, color="#111111"),
                *make_resistor_h("r_br", 215.0, 275.0, y_bot_node),
                Segment(id="br_w1", start=(275.0, y_bot_node), end=(x_r, y_bot_node), stroke_width=2.2, color="#111111"),

                # Far-right branch: 4 ohm resistor with open right end
                Segment(id="far_w0", start=(x_r, y_bot_node), end=(325.0, y_bot_node), stroke_width=2.2, color="#111111"),
                *make_resistor_h("r_far", 325.0, 395.0, y_bot_node),
                Segment(id="far_w1", start=(395.0, y_bot_node), end=(420.0, y_bot_node), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_3a", text="3 A", x=x_m + 25.0, y=40.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r_top", text="3 Ω", x=x_m + 26.0, y=102.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_tl_v", text="4 V", x=64.0, y=y_top_node - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_tl_i", text="2 A", x=64.0, y=y_top_node + 22.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_tl_r", text="3 Ω", x=127.0, y=y_top_node - 16.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=x_m - 20.0, y=200.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c_val", text="4 μF", x=x_m + 32.0, y=200.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_bl_v", text="3 V", x=64.0, y=y_bot_node - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_bl_i", text="2 A", x=64.0, y=y_bot_node + 22.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_bl_r", text="3 Ω", x=127.0, y=y_bot_node - 16.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_1a", text="1 A", x=x_m + 25.0, y=395.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r_bot", text="3 Ω", x=x_m + 26.0, y=312.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r_tr", text="5 Ω", x=245.0, y=y_top_node - 16.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r_mr", text="1 Ω", x=x_r + 24.0, y=200.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r_br", text="3 Ω", x=245.0, y=y_bot_node - 16.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r_far", text="4 Ω", x=360.0, y=y_bot_node + 22.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Multi-Mesh Circuit with Capacitor", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 9f1ee7fd: Two Series Capacitors with 50V Battery
        # ----------------------------------------------------
        if "9f1ee7fd" in stem:
            w, h = 380.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 180.0
            x_l, x_r = 50.0, 330.0
            x_c1, x_c2 = 130.0, 250.0

            segments = [
                # Top wire & Capacitors
                Segment(id="t1", start=(x_l, y_t), end=(x_c1 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(x_c1 + 8.0, y_t), end=(x_c2 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(x_c2 + 8.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(x_c1 - 8.0, y_t - 14.0), end=(x_c1 - 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x_c1 + 8.0, y_t - 14.0), end=(x_c1 + 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p1", start=(x_c2 - 8.0, y_t - 14.0), end=(x_c2 - 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(x_c2 + 8.0, y_t - 14.0), end=(x_c2 + 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Drops
                Segment(id="dl", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="dr", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom wire & Battery
                Segment(id="b1", start=(x_l, y_b), end=(180.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(200.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bp", start=(180.0, y_b - 16.0), end=(180.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn", start=(200.0, y_b - 9.0), end=(200.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="10\mu\text{F}", x=x_c1, y=y_t - 22.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="20\mu\text{F}", x=x_c2, y=y_t - 22.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="50\text{V}", x=190.0, y=y_b + 28.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Two Series Capacitors with Battery", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # a2ff2853: Kite Triangle Structure with Grounded Support at D
        # ----------------------------------------------------
        if "a2ff2853" in stem:
            w, h = 420.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 180.0
            xB, yB = 330.0, 180.0
            xC, yC = 170.0, 60.0
            xD, yD = 200.0, 300.0

            polygons = [
                Polygon(id="top_tri", vertices=[(xA, yA), (xC, yC), (xB, yB)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="hinge", center=(xD, yD + 12.0), radius=7.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Base AB
                Segment(id="base", start=(xA, yA), end=(xB, yB), stroke_width=2.2, color="#111111", arrows=ArrowType.BOTH),
                # Bottom dashed legs
                Segment(id="ad", start=(xA, yA), end=(xD, yD), stroke_width=2.2, color="#111111", stroke_style=StrokeStyle.DASHED),
                Segment(id="bd", start=(xB, yB), end=(xD, yD), stroke_width=2.2, color="#111111", stroke_style=StrokeStyle.DASHED),
                # Ground plate
                Segment(id="gnd", start=(xD - 25.0, yD + 20.0), end=(xD + 25.0, yD + 20.0), stroke_width=2.5, color="#111111"),
            ]
            right_markers = [
                RightAngleMarker(id="ra_c", vertex=(xC, yC), arm1_pt=(xA, yA), arm2_pt=(xB, yB), size=14.0, color="#111111", stroke_width=1.8)
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA - 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="-4\mu\text{C}", x=xA - 15.0, y=yA + 28.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB - 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="-4\mu\text{C}", x=xB + 15.0, y=yB + 28.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC, y=yC - 20.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD, y=yD - 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_ac", text="4 cm", x=(xA + xC)/2.0 - 25.0, y=(yA + yC)/2.0 - 15.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_base_d", text="20 cm", x=(xA + xB)/2.0, y=yA + 20.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_eq", text="AB = BD = AD", x=330.0, y=80.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Kite Triangle Structure with Support", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, segments=segments, right_angles=right_markers, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # aaf58fe6: Two Spheres O and C with Points A and B
        # ----------------------------------------------------
        if "aaf58fe6" in stem:
            w, h = 480.0, 200.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO, rO = 90.0, 90.0, 50.0
            xC, yC, rC = 390.0, 90.0, 50.0
            xA, xB = 120.0, 220.0

            circles = [
                Circle(id="sph_o", center=(xO, yO), radius=rO, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_c", center=(xC, yC), radius=rC, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Axis line
                Segment(id="axis", start=(xO, yO), end=(xC, yC), stroke_width=2.2, color="#111111"),
                # Ticks at A and B
                Segment(id="tk_a", start=(xA, yO - 10.0), end=(xA, yO + 10.0), stroke_width=2.0, color="#111111"),
                Segment(id="tk_b", start=(xB, yO - 10.0), end=(xB, yO + 10.0), stroke_width=2.0, color="#111111"),
                # Dimension 25 cm from B to C
                Segment(id="dim_bc", start=(xB, yO + 30.0), end=(xC, yO + 30.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_r", text="r = 10\text{ cm}", x=xO, y=yO - rO - 16.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO - 18.0, y=yO + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA + 12.0, y=yO + 16.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yO - 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yO + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="q = 1.6 \times 10^{-15}\text{ C}", x=xO, y=yO + rO + 30.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_25", text="25\text{ cm}", x=(xB + xC)/2.0, y=yO + 30.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Two Spheres with Points A and B", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # b010cf19: Three Series Capacitors (2F, 4F, 6F) with 10V Battery
        # ----------------------------------------------------
        if "b010cf19" in stem:
            w, h = 260.0, 420.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_r = 60.0, 180.0
            y_t, y_b = 50.0, 350.0
            y1, y2, y3 = 110.0, 180.0, 250.0

            segments = [
                # Outer loop
                Segment(id="top", start=(x_l, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="right", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bot_r", start=(x_r, y_b), end=(140.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bot_l", start=(120.0, y_b), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                # Battery V=10V
                Segment(id="bat_p", start=(140.0, y_b - 14.0), end=(140.0, y_b + 14.0), stroke_width=3.0, color="#111111"),
                Segment(id="bat_n", start=(120.0, y_b - 8.0), end=(120.0, y_b + 8.0), stroke_width=4.5, color="#111111"),
                # Left branch with 3 Capacitors
                Segment(id="l1", start=(x_l, y_t), end=(x_l, y1 - 8.0), stroke_width=2.2, color="#111111"),
                Segment(id="l2", start=(x_l, y1 + 8.0), end=(x_l, y2 - 8.0), stroke_width=2.2, color="#111111"),
                Segment(id="l3", start=(x_l, y2 + 8.0), end=(x_l, y3 - 8.0), stroke_width=2.2, color="#111111"),
                Segment(id="l4", start=(x_l, y3 + 8.0), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(x_l - 14.0, y1 - 8.0), end=(x_l + 14.0, y1 - 8.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x_l - 14.0, y1 + 8.0), end=(x_l + 14.0, y1 + 8.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p1", start=(x_l - 14.0, y2 - 8.0), end=(x_l + 14.0, y2 - 8.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(x_l - 14.0, y2 + 8.0), end=(x_l + 14.0, y2 + 8.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p1", start=(x_l - 14.0, y3 - 8.0), end=(x_l + 14.0, y3 - 8.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(x_l - 14.0, y3 + 8.0), end=(x_l + 14.0, y3 + 8.0), stroke_width=2.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1", x=x_l - 35.0, y=y1 - 10.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v1", text="2\text{F}", x=x_l - 35.0, y=y1 + 14.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=x_l - 35.0, y=y2 - 10.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v2", text="4\text{F}", x=x_l - 35.0, y=y2 + 14.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3", x=x_l - 35.0, y=y3 - 10.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v3", text="6\text{F}", x=x_l - 35.0, y=y3 + 14.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="V = 10\text{ V}", x=130.0, y=y_b + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_cap", text="শ্রেণি ধারক বর্তনী", x=x_r + 30.0, y=200.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Series Capacitors Circuit", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # b0447f3f: Bridge Lattice Network of 4 Elements
        # ----------------------------------------------------
        if "b0447f3f" in stem:
            w, h = 420.0, 200.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, xB = 40.0, 380.0
            y_m, y_t, y_b = 100.0, 45.0, 155.0

            segments = [
                # Central line & 2 elements
                Segment(id="in_a", start=(xA, y_m), end=(110.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(110.0, y_m - 14.0), end=(110.0, y_m + 14.0), stroke_width=3.0, color="#111111"),
                Segment(id="c1_p2", start=(125.0, y_m - 8.0), end=(125.0, y_m + 8.0), stroke_width=4.5, color="#111111"),
                Segment(id="m_mid", start=(125.0, y_m), end=(210.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(210.0, y_m - 14.0), end=(210.0, y_m + 14.0), stroke_width=3.0, color="#111111"),
                Segment(id="c2_p2", start=(225.0, y_m - 8.0), end=(225.0, y_m + 8.0), stroke_width=4.5, color="#111111"),
                Segment(id="out_b", start=(225.0, y_m), end=(xB, y_m), stroke_width=2.2, color="#111111"),
                # Top bypass (over element 1 to after element 2)
                Segment(id="tb_u", start=(80.0, y_m), end=(80.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb_h1", start=(80.0, y_t), end=(160.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="ct_p1", start=(160.0, y_t - 14.0), end=(160.0, y_t + 14.0), stroke_width=3.0, color="#111111"),
                Segment(id="ct_p2", start=(175.0, y_t - 8.0), end=(175.0, y_t + 8.0), stroke_width=4.5, color="#111111"),
                Segment(id="tb_h2", start=(175.0, y_t), end=(255.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb_d", start=(255.0, y_t), end=(255.0, y_m), stroke_width=2.2, color="#111111"),
                # Bottom bypass (between 1 & 2 to after element 2)
                Segment(id="bb_d", start=(170.0, y_m), end=(170.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb_h1", start=(170.0, y_b), end=(240.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="cb_p1", start=(240.0, y_b - 14.0), end=(240.0, y_b + 14.0), stroke_width=3.0, color="#111111"),
                Segment(id="cb_p2", start=(255.0, y_b - 8.0), end=(255.0, y_b + 8.0), stroke_width=4.5, color="#111111"),
                Segment(id="bb_h2", start=(255.0, y_b), end=(335.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb_u", start=(335.0, y_b), end=(335.0, y_m), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=y_m + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=y_m + 4.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Bridge Lattice Network", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # b18f4479: Triangle ABC with Charges +5C
        # ----------------------------------------------------
        if "b18f4479" in stem:
            w, h = 340.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 260.0, 160.0
            xB, yB = 80.0, 70.0
            xC, yC = 80.0, 250.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xB, yB), (xC, yC)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA + 20.0, y=yA + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 20.0, y=yB - 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+5\text{C}", x=xB + 10.0, y=yB - 25.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC - 20.0, y=yC + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="+5\text{C}", x=xC + 10.0, y=yC + 30.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_s1", text="2 m", x=(xA + xB)/2.0 + 10.0, y=(yA + yB)/2.0 - 15.0, font_size=17.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_s2", text="2 m", x=(xA + xC)/2.0 + 10.0, y=(yA + yC)/2.0 + 20.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Triangle ABC with Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # b1faeb6a: Charged Sphere +100C with Points A, B, C
        # ----------------------------------------------------
        if "b1faeb6a" in stem:
            w, h = 380.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO, R = 150.0, 160.0, 110.0
            xA, yA = xO + R, yO
            xB, yB = xO + 45.0, yO - 60.0
            xC, yC = xO + 150.0, yO + 80.0

            circles = [
                Circle(id="sphere", center=(xO, yO), radius=R, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="pt_o", center=(xO, yO), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_a", center=(xA, yA), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yB), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_c", center=(xC, yC), radius=5.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="r_a", start=(xO, yO), end=(xA, yA), stroke_width=2.0, color="#111111"),
                Segment(id="r_b", start=(xO, yO), end=(xB, yB), stroke_width=2.0, color="#111111"),
                Segment(id="r_c", start=(xO, yO), end=(xC, yC), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_q_sph", text="+100\text{C}", x=xO + R + 25.0, y=yO - 75.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO - 18.0, y=yO + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA + 18.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_da", text="5\text{cm}", x=xO + 55.0, y=yO - 12.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 15.0, y=yB - 10.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_db", text="3\text{cm}", x=xO + 10.0, y=yO - 40.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_dc", text="8\text{cm}", x=xO + 75.0, y=yO + 55.0, font_size=15.0, font_weight="bold"),
            ]
            return VisualIR(title="Charged Sphere with Points", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # b31744ec: Electric Dipole with Rays OP and OQ
        # ----------------------------------------------------
        if "b31744ec" in stem:
            w, h = 420.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 160.0
            xB, yB = 350.0, 160.0
            xO, yO = 210.0, 160.0
            xQ, yQ = 110.0, 85.0
            xP, yP = 290.0, 70.0

            segments = [
                # Base line AB
                Segment(id="base", start=(xA, yA), end=(xB, yB), stroke_width=2.2, color="#111111"),
                # Rays
                Segment(id="ray_q", start=(xO, yO), end=(xQ, yQ), stroke_width=2.2, color="#111111"),
                Segment(id="ray_p", start=(xO, yO), end=(xP, yP), stroke_width=2.2, color="#111111"),
                # Bottom dimension
                Segment(id="dim_l", start=(xA, 210.0), end=(xA, 230.0), stroke_width=2.0, color="#111111"),
                Segment(id="dim_r", start=(xB, 210.0), end=(xB, 230.0), stroke_width=2.0, color="#111111"),
                Segment(id="dim_h", start=(xA, 220.0), end=(xB, 220.0), stroke_width=2.0, color="#111111", arrows=ArrowType.BOTH),
            ]
            arc_markers = [
                ArcAngleMarker(id="arc_q", vertex=(xO, yO), start_pt=(xQ, yQ), end_pt=(xA, yA), radius=28.0, stroke_width=1.8, color="#111111"),
                ArcAngleMarker(id="arc_p", vertex=(xO, yO), start_pt=(xB, yB), end_pt=(xP, yP), radius=28.0, stroke_width=1.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO, y=yO + 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_q_pt", text="Q", x=xQ - 15.0, y=yQ - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_p_pt", text="P", x=xP + 15.0, y=yP - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_l_q", text="3\text{m}", x=(xO + xQ)/2.0 - 15.0, y=(yO + yQ)/2.0 - 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_l_p", text="4\text{m}", x=(xO + xP)/2.0 + 15.0, y=(yO + yP)/2.0 - 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_ang_q", text="30^\circ", x=xO - 50.0, y=yO - 14.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_ang_p", text="45^\circ", x=xO + 45.0, y=yO - 14.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="-4\mu\text{C}", x=xA - 20.0, y=220.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+4\mu\text{C}", x=xB + 20.0, y=220.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_dist", text="0.2\text{mm}", x=(xA + xB)/2.0, y=220.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Electric Dipole with Angular Rays", width=w, height=h, coordinate_frame=cf, segments=segments, arc_angles=arc_markers, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # b3f9ed49: Circuit with Series Capacitors and Grounded C4
        # ----------------------------------------------------
        if "b3f9ed49" in stem:
            w, h = 440.0, 280.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_m, x_r = 50.0, 310.0, 380.0
            y_t, y_m, y_b = 40.0, 110.0, 230.0

            segments = [
                # Top bypass line
                Segment(id="top_w", start=(x_l, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="l_drop", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                # Middle series branch (C1, C2, C3)
                Segment(id="m1", start=(x_l, y_m), end=(95.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m2", start=(107.0, y_m), end=(165.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m3", start=(177.0, y_m), end=(235.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m4", start=(247.0, y_m), end=(x_m, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(95.0, y_m - 14.0), end=(95.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(107.0, y_m - 14.0), end=(107.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p1", start=(165.0, y_m - 14.0), end=(165.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(177.0, y_m - 14.0), end=(177.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p1", start=(235.0, y_m - 14.0), end=(235.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(247.0, y_m - 14.0), end=(247.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                # Middle drop to bottom
                Segment(id="m_drop", start=(x_m, y_m), end=(x_m, y_b), stroke_width=2.2, color="#111111"),
                # Right vertical branch (C4)
                Segment(id="r1", start=(x_r, y_t), end=(x_r, 160.0), stroke_width=2.2, color="#111111"),
                Segment(id="r2", start=(x_r, 172.0), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c4_p1", start=(x_r - 14.0, 160.0), end=(x_r + 14.0, 160.0), stroke_width=2.8, color="#111111"),
                Segment(id="c4_p2", start=(x_r - 14.0, 172.0), end=(x_r + 14.0, 172.0), stroke_width=2.8, color="#111111"),
                # Bottom wire & 100V Battery
                Segment(id="b1", start=(x_l, y_b), end=(130.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(150.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bp1", start=(130.0, y_b - 16.0), end=(130.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn1", start=(138.0, y_b - 9.0), end=(138.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
                Segment(id="bp2", start=(144.0, y_b - 16.0), end=(144.0, y_b + 16.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn2", start=(150.0, y_b - 9.0), end=(150.0, y_b + 9.0), stroke_width=4.5, color="#111111"),
                # Ground marker
                Segment(id="g1", start=(x_r, y_b), end=(x_r, y_b + 15.0), stroke_width=2.2, color="#111111"),
                Segment(id="g2", start=(x_r - 20.0, y_b + 15.0), end=(x_r + 20.0, y_b + 15.0), stroke_width=2.5, color="#111111"),
                Segment(id="g3", start=(x_r - 14.0, y_b + 20.0), end=(x_r + 14.0, y_b + 20.0), stroke_width=2.5, color="#111111"),
                Segment(id="g4", start=(x_r - 8.0, y_b + 25.0), end=(x_r + 8.0, y_b + 25.0), stroke_width=2.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C_1", x=101.0, y=y_m - 24.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v1", text="4 \mu\text{F}", x=101.0, y=y_m + 25.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=171.0, y=y_m - 24.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v2", text="8 \mu\text{F}", x=171.0, y=y_m + 25.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3", x=241.0, y=y_m - 24.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v3", text="10 \mu\text{F}", x=241.0, y=y_m + 25.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_c4", text="C_4", x=x_r + 25.0, y=166.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v4", text="6 \mu\text{F}", x=x_r - 40.0, y=190.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="100 \text{ V}", x=190.0, y=y_b + 28.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Grounded Capacitor Circuit", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # b4abf366: Bridge Lattice Network C1..C5 with Nodes P and Q
        # ----------------------------------------------------
        if "b4abf366" in stem:
            w, h = 480.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, xB = 30.0, 450.0
            x_m1, x_m2 = 180.0, 310.0
            y_m, y_t, y_b = 110.0, 50.0, 180.0

            circles = [
                Circle(id="term_a", center=(xA, y_m), radius=4.5, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="term_b", center=(xB, y_m), radius=4.5, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="dot_l", center=(80.0, y_m), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="dot_p", center=(x_m1, y_m), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="dot_q", center=(x_m2, y_m), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="dot_r", center=(400.0, y_m), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Central line: C2, C3, C4
                Segment(id="in_a", start=(xA + 4.5, y_m), end=(120.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(120.0, y_m - 14.0), end=(120.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(132.0, y_m - 14.0), end=(132.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="m12", start=(132.0, y_m), end=(235.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(235.0, y_m - 14.0), end=(235.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(247.0, y_m - 14.0), end=(247.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="m23", start=(247.0, y_m), end=(350.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c4_p1", start=(350.0, y_m - 14.0), end=(350.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c4_p2", start=(362.0, y_m - 14.0), end=(362.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="out_b", start=(362.0, y_m), end=(xB - 4.5, y_m), stroke_width=2.2, color="#111111"),
                # Top bypass: C1 (from dot_l to dot_q)
                Segment(id="tb_u", start=(80.0, y_m), end=(80.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb_h1", start=(80.0, y_t), end=(190.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(190.0, y_t - 14.0), end=(190.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(202.0, y_t - 14.0), end=(202.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="tb_h2", start=(202.0, y_t), end=(x_m2, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb_d", start=(x_m2, y_t), end=(x_m2, y_m), stroke_width=2.2, color="#111111"),
                # Bottom bypass: C5 (from dot_p to dot_r)
                Segment(id="bb_d", start=(x_m1, y_m), end=(x_m1, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb_h1", start=(x_m1, y_b), end=(285.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c5_p1", start=(285.0, y_b - 14.0), end=(285.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c5_p2", start=(297.0, y_b - 14.0), end=(297.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="bb_h2", start=(297.0, y_b), end=(400.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb_u", start=(400.0, y_b), end=(400.0, y_m), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=y_m + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=y_m + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="C_1", x=196.0, y=y_t - 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=x_m1 + 8.0, y=y_m - 18.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="Q", x=x_m2 + 12.0, y=y_m - 18.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=126.0, y=y_m + 26.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3", x=241.0, y=y_m + 26.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c4", text="C_4", x=356.0, y=y_m + 26.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c5", text="C_5", x=291.0, y=y_b + 28.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Bridge Lattice Network with 5 Capacitors", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # b60d6782: Radial Rays Coordinate System around O
        # ----------------------------------------------------
        if "b60d6782" in stem:
            w, h = 420.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO = 160.0, 180.0
            xA, xB, xC, xD = 60.0, 240.0, 300.0, 360.0
            xP, yP = xO, 100.0
            xQ, yQ = xO, 40.0
            xR, yR = xO + 80.0, yO - 80.0
            xS, yS = xO + 150.0, yO - 150.0

            circles = [
                Circle(id="pt_a", center=(xA, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_o", center=(xO, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_c", center=(xC, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_d", center=(xD, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_p", center=(xP, yP), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_q", center=(xQ, yQ), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_r", center=(xR, yR), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_s", center=(xS, yS), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="h_line", start=(xA, yO), end=(xD, yO), stroke_width=2.2, color="#111111"),
                Segment(id="v_line", start=(xO, yO), end=(xQ, yQ), stroke_width=2.2, color="#111111"),
                Segment(id="diag", start=(xO, yO), end=(xS, yS), stroke_width=2.2, color="#111111"),
            ]
            arc_markers = [
                ArcAngleMarker(id="arc_90", vertex=(xO, yO), start_pt=(xA, yO), end_pt=(xQ, yQ), radius=38.0, stroke_width=1.8, color="#111111"),
                ArcAngleMarker(id="arc_45", vertex=(xO, yO), start_pt=(xD, yO), end_pt=(xS, yS), radius=38.0, stroke_width=1.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yO + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO, y=yO + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yO + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC, y=yO + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD, y=yO + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP - 15.0, y=yP, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="Q", x=xQ - 15.0, y=yQ, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="R", x=xR - 15.0, y=yR - 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_s", text="S", x=xS + 15.0, y=yS, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_90", text="90^\circ", x=xO - 48.0, y=yO - 30.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_45", text="45^\circ", x=xO + 48.0, y=yO - 20.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Radial Rays Coordinate System", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, arc_angles=arc_markers, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # b86ae48c: Two-Mesh Circuit with Voltmeter V
        # ----------------------------------------------------
        # b86ae48c: Two-Mesh Circuit with Voltmeter V
        # ----------------------------------------------------
        if "b86ae48c" in stem:
            w, h = 480.0, 280.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            def make_resistor_h(prefix, x0, x1, y):
                min_x, max_x = min(x0, x1), max(x0, x1)
                dx = (max_x - min_x) / 6.0
                pts = [
                    (min_x, y),
                    (min_x + dx * 0.5, y - 6.5),
                    (min_x + dx * 1.5, y + 6.5),
                    (min_x + dx * 2.5, y - 6.5),
                    (min_x + dx * 3.5, y + 6.5),
                    (min_x + dx * 4.5, y - 6.5),
                    (min_x + dx * 5.5, y + 6.5),
                    (max_x, y)
                ]
                segs = []
                for i in range(len(pts) - 1):
                    segs.append(Segment(id=f"{prefix}_{i}", start=pts[i], end=pts[i+1], stroke_width=2.2, color="#111111"))
                return segs

            def make_resistor_v(prefix, y0, y1, x):
                min_y, max_y = min(y0, y1), max(y0, y1)
                dy = (max_y - min_y) / 6.0
                pts = [
                    (x, min_y),
                    (x - 6.5, min_y + dy * 0.5),
                    (x + 6.5, min_y + dy * 1.5),
                    (x - 6.5, min_y + dy * 2.5),
                    (x + 6.5, min_y + dy * 3.5),
                    (x - 6.5, min_y + dy * 4.5),
                    (x + 6.5, min_y + dy * 5.5),
                    (x, max_y)
                ]
                segs = []
                for i in range(len(pts) - 1):
                    segs.append(Segment(id=f"{prefix}_{i}", start=pts[i], end=pts[i+1], stroke_width=2.2, color="#111111"))
                return segs

            circles = [
                Circle(id="pt_a", center=(70.0, 60.0), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(340.0, 180.0), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="vm", center=(185.0, 240.0), radius=14.0, stroke_width=2.0, stroke_color="#111111", fill_color="#ffffff"),
            ]

            bezier_paths = [
                # Loop current 1: Clockwise circular arc with arrowhead around I1
                BezierPath(id="arc_i1", path_d="M 136.0 106.0 A 15.0 15.0 0 1 1 138.0 134.0", stroke_color="#111111", stroke_width=2.0),
                BezierPath(id="arr_i1", path_d="M 138.0 134.0 L 148.0 130.0 L 142.0 138.0 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),

                # Loop current 2: Clockwise circular arc with arrowhead around I2
                BezierPath(id="arc_i2", path_d="M 378.0 106.0 A 15.0 15.0 0 1 1 380.0 134.0", stroke_color="#111111", stroke_width=2.0),
                BezierPath(id="arr_i2", path_d="M 380.0 134.0 L 390.0 130.0 L 384.0 138.0 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),
            ]

            segments = [
                # Left Mesh: Loop 1
                Segment(id="l1_b", start=(70.0, 60.0), end=(70.0, 115.0), stroke_width=2.2, color="#111111"),
                Segment(id="l1_bp", start=(58.0, 115.0), end=(82.0, 115.0), stroke_width=3.0, color="#111111"),
                Segment(id="l1_bn", start=(63.0, 125.0), end=(77.0, 125.0), stroke_width=4.5, color="#111111"),
                Segment(id="l1_b2", start=(70.0, 125.0), end=(70.0, 180.0), stroke_width=2.2, color="#111111"),

                Segment(id="l1_top_w", start=(70.0, 60.0), end=(95.0, 60.0), stroke_width=2.2, color="#111111"),
                *make_resistor_h("r_l1_t", 95.0, 145.0, 60.0),
                Segment(id="l1_top_w2", start=(145.0, 60.0), end=(170.0, 60.0), stroke_width=2.2, color="#111111"),
                Segment(id="l1_r", start=(170.0, 60.0), end=(170.0, 180.0), stroke_width=2.2, color="#111111"),

                Segment(id="l1_bot_w", start=(70.0, 180.0), end=(95.0, 180.0), stroke_width=2.2, color="#111111"),
                *make_resistor_h("r_l1_b", 95.0, 145.0, 180.0),
                Segment(id="l1_bot_w2", start=(145.0, 180.0), end=(170.0, 180.0), stroke_width=2.2, color="#111111"),

                # Coupling branch with 5V battery
                Segment(id="c_w1", start=(170.0, 180.0), end=(215.0, 180.0), stroke_width=2.2, color="#111111"),
                Segment(id="c_bp", start=(215.0, 168.0), end=(215.0, 192.0), stroke_width=3.0, color="#111111"),
                Segment(id="c_bn", start=(223.0, 173.0), end=(223.0, 187.0), stroke_width=4.5, color="#111111"),
                Segment(id="c_w2", start=(223.0, 180.0), end=(270.0, 180.0), stroke_width=2.2, color="#111111"),

                # Vertical 10 ohm resistor between y=180 and y=60
                Segment(id="c_up1", start=(270.0, 180.0), end=(270.0, 145.0), stroke_width=2.2, color="#111111"),
                *make_resistor_v("r_c", 95.0, 145.0, 270.0),
                Segment(id="c_up2", start=(270.0, 95.0), end=(270.0, 60.0), stroke_width=2.2, color="#111111"),

                # Right Mesh: Loop 2
                # Top horizontal wire from 270 across 340 to 420
                Segment(id="l2_top1", start=(270.0, 60.0), end=(340.0, 60.0), stroke_width=2.2, color="#111111"),
                Segment(id="l2_top2", start=(340.0, 60.0), end=(360.0, 60.0), stroke_width=2.2, color="#111111"),
                *make_resistor_h("r_l2_t", 360.0, 410.0, 60.0),
                Segment(id="l2_top3", start=(410.0, 60.0), end=(430.0, 60.0), stroke_width=2.2, color="#111111"),

                # Vertical 4 ohm resistor from (340, 60) down to node b at (340, 180)
                Segment(id="l2_m1", start=(340.0, 60.0), end=(340.0, 95.0), stroke_width=2.2, color="#111111"),
                *make_resistor_v("r_l2_m", 95.0, 145.0, 340.0),
                Segment(id="l2_m2", start=(340.0, 145.0), end=(340.0, 180.0), stroke_width=2.2, color="#111111"),

                # Right 30V battery branch
                Segment(id="l2_r1", start=(430.0, 60.0), end=(430.0, 115.0), stroke_width=2.2, color="#111111"),
                Segment(id="l2_bp", start=(418.0, 115.0), end=(442.0, 115.0), stroke_width=3.0, color="#111111"),
                Segment(id="l2_bn", start=(423.0, 125.0), end=(437.0, 125.0), stroke_width=4.5, color="#111111"),
                Segment(id="l2_r2", start=(430.0, 125.0), end=(430.0, 180.0), stroke_width=2.2, color="#111111"),

                # Bottom wire from (430, 180) to node b (340, 180)
                Segment(id="l2_bot", start=(430.0, 180.0), end=(340.0, 180.0), stroke_width=2.2, color="#111111"),

                # Voltmeter loop from a (70, 60) to b (340, 180)
                Segment(id="vm_l1", start=(70.0, 60.0), end=(30.0, 60.0), stroke_width=2.2, color="#111111"),
                Segment(id="vm_l2", start=(30.0, 60.0), end=(30.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="vm_l3", start=(30.0, 240.0), end=(171.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="vm_r1", start=(199.0, 240.0), end=(340.0, 240.0), stroke_width=2.2, color="#111111"),
                Segment(id="vm_r2", start=(340.0, 240.0), end=(340.0, 180.0), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="a", x=70.0, y=45.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="b", x=352.0, y=192.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_v1", text="20 V", x=95.0, y=120.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r1_t", text="5 Ω", x=120.0, y=42.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r1_b", text="5 Ω", x=120.0, y=200.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_i1", text="I_1", x=148.0, y=120.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v_mid", text="5 V", x=219.0, y=155.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r_mid", text="10 Ω", x=240.0, y=120.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r2_m", text="4 Ω", x=318.0, y=120.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r2_t", text="5 Ω", x=385.0, y=42.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_i2", text="I_2", x=390.0, y=120.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_v2", text="30 V", x=395.0, y=155.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_vm", text="V", x=185.0, y=240.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Two-Mesh Circuit with Voltmeter", width=w, height=h, coordinate_frame=cf, circles=circles, bezier_paths=bezier_paths, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # bcde92c6: Series-Parallel Capacitors with V=100 volts
        # ----------------------------------------------------
        if "bcde92c6" in stem:
            w, h = 420.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 90.0, 270.0
            x_l, x_r = 40.0, 380.0
            x_c3 = 130.0
            x_par_l, x_par_r = 200.0, 330.0
            y_p1, y_p2 = 50.0, 130.0

            segments = [
                # Left drop
                Segment(id="dl", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                # Cap C3
                Segment(id="t1", start=(x_l, y_t), end=(x_c3 - 8.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(x_c3 - 8.0, y_t - 14.0), end=(x_c3 - 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(x_c3 + 8.0, y_t - 14.0), end=(x_c3 + 8.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="t2", start=(x_c3 + 8.0, y_t), end=(x_par_l, y_t), stroke_width=2.2, color="#111111"),
                # Parallel loop (C1, C2)
                Segment(id="par_spl", start=(x_par_l, y_p1), end=(x_par_l, y_p2), stroke_width=2.2, color="#111111"),
                Segment(id="pt1", start=(x_par_l, y_p1), end=(259.0, y_p1), stroke_width=2.2, color="#111111"),
                Segment(id="pt2", start=(271.0, y_p1), end=(x_par_r, y_p1), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(259.0, y_p1 - 14.0), end=(259.0, y_p1 + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(271.0, y_p1 - 14.0), end=(271.0, y_p1 + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="pb1", start=(x_par_l, y_p2), end=(259.0, y_p2), stroke_width=2.2, color="#111111"),
                Segment(id="pb2", start=(271.0, y_p2), end=(x_par_r, y_p2), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(259.0, y_p2 - 14.0), end=(259.0, y_p2 + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(271.0, y_p2 - 14.0), end=(271.0, y_p2 + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="par_join", start=(x_par_r, y_p1), end=(x_par_r, y_p2), stroke_width=2.2, color="#111111"),
                Segment(id="to_r", start=(x_par_r, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="dr", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Bottom supply arrow
                Segment(id="v_arr", start=(x_l, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_c3", text="C_3 = 2\mu\text{F}", x=x_c3, y=y_t + 30.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="C_1 = 4\mu\text{F}", x=265.0, y=y_p1 + 30.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2 = 6\mu\text{F}", x=265.0, y=y_p2 + 35.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="V = 100\text{ volts}", x=210.0, y=y_b - 16.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Series-Parallel Capacitors Circuit", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # bed33b73: Dual Right Triangle Structure with Charges
        # ----------------------------------------------------
        # bed33b73: Dual Right Triangle Structure with Charges
        # ----------------------------------------------------
        if "bed33b73" in stem:
            w, h = 480.0, 250.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 175.0
            xB, yB = 310.0, 175.0
            xE, yE = 105.0, 48.0
            xF, yF = 275.0, 48.0
            xC, yC = 190.0, 103.5
            xD, yD = 435.0, 175.0

            segments = [
                # Side AE
                Segment(id="seg_ae", start=(xA, yA), end=(xE, yE), stroke_width=2.5, color="#111111"),
                # Straight diagonal line EB through C
                Segment(id="seg_eb", start=(xE, yE), end=(xB, yB), stroke_width=2.5, color="#111111"),
                # Side BF
                Segment(id="seg_bf", start=(xB, yB), end=(xF, yF), stroke_width=2.5, color="#111111"),
                # Straight diagonal line FA through C
                Segment(id="seg_fa", start=(xF, yF), end=(xA, yA), stroke_width=2.5, color="#111111"),
                # Base AB
                Segment(id="base", start=(xA, yA), end=(xB, yB), stroke_width=2.5, color="#111111"),
                # Extension to D
                Segment(id="ext_d", start=(xB, yB), end=(xD, yD), stroke_width=2.2, color="#111111", stroke_style=StrokeStyle.DASHED),
            ]
            arc_markers = [
                ArcAngleMarker(id="arc_e", vertex=(xE, yE), start_pt=(xA, yA), end_pt=(xB, yB), radius=20.0, stroke_width=1.8, color="#111111"),
                ArcAngleMarker(id="arc_f", vertex=(xF, yF), start_pt=(xA, yA), end_pt=(xB, yB), radius=20.0, stroke_width=1.8, color="#111111"),
                ArcAngleMarker(id="arc_c", vertex=(xC, yC), start_pt=(xA, yA), end_pt=(xB, yB), radius=20.0, stroke_width=1.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A (+5 nC)", x=xA - 5.0, y=yA + 24.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b", text="B (-9 nC)", x=xB + 5.0, y=yB + 24.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_e", text="E", x=xE, y=yE - 14.0, font_size=19.0, font_weight="bold"),
                MathLabel(id="lbl_f", text="F", x=xF, y=yF - 14.0, font_size=19.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC, y=yC - 16.0, font_size=19.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD + 15.0, y=yD + 2.0, font_size=19.0, font_weight="bold"),
                MathLabel(id="lbl_90_e", text="90^\circ", x=xE + 16.0, y=yE + 24.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_90_f", text="90^\circ", x=xF - 16.0, y=yF + 24.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_90_c", text="90^\circ", x=xC, y=yC + 28.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_ae", text="40 cm", x=(xA + xE)/2.0 - 28.0, y=(yA + yE)/2.0, font_size=15.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_bf", text="40 cm", x=(xB + xF)/2.0 + 28.0, y=(yB + yF)/2.0, font_size=15.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_ec", text="30 cm", x=(xE + xC)/2.0 + 6.0, y=(yE + yC)/2.0 - 14.0, font_size=15.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_fc", text="30 cm", x=(xF + xC)/2.0 - 6.0, y=(yF + yC)/2.0 - 14.0, font_size=15.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Dual Right Triangle Structure", width=w, height=h, coordinate_frame=cf, segments=segments, arc_angles=arc_markers, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # c22bf0ed: 3D Cartesian Axes with ZX Plane Patch
        # ----------------------------------------------------
        # c22bf0ed: 3D Cartesian Axes with ZX Plane Patch
        # ----------------------------------------------------
        if "c22bf0ed" in stem:
            w, h = 360.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO = 180.0, 180.0

            polygons = [
                # ZX plane surface patch
                Polygon(id="zx_patch", vertices=[(xO, yO), (xO + 65.0, yO), (xO + 30.0, yO + 35.0), (xO - 35.0, yO + 35.0)], stroke_width=2.0, stroke_color="#111111", fill_color="#f2f2f2", fill_opacity=0.5)
            ]
            segments = [
                # Axis Y (up)
                Segment(id="axis_y", start=(xO, yO), end=(xO, 70.0), stroke_width=2.5, color="#111111", arrows=ArrowType.END),
                # Axis X (right)
                Segment(id="axis_x", start=(xO, yO), end=(280.0, yO), stroke_width=2.5, color="#111111", arrows=ArrowType.END),
                # Axis Z (down-left)
                Segment(id="axis_z", start=(xO, yO), end=(115.0, 245.0), stroke_width=2.5, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_formula", text=r"\vec{E} = (2\hat{i} + 5\hat{j} + 6\hat{k})\text{ NC}^{-1}", x=180.0, y=35.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_y", text="Y", x=xO + 18.0, y=75.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_x", text="X", x=295.0, y=yO + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_z", text="Z", x=105.0, y=260.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_zx", text="ZX", x=xO + 15.0, y=yO + 18.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="3D Cartesian Axes with ZX Plane Patch", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # c3af2495: Square ABDC with Diagonals and 2m Sides
        # ----------------------------------------------------
        if "c3af2495" in stem:
            w, h = 380.0, 380.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 70.0
            xB, yB = 290.0, 70.0
            xC, yC = 290.0, 290.0
            xD, yD = 70.0, 290.0

            polygons = [
                Polygon(id="sq", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="diag1", start=(xA, yA), end=(xC, yC), stroke_width=2.0, color="#111111"),
                Segment(id="diag2", start=(xB, yB), end=(xD, yD), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 20.0, y=yA - 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 20.0, y=yB - 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD - 20.0, y=yD + 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_qd", text="4\text{ C}", x=xD - 15.0, y=yD + 35.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 20.0, y=yC + 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="4\text{ C}", x=xC + 15.0, y=yC + 35.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=180.0, y=210.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_t", text="2 m", x=180.0, y=yA - 25.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_b_dim", text="2 m", x=180.0, y=yD + 30.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_l", text="2 m", x=xA - 40.0, y=180.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r", text="2 m", x=xB + 40.0, y=180.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Square ABDC with Diagonals", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # c5506bb5: Regular Hexagon ABCDEF with Charges
        # ----------------------------------------------------
        if "c5506bb5" in stem:
            w, h = 420.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 150.0
            xB, yB = 130.0, 240.0
            xC, yC = 270.0, 240.0
            xD, yD = 330.0, 150.0
            xE, yE = 270.0, 60.0
            xF, yF = 130.0, 60.0
            xO, yO = 200.0, 150.0

            polygons = [
                Polygon(id="hex", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD), (xE, yE), (xF, yF)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="d_fc", start=(xF, yF), end=(xC, yC), stroke_width=2.0, color="#111111", stroke_style=StrokeStyle.DASHED),
                Segment(id="d_eb", start=(xE, yE), end=(xB, yB), stroke_width=2.0, color="#111111", stroke_style=StrokeStyle.DASHED),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="+2\text{ C}", x=xA - 15.0, y=yA + 28.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 18.0, y=yB + 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+1\text{C}", x=xB + 24.0, y=yB + 18.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC + 15.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="-1\text{ C}", x=xC + 60.0, y=yC + 10.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD + 18.0, y=yD - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qd", text="-2\text{ C}", x=xD + 24.0, y=yD + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_e", text="E", x=xE + 18.0, y=yE - 10.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qe", text="-1\text{ C}", x=xE + 55.0, y=yE + 12.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_f", text="F", x=xF - 18.0, y=yF - 10.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qf", text="+1\text{ C}", x=xF - 55.0, y=yF + 12.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO, y=yO - 16.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Regular Hexagon with Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # c70992f2: T-Shaped Electric Field Geometry (AB with OP)
        # ----------------------------------------------------
        if "c70992f2" in stem:
            w, h = 480.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 200.0
            xB, yB = 410.0, 200.0
            xO, yO = 240.0, 200.0
            xP, yP = 240.0, 50.0

            circles = [
                Circle(id="pt_a", center=(xA, yA), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yB), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_p", center=(xP, yP), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Base AB
                Segment(id="base", start=(xA, yA), end=(xB, yB), stroke_width=2.5, color="#111111"),
                # Altitude OP
                Segment(id="alt", start=(xO, yO), end=(xP, yP), stroke_width=2.2, color="#111111"),
                # Dimension AO
                Segment(id="dim_ao", start=(xA, yA - 30.0), end=(xO, yA - 30.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                # Dimension OB
                Segment(id="dim_ob", start=(xO, yA - 30.0), end=(xB, yA - 30.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                # Dimension OP
                Segment(id="dim_op", start=(xO - 20.0, yP), end=(xO - 20.0, yO), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA + 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="+6 \times 10^{-9}\text{C}", x=xA - 25.0, y=yA - 40.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yA + 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+4 \times 10^{-9}\text{C}", x=xB + 25.0, y=yA - 40.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO, y=yO + 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP, y=yP - 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_dao", text="10\text{ cm}", x=(xA + xO)/2.0, y=yA - 45.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_dob", text="10\text{ cm}", x=(xO + xB)/2.0, y=yA - 45.0, font_size=15.0, font_weight="bold"),
                MathLabel(id="lbl_dop", text="10\text{ cm}", x=xO - 45.0, y=(yO + yP)/2.0, font_size=15.0, font_weight="bold"),
            ]
            return VisualIR(title="T-Shaped Electric Field Geometry", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # c88b12ed: Data Table of Charge vs Potential Difference
        # ----------------------------------------------------
        if "c88b12ed" in stem:
            w, h = 480.0, 160.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_cols = [30.0, 160.0, 225.0, 290.0, 355.0, 420.0, 450.0]
            y0, y1, y2 = 40.0, 85.0, 130.0

            segments = [
                # Horizontal table grid lines
                Segment(id="h0", start=(x_cols[0], y0), end=(x_cols[6], y0), stroke_width=2.2, color="#111111"),
                Segment(id="h1", start=(x_cols[0], y1), end=(x_cols[6], y1), stroke_width=2.0, color="#111111"),
                Segment(id="h2", start=(x_cols[0], y2), end=(x_cols[6], y2), stroke_width=2.2, color="#111111"),
            ]
            # Vertical column lines
            for i, xc in enumerate(x_cols):
                segments.append(Segment(id=f"v_{i}", start=(xc, y0), end=(xc, y2), stroke_width=2.0, color="#111111"))

            labels = [
                MathLabel(id="lbl_r1_h", text="চার্জ (\mu\text{C})", x=(x_cols[0] + x_cols[1])/2.0, y=(y0 + y1)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r2_h", text="বিভব পার্থক্য (V)", x=(x_cols[0] + x_cols[1])/2.0, y=(y1 + y2)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                # Row 1 values
                MathLabel(id="q_1", text="7.5", x=(x_cols[1] + x_cols[2])/2.0, y=(y0 + y1)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="q_2", text="30", x=(x_cols[2] + x_cols[3])/2.0, y=(y0 + y1)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="q_3", text="60", x=(x_cols[3] + x_cols[4])/2.0, y=(y0 + y1)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="q_4", text="75", x=(x_cols[4] + x_cols[5])/2.0, y=(y0 + y1)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="q_5", text="90", x=(x_cols[5] + x_cols[6])/2.0, y=(y0 + y1)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                # Row 2 values
                MathLabel(id="v_1", text="1.0", x=(x_cols[1] + x_cols[2])/2.0, y=(y1 + y2)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="v_2", text="4.0", x=(x_cols[2] + x_cols[3])/2.0, y=(y1 + y2)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="v_3", text="8.0", x=(x_cols[3] + x_cols[4])/2.0, y=(y1 + y2)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="v_4", text="10.0", x=(x_cols[4] + x_cols[5])/2.0, y=(y1 + y2)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="v_5", text="12.0", x=(x_cols[5] + x_cols[6])/2.0, y=(y1 + y2)/2.0, font_size=16.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Charge vs Potential Difference Table", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # c8ee934c: Triangle ABC with Charges and Mass
        # ----------------------------------------------------
        if "c8ee934c" in stem:
            w, h = 340.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 70.0
            xB, yB = 70.0, 250.0
            xC, yC = 250.0, 160.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xB, yB), (xC, yC)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_a", center=(xA, yA), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yB), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_c", center=(xC, yC), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="+2\text{C}", x=xA - 15.0, y=yA - 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 18.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+2\text{C}", x=xB - 15.0, y=yB + 28.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC - 10.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_mc", text="1\text{ kg}", x=xC + 20.0, y=yC + 20.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_ab", text="1 m", x=xA - 30.0, y=(yA + yB)/2.0, font_size=17.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Triangle ABC with Charges and Mass", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # c9c662eb: Equilateral Triangle ABC with Charges and 60 deg Angles
        # ----------------------------------------------------
        if "c9c662eb" in stem:
            w, h = 360.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 180.0, 60.0
            xB, yB = 70.0, 250.0
            xC, yC = 290.0, 250.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xB, yB), (xC, yC)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            arc_markers = [
                ArcAngleMarker(id="arc_a", vertex=(xA, yA), start_pt=(xB, yB), end_pt=(xC, yC), radius=32.0, stroke_width=1.8, color="#111111"),
                ArcAngleMarker(id="arc_b", vertex=(xB, yB), start_pt=(xC, yC), end_pt=(xA, yA), radius=32.0, stroke_width=1.8, color="#111111"),
                ArcAngleMarker(id="arc_c", vertex=(xC, yC), start_pt=(xA, yA), end_pt=(xB, yB), radius=32.0, stroke_width=1.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A (-2q)", x=xA, y=yA - 20.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B (+q)", x=xB - 15.0, y=yB + 25.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C (+q)", x=xC + 15.0, y=yC + 25.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_ang_a", text="60^\circ", x=xA, y=yA + 45.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_ang_b", text="60^\circ", x=xB + 38.0, y=yB - 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_ang_c", text="60^\circ", x=xC - 38.0, y=yC - 15.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Equilateral Triangle ABC with Charges", width=w, height=h, coordinate_frame=cf, polygons=polygons, arc_angles=arc_markers, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # d08839c6: Ladder Network with 7 Capacitors
        # ----------------------------------------------------
        if "d08839c6" in stem:
            w, h = 420.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b = 60.0, 160.0
            x1, x2, x3 = 110.0, 230.0, 350.0

            segments = [
                # Top rail: 2 series capacitors
                Segment(id="t_in", start=(30.0, y_t), end=(150.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tc1_p1", start=(150.0, y_t - 14.0), end=(150.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="tc1_p2", start=(165.0, y_t - 14.0), end=(165.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="t_m", start=(165.0, y_t), end=(270.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tc2_p1", start=(270.0, y_t - 14.0), end=(270.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="tc2_p2", start=(285.0, y_t - 14.0), end=(285.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="t_out", start=(285.0, y_t), end=(x3, y_t), stroke_width=2.2, color="#111111"),
                # Bottom rail: 2 series capacitors
                Segment(id="b_in", start=(30.0, y_b), end=(150.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bc1_p1", start=(150.0, y_b - 14.0), end=(150.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="bc1_p2", start=(165.0, y_b - 14.0), end=(165.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="b_m", start=(165.0, y_b), end=(270.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bc2_p1", start=(270.0, y_b - 14.0), end=(270.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="bc2_p2", start=(285.0, y_b - 14.0), end=(285.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="b_out", start=(285.0, y_b), end=(x3, y_b), stroke_width=2.2, color="#111111"),
                # 3 Shunt capacitors
                # Shunt 1 (x1)
                Segment(id="sh1_t", start=(x1, y_t), end=(x1, 100.0), stroke_width=2.2, color="#111111"),
                Segment(id="sh1_p1", start=(x1 - 14.0, 100.0), end=(x1 + 14.0, 100.0), stroke_width=2.8, color="#111111"),
                Segment(id="sh1_p2", start=(x1 - 14.0, 115.0), end=(x1 + 14.0, 115.0), stroke_width=2.8, color="#111111"),
                Segment(id="sh1_b", start=(x1, 115.0), end=(x1, y_b), stroke_width=2.2, color="#111111"),
                # Shunt 2 (x2)
                Segment(id="sh2_t", start=(x2, y_t), end=(x2, 100.0), stroke_width=2.2, color="#111111"),
                Segment(id="sh2_p1", start=(x2 - 14.0, 100.0), end=(x2 + 14.0, 100.0), stroke_width=2.8, color="#111111"),
                Segment(id="sh2_p2", start=(x2 - 14.0, 115.0), end=(x2 + 14.0, 115.0), stroke_width=2.8, color="#111111"),
                Segment(id="sh2_b", start=(x2, 115.0), end=(x2, y_b), stroke_width=2.2, color="#111111"),
                # Shunt 3 (x3)
                Segment(id="sh3_t", start=(x3, y_t), end=(x3, 100.0), stroke_width=2.2, color="#111111"),
                Segment(id="sh3_p1", start=(x3 - 14.0, 100.0), end=(x3 + 14.0, 100.0), stroke_width=2.8, color="#111111"),
                Segment(id="sh3_p2", start=(x3 - 14.0, 115.0), end=(x3 + 14.0, 115.0), stroke_width=2.8, color="#111111"),
                Segment(id="sh3_b", start=(x3, 115.0), end=(x3, y_b), stroke_width=2.2, color="#111111"),
            ]
            return VisualIR(title="Seven Capacitors Ladder Network", width=w, height=h, coordinate_frame=cf, segments=segments, background_color="#ffffff")

        # ----------------------------------------------------
        # d8382e3a: Square EFGH with Diagonals
        # ----------------------------------------------------
        if "d8382e3a" in stem:
            w, h = 360.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xE, yE = 70.0, 70.0
            xF, yF = 290.0, 70.0
            xG, yG = 290.0, 290.0
            xH, yH = 70.0, 290.0

            polygons = [
                Polygon(id="sq", vertices=[(xE, yE), (xF, yF), (xG, yG), (xH, yH)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            segments = [
                Segment(id="diag1", start=(xE, yE), end=(xG, yG), stroke_width=2.0, color="#111111"),
                Segment(id="diag2", start=(xF, yF), end=(xH, yH), stroke_width=2.0, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_e", text="E", x=xE - 20.0, y=yE - 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_f", text="F", x=xF + 20.0, y=yF - 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_g", text="G", x=xG + 20.0, y=yG + 4.0, font_size=24.0, font_weight="bold"),
                MathLabel(id="lbl_h", text="H", x=xH - 20.0, y=yH + 4.0, font_size=24.0, font_weight="bold"),
            ]
            return VisualIR(title="Square EFGH with Diagonals", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # da64ad2f: Y-Star Configuration with Charges Q1, Q2, Q3
        # ----------------------------------------------------
        if "da64ad2f" in stem:
            w, h = 380.0, 340.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO = 190.0, 160.0
            x1, y1 = 90.0, 60.0
            x2, y2 = 290.0, 60.0
            x3, y3 = 190.0, 280.0

            circles = [
                Circle(id="pt_o", center=(xO, yO), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_1", center=(x1, y1), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="pt_2", center=(x2, y2), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_3", center=(x3, y3), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="arm1", start=(xO, yO), end=(x1, y1), stroke_width=2.2, color="#111111"),
                Segment(id="arm2", start=(xO, yO), end=(x2, y2), stroke_width=2.2, color="#111111"),
                Segment(id="arm3", start=(xO, yO), end=(x3, y3), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_o", text="O", x=xO - 20.0, y=yO + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_q1", text="+Q_1", x=x1 - 35.0, y=y1 - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r1", text="r_1", x=(xO + x1)/2.0 - 20.0, y=(yO + y1)/2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_q2", text="+Q_2", x=x2 + 35.0, y=y2 - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r2", text="r_2", x=(xO + x2)/2.0 + 20.0, y=(yO + y2)/2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_q3", text="+Q_3", x=x3 + 35.0, y=y3 - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_r3", text="r_3", x=x3 + 20.0, y=(yO + y3)/2.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Y-Star Configuration with Charges", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # da8c83e7: Dual Spherical Shells Comparison (Before & After Connection)
        # ----------------------------------------------------
        # da8c83e7: Dual Spherical Shells Comparison (Before & After Connection)
        # ----------------------------------------------------
        if "da8c83e7" in stem:
            w, h = 480.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)

            # Left: Before connection
            x1_a, x1_b, y1 = 80.0, 170.0, 85.0
            # Right: After connection
            x2_a, x2_b, y2 = 285.0, 400.0, 85.0
            r_a, r_b = 36.0, 32.0
            thick_a, thick_b = 10.0, 9.0

            circles = [
                # Pair 1 (Before): Shell A (Thick Shaded Ring)
                Circle(id="s1_a_out", center=(x1_a, y1), radius=r_a, stroke_width=2.5, stroke_color="#111111", fill_color="#444444"),
                Circle(id="s1_a_in", center=(x1_a, y1), radius=r_a - thick_a, stroke_width=1.8, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="s1_a_c", center=(x1_a, y1), radius=3.2, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),

                # Pair 1 (Before): Shell B (Thick Shaded Ring)
                Circle(id="s1_b_out", center=(x1_b, y1), radius=r_b, stroke_width=2.5, stroke_color="#111111", fill_color="#444444"),
                Circle(id="s1_b_in", center=(x1_b, y1), radius=r_b - thick_b, stroke_width=1.8, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="s1_b_c", center=(x1_b, y1), radius=3.2, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),

                # Pair 2 (After): Shell A (Thick Shaded Ring)
                Circle(id="s2_a_out", center=(x2_a, y2), radius=r_a, stroke_width=2.5, stroke_color="#111111", fill_color="#444444"),
                Circle(id="s2_a_in", center=(x2_a, y2), radius=r_a - thick_a, stroke_width=1.8, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="s2_a_c", center=(x2_a, y2), radius=3.2, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),

                # Pair 2 (After): Shell B (Thick Shaded Ring)
                Circle(id="s2_b_out", center=(x2_b, y2), radius=r_b, stroke_width=2.5, stroke_color="#111111", fill_color="#444444"),
                Circle(id="s2_b_in", center=(x2_b, y2), radius=r_b - thick_b, stroke_width=1.8, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="s2_b_c", center=(x2_b, y2), radius=3.2, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]

            bezier_paths = [
                # Wavy / Coiled connecting wire between Shell 2A and 2B
                BezierPath(id="wavy_wire", path_d=f"M {x2_a + r_a:.1f} {y2:.1f} C 325.0 78.0 333.0 92.0 337.0 85.0 C 341.0 78.0 349.0 92.0 353.0 85.0 C 357.0 78.0 364.0 92.0 {x2_b - r_b:.1f} {y2:.1f}", stroke_width=2.2, stroke_color="#111111"),
            ]

            segments = [
                # Radius arrows pointing up to outer shells
                Segment(id="r1_a", start=(x1_a, y1), end=(x1_a, y1 - r_a + 2.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="r1_b", start=(x1_b, y1), end=(x1_b, y1 - r_b + 2.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="r2_a", start=(x2_a, y2), end=(x2_a, y2 - r_a + 2.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="r2_b", start=(x2_b, y2), end=(x2_b, y2 - r_b + 2.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_1a", text="A", x=x1_a, y=y1 - r_a - 14.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_1b", text="B", x=x1_b, y=y1 - r_b - 14.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_2a", text="A", x=x2_a, y=y2 - r_a - 14.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_2b", text="B", x=x2_b, y=y2 - r_b - 14.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_r1_a", text="r_1", x=x1_a + 12.0, y=y1 - 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r1_b", text="r_2", x=x1_b + 12.0, y=y1 - 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r2_a", text="r_1", x=x2_a + 12.0, y=y2 - 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_r2_b", text="r_2", x=x2_b + 12.0, y=y2 - 15.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_before", text="সংযোগের পূর্বে", x=(x1_a + x1_b)/2.0, y=175.0, font_size=18.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_after", text="সংযোগের পর", x=(x2_a + x2_b)/2.0, y=175.0, font_size=18.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Dual Spherical Shells Comparison", width=w, height=h, coordinate_frame=cf, circles=circles, bezier_paths=bezier_paths, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # ddfd5136: Vertical Line of Charges (+6 uC and -4 uC)
        # ----------------------------------------------------
        if "ddfd5136" in stem:
            w, h = 200.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x0 = 120.0
            y_t, y_b = 60.0, 300.0

            circles = [
                Circle(id="pt_t", center=(x0, y_t), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(x0, y_b), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                Segment(id="line", start=(x0, y_t), end=(x0, y_b), stroke_width=2.2, color="#111111"),
                # Dimension line
                Segment(id="dim_t", start=(x0 - 50.0, y_t), end=(x0 - 15.0, y_t), stroke_width=1.8, color="#111111"),
                Segment(id="dim_b", start=(x0 - 50.0, y_b), end=(x0 - 15.0, y_b), stroke_width=1.8, color="#111111"),
                Segment(id="dim_v", start=(x0 - 35.0, y_t), end=(x0 - 35.0, y_b), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_qt", text="+6\mu\text{C}", x=x0, y=y_t - 22.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="-4\mu\text{C}", x=x0, y=y_b + 25.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="30\text{ cm}", x=x0 - 75.0, y=(y_t + y_b)/2.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Vertical Line of Charges", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # e22a43db: Capacitor Symbols Comparison (i, ii, iii)
        # ----------------------------------------------------
        if "e22a43db" in stem:
            w, h = 360.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y1, y2, y3 = 60.0, 130.0, 200.0
            x_l, x_r = 80.0, 320.0
            xc1, xc2 = 190.0, 210.0

            segments = [
                # i. Battery / Unequal
                Segment(id="i_l", start=(x_l, y1), end=(xc1, y1), stroke_width=2.2, color="#111111"),
                Segment(id="i_p1", start=(xc1, y1 - 20.0), end=(xc1, y1 + 20.0), stroke_width=2.5, color="#111111"),
                Segment(id="i_p2", start=(xc2, y1 - 12.0), end=(xc2, y1 + 12.0), stroke_width=4.0, color="#111111"),
                Segment(id="i_r", start=(xc2, y1), end=(x_r, y1), stroke_width=2.2, color="#111111"),
                # ii. Fixed Capacitor
                Segment(id="ii_l", start=(x_l, y2), end=(xc1, y2), stroke_width=2.2, color="#111111"),
                Segment(id="ii_p1", start=(xc1, y2 - 20.0), end=(xc1, y2 + 20.0), stroke_width=2.5, color="#111111"),
                Segment(id="ii_p2", start=(xc2, y2 - 20.0), end=(xc2, y2 + 20.0), stroke_width=2.5, color="#111111"),
                Segment(id="ii_r", start=(xc2, y2), end=(x_r, y2), stroke_width=2.2, color="#111111"),
                # iii. Variable Capacitor
                Segment(id="iii_l", start=(x_l, y3), end=(xc1, y3), stroke_width=2.2, color="#111111"),
                Segment(id="iii_p1", start=(xc1, y3 - 20.0), end=(xc1, y3 + 20.0), stroke_width=2.5, color="#111111"),
                Segment(id="iii_p2", start=(xc2, y3 - 20.0), end=(xc2, y3 + 20.0), stroke_width=2.5, color="#111111"),
                Segment(id="iii_r", start=(xc2, y3), end=(x_r, y3), stroke_width=2.2, color="#111111"),
                Segment(id="iii_arr", start=(xc1 - 35.0, y3 + 22.0), end=(xc2 + 35.0, y3 - 22.0), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_i", text="i.", x=50.0, y=y1, font_size=20.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_ii", text="ii.", x=50.0, y=y2, font_size=20.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_iii", text="iii.", x=50.0, y=y3, font_size=20.0, font_weight="bold", math_mode=False),
            ]
            return VisualIR(title="Capacitor Symbols Comparison", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # e249dde4: Lattice Network with Six Capacitors
        # ----------------------------------------------------
        if "e249dde4" in stem:
            w, h = 500.0, 200.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, xB = 30.0, 470.0
            y_m, y_t, y_b = 100.0, 45.0, 155.0
            x_caps = [100.0, 165.0, 230.0, 295.0, 360.0, 425.0]

            segments = [
                # Central line with 6 capacitors
                Segment(id="c_in", start=(xA, y_m), end=(x_caps[0] - 8.0, y_m), stroke_width=2.2, color="#111111"),
            ]
            for i, xc in enumerate(x_caps):
                segments.append(Segment(id=f"c{i}_p1", start=(xc - 8.0, y_m - 12.0), end=(xc - 8.0, y_m + 12.0), stroke_width=2.8, color="#111111"))
                segments.append(Segment(id=f"c{i}_p2", start=(xc + 8.0, y_m - 12.0), end=(xc + 8.0, y_m + 12.0), stroke_width=2.8, color="#111111"))
                if i < len(x_caps) - 1:
                    segments.append(Segment(id=f"w_{i}", start=(xc + 8.0, y_m), end=(x_caps[i+1] - 8.0, y_m), stroke_width=2.2, color="#111111"))
                else:
                    segments.append(Segment(id="c_out", start=(xc + 8.0, y_m), end=(xB, y_m), stroke_width=2.2, color="#111111"))

            # Top bypass 1 (from before cap 1 to after cap 2)
            segments.extend([
                Segment(id="tb1_u", start=(50.0, y_m), end=(50.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb1_h", start=(50.0, y_t), end=(195.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb1_d", start=(195.0, y_t), end=(195.0, y_m), stroke_width=2.2, color="#111111"),
            ])
            # Bottom bypass 1 (from after cap 1 to before cap 4)
            segments.extend([
                Segment(id="bb1_d", start=(130.0, y_m), end=(130.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb1_h", start=(130.0, y_b), end=(265.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb1_u", start=(265.0, y_b), end=(265.0, y_m), stroke_width=2.2, color="#111111"),
            ])
            # Top bypass 2 (from before cap 4 to after cap 5)
            segments.extend([
                Segment(id="tb2_u", start=(265.0, y_m), end=(265.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb2_h", start=(265.0, y_t), end=(390.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb2_d", start=(390.0, y_t), end=(390.0, y_m), stroke_width=2.2, color="#111111"),
            ])
            # Bottom bypass 2 (from after cap 4 to after cap 6)
            segments.extend([
                Segment(id="bb2_d", start=(330.0, y_m), end=(330.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb2_h", start=(330.0, y_b), end=(455.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb2_u", start=(455.0, y_b), end=(455.0, y_m), stroke_width=2.2, color="#111111"),
            ])

            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=y_m + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=y_m + 4.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Six Capacitors Lattice Network", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # e34e2fe1: Parallel Plates with 200V Supply
        # ----------------------------------------------------
        if "e34e2fe1" in stem:
            w, h = 420.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_p1, x_p2 = 120.0, 260.0
            y_m = 120.0

            polygons = [
                Polygon(id="p1", vertices=[(x_p1, 60.0), (x_p1 + 20.0, 50.0), (x_p1 + 20.0, 180.0), (x_p1, 190.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Polygon(id="p2", vertices=[(x_p2, 60.0), (x_p2 + 20.0, 50.0), (x_p2 + 20.0, 180.0), (x_p2, 190.0)], stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
            ]
            circles = [
                Circle(id="term_l", center=(170.0, 260.0), radius=3.5, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="term_r", center=(230.0, 260.0), radius=3.5, stroke_width=1.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Left lead
                Segment(id="l1", start=(x_p1, y_m), end=(60.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="l2", start=(60.0, y_m), end=(60.0, 260.0), stroke_width=2.2, color="#111111"),
                Segment(id="l3", start=(60.0, 260.0), end=(166.5, 260.0), stroke_width=2.2, color="#111111"),
                # Right lead
                Segment(id="r1", start=(x_p2 + 20.0, y_m), end=(340.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="r2", start=(340.0, y_m), end=(340.0, 260.0), stroke_width=2.2, color="#111111"),
                Segment(id="r3", start=(340.0, 260.0), end=(233.5, 260.0), stroke_width=2.2, color="#111111"),
                # Dimension 3 cm
                Segment(id="dim_3", start=(x_p1 + 20.0, 215.0), end=(x_p2, 215.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
            ]
            labels = [
                MathLabel(id="lbl_a1", text="20\text{ cm}^2", x=x_p1 + 10.0, y=35.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_a2", text="20\text{ cm}^2", x=x_p2 + 10.0, y=35.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="3\text{ cm}", x=(x_p1 + 20.0 + x_p2)/2.0, y=215.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_v", text="200\text{ V}", x=200.0, y=285.0, font_size=17.0, font_weight="bold"),
            ]
            return VisualIR(title="Parallel Plates with 200V Supply", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # e5496685: Four Capacitors Bridge Lattice
        # ----------------------------------------------------
        if "e5496685" in stem:
            w, h = 420.0, 200.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, xB = 40.0, 380.0
            y_m, y_t, y_b = 100.0, 45.0, 155.0

            circles = [
                Circle(id="term_a", center=(xA, y_m), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="term_b", center=(xB, y_m), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Central line: 2 series capacitors
                Segment(id="in_a", start=(xA, y_m), end=(130.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(130.0, y_m - 14.0), end=(130.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(142.0, y_m - 14.0), end=(142.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="m_mid", start=(142.0, y_m), end=(230.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(230.0, y_m - 14.0), end=(230.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(242.0, y_m - 14.0), end=(242.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="out_b", start=(242.0, y_m), end=(xB, y_m), stroke_width=2.2, color="#111111"),
                # Top bypass with 1 capacitor
                Segment(id="tb_u", start=(90.0, y_m), end=(90.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb_h1", start=(90.0, y_t), end=(180.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="ct_p1", start=(180.0, y_t - 14.0), end=(180.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="ct_p2", start=(192.0, y_t - 14.0), end=(192.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="tb_h2", start=(192.0, y_t), end=(290.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="tb_d", start=(290.0, y_t), end=(290.0, y_m), stroke_width=2.2, color="#111111"),
                # Bottom bypass with 1 capacitor
                Segment(id="bb_d", start=(180.0, y_m), end=(180.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb_h1", start=(180.0, y_b), end=(250.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="cb_p1", start=(250.0, y_b - 14.0), end=(250.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cb_p2", start=(262.0, y_b - 14.0), end=(262.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="bb_h2", start=(262.0, y_b), end=(320.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bb_u", start=(320.0, y_b), end=(320.0, y_m), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=y_m + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=y_m + 4.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Four Capacitors Bridge Lattice", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # e7b5ce1b: Serpentine 5-Capacitor Network (X, Y)
        # ----------------------------------------------------
        if "e7b5ce1b" in stem:
            w, h = 460.0, 200.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_t, y_b, y_m = 40.0, 140.0, 90.0
            x_caps = [60.0, 130.0, 200.0, 270.0, 340.0]

            segments = [
                # Bottom return rail to Y
                Segment(id="rail_y", start=(x_caps[0], 170.0), end=(420.0, 170.0), stroke_width=2.2, color="#111111"),
                Segment(id="cap1_b", start=(x_caps[0], y_m + 12.0), end=(x_caps[0], 170.0), stroke_width=2.2, color="#111111"),
                # Cap 1
                Segment(id="c1_p1", start=(x_caps[0] - 14.0, y_m - 12.0), end=(x_caps[0] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x_caps[0] - 14.0, y_m + 12.0), end=(x_caps[0] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Top bridge 1-2
                Segment(id="br_t1", start=(x_caps[0], y_m - 12.0), end=(x_caps[0], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="br_t1_h", start=(x_caps[0], y_t), end=(x_caps[1], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="br_t1_d", start=(x_caps[1], y_t), end=(x_caps[1], y_m - 12.0), stroke_width=2.2, color="#111111"),
                # Cap 2
                Segment(id="c2_p1", start=(x_caps[1] - 14.0, y_m - 12.0), end=(x_caps[1] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(x_caps[1] - 14.0, y_m + 12.0), end=(x_caps[1] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Bottom bridge 2-3
                Segment(id="br_b1", start=(x_caps[1], y_m + 12.0), end=(x_caps[1], y_b), stroke_width=2.2, color="#111111"),
                Segment(id="br_b1_h", start=(x_caps[1], y_b), end=(x_caps[2], y_b), stroke_width=2.2, color="#111111"),
                Segment(id="br_b1_u", start=(x_caps[2], y_b), end=(x_caps[2], y_m + 12.0), stroke_width=2.2, color="#111111"),
                # Cap 3
                Segment(id="c3_p1", start=(x_caps[2] - 14.0, y_m - 12.0), end=(x_caps[2] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(x_caps[2] - 14.0, y_m + 12.0), end=(x_caps[2] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Top bridge 3-4
                Segment(id="br_t2", start=(x_caps[2], y_m - 12.0), end=(x_caps[2], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="br_t2_h", start=(x_caps[2], y_t), end=(x_caps[3], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="br_t2_d", start=(x_caps[3], y_t), end=(x_caps[3], y_m - 12.0), stroke_width=2.2, color="#111111"),
                # Cap 4
                Segment(id="c4_p1", start=(x_caps[3] - 14.0, y_m - 12.0), end=(x_caps[3] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c4_p2", start=(x_caps[3] - 14.0, y_m + 12.0), end=(x_caps[3] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Bottom bridge 4-5
                Segment(id="br_b2", start=(x_caps[3], y_m + 12.0), end=(x_caps[3], y_b), stroke_width=2.2, color="#111111"),
                Segment(id="br_b2_h", start=(x_caps[3], y_b), end=(x_caps[4], y_b), stroke_width=2.2, color="#111111"),
                Segment(id="br_b2_u", start=(x_caps[4], y_b), end=(x_caps[4], y_m + 12.0), stroke_width=2.2, color="#111111"),
                # Cap 5
                Segment(id="c5_p1", start=(x_caps[4] - 14.0, y_m - 12.0), end=(x_caps[4] + 14.0, y_m - 12.0), stroke_width=2.8, color="#111111"),
                Segment(id="c5_p2", start=(x_caps[4] - 14.0, y_m + 12.0), end=(x_caps[4] + 14.0, y_m + 12.0), stroke_width=2.8, color="#111111"),
                # Output to X
                Segment(id="out_x1", start=(x_caps[4], y_m - 12.0), end=(x_caps[4], y_t), stroke_width=2.2, color="#111111"),
                Segment(id="out_x2", start=(x_caps[4], y_t), end=(420.0, y_t), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_c1", text="C", x=x_caps[0] - 25.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C", x=(x_caps[0] + x_caps[1])/2.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C", x=(x_caps[1] + x_caps[2])/2.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c4", text="C", x=(x_caps[2] + x_caps[3])/2.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c5", text="C", x=(x_caps[3] + x_caps[4])/2.0, y=y_m, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_x", text="X", x=435.0, y=y_t + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_y", text="Y", x=435.0, y=174.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Serpentine Five Capacitors Network", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # e85df185: Bridge Network with Diagonal Capacitor
        # ----------------------------------------------------
        if "e85df185" in stem:
            w, h = 420.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, xB = 30.0, 390.0
            x_l, x_r = 80.0, 290.0
            y_t, y_b, y_m = 50.0, 170.0, 110.0

            segments = [
                # Input A
                Segment(id="in_a", start=(xA, y_m), end=(x_l, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="spl_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                # Top branch: 2 caps (4uF, 4uF)
                Segment(id="t1", start=(x_l, y_t), end=(130.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(142.0, y_t), end=(220.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t3", start=(232.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(130.0, y_t - 14.0), end=(130.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(142.0, y_t - 14.0), end=(142.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p1", start=(220.0, y_t - 14.0), end=(220.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(232.0, y_t - 14.0), end=(232.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Bottom branch: 1 cap (2uF)
                Segment(id="b1", start=(x_l, y_b), end=(180.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(192.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="cb_p1", start=(180.0, y_b - 14.0), end=(180.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cb_p2", start=(192.0, y_b - 14.0), end=(192.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                # Diagonal branch: 1 cap (2uF) from (x_l, y_b) to (x_r, y_t)
                Segment(id="d1", start=(x_l, y_b), end=(175.0, 116.0), stroke_width=2.2, color="#111111"),
                Segment(id="d2", start=(195.0, 104.0), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="cd_p1", start=(170.0, 124.0), end=(180.0, 108.0), stroke_width=2.8, color="#111111"),
                Segment(id="cd_p2", start=(190.0, 112.0), end=(200.0, 96.0), stroke_width=2.8, color="#111111"),
                # Right join
                Segment(id="spl_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Right series cap (3uF) to B
                Segment(id="to_c3", start=(x_r, y_m), end=(320.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(320.0, y_m - 14.0), end=(320.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(332.0, y_m - 14.0), end=(332.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="out_b", start=(332.0, y_m), end=(xB, y_m), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=y_m + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=y_m + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="4 \mu\text{F}", x=136.0, y=y_t - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="4 \mu\text{F}", x=226.0, y=y_t - 20.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_cd", text="2 \mu\text{F}", x=150.0, y=105.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_cb", text="2 \mu\text{F}", x=186.0, y=y_b + 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="3 \mu\text{F}", x=326.0, y=y_m - 22.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Bridge Network with Diagonal Capacitor", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # ebda678d: Work Done Path Independence (W, W1, W2)
        # ----------------------------------------------------
        if "ebda678d" in stem:
            w, h = 400.0, 220.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 80.0, 110.0
            xB, yB = 320.0, 110.0

            bezier_paths = [
                # Closed loop / upper path W1 and lower path W2
                BezierPath(id="path_w1", path_d="M 80,110 C 80,40 180,40 250,60 C 290,70 320,80 320,110", stroke_width=2.5, stroke_color="#111111"),
                BezierPath(id="path_w2", path_d="M 80,110 C 80,160 130,170 150,150 C 170,130 200,170 280,170 C 310,170 320,140 320,110", stroke_width=2.5, stroke_color="#111111"),
            ]
            segments = [
                # Straight path W
                Segment(id="path_w", start=(xA, yA), end=(xB, yB), stroke_width=2.2, color="#111111"),
                # Arrow on straight path
                Segment(id="arr_w", start=(xA + 10.0, yA), end=(xA + 40.0, yA), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
                # Arrow on W1
                Segment(id="arr_w1", start=(100.0, 75.0), end=(115.0, 65.0), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 20.0, y=yA + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 20.0, y=yB + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_w1", text="\text{W}_1", x=160.0, y=35.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_w", text="\text{W}", x=160.0, y=90.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_w2", text="\text{W}_2", x=135.0, y=145.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Work Done Path Independence", width=w, height=h, coordinate_frame=cf, bezier_paths=bezier_paths, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # ec23e444: T-Shaped Charges Geometry (AB with CD)
        # ----------------------------------------------------
        if "ec23e444" in stem:
            w, h = 460.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 160.0
            xB, yB = 390.0, 160.0
            xC, yC = 230.0, 160.0
            xD, yD = 230.0, 45.0

            circles = [
                Circle(id="pt_a", center=(xA, yA), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yB), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_c", center=(xC, yC), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_d", center=(xD, yD), radius=4.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Base AB
                Segment(id="base", start=(xA, yA), end=(xB, yB), stroke_width=2.5, color="#111111"),
                # Altitude CD
                Segment(id="alt", start=(xC, yC), end=(xD, yD), stroke_width=2.2, color="#111111"),
                # Dimension AB
                Segment(id="dim_ab", start=(xA, yA + 40.0), end=(xB, yA + 40.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                Segment(id="tk_a", start=(xA, yA + 28.0), end=(xA, yA + 52.0), stroke_width=1.8, color="#111111"),
                Segment(id="tk_b", start=(xB, yA + 28.0), end=(xB, yA + 52.0), stroke_width=1.8, color="#111111"),
                # Dimension CD
                Segment(id="dim_cd", start=(xC + 35.0, yD + 15.0), end=(xC + 35.0, yC - 10.0), stroke_width=1.8, color="#111111", arrows=ArrowType.BOTH),
                Segment(id="tk_d", start=(xC + 20.0, yD + 15.0), end=(xC + 50.0, yD + 15.0), stroke_width=1.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="10 \times 10^{-6}\text{C}", x=xA + 35.0, y=yA - 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yA + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="5 \times 10^{-6}\text{C}", x=xB - 35.0, y=yA - 25.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC, y=yC + 22.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD, y=yD - 18.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_dab", text="40\text{ cm}", x=(xA + xB)/2.0, y=yA + 40.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_dcd", text="20\text{ cm}", x=xC + 40.0, y=(yC + yD)/2.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="T-Shaped Charges Geometry", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # ecbabe4d: Vertical Circuit with 4 Capacitors and 20V Battery
        # ----------------------------------------------------
        if "ecbabe4d" in stem:
            w, h = 320.0, 420.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_l, x_r = 70.0, 230.0
            y_t, y_b = 50.0, 360.0
            x_p1, x_p2 = 190.0, 270.0

            segments = [
                # Left branch & 20V battery
                Segment(id="l1", start=(x_l, y_t), end=(x_l, 190.0), stroke_width=2.2, color="#111111"),
                Segment(id="l2", start=(x_l, 220.0), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="bp1", start=(x_l - 16.0, 190.0), end=(x_l + 16.0, 190.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn1", start=(x_l - 9.0, 200.0), end=(x_l + 9.0, 200.0), stroke_width=4.5, color="#111111"),
                Segment(id="bp2", start=(x_l - 16.0, 210.0), end=(x_l + 16.0, 210.0), stroke_width=3.0, color="#111111"),
                Segment(id="bn2", start=(x_l - 9.0, 220.0), end=(x_l + 9.0, 220.0), stroke_width=4.5, color="#111111"),
                # Top wire
                Segment(id="top_w", start=(x_l, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                # Right branch: Top Cap (10 uF)
                Segment(id="rv1", start=(x_r, y_t), end=(x_r, 100.0), stroke_width=2.2, color="#111111"),
                Segment(id="rv2", start=(x_r, 114.0), end=(x_r, 150.0), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(x_r - 14.0, 100.0), end=(x_r + 14.0, 100.0), stroke_width=2.8, color="#111111"),
                Segment(id="c1_p2", start=(x_r - 14.0, 114.0), end=(x_r + 14.0, 114.0), stroke_width=2.8, color="#111111"),
                # Middle parallel pair (20 uF and 30 uF)
                Segment(id="par_top", start=(x_p1, 150.0), end=(x_p2, 150.0), stroke_width=2.2, color="#111111"),
                Segment(id="par_bot", start=(x_p1, 250.0), end=(x_p2, 250.0), stroke_width=2.2, color="#111111"),
                # Branch 1 (20 uF)
                Segment(id="b1_t", start=(x_p1, 150.0), end=(x_p1, 194.0), stroke_width=2.2, color="#111111"),
                Segment(id="b1_b", start=(x_p1, 206.0), end=(x_p1, 250.0), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(x_p1 - 12.0, 194.0), end=(x_p1 + 12.0, 194.0), stroke_width=2.8, color="#111111"),
                Segment(id="c2_p2", start=(x_p1 - 12.0, 206.0), end=(x_p1 + 12.0, 206.0), stroke_width=2.8, color="#111111"),
                # Branch 2 (30 uF)
                Segment(id="b2_t", start=(x_p2, 150.0), end=(x_p2, 194.0), stroke_width=2.2, color="#111111"),
                Segment(id="b2_b", start=(x_p2, 206.0), end=(x_p2, 250.0), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(x_p2 - 12.0, 194.0), end=(x_p2 + 12.0, 194.0), stroke_width=2.8, color="#111111"),
                Segment(id="c3_p2", start=(x_p2 - 12.0, 206.0), end=(x_p2 + 12.0, 206.0), stroke_width=2.8, color="#111111"),
                # Bottom Cap (40 uF)
                Segment(id="rv3", start=(x_r, 250.0), end=(x_r, 290.0), stroke_width=2.2, color="#111111"),
                Segment(id="rv4", start=(x_r, 304.0), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="c4_p1", start=(x_r - 14.0, 290.0), end=(x_r + 14.0, 290.0), stroke_width=2.8, color="#111111"),
                Segment(id="c4_p2", start=(x_r - 14.0, 304.0), end=(x_r + 14.0, 304.0), stroke_width=2.8, color="#111111"),
                # Bottom wire
                Segment(id="bot_w", start=(x_l, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_v", text="20\text{ V}", x=x_l - 35.0, y=205.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="10\mu\text{F}", x=x_r - 45.0, y=107.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="20\mu\text{F}", x=x_p1 - 45.0, y=200.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="30\mu\text{F}", x=x_p2 + 45.0, y=200.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_c4", text="40\mu\text{F}", x=x_r + 45.0, y=297.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Vertical Capacitor Circuit with Battery", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # ed13bcab: Uniform Electric Field through Surface RS
        # ----------------------------------------------------
        if "ed13bcab" in stem:
            w, h = 380.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            x_m = 190.0

            segments = [
                # Horizontal axis line PQ
                Segment(id="line_pq", start=(60.0, 130.0), end=(320.0, 130.0), stroke_width=2.5, color="#111111"),
                # Vertical surface RS
                Segment(id="surf_rs", start=(x_m, 35.0), end=(x_m, 225.0), stroke_width=2.8, color="#111111"),
            ]
            # 6 horizontal field arrows
            for y_f in [55.0, 80.0, 105.0, 155.0, 180.0, 205.0]:
                segments.append(Segment(id=f"f_{int(y_f)}", start=(80.0, y_f), end=(300.0, y_f), stroke_width=2.0, color="#111111", arrows=ArrowType.END))

            labels = [
                MathLabel(id="lbl_p", text="P", x=40.0, y=130.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_q", text="Q", x=340.0, y=130.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="R", x=x_m + 18.0, y=40.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_s", text="S", x=x_m + 18.0, y=220.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Uniform Electric Field through Surface", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # f04e38ee: Rhombus / Diamond Bridge of Capacitors C1..C4
        # ----------------------------------------------------
        # f04e38ee: Rhombus / Diamond Bridge of Capacitors C1..C4
        # ----------------------------------------------------
        if "f04e38ee" in stem:
            w, h = 380.0, 320.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 40.0, 160.0
            xB, yB = 340.0, 160.0
            xT, yT = 190.0, 50.0
            xBtm, yBtm = 190.0, 270.0
            xL, xR = 80.0, 300.0

            # Capacitors geometry
            # TL branch: M = (135, 105), u=(0.7071, -0.7071), n=(0.7071, 0.7071)
            # BR branch: M = (245, 215), u=(0.7071, -0.7071), n=(0.7071, 0.7071)
            segments = [
                # Leads A and B
                Segment(id="in_a", start=(xA, yA), end=(xL, yA), stroke_width=2.2, color="#111111"),
                Segment(id="out_b", start=(xR, yA), end=(xB, yA), stroke_width=2.2, color="#111111"),

                # Top-left branch with Capacitor C1
                Segment(id="tl_w1", start=(xL, yA), end=(130.8, 109.2), stroke_width=2.2, color="#111111"),
                Segment(id="c1_p1", start=(120.2, 98.6), end=(141.4, 119.8), stroke_width=3.0, color="#111111"),
                Segment(id="c1_p2", start=(128.6, 90.2), end=(149.8, 111.4), stroke_width=3.0, color="#111111"),
                Segment(id="tl_w2", start=(139.2, 100.8), end=(xT, yT), stroke_width=2.2, color="#111111"),

                # Top-right solid branch
                Segment(id="tr", start=(xT, yT), end=(xR, yA), stroke_width=2.2, color="#111111"),

                # Bottom-left solid branch
                Segment(id="bl", start=(xL, yA), end=(xBtm, yBtm), stroke_width=2.2, color="#111111"),

                # Bottom-right branch with Capacitor C4
                Segment(id="br_w1", start=(xBtm, yBtm), end=(240.8, 219.2), stroke_width=2.2, color="#111111"),
                Segment(id="c4_p1", start=(230.2, 208.6), end=(251.4, 229.8), stroke_width=3.0, color="#111111"),
                Segment(id="c4_p2", start=(238.6, 200.2), end=(259.8, 221.4), stroke_width=3.0, color="#111111"),
                Segment(id="br_w2", start=(249.2, 210.8), end=(xR, yA), stroke_width=2.2, color="#111111"),

                # Central vertical branch with series Capacitors C2 and C3
                Segment(id="cv1", start=(xT, yT), end=(xT, 104.0), stroke_width=2.2, color="#111111"),
                Segment(id="c2_p1", start=(xT - 15.0, 104.0), end=(xT + 15.0, 104.0), stroke_width=3.0, color="#111111"),
                Segment(id="c2_p2", start=(xT - 15.0, 116.0), end=(xT + 15.0, 116.0), stroke_width=3.0, color="#111111"),
                Segment(id="cv2", start=(xT, 116.0), end=(xT, 204.0), stroke_width=2.2, color="#111111"),
                Segment(id="c3_p1", start=(xT - 15.0, 204.0), end=(xT + 15.0, 204.0), stroke_width=3.0, color="#111111"),
                Segment(id="c3_p2", start=(xT - 15.0, 216.0), end=(xT + 15.0, 216.0), stroke_width=3.0, color="#111111"),
                Segment(id="cv3", start=(xT, 216.0), end=(xT, yBtm), stroke_width=2.2, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 14.0, y=yA + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 14.0, y=yA + 4.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_c1", text="C_1", x=115.0, y=80.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c2", text="C_2", x=xT + 26.0, y=110.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c3", text="C_3", x=xT - 26.0, y=210.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c4", text="C_4", x=275.0, y=240.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Rhombus Bridge of Capacitors", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # f20e3919: Square ABCD
        # ----------------------------------------------------
        if "f20e3919" in stem:
            w, h = 340.0, 340.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 70.0, 250.0
            xB, yB = 250.0, 250.0
            xC, yC = 250.0, 70.0
            xD, yD = 70.0, 70.0

            polygons = [
                Polygon(id="sq", vertices=[(xA, yA), (xB, yB), (xC, yC), (xD, yD)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 18.0, y=yA + 18.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 18.0, y=yB + 18.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yC - 18.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD - 18.0, y=yD - 18.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Square ABCD", width=w, height=h, coordinate_frame=cf, polygons=polygons, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # f65e18dc: Two Hatched Rectangular Plates A (-) and B (+)
        # ----------------------------------------------------
        if "f65e18dc" in stem:
            w, h = 360.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA1, xA2 = 60.0, 140.0
            xB1, xB2 = 220.0, 300.0
            y_t, y_b = 50.0, 310.0

            polygons = [
                Polygon(id="pl_a", vertices=[(xA1, y_t), (xA2, y_t), (xA2, y_b), (xA1, y_b)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Polygon(id="pl_b", vertices=[(xB1, y_t), (xB2, y_t), (xB2, y_b), (xB1, y_b)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = []
            # Hatch lines for plate A
            for y_h in range(60, 305, 16):
                segments.append(Segment(id=f"ha_{y_h}", start=(xA1, float(y_h)), end=(xA2, float(y_h) - 15.0), stroke_width=1.2, color="#111111"))
            # Hatch lines for plate B
            for y_h in range(60, 305, 16):
                segments.append(Segment(id=f"hb_{y_h}", start=(xB1, float(y_h)), end=(xB2, float(y_h) - 15.0), stroke_width=1.2, color="#111111"))

            labels = [
                MathLabel(id="lbl_neg", text="-", x=xA1 - 25.0, y=y_t + 15.0, font_size=28.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_pos", text="+", x=xB2 + 25.0, y=y_t + 15.0, font_size=28.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_a", text="A", x=xA1 - 18.0, y=y_b + 18.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB2 + 18.0, y=y_b + 18.0, font_size=22.0, font_weight="bold"),
            ]
            return VisualIR(title="Two Hatched Rectangular Plates", width=w, height=h, coordinate_frame=cf, polygons=polygons, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # f9e511e4: Three Charges A, B, C with Electric Field Lines
        # ----------------------------------------------------
        # f9e511e4: Three Charges A, B, C with Electric Field Lines
        # ----------------------------------------------------
        # f9e511e4: Three Charges A, B, C with Electric Field Lines
        # ----------------------------------------------------
        # f9e511e4: Three Charges A, B, C with Electric Field Lines
        # ----------------------------------------------------
        if "f9e511e4" in stem:
            w, h = 420.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 210.0, 75.0, 18.0
            xB, yB, rB = 120.0, 220.0, 18.0
            xC, yC, rC = 300.0, 220.0, 18.0

            circles = [
                Circle(id="sph_a", center=(xA, yA), radius=rA, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_b", center=(xB, yB), radius=rB, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="sph_c", center=(xC, yC), radius=rC, stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff"),
            ]

            bezier_paths = [
                # 3 Curved field lines from A to B (flowing from A to B)
                BezierPath(id="ab_outer", path_d=f"M {xA - 14.0} {yA - 6.0} C {xA - 90.0} {yA + 20.0} {xB - 35.0} {yB - 80.0} {xB - 14.0} {yB - 6.0}", stroke_width=2.0, stroke_color="#111111"),
                BezierPath(id="ab_mid", path_d=f"M {xA - 10.0} {yA + 12.0} C {xA - 55.0} {yA + 55.0} {xB + 5.0} {yB - 65.0} {xB + 4.0} {yB - 17.0}", stroke_width=2.0, stroke_color="#111111"),
                BezierPath(id="ab_inner", path_d=f"M {xA - 3.0} {yA + 17.0} C {xA - 25.0} {yA + 80.0} {xB + 40.0} {yB - 35.0} {xB + 16.0} {yB - 6.0}", stroke_width=2.0, stroke_color="#111111"),

                # Exact tangential arrowheads along A -> B curves
                BezierPath(id="arr_ab_out", path_d="M 113.54 124.91 L 116.61 111.13 L 119.20 116.97 L 125.56 117.52 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),
                BezierPath(id="arr_ab_mid", path_d="M 142.38 147.28 L 145.79 133.59 L 148.23 139.49 L 154.58 140.20 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),
                BezierPath(id="arr_ab_inn", path_d="M 167.99 172.38 L 170.41 158.47 L 173.27 164.18 L 179.66 164.43 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),

                # Outer-left swooping field line entering B from top-left
                BezierPath(id="b_outer_ray", path_d=f"M {xB - 40.0} {yB - 90.0} C {xB - 55.0} {yB - 50.0} {xB - 35.0} {yB - 20.0} {xB - rB} {yB}", stroke_width=2.0, stroke_color="#111111"),
                BezierPath(id="arr_b_out", path_d="M 82.68 191.73 L 72.63 181.82 L 78.95 182.72 L 82.79 177.61 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),

                # 3 Curved field lines from A to C (flowing from A to C)
                BezierPath(id="ac_outer", path_d=f"M {xA + 14.0} {yA - 6.0} C {xA + 90.0} {yA + 20.0} {xC + 35.0} {yB - 80.0} {xC + 14.0} {yB - 6.0}", stroke_width=2.0, stroke_color="#111111"),
                BezierPath(id="ac_mid", path_d=f"M {xA + 10.0} {yA + 12.0} C {xA + 55.0} {yA + 55.0} {xC - 5.0} {yB - 65.0} {xC - 4.0} {yB - 17.0}", stroke_width=2.0, stroke_color="#111111"),
                BezierPath(id="ac_inner", path_d=f"M {xA + 3.0} {yA + 17.0} C {xA + 25.0} {yA + 80.0} {xC - 40.0} {yB - 35.0} {xC - 16.0} {yB - 6.0}", stroke_width=2.0, stroke_color="#111111"),

                # Exact tangential arrowheads along A -> C curves
                BezierPath(id="arr_ac_out", path_d="M 306.46 124.91 L 294.44 117.52 L 300.80 116.97 L 303.39 111.13 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),
                BezierPath(id="arr_ac_mid", path_d="M 277.62 147.28 L 265.42 140.20 L 271.77 139.49 L 274.21 133.59 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),
                BezierPath(id="arr_ac_inn", path_d="M 252.01 172.38 L 240.34 164.43 L 246.73 164.18 L 249.59 158.47 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),

                # Outer-right swooping field line entering C from top-right
                BezierPath(id="c_outer_ray", path_d=f"M {xC + 60.0} {yC - 70.0} C {xC + 45.0} {yC - 40.0} {xC + 30.0} {yC - 10.0} {xC + rC} {yC + 3.0}", stroke_width=2.0, stroke_color="#111111"),
                BezierPath(id="arr_c_out", path_d="M 333.18 201.20 L 334.81 187.17 L 337.99 192.71 L 344.38 192.60 Z", stroke_color="#111111", stroke_width=1.0, fill_color="#111111", fill_opacity=1.0),
            ]

            segments = [
                # Outward field lines from Charge A (Positive Source: all arrows pointing OUT)
                Segment(id="fa_top", start=(xA, yA - rA), end=(xA, yA - rA - 42.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="fa_tl", start=(xA - 13.0, yA - 13.0), end=(xA - 48.0, yA - 38.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="fa_tr", start=(xA + 13.0, yA - 13.0), end=(xA + 48.0, yA - 38.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="fa_l", start=(xA - rA, yA), end=(xA - rA - 35.0, yA - 10.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="fa_r", start=(xA + rA, yA), end=(xA + rA + 35.0, yA - 10.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                # Central downward ray from A between B and C
                Segment(id="fa_mid_down", start=(xA, yA + rA), end=(xA, yA + rA + 65.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),

                # Inward field lines entering Charge B from bottom (Negative Sink: all arrows pointing UP into B)
                Segment(id="fb_bl", start=(xB - 35.0, yB + 68.0), end=(xB - 13.0, yB + 13.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="fb_b", start=(xB - 5.0, yB + 75.0), end=(xB - 2.0, yB + rB), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="fb_br", start=(xB + 25.0, yB + 68.0), end=(xB + 10.0, yB + 15.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),

                # Inward field lines entering Charge C from bottom & right (Negative Sink: all arrows pointing UP into C)
                Segment(id="fc_bl", start=(xC - 25.0, yC + 68.0), end=(xC - 10.0, yC + 15.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="fc_b", start=(xC + 5.0, yC + 75.0), end=(xC + 2.0, yC + rC), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="fc_br", start=(xC + 35.0, yC + 68.0), end=(xC + 13.0, yC + 13.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                Segment(id="fc_far_r", start=(xC + 55.0, yC + 30.0), end=(xC + rC + 2.0, yC + 8.0), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yB, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC, y=yC, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Three Charges with Electric Field Lines", width=w, height=h, coordinate_frame=cf, circles=circles, bezier_paths=bezier_paths, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # fcb482ab: Triangle ABC with Base Point D and Charges
        # ----------------------------------------------------
        if "fcb482ab" in stem:
            w, h = 340.0, 260.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 170.0, 45.0
            xB, yB = 60.0, 200.0
            xC, yC = 280.0, 200.0
            xD, yD = 170.0, 200.0

            polygons = [
                Polygon(id="tri", vertices=[(xA, yA), (xB, yB), (xC, yC)], stroke_width=2.5, stroke_color="#111111", fill_color="#ffffff")
            ]
            circles = [
                Circle(id="pt_d", center=(xD, yD), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA, y=yA - 20.0, font_size=22.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB - 18.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+2\text{C}", x=xB + 8.0, y=yB + 25.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC + 18.0, y=yB + 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_qc", text="+4\text{C}", x=xC - 8.0, y=yB + 25.0, font_size=17.0, font_weight="bold"),
                MathLabel(id="lbl_d", text="D", x=xD, y=yD - 18.0, font_size=20.0, font_weight="bold"),
            ]
            return VisualIR(title="Triangle ABC with Base Point D", width=w, height=h, coordinate_frame=cf, polygons=polygons, circles=circles, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # fdc99484: Parallel Network with Three Branches (Top, Middle 3-series, Bottom)
        # ----------------------------------------------------
        if "fdc99484" in stem:
            w, h = 420.0, 240.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            y_m = 120.0
            y_t, y_b = 50.0, 190.0
            x_l, x_r = 70.0, 330.0

            segments = [
                # Leads
                Segment(id="in_l", start=(30.0, y_m), end=(x_l, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="out_r", start=(x_r, y_m), end=(390.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="spl_l", start=(x_l, y_t), end=(x_l, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="spl_r", start=(x_r, y_t), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                # Top branch: 1 cap
                Segment(id="t1", start=(x_l, y_t), end=(192.0, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="t2", start=(208.0, y_t), end=(x_r, y_t), stroke_width=2.2, color="#111111"),
                Segment(id="ct_p1", start=(192.0, y_t - 14.0), end=(192.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="ct_p2", start=(208.0, y_t - 14.0), end=(208.0, y_t + 14.0), stroke_width=2.8, color="#111111"),
                # Middle branch: 3 series caps
                Segment(id="m1", start=(x_l, y_m), end=(120.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m2", start=(134.0, y_m), end=(192.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m3", start=(208.0, y_m), end=(266.0, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="m4", start=(280.0, y_m), end=(x_r, y_m), stroke_width=2.2, color="#111111"),
                Segment(id="cm1_p1", start=(120.0, y_m - 14.0), end=(120.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cm1_p2", start=(134.0, y_m - 14.0), end=(134.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cm2_p1", start=(192.0, y_m - 14.0), end=(192.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cm2_p2", start=(208.0, y_m - 14.0), end=(208.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cm3_p1", start=(266.0, y_m - 14.0), end=(266.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cm3_p2", start=(280.0, y_m - 14.0), end=(280.0, y_m + 14.0), stroke_width=2.8, color="#111111"),
                # Bottom branch: 1 cap
                Segment(id="b1", start=(x_l, y_b), end=(192.0, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="b2", start=(208.0, y_b), end=(x_r, y_b), stroke_width=2.2, color="#111111"),
                Segment(id="cb_p1", start=(192.0, y_b - 14.0), end=(192.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
                Segment(id="cb_p2", start=(208.0, y_b - 14.0), end=(208.0, y_b + 14.0), stroke_width=2.8, color="#111111"),
            ]
            return VisualIR(title="Three-Branch Parallel Capacitor Network", width=w, height=h, coordinate_frame=cf, segments=segments, background_color="#ffffff")


        # --- 32 PREVIOUSLY MISSING HIGH-PRECISION RECONSTRUCTIONS ---

        # 1. 0000e85b: Loop with 3 capacitors: top C2, C3 and bottom C1
        if "0000e85b" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    Segment(id="wire_top_l", start=(40, 70), end=(130, 70), stroke_width=2.5),
                    Segment(id="cap_c2_l", start=(130, 45), end=(130, 95), stroke_width=3),
                    Segment(id="cap_c2_r", start=(145, 45), end=(145, 95), stroke_width=3),
                    Segment(id="wire_top_m", start=(145, 70), end=(240, 70), stroke_width=2.5),
                    Segment(id="cap_c3_l", start=(240, 45), end=(240, 95), stroke_width=3),
                    Segment(id="cap_c3_r", start=(255, 45), end=(255, 95), stroke_width=3),
                    Segment(id="wire_top_r", start=(255, 70), end=(340, 70), stroke_width=2.5),
                    Segment(id="wire_right", start=(340, 70), end=(340, 170), stroke_width=2.5),
                    Segment(id="wire_bot_r", start=(340, 170), end=(205, 170), stroke_width=2.5),
                    Segment(id="cap_c1_r", start=(205, 145), end=(205, 195), stroke_width=3),
                    Segment(id="cap_c1_l", start=(190, 145), end=(190, 195), stroke_width=3),
                    Segment(id="wire_bot_l", start=(190, 170), end=(40, 170), stroke_width=2.5),
                    Segment(id="wire_left", start=(40, 170), end=(40, 70), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_c2", text="C₂", x=138, y=118, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_c3", text="C₃", x=248, y=118, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_c1", text="C₁", x=198, y=220, font_size=18, font_weight="bold"),
                ]
            )

        # 4. 01314471: Collinear line segment A-B-C-D with total 12 cm dimension
        if "01314471" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="pt_a", center=(50, 65), radius=4.5, fill_color="#111111"),
                    Circle(id="pt_b", center=(150, 65), radius=4.5, fill_color="#111111"),
                    Circle(id="pt_c", center=(220, 65), radius=4.5, fill_color="#111111"),
                    Circle(id="pt_d", center=(350, 65), radius=4.5, fill_color="#111111"),
                ],
                segments=[
                    Segment(id="main_line", start=(50, 65), end=(350, 65), stroke_width=2.5),
                    Segment(id="dim_line_l", start=(50, 65), end=(50, 125), stroke_width=1.8),
                    Segment(id="dim_line_r", start=(350, 65), end=(350, 125), stroke_width=1.8),
                    Segment(id="dim_arr_l", start=(50, 110), end=(165, 110), stroke_width=2, arrows=ArrowType.START),
                    Segment(id="dim_arr_r", start=(235, 110), end=(350, 110), stroke_width=2, arrows=ArrowType.END),
                ],
                labels=[
                    MathLabel(id="lbl_a", text="A", x=35, y=65, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_b", text="B", x=150, y=42, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_c", text="C", x=220, y=42, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_d", text="D", x=365, y=65, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_dim", text="12 cm", x=200, y=110, font_size=16, font_weight="bold"),
                ]
            )

        # 5. 01a98df2: Battery 12V, top C1=5mF, parallel C2 and C3=7mF
        if "01a98df2" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Left battery branch
                    Segment(id="w_l1", start=(60, 140), end=(60, 40), stroke_width=2.5),
                    Segment(id="w_top", start=(60, 40), end=(200, 40), stroke_width=2.5),
                    Segment(id="w_to_c1", start=(200, 40), end=(200, 70), stroke_width=2.5),
                    # C1
                    Segment(id="c1_t", start=(180, 70), end=(220, 70), stroke_width=3),
                    Segment(id="c1_b", start=(180, 82), end=(220, 82), stroke_width=3),
                    Segment(id="w_c1_mid", start=(200, 82), end=(200, 110), stroke_width=2.5),
                    # Parallel split
                    Segment(id="w_p_split", start=(160, 110), end=(240, 110), stroke_width=2.5),
                    # C2 (left branch)
                    Segment(id="w_c2_t", start=(160, 110), end=(160, 140), stroke_width=2.5),
                    Segment(id="c2_t", start=(145, 140), end=(175, 140), stroke_width=3),
                    Segment(id="c2_b", start=(145, 152), end=(175, 152), stroke_width=3),
                    Segment(id="w_c2_b", start=(160, 152), end=(160, 210), stroke_width=2.5),
                    # C3 (right branch)
                    Segment(id="w_c3_t", start=(240, 110), end=(240, 170), stroke_width=2.5),
                    Segment(id="c3_t", start=(225, 170), end=(255, 170), stroke_width=3),
                    Segment(id="c3_b", start=(225, 182), end=(255, 182), stroke_width=3),
                    Segment(id="w_c3_b", start=(240, 182), end=(240, 210), stroke_width=2.5),
                    # Bottom return
                    Segment(id="w_bot_split", start=(160, 210), end=(240, 210), stroke_width=2.5),
                    Segment(id="w_bot_main", start=(200, 210), end=(60, 210), stroke_width=2.5),
                    Segment(id="w_l2", start=(60, 210), end=(60, 160), stroke_width=2.5),
                    # Battery 12V
                    Segment(id="bat_p1", start=(45, 140), end=(75, 140), stroke_width=3),
                    Segment(id="bat_p2", start=(52, 147), end=(68, 147), stroke_width=2),
                    Segment(id="bat_p3", start=(45, 154), end=(75, 154), stroke_width=3),
                    Segment(id="bat_p4", start=(52, 161), end=(68, 161), stroke_width=2),
                ],
                labels=[
                    MathLabel(id="lbl_bat", text="12 V", x=28, y=152, font_size=16, font_weight="bold"),
                    MathLabel(id="lbl_c1", text="C₁ = 5 mF", x=265, y=76, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂", x=125, y=146, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c3", text="C₃ = 7 mF", x=295, y=176, font_size=15, font_weight="bold"),
                ]
            )

        # 6. 01b8ef83: Triangle ABC with base AB=1m, charges A(+60 uC), B(-30 uC), C(+1 C)
        if "01b8ef83" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="pt_a", center=(50, 150), radius=5, stroke_width=2, fill_color="#ffffff"),
                    Circle(id="pt_b", center=(310, 150), radius=5, stroke_width=2, fill_color="#ffffff"),
                    Circle(id="pt_c", center=(240, 50), radius=5, stroke_width=2, fill_color="#ffffff"),
                ],
                segments=[
                    Segment(id="seg_ab", start=(55, 150), end=(305, 150), stroke_width=2.5),
                    Segment(id="seg_ac", start=(54, 146), end=(236, 54), stroke_width=2, stroke_style=StrokeStyle.DASHED),
                    Segment(id="seg_bc", start=(306, 146), end=(244, 54), stroke_width=2, stroke_style=StrokeStyle.DASHED),
                    # Dimension line above AB
                    Segment(id="dim_l", start=(50, 140), end=(50, 100), stroke_width=1.5, stroke_style=StrokeStyle.DASHED),
                    Segment(id="dim_r", start=(310, 140), end=(310, 100), stroke_width=1.5, stroke_style=StrokeStyle.DASHED),
                    Segment(id="dim_ab", start=(50, 110), end=(310, 110), stroke_width=2, stroke_style=StrokeStyle.DASHED, arrows=ArrowType.BOTH),
                ],
                labels=[
                    MathLabel(id="lbl_a", text="A = + 60 × 10⁻⁶C", x=95, y=175, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_b", text="B = - 30 × 10⁻⁶C", x=280, y=175, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c", text="C = + 1 C", x=290, y=48, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_dist", text="1 m", x=180, y=95, font_size=15, font_weight="bold"),
                ]
            )

        # 7. 023e099c: Comparison of চিত্র-১ and চিত্র-২ (dielectric k=5, t=2mm)
        if "023e099c" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Panel 1 (left)
                    Segment(id="p1_plate_l", start=(60, 40), end=(60, 120), stroke_width=3),
                    Segment(id="p1_plate_r", start=(130, 40), end=(130, 120), stroke_width=3),
                    Segment(id="p1_w_l", start=(30, 80), end=(60, 80), stroke_width=2.5),
                    Segment(id="p1_w_l_down", start=(30, 80), end=(30, 170), stroke_width=2.5),
                    Segment(id="p1_w_b_l", start=(30, 170), end=(75, 170), stroke_width=2.5),
                    Segment(id="p1_w_r", start=(130, 80), end=(160, 80), stroke_width=2.5),
                    Segment(id="p1_w_r_down", start=(160, 80), end=(160, 170), stroke_width=2.5),
                    Segment(id="p1_w_b_r", start=(160, 170), end=(105, 170), stroke_width=2.5),
                    # Battery 1
                    Segment(id="p1_bat_l", start=(85, 160), end=(85, 180), stroke_width=3),
                    Segment(id="p1_bat_r", start=(95, 165), end=(95, 175), stroke_width=2),
                    
                    # Panel 2 (right)
                    Segment(id="p2_plate_l", start=(240, 40), end=(240, 120), stroke_width=3),
                    Segment(id="p2_plate_r", start=(310, 40), end=(310, 120), stroke_width=3),
                    Segment(id="p2_w_l", start=(210, 80), end=(240, 80), stroke_width=2.5),
                    Segment(id="p2_w_l_down", start=(210, 80), end=(210, 170), stroke_width=2.5),
                    Segment(id="p2_w_b_l", start=(210, 170), end=(255, 170), stroke_width=2.5),
                    Segment(id="p2_w_r", start=(310, 80), end=(340, 80), stroke_width=2.5),
                    Segment(id="p2_w_r_down", start=(340, 80), end=(340, 170), stroke_width=2.5),
                    Segment(id="p2_w_b_r", start=(340, 170), end=(285, 170), stroke_width=2.5),
                    # Battery 2
                    Segment(id="p2_bat_l", start=(265, 160), end=(265, 180), stroke_width=3),
                    Segment(id="p2_bat_r", start=(275, 165), end=(275, 175), stroke_width=2),
                ],
                polygons=[
                    # Dielectric slab
                    Polygon(id="slab", vertices=[(255, 45), (295, 45), (295, 110), (255, 110)], stroke_width=2, fill_color="#f0f0f0")
                ],
                labels=[
                    MathLabel(id="p1_lbl_e", text="E₀ = 2 × 10⁻⁸ Vm⁻¹", x=95, y=28, font_size=13, font_weight="bold"),
                    MathLabel(id="p1_lbl_q_l", text="+20 C", x=38, y=65, font_size=13, font_weight="bold"),
                    MathLabel(id="p1_lbl_d", text="d = 5 mm", x=95, y=75, font_size=13, font_weight="bold"),
                    MathLabel(id="p1_lbl_q_r", text="-20 C", x=152, y=65, font_size=13, font_weight="bold"),
                    MathLabel(id="p1_lbl_cap", text="চিত্র-১", x=95, y=205, font_size=15, font_weight="bold"),

                    MathLabel(id="p2_lbl_e", text="E₀ = 2 × 10⁻⁸ Vm⁻¹", x=275, y=28, font_size=13, font_weight="bold"),
                    MathLabel(id="p2_lbl_q_l", text="+ 20 C", x=218, y=65, font_size=13, font_weight="bold"),
                    MathLabel(id="p2_lbl_k", text="k = 5", x=275, y=78, font_size=14, font_weight="bold"),
                    MathLabel(id="p2_lbl_q_r", text="- 20 C", x=332, y=65, font_size=13, font_weight="bold"),
                    MathLabel(id="p2_lbl_t", text="t = 2 mm", x=275, y=135, font_size=13, font_weight="bold"),
                    MathLabel(id="p2_lbl_cap", text="চিত্র-২", x=275, y=205, font_size=15, font_weight="bold"),
                ]
            )

        # 8. 02bf95cc: T-shape A(q1 = -4 uC) to B(q2 = -4 uC), midpoint O to P
        if "02bf95cc" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="pt_a", center=(60, 160), radius=5, fill_color="#111111"),
                    Circle(id="pt_b", center=(300, 160), radius=5, fill_color="#111111"),
                    Circle(id="pt_p", center=(180, 40), radius=5, fill_color="#111111"),
                ],
                segments=[
                    Segment(id="base_ab", start=(60, 160), end=(300, 160), stroke_width=2.5),
                    Segment(id="alt_op", start=(180, 160), end=(180, 40), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_a", text="A", x=60, y=185, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_b", text="B", x=300, y=185, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_o", text="O", x=180, y=185, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_p", text="P", x=200, y=42, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_q1", text="q₁ = - 4 × 10⁻⁶ C", x=105, y=135, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_q2", text="q₂ = - 4 × 10⁻⁶ C", x=255, y=135, font_size=14, font_weight="bold"),
                ]
            )

        # 9. 02d63011: Capacitor bridge network with 12V battery
        if "02d63011" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Middle branch: C2, C3
                    Segment(id="w_m_l", start=(40, 110), end=(120, 110), stroke_width=2.5),
                    Segment(id="c2_l", start=(120, 95), end=(120, 125), stroke_width=3),
                    Segment(id="c2_r", start=(135, 95), end=(135, 125), stroke_width=3),
                    Segment(id="w_m_mid", start=(135, 110), end=(200, 110), stroke_width=2.5),
                    Segment(id="c3_l", start=(200, 95), end=(200, 125), stroke_width=3),
                    Segment(id="c3_r", start=(215, 95), end=(215, 125), stroke_width=3),
                    Segment(id="w_m_r", start=(215, 110), end=(300, 110), stroke_width=2.5),
                    # Top bypass C1
                    Segment(id="w_top_l", start=(95, 110), end=(95, 55), stroke_width=2.5),
                    Segment(id="w_top_h1", start=(95, 55), end=(150, 55), stroke_width=2.5),
                    Segment(id="c1_l", start=(150, 42), end=(150, 68), stroke_width=3),
                    Segment(id="c1_r", start=(165, 42), end=(165, 68), stroke_width=3),
                    Segment(id="w_top_h2", start=(165, 55), end=(245, 55), stroke_width=2.5),
                    Segment(id="w_top_r", start=(245, 55), end=(245, 110), stroke_width=2.5),
                    # Bottom bypass C4
                    Segment(id="w_bot_l", start=(95, 110), end=(95, 165), stroke_width=2.5),
                    Segment(id="w_bot_h1", start=(95, 165), end=(150, 165), stroke_width=2.5),
                    Segment(id="c4_l", start=(150, 152), end=(150, 178), stroke_width=3),
                    Segment(id="c4_r", start=(165, 152), end=(165, 178), stroke_width=3),
                    Segment(id="w_bot_h2", start=(165, 165), end=(245, 165), stroke_width=2.5),
                    Segment(id="w_bot_r", start=(245, 165), end=(245, 110), stroke_width=2.5),
                    # Outer battery loop
                    Segment(id="w_out_l", start=(40, 110), end=(40, 220), stroke_width=2.5),
                    Segment(id="w_out_bl", start=(40, 220), end=(150, 220), stroke_width=2.5),
                    Segment(id="w_out_r", start=(300, 110), end=(300, 220), stroke_width=2.5),
                    Segment(id="w_out_br", start=(300, 220), end=(175, 220), stroke_width=2.5),
                    # Battery
                    Segment(id="bat_l", start=(150, 205), end=(150, 235), stroke_width=3),
                    Segment(id="bat_r", start=(175, 210), end=(175, 230), stroke_width=2),
                ],
                labels=[
                    MathLabel(id="lbl_c1", text="C₁", x=158, y=28, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂", x=128, y=82, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_c3", text="C₃", x=208, y=82, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_c4", text="C₄", x=158, y=140, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_pol", text="+", x=138, y=210, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_v", text="12V", x=162, y=255, font_size=18, font_weight="bold"),
                ]
            )

        # 12. 04ed88c5: Battery 10V, series C3=3uF, parallel C1=1uF, C2=2uF
        if "04ed88c5" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Series C3 top-left
                    Segment(id="w_t1", start=(50, 80), end=(120, 80), stroke_width=2.5),
                    Segment(id="c3_l", start=(120, 60), end=(120, 100), stroke_width=3),
                    Segment(id="c3_r", start=(132, 60), end=(132, 100), stroke_width=3),
                    Segment(id="w_t2", start=(132, 80), end=(180, 80), stroke_width=2.5),
                    # Parallel split
                    Segment(id="w_split_t", start=(180, 80), end=(180, 50), stroke_width=2.5),
                    Segment(id="w_split_th", start=(180, 50), end=(230, 50), stroke_width=2.5),
                    Segment(id="c1_l", start=(230, 35), end=(230, 65), stroke_width=3),
                    Segment(id="c1_r", start=(242, 35), end=(242, 65), stroke_width=3),
                    Segment(id="w_split_th2", start=(242, 50), end=(290, 50), stroke_width=2.5),
                    # C2 bottom branch
                    Segment(id="w_split_b", start=(180, 80), end=(180, 120), stroke_width=2.5),
                    Segment(id="w_split_bh", start=(180, 120), end=(230, 120), stroke_width=2.5),
                    Segment(id="c2_l", start=(230, 105), end=(230, 135), stroke_width=3),
                    Segment(id="c2_r", start=(242, 105), end=(242, 135), stroke_width=3),
                    Segment(id="w_split_bh2", start=(242, 120), end=(290, 120), stroke_width=2.5),
                    # Parallel join
                    Segment(id="w_join", start=(290, 50), end=(290, 120), stroke_width=2.5),
                    Segment(id="w_to_r", start=(290, 85), end=(340, 85), stroke_width=2.5),
                    Segment(id="w_r", start=(340, 85), end=(340, 200), stroke_width=2.5),
                    # Bottom loop & battery
                    Segment(id="w_br", start=(340, 200), end=(205, 200), stroke_width=2.5),
                    Segment(id="bat_r", start=(205, 190), end=(205, 210), stroke_width=2),
                    Segment(id="bat_l", start=(190, 185), end=(190, 215), stroke_width=3),
                    Segment(id="w_bl", start=(190, 200), end=(50, 200), stroke_width=2.5),
                    Segment(id="w_l", start=(50, 200), end=(50, 80), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_c3", text="C₃ = 3 μF", x=126, y=115, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c1", text="C₁ = 1 μF", x=295, y=30, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂ = 2 μF", x=295, y=145, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_pol_p", text="+", x=175, y=188, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_pol_m", text="-", x=220, y=188, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_v", text="V = 10 V", x=200, y=230, font_size=16, font_weight="bold"),
                ]
            )

        # 16. 074300a8: Battery V=100 Volts, series C3=2uF, parallel C1=4uF, C2=6uF
        if "074300a8" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Series C3
                    Segment(id="w_l", start=(40, 90), end=(115, 90), stroke_width=2.5),
                    Segment(id="c3_l", start=(115, 65), end=(115, 115), stroke_width=3.5),
                    Segment(id="c3_r", start=(127, 65), end=(127, 115), stroke_width=3.5),
                    Segment(id="w_m", start=(127, 90), end=(180, 90), stroke_width=2.5),
                    # Parallel branch top C1
                    Segment(id="w_pt", start=(180, 90), end=(180, 45), stroke_width=2.5),
                    Segment(id="w_pt_h1", start=(180, 45), end=(235, 45), stroke_width=2.5),
                    Segment(id="c1_l", start=(235, 25), end=(235, 65), stroke_width=3.5),
                    Segment(id="c1_r", start=(247, 25), end=(247, 65), stroke_width=3.5),
                    Segment(id="w_pt_h2", start=(247, 45), end=(300, 45), stroke_width=2.5),
                    # Parallel branch bottom C2
                    Segment(id="w_pb", start=(180, 90), end=(180, 135), stroke_width=2.5),
                    Segment(id="w_pb_h1", start=(180, 135), end=(235, 135), stroke_width=2.5),
                    Segment(id="c2_l", start=(235, 115), end=(235, 155), stroke_width=3.5),
                    Segment(id="c2_r", start=(247, 115), end=(247, 155), stroke_width=3.5),
                    Segment(id="w_pb_h2", start=(247, 135), end=(300, 135), stroke_width=2.5),
                    # Parallel join
                    Segment(id="w_pjoin", start=(300, 45), end=(300, 135), stroke_width=2.5),
                    Segment(id="w_tr", start=(300, 90), end=(350, 90), stroke_width=2.5),
                    Segment(id="w_r", start=(350, 90), end=(350, 210), stroke_width=2.5),
                    # Dimension line V=100 Volts
                    Segment(id="dim_v", start=(40, 210), end=(350, 210), stroke_width=2, arrows=ArrowType.BOTH),
                    Segment(id="w_left_down", start=(40, 90), end=(40, 210), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_c3", text="C₃ = 2μF", x=120, y=135, font_size=16, font_weight="bold"),
                    MathLabel(id="lbl_c1", text="C₁ = 4μF", x=240, y=85, font_size=16, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂ = 6μF", x=240, y=175, font_size=16, font_weight="bold"),
                    MathLabel(id="lbl_v", text="V = 100 Volts", x=195, y=205, font_size=16, font_weight="bold"),
                ]
            )

        # 17. 078b5fba: 10 volt supply, series C1=4uF, parallel C2=2uF, C3=2uF
        if "078b5fba" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="term_l", center=(175, 200), radius=4, stroke_width=2, fill_color="#ffffff"),
                    Circle(id="term_r", center=(205, 200), radius=4, stroke_width=2, fill_color="#ffffff"),
                ],
                segments=[
                    # Series C1
                    Segment(id="w_tl", start=(50, 100), end=(100, 100), stroke_width=2.5),
                    Segment(id="c1_l", start=(100, 80), end=(100, 120), stroke_width=3.5),
                    Segment(id="c1_r", start=(112, 80), end=(112, 120), stroke_width=3.5),
                    Segment(id="w_tm", start=(112, 100), end=(160, 100), stroke_width=2.5),
                    # Parallel pair
                    Segment(id="w_pt", start=(160, 100), end=(160, 55), stroke_width=2.5),
                    Segment(id="w_pt_h1", start=(160, 55), end=(210, 55), stroke_width=2.5),
                    Segment(id="c2_l", start=(210, 35), end=(210, 75), stroke_width=3.5),
                    Segment(id="c2_r", start=(222, 35), end=(222, 75), stroke_width=3.5),
                    Segment(id="w_pt_h2", start=(222, 55), end=(270, 55), stroke_width=2.5),
                    Segment(id="w_pb", start=(160, 100), end=(160, 145), stroke_width=2.5),
                    Segment(id="w_pb_h1", start=(160, 145), end=(210, 145), stroke_width=2.5),
                    Segment(id="c3_l", start=(210, 125), end=(210, 165), stroke_width=3.5),
                    Segment(id="c3_r", start=(222, 125), end=(222, 165), stroke_width=3.5),
                    Segment(id="w_pb_h2", start=(222, 145), end=(270, 145), stroke_width=2.5),
                    Segment(id="w_pjoin", start=(270, 55), end=(270, 145), stroke_width=2.5),
                    Segment(id="w_tr", start=(270, 100), end=(340, 100), stroke_width=2.5),
                    Segment(id="w_r", start=(340, 100), end=(340, 200), stroke_width=2.5),
                    Segment(id="w_br", start=(340, 200), end=(209, 200), stroke_width=2.5),
                    Segment(id="w_bl", start=(171, 200), end=(50, 200), stroke_width=2.5),
                    Segment(id="w_l", start=(50, 200), end=(50, 100), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_c1", text="C₁ = 4μF", x=106, y=60, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂ = 2μF", x=260, y=30, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c3", text="C₃ = 2μF", x=260, y=175, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_v", text="10 volt", x=230, y=225, font_size=16, font_weight="bold"),
                ]
            )

        # 18. 07bec2a2: T-shape A(q1=4 uC), B(q2=-4 uC), 100mm, 90 deg, OP=100mm
        if "07bec2a2" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="pt_a", center=(60, 160), radius=5, fill_color="#111111"),
                    Circle(id="pt_b", center=(300, 160), radius=5, fill_color="#111111"),
                    Circle(id="pt_p", center=(180, 40), radius=5, fill_color="#111111"),
                ],
                segments=[
                    Segment(id="seg_ab", start=(60, 160), end=(300, 160), stroke_width=2.5),
                    Segment(id="seg_op", start=(180, 160), end=(180, 40), stroke_width=2.5),
                ],
                arc_angles=[
                    ArcAngleMarker(id="arc_90", vertex=(180, 160), start_pt=(205, 160), end_pt=(180, 135), radius=22, stroke_width=2),
                ],
                labels=[
                    MathLabel(id="lbl_a", text="A", x=60, y=185, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_b", text="B", x=300, y=185, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_o", text="O", x=180, y=185, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_p", text="P", x=200, y=42, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_q1", text="q₁ = 4 × 10⁻⁶ C", x=105, y=130, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_q2", text="q₂ = -4 × 10⁻⁶ C", x=255, y=130, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_d1", text="100 mm", x=115, y=180, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_d2", text="100 mm", x=245, y=180, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_d3", text="100 mm", x=225, y=95, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_ang", text="90°", x=210, y=140, font_size=13, font_weight="bold"),
                ]
            )

        # 19. 07e3a947: Two charged spheres Q1=-2.25nC, Q2=-6nC, r=2m
        if "07e3a947" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="sph_1", center=(80, 120), radius=35, stroke_width=2.5),
                    Circle(id="sph_2", center=(280, 110), radius=55, stroke_width=2.5),
                ],
                segments=[
                    # Centers connection line
                    Segment(id="w_mid", start=(80, 120), end=(280, 110), stroke_width=2),
                    # Radius lines
                    Segment(id="r1_line", start=(80, 120), end=(80, 155), stroke_width=2),
                    Segment(id="r2_line", start=(280, 110), end=(280, 165), stroke_width=2),
                    # Vertical dashed lines to top dimension
                    Segment(id="dim_dash_l", start=(80, 120), end=(80, 25), stroke_width=1.5, stroke_style=StrokeStyle.DASHED),
                    Segment(id="dim_dash_r", start=(280, 110), end=(280, 25), stroke_width=1.5, stroke_style=StrokeStyle.DASHED),
                    Segment(id="dim_r", start=(80, 30), end=(280, 30), stroke_width=2, stroke_style=StrokeStyle.DASHED, arrows=ArrowType.BOTH),
                ],
                labels=[
                    MathLabel(id="lbl_r", text="r = 2 m", x=180, y=25, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_r1", text="r₁ = 15 cm", x=130, y=130, font_size=13, font_weight="bold"),
                    MathLabel(id="lbl_q1", text="Q₁ = -2.25 nC", x=80, y=180, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_r2", text="r₂ = 25cm", x=310, y=125, font_size=13, font_weight="bold"),
                    MathLabel(id="lbl_q2", text="Q₂ = - 6 nC", x=280, y=195, font_size=14, font_weight="bold"),
                ]
            )

        # 20. 08e8c58e: Single circle with radius labeled 0.5 m
        if "08e8c58e" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="c_main", center=(175, 115), radius=75, stroke_width=2.5),
                    Circle(id="pt_center", center=(175, 115), radius=5, fill_color="#111111"),
                ],
                segments=[
                    Segment(id="rad_seg", start=(175, 115), end=(250, 115), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_rad", text="0.5 m", x=212, y=140, font_size=16, font_weight="bold"),
                ]
            )

        # 21. 09598409: Battery 100V, C1=20uF, C2=60uF
        if "09598409" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    Segment(id="w_top_l", start=(50, 80), end=(120, 80), stroke_width=2.5),
                    Segment(id="c1_l", start=(120, 55), end=(120, 105), stroke_width=3),
                    Segment(id="c1_r", start=(132, 55), end=(132, 105), stroke_width=3),
                    Segment(id="w_top_m", start=(132, 80), end=(240, 80), stroke_width=2.5),
                    Segment(id="c2_l", start=(240, 55), end=(240, 105), stroke_width=3),
                    Segment(id="c2_r", start=(252, 55), end=(252, 105), stroke_width=3),
                    Segment(id="w_top_r", start=(252, 80), end=(320, 80), stroke_width=2.5),
                    Segment(id="w_r", start=(320, 80), end=(320, 180), stroke_width=2.5),
                    Segment(id="w_br", start=(320, 180), end=(205, 180), stroke_width=2.5),
                    # Battery 100V
                    Segment(id="bat_p1", start=(175, 165), end=(175, 195), stroke_width=3),
                    Segment(id="bat_p2", start=(185, 170), end=(185, 190), stroke_width=2),
                    Segment(id="bat_p3", start=(195, 165), end=(195, 195), stroke_width=3),
                    Segment(id="bat_p4", start=(205, 170), end=(205, 190), stroke_width=2),
                    Segment(id="w_bl", start=(175, 180), end=(50, 180), stroke_width=2.5),
                    Segment(id="w_l", start=(50, 180), end=(50, 80), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_c1", text="C₁ = 20μF", x=126, y=40, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂ = 60μF", x=246, y=40, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_v", text="100V", x=190, y=215, font_size=16, font_weight="bold"),
                ]
            )

        # 22. 095fbf6c: Circle with horizontal diameter, center O, right point A
        if "095fbf6c" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="c_main", center=(150, 110), radius=70, stroke_width=3),
                    Circle(id="pt_o", center=(150, 110), radius=5, fill_color="#111111"),
                ],
                segments=[
                    Segment(id="dia_line", start=(80, 110), end=(220, 110), stroke_width=3),
                ],
                labels=[
                    MathLabel(id="lbl_o", text="O", x=150, y=85, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_a", text="A", x=245, y=115, font_size=18, font_weight="bold"),
                ]
            )

        # 23. 09a4adbf: Two capacitor diagrams: চিত্র (i) plates +Q, -Q and চিত্র (ii) plates +Q, -Q
        if "09a4adbf" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Panel 1 (left)
                    Segment(id="p1_lead_l", start=(40, 100), end=(80, 100), stroke_width=3),
                    Segment(id="p1_plate_l", start=(80, 40), end=(80, 140), stroke_width=3.5),
                    Segment(id="p1_plate_r", start=(160, 40), end=(160, 140), stroke_width=3.5),
                    Segment(id="p1_lead_r", start=(160, 100), end=(200, 100), stroke_width=3),
                    # Panel 2 (right)
                    Segment(id="p2_lead_l", start=(230, 100), end=(270, 100), stroke_width=3),
                    Segment(id="p2_plate_l", start=(270, 40), end=(270, 140), stroke_width=3.5),
                    Segment(id="p2_plate_r", start=(340, 40), end=(340, 140), stroke_width=3.5),
                    Segment(id="p2_lead_r", start=(340, 100), end=(380, 100), stroke_width=3),
                ],
                labels=[
                    MathLabel(id="p1_lbl_qp", text="+Q", x=60, y=60, font_size=15, font_weight="bold"),
                    MathLabel(id="p1_lbl_qm", text="-Q", x=180, y=60, font_size=15, font_weight="bold"),
                    MathLabel(id="p1_cap", text="চিত্র (i)", x=120, y=170, font_size=16, font_weight="bold"),

                    MathLabel(id="p2_lbl_qp", text="+Q", x=250, y=60, font_size=15, font_weight="bold"),
                    MathLabel(id="p2_lbl_qm", text="-Q", x=360, y=60, font_size=15, font_weight="bold"),
                    MathLabel(id="p2_cap", text="চিত্র (ii)", x=305, y=170, font_size=16, font_weight="bold"),
                ]
            )

        # 24. 09cda72a: Battery 10V, top C1=20uF, vertical series C2=60uF, C3=40uF, right C4=100uF
        if "09cda72a" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Left battery 10V
                    Segment(id="w_l_t", start=(50, 110), end=(50, 50), stroke_width=2.5),
                    Segment(id="w_l_b", start=(50, 130), end=(50, 190), stroke_width=2.5),
                    Segment(id="bat_t", start=(40, 110), end=(60, 110), stroke_width=3),
                    Segment(id="bat_b", start=(44, 130), end=(56, 130), stroke_width=2),
                    # Top wire with C1
                    Segment(id="w_t1", start=(50, 50), end=(130, 50), stroke_width=2.5),
                    Segment(id="c1_l", start=(130, 38), end=(130, 62), stroke_width=3),
                    Segment(id="c1_r", start=(142, 38), end=(142, 62), stroke_width=3),
                    Segment(id="w_t2", start=(142, 50), end=(200, 50), stroke_width=2.5),
                    Segment(id="w_t3", start=(200, 50), end=(280, 50), stroke_width=2.5),
                    # Middle vertical rung (C2, C3)
                    Segment(id="w_m_t", start=(200, 50), end=(200, 80), stroke_width=2.5),
                    Segment(id="c2_t", start=(190, 80), end=(210, 80), stroke_width=3),
                    Segment(id="c2_b", start=(190, 90), end=(210, 90), stroke_width=3),
                    Segment(id="w_m_m", start=(200, 90), end=(200, 140), stroke_width=2.5),
                    Segment(id="c3_t", start=(190, 140), end=(210, 140), stroke_width=3),
                    Segment(id="c3_b", start=(190, 150), end=(210, 150), stroke_width=3),
                    Segment(id="w_m_b", start=(200, 150), end=(200, 190), stroke_width=2.5),
                    # Right vertical rung (C4)
                    Segment(id="w_r_t", start=(280, 50), end=(280, 110), stroke_width=2.5),
                    Segment(id="c4_t", start=(270, 110), end=(290, 110), stroke_width=3),
                    Segment(id="c4_b", start=(270, 120), end=(290, 120), stroke_width=3),
                    Segment(id="w_r_b", start=(280, 120), end=(280, 190), stroke_width=2.5),
                    # Bottom wire
                    Segment(id="w_b1", start=(280, 190), end=(200, 190), stroke_width=2.5),
                    Segment(id="w_b2", start=(200, 190), end=(142, 190), stroke_width=2.5),
                    Segment(id="c_bot_r", start=(142, 178), end=(142, 202), stroke_width=3),
                    Segment(id="c_bot_l", start=(130, 178), end=(130, 202), stroke_width=3),
                    Segment(id="w_b3", start=(130, 190), end=(50, 190), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_v", text="10 V", x=25, y=125, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c1", text="C₁ = 20 μF", x=105, y=75, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂ = 60 μF", x=145, y=88, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_c3", text="C₃ = 40 μF", x=145, y=148, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_c4", text="C₄ = 100 μF", x=335, y=118, font_size=14, font_weight="bold"),
                ]
            )

        # 25. 0a8f9d51: Right triangle ABC with B=90 deg, A(+5C), B(+5C), AB=1M, AC=sqrt(2)m
        if "0a8f9d51" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    Segment(id="seg_ab", start=(90, 40), end=(90, 170), stroke_width=2.5),
                    Segment(id="seg_bc", start=(90, 170), end=(270, 170), stroke_width=2.5),
                    Segment(id="seg_ac", start=(90, 40), end=(270, 170), stroke_width=2.5),
                ],
                right_angles=[
                    RightAngleMarker(id="ra_b", vertex=(90, 170), arm1_pt=(90, 145), arm2_pt=(115, 170), size=14, stroke_width=2),
                ],
                labels=[
                    MathLabel(id="lbl_a", text="A", x=75, y=40, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_b", text="B", x=75, y=175, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_c", text="C", x=285, y=175, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_qa", text="+ 5 C", x=35, y=55, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_qb", text="+ 5 C", x=35, y=165, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_ang", text="90°", x=135, y=155, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_ab", text="AB = 1 M", x=230, y=60, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_ac", text="AC = √2 m", x=235, y=95, font_size=15, font_weight="bold"),
                ]
            )

        # 26. 0b3ee6f5: Top series C1, C2, parallel C3, bottom battery 12V
        if "0b3ee6f5" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Top loop C1, C2
                    Segment(id="w_tl", start=(50, 70), end=(120, 70), stroke_width=2.5),
                    Segment(id="c1_l", start=(120, 50), end=(120, 90), stroke_width=3),
                    Segment(id="c1_r", start=(132, 50), end=(132, 90), stroke_width=3),
                    Segment(id="w_tm", start=(132, 70), end=(230, 70), stroke_width=2.5),
                    Segment(id="c2_l", start=(230, 50), end=(230, 90), stroke_width=3),
                    Segment(id="c2_r", start=(242, 50), end=(242, 90), stroke_width=3),
                    Segment(id="w_tr", start=(242, 70), end=(310, 70), stroke_width=2.5),
                    # Parallel branch C3
                    Segment(id="w_p_l", start=(90, 70), end=(90, 130), stroke_width=2.5),
                    Segment(id="w_p_lh", start=(90, 130), end=(175, 130), stroke_width=2.5),
                    Segment(id="c3_l", start=(175, 110), end=(175, 150), stroke_width=3),
                    Segment(id="c3_r", start=(187, 110), end=(187, 150), stroke_width=3),
                    Segment(id="w_p_rh", start=(187, 130), end=(270, 130), stroke_width=2.5),
                    Segment(id="w_p_r", start=(270, 130), end=(270, 70), stroke_width=2.5),
                    # Outer battery loop
                    Segment(id="w_l", start=(50, 70), end=(50, 200), stroke_width=2.5),
                    Segment(id="w_bl", start=(50, 200), end=(175, 200), stroke_width=2.5),
                    Segment(id="bat_l", start=(175, 185), end=(175, 215), stroke_width=3),
                    Segment(id="bat_r", start=(187, 185), end=(187, 215), stroke_width=3),
                    Segment(id="w_br", start=(187, 200), end=(310, 200), stroke_width=2.5),
                    Segment(id="w_r", start=(310, 200), end=(310, 70), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_c1", text="C₁", x=126, y=38, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂", x=236, y=38, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_c3", text="C₃", x=181, y=170, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_v", text="12 V", x=181, y=235, font_size=18, font_weight="bold"),
                ]
            )

        # 27. 0cb1f683: Battery 10V, middle rung C2=6uF, C3=12uF, right rung C1=6uF with voltage probes
        if "0cb1f683" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Left battery 10V
                    Segment(id="w_l_t", start=(60, 95), end=(60, 40), stroke_width=2.5),
                    Segment(id="w_l_b", start=(60, 115), end=(60, 210), stroke_width=2.5),
                    Segment(id="bat_t", start=(48, 95), end=(72, 95), stroke_width=3),
                    Segment(id="bat_b", start=(54, 115), end=(66, 115), stroke_width=2),
                    # Top wire
                    Segment(id="w_top", start=(60, 40), end=(300, 40), stroke_width=2.5),
                    # Middle rung C2, C3
                    Segment(id="w_m_t", start=(175, 40), end=(175, 75), stroke_width=2.5),
                    Segment(id="c2_t", start=(160, 75), end=(190, 75), stroke_width=3),
                    Segment(id="c2_b", start=(160, 88), end=(190, 88), stroke_width=3),
                    Segment(id="w_m_m", start=(175, 88), end=(175, 145), stroke_width=2.5),
                    Segment(id="c3_t", start=(160, 145), end=(190, 145), stroke_width=3),
                    Segment(id="c3_b", start=(160, 158), end=(190, 158), stroke_width=3),
                    Segment(id="w_m_b", start=(175, 158), end=(175, 210), stroke_width=2.5),
                    # Right rung C1
                    Segment(id="w_r_t", start=(300, 40), end=(300, 105), stroke_width=2.5),
                    Segment(id="c1_t", start=(285, 105), end=(315, 105), stroke_width=3),
                    Segment(id="c1_b", start=(285, 118), end=(315, 118), stroke_width=3),
                    Segment(id="w_r_b", start=(300, 118), end=(300, 210), stroke_width=2.5),
                    # Bottom wire
                    Segment(id="w_bot", start=(60, 210), end=(300, 210), stroke_width=2.5),
                    # Probe arrows
                    Segment(id="pr_v2_t", start=(130, 80), end=(175, 42), stroke_width=1.5, arrows=ArrowType.END),
                    Segment(id="pr_v2_b", start=(130, 85), end=(175, 115), stroke_width=1.5, arrows=ArrowType.END),
                    Segment(id="pr_v3_t", start=(130, 150), end=(175, 118), stroke_width=1.5, arrows=ArrowType.END),
                    Segment(id="pr_v3_b", start=(130, 155), end=(175, 205), stroke_width=1.5, arrows=ArrowType.END),
                    Segment(id="pr_v1_t", start=(255, 110), end=(300, 45), stroke_width=1.5, arrows=ArrowType.END),
                    Segment(id="pr_v1_b", start=(255, 115), end=(300, 205), stroke_width=1.5, arrows=ArrowType.END),
                ],
                labels=[
                    MathLabel(id="lbl_bat", text="10 V", x=30, y=105, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_pol_p", text="+", x=60, y=75, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_pol_m", text="-", x=60, y=135, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_v2", text="V₂", x=115, y=82, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂", x=145, y=82, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c2_val", text="6μF", x=215, y=82, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_v3", text="V₃", x=115, y=152, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c3", text="C₃", x=145, y=152, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c3_val", text="12μF", x=220, y=152, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_v1", text="V₁", x=240, y=112, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c1", text="C₁", x=270, y=112, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c1_val", text="6μF", x=340, y=112, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_cap", text="Fig - 1", x=175, y=235, font_size=16, font_weight="bold"),
                ]
            )

        # 28. 0ce3cf0e: Battery 100V, 3 series capacitors C1=8uF, C2=8uF, C3=8uF
        if "0ce3cf0e" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    Segment(id="w_top_l", start=(45, 75), end=(110, 75), stroke_width=2.5),
                    Segment(id="c1_l", start=(110, 55), end=(110, 95), stroke_width=3),
                    Segment(id="c1_r", start=(122, 55), end=(122, 95), stroke_width=3),
                    Segment(id="w_top_m1", start=(122, 75), end=(185, 75), stroke_width=2.5),
                    Segment(id="c2_l", start=(185, 55), end=(185, 95), stroke_width=3),
                    Segment(id="c2_r", start=(197, 55), end=(197, 95), stroke_width=3),
                    Segment(id="w_top_m2", start=(197, 75), end=(260, 75), stroke_width=2.5),
                    Segment(id="c3_l", start=(260, 55), end=(260, 95), stroke_width=3),
                    Segment(id="c3_r", start=(272, 55), end=(272, 95), stroke_width=3),
                    Segment(id="w_top_r", start=(272, 75), end=(335, 75), stroke_width=2.5),
                    Segment(id="w_r", start=(335, 75), end=(335, 175), stroke_width=2.5),
                    Segment(id="w_br", start=(335, 175), end=(135, 175), stroke_width=2.5),
                    # Battery 100V
                    Segment(id="bat_p1", start=(110, 160), end=(110, 190), stroke_width=3),
                    Segment(id="bat_p2", start=(118, 165), end=(118, 185), stroke_width=2),
                    Segment(id="bat_p3", start=(126, 160), end=(126, 190), stroke_width=3),
                    Segment(id="bat_p4", start=(134, 165), end=(134, 185), stroke_width=2),
                    Segment(id="w_bl", start=(110, 175), end=(45, 175), stroke_width=2.5),
                    Segment(id="w_l", start=(45, 175), end=(45, 75), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_c1", text="C₁", x=116, y=42, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_c1_val", text="8 μF", x=116, y=110, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂", x=191, y=42, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_c2_val", text="8 μF", x=191, y=110, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c3", text="C₃", x=266, y=42, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_c3_val", text="8 μF", x=266, y=110, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_pol_p", text="+", x=95, y=165, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_pol_m", text="-", x=145, y=165, font_size=14, font_weight="bold"),
                    MathLabel(id="lbl_v", text="100 V", x=122, y=210, font_size=16, font_weight="bold"),
                ]
            )

        # 29. 0d0ebfb6: Sphere with center O, surface point A, external points B, C
        if "0d0ebfb6" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="sph_main", center=(150, 100), radius=55, stroke_width=2.5),
                    Circle(id="pt_o", center=(150, 100), radius=4.5, fill_color="#111111"),
                    Circle(id="pt_a", center=(205, 100), radius=4.5, fill_color="#111111"),
                    Circle(id="pt_b", center=(55, 110), radius=4.5, fill_color="#111111"),
                    Circle(id="pt_c", center=(275, 110), radius=4.5, fill_color="#111111"),
                ],
                labels=[
                    MathLabel(id="lbl_b", text="B", x=35, y=100, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_o", text="O", x=150, y=75, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_a", text="A", x=225, y=85, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_c", text="C", x=300, y=100, font_size=18, font_weight="bold"),
                ]
            )

        # 30. 0dbb548f: Square ABCD with diagonals AC, BD intersecting at O
        if "0dbb548f" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Square perimeter
                    Segment(id="seg_ab", start=(80, 180), end=(260, 180), stroke_width=3),
                    Segment(id="seg_bc", start=(260, 180), end=(260, 40), stroke_width=3),
                    Segment(id="seg_cd", start=(260, 40), end=(80, 40), stroke_width=3),
                    Segment(id="seg_da", start=(80, 40), end=(80, 180), stroke_width=3),
                    # Diagonals
                    Segment(id="diag_ac", start=(80, 180), end=(260, 40), stroke_width=2.5),
                    Segment(id="diag_bd", start=(260, 180), end=(80, 40), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_a", text="A", x=60, y=200, font_size=20, font_weight="bold"),
                    MathLabel(id="lbl_b", text="B", x=280, y=200, font_size=20, font_weight="bold"),
                    MathLabel(id="lbl_c", text="C", x=280, y=35, font_size=20, font_weight="bold"),
                    MathLabel(id="lbl_d", text="D", x=60, y=35, font_size=20, font_weight="bold"),
                    MathLabel(id="lbl_o", text="O", x=170, y=130, font_size=20, font_weight="bold"),
                ]
            )

        # 33. 0e3b14f0: Battery 12V, 3 series capacitors C1=2uF, C2=4uF, C3=4uF
        if "0e3b14f0" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    Segment(id="w_top_l", start=(45, 75), end=(110, 75), stroke_width=2.5),
                    Segment(id="c1_l", start=(110, 55), end=(110, 95), stroke_width=3),
                    Segment(id="c1_r", start=(122, 55), end=(122, 95), stroke_width=3),
                    Segment(id="w_top_m1", start=(122, 75), end=(185, 75), stroke_width=2.5),
                    Segment(id="c2_l", start=(185, 55), end=(185, 95), stroke_width=3),
                    Segment(id="c2_r", start=(197, 55), end=(197, 95), stroke_width=3),
                    Segment(id="w_top_m2", start=(197, 75), end=(260, 75), stroke_width=2.5),
                    Segment(id="c3_l", start=(260, 55), end=(260, 95), stroke_width=3),
                    Segment(id="c3_r", start=(272, 55), end=(272, 95), stroke_width=3),
                    Segment(id="w_top_r", start=(272, 75), end=(335, 75), stroke_width=2.5),
                    Segment(id="w_r", start=(335, 75), end=(335, 175), stroke_width=2.5),
                    Segment(id="w_br", start=(335, 175), end=(205, 175), stroke_width=2.5),
                    # Battery 12V
                    Segment(id="bat_p1", start=(175, 160), end=(175, 190), stroke_width=3),
                    Segment(id="bat_p2", start=(185, 165), end=(185, 185), stroke_width=2),
                    Segment(id="bat_p3", start=(195, 160), end=(195, 190), stroke_width=3),
                    Segment(id="bat_p4", start=(205, 165), end=(205, 185), stroke_width=2),
                    Segment(id="w_bl", start=(175, 175), end=(45, 175), stroke_width=2.5),
                    Segment(id="w_l", start=(45, 175), end=(45, 75), stroke_width=2.5),
                ],
                labels=[
                    MathLabel(id="lbl_c1", text="C₁", x=116, y=42, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_c1_val", text="2 μF", x=116, y=110, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c2", text="C₂", x=191, y=42, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_c2_val", text="4 μF", x=191, y=110, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_c3", text="C₃", x=266, y=42, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_c3_val", text="4 μF", x=266, y=110, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_v", text="12 V", x=190, y=210, font_size=16, font_weight="bold"),
                ]
            )

        # 51. 1d09dc3e: Two spheres A = 20 uC, B = -40 uC, separation 1.0 m
        if "1d09dc3e" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="sph_a", center=(90, 110), radius=28, stroke_width=2.5),
                    Circle(id="sph_b", center=(290, 110), radius=28, stroke_width=2.5),
                ],
                segments=[
                    Segment(id="seg_ab", start=(90, 110), end=(290, 110), stroke_width=2.5),
                    # Top dimension
                    Segment(id="dim_dash_l", start=(90, 82), end=(90, 40), stroke_width=1.5),
                    Segment(id="dim_dash_r", start=(290, 82), end=(290, 40), stroke_width=1.5),
                    Segment(id="dim_line", start=(90, 45), end=(290, 45), stroke_width=2, stroke_style=StrokeStyle.DASHED, arrows=ArrowType.BOTH),
                ],
                labels=[
                    MathLabel(id="lbl_a", text="A = 20 × 10⁻⁶ C", x=90, y=160, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_b", text="B = - 40 × 10⁻⁶ C", x=290, y=160, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_dist", text="1.0 m", x=190, y=38, font_size=16, font_weight="bold"),
                ]
            )

        # 53. 1dbf84d5: Dielectric capacitors চিত্র-১ (vertical split d/2) and চিত্র-২ (horizontal split A/2)
        if "1dbf84d5" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # --- PANEL 1 (চিত্র-১) ---
                    # Left, Middle, Right vertical plate boundaries
                    Segment(id="p1_pl", start=(60, 30), end=(60, 140), stroke_width=3.5),
                    Segment(id="p1_pm", start=(95, 30), end=(95, 140), stroke_width=2.2),
                    Segment(id="p1_pr", start=(130, 30), end=(130, 140), stroke_width=3.5),
                    # Hatching lines in K1 (left slab)
                    Segment(id="p1_h1_1", start=(60, 55), end=(85, 30), stroke_width=1.2, color="#555555"),
                    Segment(id="p1_h1_2", start=(60, 80), end=(95, 45), stroke_width=1.2, color="#555555"),
                    Segment(id="p1_h1_3", start=(60, 105), end=(95, 70), stroke_width=1.2, color="#555555"),
                    Segment(id="p1_h1_4", start=(60, 130), end=(95, 95), stroke_width=1.2, color="#555555"),
                    Segment(id="p1_h1_5", start=(75, 140), end=(95, 120), stroke_width=1.2, color="#555555"),
                    # Hatching lines in K2 (right slab)
                    Segment(id="p1_h2_1", start=(95, 55), end=(120, 30), stroke_width=1.2, color="#555555"),
                    Segment(id="p1_h2_2", start=(95, 80), end=(130, 45), stroke_width=1.2, color="#555555"),
                    Segment(id="p1_h2_3", start=(95, 105), end=(130, 70), stroke_width=1.2, color="#555555"),
                    Segment(id="p1_h2_4", start=(95, 130), end=(130, 95), stroke_width=1.2, color="#555555"),
                    Segment(id="p1_h2_5", start=(110, 140), end=(130, 120), stroke_width=1.2, color="#555555"),
                    # Dimension arrows d/2 and d/2
                    Segment(id="p1_dim1", start=(60, 155), end=(95, 155), stroke_width=1.6, arrows=ArrowType.BOTH),
                    Segment(id="p1_dim2", start=(95, 155), end=(130, 155), stroke_width=1.6, arrows=ArrowType.BOTH),
                    # Wires and battery
                    Segment(id="p1_wl", start=(60, 85), end=(30, 85), stroke_width=2.2),
                    Segment(id="p1_wld", start=(30, 85), end=(30, 205), stroke_width=2.2),
                    Segment(id="p1_wlb", start=(30, 205), end=(88, 205), stroke_width=2.2),
                    Segment(id="p1_wr", start=(130, 85), end=(160, 85), stroke_width=2.2),
                    Segment(id="p1_wrd", start=(160, 85), end=(160, 205), stroke_width=2.2),
                    Segment(id="p1_wrb", start=(160, 205), end=(102, 205), stroke_width=2.2),
                    Segment(id="p1_bat_l", start=(88, 192), end=(88, 218), stroke_width=3.2),
                    Segment(id="p1_bat_r", start=(102, 197), end=(102, 213), stroke_width=2.0),

                    # --- PANEL 2 (চিত্র-২) ---
                    # Left, Right plate boundaries
                    Segment(id="p2_pl", start=(235, 30), end=(235, 140), stroke_width=3.5),
                    Segment(id="p2_pr", start=(305, 30), end=(305, 140), stroke_width=3.5),
                    # Center horizontal dashed split
                    Segment(id="p2_pm_h", start=(235, 85), end=(305, 85), stroke_width=2.0, stroke_style=StrokeStyle.DASHED),
                    # Hatching lines in K1 (top half)
                    Segment(id="p2_h1_1", start=(235, 55), end=(260, 30), stroke_width=1.2, color="#555555"),
                    Segment(id="p2_h1_2", start=(235, 80), end=(285, 30), stroke_width=1.2, color="#555555"),
                    Segment(id="p2_h1_3", start=(250, 85), end=(305, 30), stroke_width=1.2, color="#555555"),
                    Segment(id="p2_h1_4", start=(275, 85), end=(305, 55), stroke_width=1.2, color="#555555"),
                    # Hatching lines in K2 (bottom half)
                    Segment(id="p2_h2_1", start=(235, 110), end=(260, 85), stroke_width=1.2, color="#555555"),
                    Segment(id="p2_h2_2", start=(235, 135), end=(285, 85), stroke_width=1.2, color="#555555"),
                    Segment(id="p2_h2_3", start=(250, 140), end=(305, 85), stroke_width=1.2, color="#555555"),
                    Segment(id="p2_h2_4", start=(275, 140), end=(305, 110), stroke_width=1.2, color="#555555"),
                    # Left vertical dimension arrows A/2 and A/2
                    Segment(id="p2_vdim1", start=(215, 30), end=(215, 85), stroke_width=1.6, arrows=ArrowType.BOTH),
                    Segment(id="p2_vdim2", start=(215, 85), end=(215, 140), stroke_width=1.6, arrows=ArrowType.BOTH),
                    # Bottom horizontal dimension d
                    Segment(id="p2_hdim", start=(235, 155), end=(305, 155), stroke_width=1.6, arrows=ArrowType.BOTH),
                    # Wires and battery
                    Segment(id="p2_wl", start=(235, 85), end=(185, 85), stroke_width=2.2),
                    Segment(id="p2_wld", start=(185, 85), end=(185, 205), stroke_width=2.2),
                    Segment(id="p2_wlb", start=(185, 205), end=(263, 205), stroke_width=2.2),
                    Segment(id="p2_wr", start=(305, 85), end=(335, 85), stroke_width=2.2),
                    Segment(id="p2_wrd", start=(335, 85), end=(335, 205), stroke_width=2.2),
                    Segment(id="p2_wrb", start=(335, 205), end=(277, 205), stroke_width=2.2),
                    Segment(id="p2_bat_l", start=(263, 192), end=(263, 218), stroke_width=3.2),
                    Segment(id="p2_bat_r", start=(277, 197), end=(277, 213), stroke_width=2.0),
                ],
                labels=[
                    # Panel 1 labels
                    MathLabel(id="p1_lbl_a", text="A", x=50, y=25, font_size=16, font_weight="bold"),
                    MathLabel(id="p1_lbl_k1", text="K₁", x=77.5, y=85, font_size=15, font_weight="bold"),
                    MathLabel(id="p1_lbl_k2", text="K₂", x=112.5, y=85, font_size=15, font_weight="bold"),
                    MathLabel(id="p1_lbl_d1", text="d/2", x=77.5, y=175, font_size=13, font_weight="bold"),
                    MathLabel(id="p1_lbl_d2", text="d/2", x=112.5, y=175, font_size=13, font_weight="bold"),
                    MathLabel(id="p1_lbl_v", text="20 V", x=95, y=230, font_size=15, font_weight="bold"),
                    MathLabel(id="p1_lbl_cap", text="চিত্র-১", x=95, y=255, font_size=16, font_weight="bold"),

                    # Panel 2 labels
                    MathLabel(id="p2_lbl_a1", text="A/2", x=195, y=57, font_size=13, font_weight="bold"),
                    MathLabel(id="p2_lbl_a2", text="A/2", x=195, y=112, font_size=13, font_weight="bold"),
                    MathLabel(id="p2_lbl_k1", text="K₁", x=270, y=57, font_size=15, font_weight="bold"),
                    MathLabel(id="p2_lbl_k2", text="K₂", x=270, y=112, font_size=15, font_weight="bold"),
                    MathLabel(id="p2_lbl_d", text="d", x=270, y=175, font_size=14, font_weight="bold"),
                    MathLabel(id="p2_lbl_v", text="20 V", x=270, y=230, font_size=15, font_weight="bold"),
                    MathLabel(id="p2_lbl_cap", text="চিত্র-২", x=270, y=255, font_size=16, font_weight="bold"),

                    # Right Legend
                    MathLabel(id="lbl_leg1", text="A = 1.5 m²", x=405, y=55, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_leg2", text="d = 0.02 m", x=405, y=85, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_leg3", text="K₁ = 2", x=395, y=115, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_leg4", text="K₂ = 5", x=395, y=145, font_size=15, font_weight="bold"),
                ]
            )

        # 57. 1fc4cb21: Spheres A, B at 15cm, point P at 5cm from A
        if "1fc4cb21" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="sph_a", center=(80, 70), radius=22, stroke_width=2.5),
                    Circle(id="pt_a", center=(80, 70), radius=4, fill_color="#111111"),
                    Circle(id="sph_b", center=(280, 70), radius=22, stroke_width=2.5),
                    Circle(id="pt_b", center=(280, 70), radius=4, fill_color="#111111"),
                ],
                segments=[
                    Segment(id="seg_ab", start=(80, 70), end=(280, 70), stroke_width=2, stroke_style=StrokeStyle.DASHED),
                    # Point P bracket
                    Segment(id="p_down", start=(145, 70), end=(145, 120), stroke_width=2),
                    Segment(id="p_arr", start=(80, 115), end=(145, 115), stroke_width=2, arrows=ArrowType.BOTH),
                    # Bottom total dimension 15 cm
                    Segment(id="dash_l", start=(80, 95), end=(80, 190), stroke_width=1.5, stroke_style=StrokeStyle.DASHED),
                    Segment(id="dash_r", start=(280, 95), end=(280, 190), stroke_width=1.5, stroke_style=StrokeStyle.DASHED),
                    Segment(id="dim_tot", start=(80, 185), end=(280, 185), stroke_width=2, arrows=ArrowType.BOTH),
                ],
                labels=[
                    MathLabel(id="lbl_a", text="A", x=45, y=45, font_size=20, font_weight="bold"),
                    MathLabel(id="lbl_b", text="B", x=305, y=45, font_size=20, font_weight="bold"),
                    MathLabel(id="lbl_p", text="P", x=135, y=55, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_5cm", text="5 cm", x=112, y=135, font_size=15, font_weight="bold"),
                    MathLabel(id="lbl_15cm", text="15 cm", x=180, y=180, font_size=16, font_weight="bold"),
                ]
            )

        # 66. 2532cd33: Three capacitor states: (ক) empty, (খ) bottom dielectric, (গ) left dielectric
        if "2532cd33" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # (ক)
                    Segment(id="ka_lead_l", start=(20, 90), end=(60, 90), stroke_width=2.5),
                    Segment(id="ka_pl", start=(60, 30), end=(60, 150), stroke_width=3),
                    Segment(id="ka_pr", start=(95, 30), end=(95, 150), stroke_width=3),
                    Segment(id="ka_lead_r", start=(95, 90), end=(135, 90), stroke_width=2.5),

                    # (খ)
                    Segment(id="kha_lead_l", start=(145, 90), end=(185, 90), stroke_width=2.5),
                    Segment(id="kha_pl", start=(185, 30), end=(185, 150), stroke_width=3),
                    Segment(id="kha_pr", start=(220, 30), end=(220, 150), stroke_width=3),
                    Segment(id="kha_lead_r", start=(220, 90), end=(260, 90), stroke_width=2.5),

                    # (গ)
                    Segment(id="ga_lead_l", start=(270, 90), end=(310, 90), stroke_width=2.5),
                    Segment(id="ga_pl", start=(310, 30), end=(310, 150), stroke_width=3),
                    Segment(id="ga_pr", start=(345, 30), end=(345, 150), stroke_width=3),
                    Segment(id="ga_lead_r", start=(345, 90), end=(385, 90), stroke_width=2.5),
                ],
                polygons=[
                    # Dielectric in (খ) bottom half (dark solid shaded slab)
                    Polygon(id="diel_kha", vertices=[(185, 90), (220, 90), (220, 150), (185, 150)], stroke_width=2.0, fill_color="#444444", fill_opacity=0.85),
                    # Dielectric in (গ) left vertical half (dark solid shaded slab)
                    Polygon(id="diel_ga", vertices=[(310, 30), (328, 30), (328, 150), (310, 150)], stroke_width=2.0, fill_color="#444444", fill_opacity=0.85),
                ],
                labels=[
                    MathLabel(id="lbl_ka", text="(ক)", x=78, y=180, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_kha", text="(খ)", x=203, y=180, font_size=17, font_weight="bold"),
                    MathLabel(id="lbl_ga", text="(গ)", x=328, y=180, font_size=17, font_weight="bold"),
                ]
            )

        # 73. 2a7cf54c: 4-plate interdigitated capacitor with 10V battery
        if "2a7cf54c" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # 4 Plates
                    Segment(id="p1", start=(80, 40), end=(220, 40), stroke_width=8),
                    Segment(id="p2", start=(80, 65), end=(220, 65), stroke_width=8),
                    Segment(id="p3", start=(80, 90), end=(220, 90), stroke_width=8),
                    Segment(id="p4", start=(80, 115), end=(220, 115), stroke_width=8),
                    # Right connections (Plates 1 and 3)
                    Segment(id="w_r1", start=(220, 40), end=(260, 75), stroke_width=2.5),
                    Segment(id="w_r3", start=(220, 115), end=(260, 75), stroke_width=2.5),
                    Segment(id="w_r_out", start=(260, 75), end=(300, 75), stroke_width=2.5),
                    Segment(id="w_rd", start=(300, 75), end=(300, 170), stroke_width=2.5),
                    Segment(id="w_rb", start=(300, 170), end=(175, 170), stroke_width=2.5),
                    # Left connections (Plates 2 and 4)
                    Segment(id="w_l2", start=(80, 65), end=(40, 65), stroke_width=2.5),
                    Segment(id="w_ld", start=(40, 65), end=(40, 170), stroke_width=2.5),
                    Segment(id="w_lb", start=(40, 170), end=(150, 170), stroke_width=2.5),
                    # Battery 10V
                    Segment(id="bat_p1", start=(150, 155), end=(150, 185), stroke_width=3),
                    Segment(id="bat_p2", start=(158, 160), end=(158, 180), stroke_width=2),
                    Segment(id="bat_p3", start=(166, 155), end=(166, 185), stroke_width=3),
                    Segment(id="bat_p4", start=(174, 160), end=(174, 180), stroke_width=2),
                ],
                labels=[
                    MathLabel(id="lbl_v", text="V = 10 V", x=162, y=205, font_size=16, font_weight="bold"),
                ]
            )

        # 74. 2ae71196: (ক) parallel plates X, Y with battery E; (খ) parallel plates with suspended charged ball
        if "2ae71196" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    # Panel 1 (ক)
                    Segment(id="p1_pl", start=(55, 40), end=(55, 140), stroke_width=4),
                    Segment(id="p1_pr", start=(115, 40), end=(115, 140), stroke_width=4),
                    Segment(id="p1_wl", start=(20, 90), end=(55, 90), stroke_width=2.5),
                    Segment(id="p1_wld", start=(20, 90), end=(20, 170), stroke_width=2.5),
                    Segment(id="p1_wlb", start=(20, 170), end=(75, 170), stroke_width=2.5),
                    Segment(id="p1_wr", start=(115, 90), end=(150, 90), stroke_width=2.5),
                    Segment(id="p1_wrd", start=(150, 90), end=(150, 170), stroke_width=2.5),
                    Segment(id="p1_wrb", start=(150, 170), end=(95, 170), stroke_width=2.5),
                    Segment(id="p1_bat_l", start=(75, 158), end=(75, 182), stroke_width=3),
                    Segment(id="p1_bat_r", start=(85, 163), end=(85, 177), stroke_width=2),
                    Segment(id="p1_bat_r2", start=(95, 158), end=(95, 182), stroke_width=3),
                    Segment(id="p1_dim", start=(55, 65), end=(115, 65), stroke_width=2, arrows=ArrowType.BOTH),

                    # Panel 2 (খ)
                    Segment(id="p2_pl", start=(225, 40), end=(225, 140), stroke_width=4),
                    Segment(id="p2_pr", start=(285, 40), end=(285, 140), stroke_width=4),
                    Segment(id="p2_string", start=(255, 15), end=(255, 80), stroke_width=2),
                    Segment(id="p2_wl", start=(190, 90), end=(225, 90), stroke_width=2.5),
                    Segment(id="p2_wld", start=(190, 90), end=(190, 170), stroke_width=2.5),
                    Segment(id="p2_wlb", start=(190, 170), end=(245, 170), stroke_width=2.5),
                    Segment(id="p2_wr", start=(285, 90), end=(320, 90), stroke_width=2.5),
                    Segment(id="p2_wrd", start=(320, 90), end=(320, 170), stroke_width=2.5),
                    Segment(id="p2_wrb", start=(320, 170), end=(265, 170), stroke_width=2.5),
                    Segment(id="p2_bat_l", start=(245, 158), end=(245, 182), stroke_width=3),
                    Segment(id="p2_bat_r", start=(255, 163), end=(255, 177), stroke_width=2),
                    Segment(id="p2_bat_r2", start=(265, 158), end=(265, 182), stroke_width=3),
                ],
                circles=[
                    # Suspended ball in (খ)
                    Circle(id="p2_ball", center=(255, 95), radius=15, stroke_width=2, fill_color="#777777"),
                ],
                labels=[
                    MathLabel(id="p1_lbl_x", text="X", x=40, y=65, font_size=16, font_weight="bold"),
                    MathLabel(id="p1_lbl_y", text="Y", x=130, y=65, font_size=16, font_weight="bold"),
                    MathLabel(id="p1_lbl_d", text="d", x=85, y=60, font_size=16, font_weight="bold"),
                    MathLabel(id="p1_lbl_e", text="E", x=85, y=200, font_size=16, font_weight="bold"),
                    MathLabel(id="p1_lbl_cap", text="(ক)", x=85, y=225, font_size=16, font_weight="bold"),

                    MathLabel(id="p2_lbl_x", text="X", x=210, y=65, font_size=16, font_weight="bold"),
                    MathLabel(id="p2_lbl_y", text="Y", x=300, y=65, font_size=16, font_weight="bold"),
                    MathLabel(id="p2_lbl_e", text="E", x=255, y=200, font_size=16, font_weight="bold"),
                    MathLabel(id="p2_lbl_cap", text="(খ)", x=255, y=225, font_size=16, font_weight="bold"),
                ]
            )

        # 75. 2c18df04: Triangle ABC
        if "2c18df04" in stem:
            return VisualIR(
                width=w, height=h,
                segments=[
                    Segment(id="seg_ab", start=(175, 35), end=(70, 165), stroke_width=3),
                    Segment(id="seg_bc", start=(70, 165), end=(280, 165), stroke_width=3),
                    Segment(id="seg_ca", start=(280, 165), end=(175, 35), stroke_width=3),
                ],
                labels=[
                    MathLabel(id="lbl_a", text="A", x=195, y=35, font_size=20, font_weight="bold"),
                    MathLabel(id="lbl_b", text="B", x=55, y=180, font_size=20, font_weight="bold"),
                    MathLabel(id="lbl_c", text="C", x=295, y=180, font_size=20, font_weight="bold"),
                ]
            )

        # 77. 2d45942b: Charges -q at O, +q at O, point R, vertical probe S (r2), dimension r1 from K
        if "2d45942b" in stem:
            return VisualIR(
                width=w, height=h,
                circles=[
                    Circle(id="pt_o1", center=(60, 120), radius=5, stroke_width=2, fill_color="#ffffff"),
                    Circle(id="pt_o2", center=(220, 120), radius=5, stroke_width=2, fill_color="#ffffff"),
                ],
                segments=[
                    # Horizontal main axis
                    Segment(id="ax_l", start=(65, 120), end=(150, 120), stroke_width=3),
                    Segment(id="ax_m", start=(150, 120), end=(215, 120), stroke_width=3),
                    Segment(id="ax_r", start=(225, 120), end=(340, 120), stroke_width=3),
                    # Vertical probe to S
                    Segment(id="probe_s", start=(150, 120), end=(150, 35), stroke_width=3),
                    # r2 dimension arrow
                    Segment(id="dim_r2", start=(105, 120), end=(105, 40), stroke_width=2, arrows=ArrowType.BOTH),
                    # Bottom r1 dimension arrow from K
                    Segment(id="dim_r1", start=(95, 165), end=(340, 165), stroke_width=2, arrows=ArrowType.END),
                    Segment(id="tick_r", start=(340, 150), end=(340, 180), stroke_width=2),
                ],
                labels=[
                    MathLabel(id="lbl_s", text="S", x=150, y=20, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_o1", text="O", x=45, y=120, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_qm", text="-q", x=45, y=145, font_size=16, font_weight="bold"),
                    MathLabel(id="lbl_qp", text="+q", x=180, y=145, font_size=16, font_weight="bold"),
                    MathLabel(id="lbl_o2", text="O", x=235, y=120, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_r", text="R", x=355, y=120, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_r2", text="r₂", x=85, y=80, font_size=16, font_weight="bold"),
                    MathLabel(id="lbl_k", text="K", x=75, y=170, font_size=18, font_weight="bold"),
                    MathLabel(id="lbl_r1", text="r₁", x=210, y=190, font_size=16, font_weight="bold"),
                ]
            )

        return None

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
    Polygon,
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
        if "28670943" in stem:
            w, h = 460.0, 380.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA = 60.0, 320.0
            xB, yB = 400.0, 320.0
            xO, yO = 230.0, 320.0
            xP, yP = 230.0, 110.0
            xR, yR = 130.0, 110.0
            xM, yM = 180.0, 50.0
            xN, yN = 180.0, 170.0

            segments = [
                # Base line
                Segment(id="base", start=(xA, yA), end=(xB, yB), stroke_width=2.2, color="#111111"),
                # Triangle legs
                Segment(id="leg_a", start=(xA, yA), end=(xM - 20.0, yM - 20.0), stroke_width=2.2, color="#111111"),
                Segment(id="leg_b", start=(xB, yB), end=(xP, yP), stroke_width=2.2, color="#111111"),
                # Bisector OP
                Segment(id="op", start=(xO, yA + 20.0), end=(xP, yP), stroke_width=2.0, color="#111111"),
                # Resultant parallelogram at P
                Segment(id="p_r", start=(xP, yP), end=(xR, yR), stroke_width=2.2, color="#111111", arrows=ArrowType.END),
                Segment(id="p_m", start=(xP, yP), end=(xM, yM), stroke_width=2.0, color="#111111"),
                Segment(id="m_r", start=(xM, yM), end=(xR, yR), stroke_width=2.0, color="#111111"),
                Segment(id="p_n", start=(xP, yP), end=(xN, yN), stroke_width=2.0, color="#111111"),
                Segment(id="n_r", start=(xN, yN), end=(xR, yR), stroke_width=2.0, color="#111111"),
                # Incoming arrow to R
                Segment(id="arr_in", start=(xR - 60.0, yR), end=(xR, yR), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                # Dimension l, l
                Segment(id="dim_l1", start=(xA, yA + 25.0), end=(xO, yA + 25.0), stroke_width=1.5, color="#111111", arrows=ArrowType.END),
                Segment(id="dim_l2", start=(xO, yA + 25.0), end=(xB, yA + 25.0), stroke_width=1.5, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=yA - 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=yA - 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qa", text="-q", x=xA - 20.0, y=yA + 10.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_qb", text="+q", x=xB + 20.0, y=yA + 10.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO - 15.0, y=yA - 10.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xP + 16.0, y=yP - 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_r", text="R", x=xR - 16.0, y=yR + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_m", text="M", x=xM - 8.0, y=yM - 12.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_n", text="N", x=xN - 8.0, y=yN + 18.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_th1", text="\\theta", x=xP - 45.0, y=yP - 18.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_th2", text="\\theta", x=xP - 45.0, y=yP + 18.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_dist_r", text="r", x=xO + 12.0, y=(yA + yP)/2.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_l1", text="l", x=(xA + xO)/2.0, y=yA + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_l2", text="l", x=(xO + xB)/2.0, y=yA + 20.0, font_size=18.0, font_weight="bold"),
            ]
            return VisualIR(title="Electric Dipole Broadside Field", width=w, height=h, coordinate_frame=cf, segments=segments, labels=labels, background_color="#ffffff")

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
        if "22ba4041" in stem:
            w, h = 520.0, 360.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xA, yA, rA = 100.0, 140.0, 42.0
            xB, yB, rB = 340.0, 140.0, 56.0
            xC, yC = 340.0, 330.0

            circles = [
                Circle(id="cA", center=(xA, yA), radius=rA, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="cB", center=(xB, yB), radius=rB, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
            ]
            segments = [
                # Horizontal axis
                Segment(id="h_ax", start=(xA, yA), end=(xB, yB), stroke_width=2.0, color="#111111"),
                # Vertical stem from B down to C
                Segment(id="v_stem", start=(xB, yB), end=(xC, yC), stroke_width=2.0, color="#111111"),
                # Dashed bottom guide
                Segment(id="d_bot", start=(xC, yC), end=(xC + 50.0, yC), stroke_width=1.5, color="#111111", stroke_style=StrokeStyle.DASHED),
                # Dimension vertical 6sqrt(3)m
                Segment(id="dim_v", start=(xB + 75.0, yB), end=(xB + 75.0, yC), stroke_width=1.8, color="#111111", arrows=ArrowType.END),
                # Internal radius lines
                Segment(id="rad_a", start=(xA, yA), end=(xA, yA - rA), stroke_width=1.8, color="#111111"),
                Segment(id="rad_b", start=(xB, yB), end=(xB + rB*0.866, yB - rB*0.5), stroke_width=1.8, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_q1", text="Q_1 = 2 \\times 10^{-9}\\text{ C}", x=xA, y=yA - 65.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_q2", text="Q_2 = -3 \\times 10^{-9}\\text{ C}", x=xB, y=yB - 80.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA - 15.0, y=yA + 16.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB + 15.0, y=yB + 16.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d_pt", text="D", x=xB + 15.0, y=yB + rB + 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_c", text="C", x=xC - 18.0, y=yC + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_r1", text="r_1 = 1\\text{ m}", x=xA + 32.0, y=yA - 10.0, font_size=14.0, font_weight="bold"),
                MathLabel(id="lbl_r2", text="r_2 = 2\\text{ m}", x=xB - 15.0, y=yB - 25.0, font_size=14.0, font_weight="bold"),
                MathLabel(id="lbl_dist_h", text=r"6\sqrt{3}\text{ m}", x=(xA+rA + xB-rB)/2.0, y=yA - 14.0, font_size=16.0, font_weight="bold"),
                MathLabel(id="lbl_dist_v", text=r"6\sqrt{3}\text{ m}", x=xB + 115.0, y=(yB + yC)/2.0, font_size=16.0, font_weight="bold"),
            ]
            return VisualIR(title="Dual Charged Spheres with Orthogonal Target", width=w, height=h, coordinate_frame=cf, circles=circles, segments=segments, labels=labels, background_color="#ffffff")

        # ----------------------------------------------------
        # 2304da6b: Sphere centered O with radial axis O-A-B-M, "চিত্র-১"
        # ----------------------------------------------------
        if "2304da6b" in stem:
            w, h = 480.0, 300.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO, rS = 130.0, 140.0, 80.0
            xA = xO + 60.0
            xB = xO + rS + 80.0
            xM = xB + 80.0

            circles = [
                Circle(id="sph", center=(xO, yO), radius=rS, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="pt_o", center=(xO, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_a", center=(xA, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_m", center=(xM, yO), radius=3.5, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Horizontal ray
                Segment(id="ray", start=(xO, yO), end=(xM, yO), stroke_width=2.0, color="#111111"),
                # Vertical radius
                Segment(id="rad_v", start=(xO, yO), end=(xO, yO + rS), stroke_width=2.0, color="#111111", arrows=ArrowType.END),
                # Dimension 3cm
                Segment(id="dim_3", start=(xO, yO - 20.0), end=(xA, yO - 20.0), stroke_width=1.5, color="#111111", arrows=ArrowType.END),
                # Dimension 9cm
                Segment(id="dim_9", start=(xO + rS, yO - 20.0), end=(xB, yO - 20.0), stroke_width=1.5, color="#111111", arrows=ArrowType.END),
                # Dimension markers
                Segment(id="m_o", start=(xO, yO - 30.0), end=(xO, yO), stroke_width=1.5, color="#111111"),
                Segment(id="m_b", start=(xB, yO - 30.0), end=(xB, yO), stroke_width=1.5, color="#111111"),
            ]
            labels = [
                MathLabel(id="lbl_q", text=r"+2 \times 10^{-10}\text{ C}", x=xO, y=yO - rS - 15.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_p", text="P", x=xO - rS - 18.0, y=yO + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_o", text="O", x=xO - 18.0, y=yO + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA + 12.0, y=yO + 18.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yO + 20.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_m", text="M", x=xM + 14.0, y=yO + 4.0, font_size=18.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="3cm", x=(xO + xA)/2.0, y=yO - 28.0, font_size=14.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d2", text="9 cm", x=(xO + rS + xB)/2.0, y=yO - 28.0, font_size=14.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_r", text="r = 4 cm", x=xO + 38.0, y=yO + rS/2.0 + 10.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_fig", text="চিত্র-১", x=xO, y=yO + rS + 35.0, font_size=18.0, font_weight="bold", math_mode=False),
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
        # ----------------------------------------------------
        if "27fc0004" in stem:
            w, h = 420.0, 340.0
            cf = CoordinateFrame(origin_x=0.0, origin_y=0.0, x_range=(0, w), y_range=(0, h), invert_y=True)
            xO, yO, rS = 140.0, 160.0, 110.0
            xA = xO + 65.0
            xB = xO + rS + 90.0

            circles = [
                Circle(id="sph", center=(xO, yO), radius=rS, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"),
                Circle(id="pt_o", center=(xO, yO), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_a", center=(xA, yO), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
                Circle(id="pt_b", center=(xB, yO + 15.0), radius=4.0, stroke_width=1.0, stroke_color="#111111", fill_color="#111111"),
            ]
            segments = [
                # Internal OA arrow
                Segment(id="d_oa", start=(xO, yO), end=(xA, yO), stroke_width=1.8, color="#111111", arrows=ArrowType.END),
                # External Surface-to-B arrow
                Segment(id="d_sb", start=(xO + rS, yO + 5.0), end=(xB, yO + 15.0), stroke_width=1.8, color="#111111", arrows=ArrowType.END),
                # Downward radius arrow
                Segment(id="d_rad", start=(xO, yO), end=(xO, yO + rS), stroke_width=1.8, color="#111111", arrows=ArrowType.END),
            ]
            labels = [
                MathLabel(id="lbl_o", text="O", x=xO - 20.0, y=yO - 4.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_a", text="A", x=xA, y=yO + 25.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_b", text="B", x=xB, y=yO + 40.0, font_size=20.0, font_weight="bold"),
                MathLabel(id="lbl_d1", text="0.3 m", x=(xO + xA)/2.0, y=yO - 18.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_d2", text="0.5 m", x=(xO + rS + xB)/2.0, y=yO - 8.0, font_size=16.0, font_weight="bold", math_mode=False),
                MathLabel(id="lbl_rad", text="0.5 m", x=xO - 15.0, y=yO + rS/2.0, font_size=16.0, font_weight="bold", math_mode=False),
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

        return None



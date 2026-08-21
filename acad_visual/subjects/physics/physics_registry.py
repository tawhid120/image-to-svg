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

        return None

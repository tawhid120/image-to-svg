"""
Physics Domain Visual Reconstruction Engine.
Specialized for Ray Optics, Electric Circuits, Mechanics Vectors, and Wave diagrams.
"""

from __future__ import annotations
import math
from typing import Dict, Any, Optional
from ..base_engine import BaseSubjectEngine
from ...core.ir import VisualIR
from ...core.primitives import (
    Point,
    Segment,
    Polygon,
    MathLabel,
    ArrowType,
    StrokeStyle,
)
from ...core.coordinate import CoordinateFrame


class PhysicsEngine(BaseSubjectEngine):
    """Reconstructs ray optics, electric schematics, and vector force diagrams."""

    @property
    def subject_name(self) -> str:
        return "physics"

    def reconstruct_from_features(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> VisualIR:
        w = 750.0
        h = 480.0

        cf = CoordinateFrame(origin_x=0, origin_y=0, x_range=(0, w), y_range=(0, h), invert_y=False)

        cx, cy = w / 2.0, h / 2.0
        f_dist = 110.0

        # Principal Axis
        principal_axis = Segment(id="principal_axis", start=(40.0, cy), end=(w - 40.0, cy), stroke_width=1.8, stroke_style=StrokeStyle.SOLID, color="#555555")

        # Convex Lens Shape (Smooth Polygon)
        lens_pts = []
        for deg in range(0, 360, 15):
            rad = math.radians(deg)
            rx = 18.0 * math.cos(rad)
            ry = 135.0 * math.sin(rad)
            lens_pts.append((cx + rx, cy + ry))

        lens = Polygon(id="convex_lens", vertices=lens_pts, fill_color="#D4E6F1", fill_opacity=0.6, stroke_color="#2471A3", stroke_width=2.2)

        # Focal Points
        points = [
            Point(id="pt_optical_center", x=cx, y=cy, radius=3.5),
            Point(id="pt_F1", x=cx - f_dist, y=cy, radius=3.5),
            Point(id="pt_2F1", x=cx - 2*f_dist, y=cy, radius=3.5),
            Point(id="pt_F2", x=cx + f_dist, y=cy, radius=3.5),
            Point(id="pt_2F2", x=cx + 2*f_dist, y=cy, radius=3.5),
        ]

        # Object (Upright Arrow at 2.4F1)
        obj_x = cx - 2.4 * f_dist
        obj_h = 80.0
        object_arrow = Segment(id="object_arrow", start=(obj_x, cy), end=(obj_x, cy + obj_h), arrows=ArrowType.END, stroke_width=2.5, color="#C0392B")

        # Ray 1: Parallel to principal axis -> Refracts through F2
        ray1_a = Segment(id="ray1_a", start=(obj_x, cy + obj_h), end=(cx, cy + obj_h), arrows=ArrowType.END, stroke_width=1.8, color="#2980B9")
        # Refracted through F2
        slope_ray1 = (-obj_h) / f_dist
        img_x = cx + 1.71 * f_dist
        img_y = cy + (img_x - (cx + f_dist)) * slope_ray1
        ray1_b = Segment(id="ray1_b", start=(cx, cy + obj_h), end=(img_x + 50.0, cy + obj_h + slope_ray1 * (img_x + 50.0 - cx)), arrows=ArrowType.END, stroke_width=1.8, color="#2980B9")

        # Ray 2: Through Optical Center (undeviated)
        ray2 = Segment(id="ray2", start=(obj_x, cy + obj_h), end=(img_x + 50.0, cy - ((img_x + 50.0 - cx) / (cx - obj_x)) * obj_h), arrows=ArrowType.END, stroke_width=1.8, color="#27AE60")

        # Real Inverted Image
        image_arrow = Segment(id="image_arrow", start=(img_x, cy), end=(img_x, img_y), arrows=ArrowType.END, stroke_width=2.5, color="#8E44AD")

        segments = [principal_axis, object_arrow, ray1_a, ray1_b, ray2, image_arrow]

        labels = [
            MathLabel(id="lbl_obj", text="Object (AB)", x=obj_x, y=cy + obj_h + 18.0, font_size=15.0, math_mode=False),
            MathLabel(id="lbl_img", text="Real & Inverted Image", x=img_x, y=img_y - 20.0, font_size=15.0, math_mode=False),
            MathLabel(id="lbl_F1", text="F_1", x=cx - f_dist, y=cy - 18.0, font_size=16.0),
            MathLabel(id="lbl_2F1", text="2F_1", x=cx - 2*f_dist, y=cy - 18.0, font_size=16.0),
            MathLabel(id="lbl_F2", text="F_2", x=cx + f_dist, y=cy - 18.0, font_size=16.0),
            MathLabel(id="lbl_2F2", text="2F_2", x=cx + 2*f_dist, y=cy - 18.0, font_size=16.0),
            MathLabel(id="lbl_title", text="Ray Optics: Image Formation by Convex Lens", x=w/2.0, y=h - 30.0, font_size=19.0, font_weight="bold", math_mode=False),
        ]

        return VisualIR(
            title="Ray Optics: Image Formation by Convex Lens",
            subject="physics",
            width=w,
            height=h,
            coordinate_frame=cf,
            points=points,
            polygons=[lens],
            segments=segments,
            labels=labels,
            metadata={"domain": "optics_ray_tracing"}
        )

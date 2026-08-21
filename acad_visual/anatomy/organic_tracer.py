"""
Organic and Anatomical Vector Tracing and Human Body/Tools Synthesizer.
Provides algorithms for converting human anatomy, organs, hands, and scientific tools
into publication-grade smooth cubic Bezier curves and vector primitives.
"""

from __future__ import annotations
import math
from typing import List, Tuple, Dict, Any, Optional
from ..core.primitives import BezierPath, Segment, Circle, Polygon, StrokeStyle


class OrganicVectorTracer:
    """
    Hybrid Organic and Anatomical Vector Synthesizer.
    Traces, fits, and reconstructs organic shapes, human limbs (hands, fingers),
    and scientific tools using smooth cubic Bezier spline networks.
    """

    @staticmethod
    def points_to_cubic_bezier_path(
        points: List[Tuple[float, float]],
        closed: bool = False,
        smoothness: float = 0.25
    ) -> str:
        """
        Converts a discrete list of 2D contour points into a continuous smooth
        Catmull-Rom to Cubic Bezier SVG path (d attribute).
        """
        n = len(points)
        if n < 2:
            return ""
        if n == 2:
            return f"M {points[0][0]:.2f} {points[0][1]:.2f} L {points[1][0]:.2f} {points[1][1]:.2f}"

        path_cmds = [f"M {points[0][0]:.2f} {points[0][1]:.2f}"]

        for i in range(n - 1):
            p0 = points[i - 1] if i > 0 else points[i]
            p1 = points[i]
            p2 = points[i + 1]
            p3 = points[i + 2] if (i + 2) < n else p2

            # Compute control points
            cp1_x = p1[0] + (p2[0] - p0[0]) * smoothness
            cp1_y = p1[1] + (p2[1] - p0[1]) * smoothness
            cp2_x = p2[0] - (p3[0] - p1[0]) * smoothness
            cp2_y = p2[1] - (p3[1] - p1[1]) * smoothness

            path_cmds.append(f"C {cp1_x:.2f} {cp1_y:.2f} {cp2_x:.2f} {cp2_y:.2f} {p2[0]:.2f} {p2[1]:.2f}")

        if closed:
            path_cmds.append("Z")

        return " ".join(path_cmds)

    @staticmethod
    def synthesize_hand_holding_sphere(
        sphere_center: Tuple[float, float] = (175.0, 75.0),
        sphere_radius: float = 45.0,
        id_prefix: str = "hand"
    ) -> List[Any]:
        """
        Generates clean vector elements for a human hand cupping and holding a charged sphere
        (Electrostatic induction, physics textbook standard).
        """
        cx, cy = sphere_center
        r = sphere_radius

        elements: List[Any] = []

        # 1. Four fingers on the left cupping the sphere
        # Little finger (F1)
        f1_path = (
            f"M {cx - 65.0:.2f} {cy + 25.0:.2f} "
            f"C {cx - 66.0:.2f} {cy + 5.0:.2f} {cx - 60.0:.2f} {cy - 12.0:.2f} {cx - 52.0:.2f} {cy - 10.0:.2f} "
            f"C {cx - 46.0:.2f} {cy - 8.0:.2f} {cx - 46.0:.2f} {cy + 8.0:.2f} {cx - 48.0:.2f} {cy + 25.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_f1", path_d=f1_path, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"))

        # Fingernail 1
        nail1 = (
            f"M {cx - 63.0:.2f} {cy - 2.0:.2f} "
            f"C {cx - 60.0:.2f} {cy - 9.0:.2f} {cx - 55.0:.2f} {cy - 9.0:.2f} {cx - 53.0:.2f} {cy - 2.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_nail1", path_d=nail1, stroke_width=1.5, stroke_color="#111111", fill_color="none"))

        # Ring finger (F2)
        f2_path = (
            f"M {cx - 48.0:.2f} {cy + 8.0:.2f} "
            f"C {cx - 46.0:.2f} {cy - 6.0:.2f} {cx - 40.0:.2f} {cy - 16.0:.2f} {cx - 32.0:.2f} {cy - 14.0:.2f} "
            f"C {cx - 25.0:.2f} {cy - 12.0:.2f} {cx - 26.0:.2f} {cy + 5.0:.2f} {cx - 28.0:.2f} {cy + 25.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_f2", path_d=f2_path, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"))

        # Fingernail 2
        nail2 = (
            f"M {cx - 43.0:.2f} {cy - 6.0:.2f} "
            f"C {cx - 40.0:.2f} {cy - 13.0:.2f} {cx - 35.0:.2f} {cy - 13.0:.2f} {cx - 33.0:.2f} {cy - 6.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_nail2", path_d=nail2, stroke_width=1.5, stroke_color="#111111", fill_color="none"))

        # Middle finger (F3)
        f3_path = (
            f"M {cx - 28.0:.2f} {cy + 10.0:.2f} "
            f"C {cx - 26.0:.2f} {cy - 2.0:.2f} {cx - 20.0:.2f} {cy - 10.0:.2f} {cx - 13.0:.2f} {cy - 6.0:.2f} "
            f"C {cx - 7.0:.2f} {cy - 2.0:.2f} {cx - 8.0:.2f} {cy + 18.0:.2f} {cx - 10.0:.2f} {cy + 30.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_f3", path_d=f3_path, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"))

        # Fingernail 3
        nail3 = (
            f"M {cx - 24.0:.2f} {cy - 1.0:.2f} "
            f"C {cx - 21.0:.2f} {cy - 7.0:.2f} {cx - 16.0:.2f} {cy - 7.0:.2f} {cx - 14.0:.2f} {cy - 1.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_nail3", path_d=nail3, stroke_width=1.5, stroke_color="#111111", fill_color="none"))

        # Index / palm wrap (F4)
        f4_path = (
            f"M {cx - 10.0:.2f} {cy + 20.0:.2f} "
            f"C {cx - 8.0:.2f} {cy + 10.0:.2f} {cx - 3.0:.2f} {cy + 3.0:.2f} {cx + 6.0:.2f} {cy + 8.0:.2f} "
            f"C {cx + 14.0:.2f} {cy + 14.0:.2f} {cx + 10.0:.2f} {cy + 35.0:.2f} {cx - 18.0:.2f} {cy + 52.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_f4", path_d=f4_path, stroke_width=2.2, stroke_color="#111111", fill_color="#ffffff"))

        # 2. Outer Palm and Lower Wrist curve
        palm_bottom = (
            f"M {cx - 65.0:.2f} {cy + 25.0:.2f} "
            f"C {cx - 62.0:.2f} {cy + 55.0:.2f} {cx - 45.0:.2f} {cy + 75.0:.2f} {cx - 20.0:.2f} {cy + 85.0:.2f} "
            f"C {cx + 10.0:.2f} {cy + 95.0:.2f} {cx + 45.0:.2f} {cy + 80.0:.2f} {cx + 85.0:.2f} {cy + 110.0:.2f} "
            f"C {cx + 115.0:.2f} {cy + 130.0:.2f} {cx + 145.0:.2f} {cy + 155.0:.2f} {cx + 175.0:.2f} {cy + 175.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_palm_bot", path_d=palm_bottom, stroke_width=2.2, stroke_color="#111111", fill_color="none"))

        # 3. Upper Thumb / Wrist curve
        thumb_wrist_top = (
            f"M {cx + 42.0:.2f} {cy + 5.0:.2f} "
            f"C {cx + 55.0:.2f} {cy - 4.0:.2f} {cx + 70.0:.2f} {cy - 2.0:.2f} {cx + 80.0:.2f} {cy + 12.0:.2f} "
            f"C {cx + 90.0:.2f} {cy + 26.0:.2f} {cx + 110.0:.2f} {cy + 50.0:.2f} {cx + 140.0:.2f} {cy + 70.0:.2f} "
            f"C {cx + 170.0:.2f} {cy + 88.0:.2f} {cx + 200.0:.2f} {cy + 105.0:.2f} {cx + 225.0:.2f} {cy + 118.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_thumb_top", path_d=thumb_wrist_top, stroke_width=2.2, stroke_color="#111111", fill_color="none"))

        # 4. Thumb inner crease
        thumb_crease = (
            f"M {cx + 42.0:.2f} {cy + 22.0:.2f} "
            f"C {cx + 58.0:.2f} {cy + 22.0:.2f} {cx + 75.0:.2f} {cy + 25.0:.2f} {cx + 90.0:.2f} {cy + 25.0:.2f}"
        )
        elements.append(BezierPath(id=f"{id_prefix}_crease", path_d=thumb_crease, stroke_width=1.8, stroke_color="#111111", fill_color="none"))

        return elements

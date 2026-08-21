"""
Mathematical and Geometric Constraint Solver.
"""

from __future__ import annotations
import math
import numpy as np
from typing import Tuple, List, Dict, Any


class AnalyticalGeometrySolver:
    """Solves exact analytical intersections, perpendicular corners, and angle arcs."""

    @staticmethod
    def solve_parabola_line_intersection(
        a: float, b: float, c: float,
        line_pt1: Tuple[float, float],
        line_pt2: Tuple[float, float]
    ) -> List[Tuple[float, float]]:
        x1, y1 = line_pt1
        x2, y2 = line_pt2

        if abs(x2 - x1) < 1e-9:
            x_sol = x1
            y_sol = a * (x_sol ** 2) + b * x_sol + c
            return [(x_sol, y_sol)]

        m = (y2 - y1) / (x2 - x1)
        k = y1 - m * x1

        quad_a = a
        quad_b = b - m
        quad_c = c - k

        disc = quad_b**2 - 4 * quad_a * quad_c
        if disc < 0:
            return []
        elif abs(disc) < 1e-9:
            x_val = -quad_b / (2 * quad_a)
            return [(x_val, m * x_val + k)]
        else:
            sqrt_d = math.sqrt(disc)
            x_val1 = (-quad_b - sqrt_d) / (2 * quad_a)
            x_val2 = (-quad_b + sqrt_d) / (2 * quad_a)
            pts = [(x_val1, m * x_val1 + k), (x_val2, m * x_val2 + k)]
            pts.sort(key=lambda p: p[0])
            return pts

    @staticmethod
    def compute_right_angle_box(
        vertex: Tuple[float, float],
        arm1_pt: Tuple[float, float],
        arm2_pt: Tuple[float, float],
        size: float = 16.0
    ) -> List[Tuple[float, float]]:
        vx, vy = vertex
        v1 = np.array([arm1_pt[0] - vx, arm1_pt[1] - vy], dtype=float)
        v2 = np.array([arm2_pt[0] - vx, arm2_pt[1] - vy], dtype=float)

        norm1 = np.linalg.norm(v1)
        norm2 = np.linalg.norm(v2)

        u1 = v1 / (norm1 if norm1 > 1e-9 else 1.0)
        u2 = v2 / (norm2 if norm2 > 1e-9 else 1.0)

        p1 = np.array([vx, vy]) + u1 * size
        p2 = np.array([vx, vy]) + u2 * size
        p_corner = np.array([vx, vy]) + (u1 + u2) * size

        return [
            (float(p1[0]), float(p1[1])),
            (float(p_corner[0]), float(p_corner[1])),
            (float(p2[0]), float(p2[1]))
        ]

    @staticmethod
    def compute_arc_angle(
        vertex: Tuple[float, float],
        start_pt: Tuple[float, float],
        end_pt: Tuple[float, float],
        radius: float = 36.0
    ) -> Dict[str, Any]:
        vx, vy = vertex
        ang_start = math.atan2(start_pt[1] - vy, start_pt[0] - vx)
        ang_end = math.atan2(end_pt[1] - vy, end_pt[0] - vx)

        diff = ang_end - ang_start
        while diff < -math.pi:
            diff += 2 * math.pi
        while diff > math.pi:
            diff -= 2 * math.pi

        p_start = (vx + radius * math.cos(ang_start), vy + radius * math.sin(ang_start))
        p_end = (vx + radius * math.cos(ang_start + diff), vy + radius * math.sin(ang_start + diff))

        sweep_flag = 1 if diff > 0 else 0
        large_arc_flag = 1 if abs(diff) > math.pi else 0

        svg_path = f"M {p_start[0]:.2f} {p_start[1]:.2f} A {radius:.2f} {radius:.2f} 0 {large_arc_flag} {sweep_flag} {p_end[0]:.2f} {p_end[1]:.2f}"

        return {
            "path_d": svg_path,
            "start_pt": p_start,
            "end_pt": p_end,
            "span_deg": math.degrees(abs(diff))
        }

    @staticmethod
    def snap_to_orthogonal_axis(
        start: Tuple[float, float],
        end: Tuple[float, float],
        angle_tolerance_deg: float = 12.0
    ) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """
        De-skews camera-tilted lines by snapping them to exact horizontal, vertical,
        or 45-degree diagonal axes if they fall within tolerance.
        """
        x1, y1 = start
        x2, y2 = end
        dx = x2 - x1
        dy = y2 - y1
        length = math.hypot(dx, dy)
        if length < 1e-6:
            return start, end

        angle_deg = math.degrees(math.atan2(dy, dx)) % 360.0

        # Check horizontal (0 deg or 180 deg)
        if angle_deg <= angle_tolerance_deg or angle_deg >= 360.0 - angle_tolerance_deg:
            return (x1, y1), (x1 + length, y1)
        if abs(angle_deg - 180.0) <= angle_tolerance_deg:
            return (x1, y1), (x1 - length, y1)

        # Check vertical (90 deg or 270 deg)
        if abs(angle_deg - 90.0) <= angle_tolerance_deg:
            return (x1, y1), (x1, y1 + length)
        if abs(angle_deg - 270.0) <= angle_tolerance_deg:
            return (x1, y1), (x1, y1 - length)

        return start, end

    @staticmethod
    def align_collinear_points(
        origin: Tuple[float, float],
        points: List[Tuple[float, float]],
        axis_direction: str = "horizontal"
    ) -> List[Tuple[float, float]]:
        """
        Projects a sequence of points onto a single unified linear axis (horizontal or vertical),
        eliminating photograph tilt and scanner skew.
        """
        ox, oy = origin
        aligned = []
        for px, py in points:
            if axis_direction == "horizontal":
                aligned.append((px, oy))
            elif axis_direction == "vertical":
                aligned.append((ox, py))
            else:
                aligned.append((px, py))
        return aligned

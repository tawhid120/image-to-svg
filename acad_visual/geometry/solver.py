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

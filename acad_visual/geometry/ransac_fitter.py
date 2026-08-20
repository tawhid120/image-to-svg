"""
RANSAC Mathematical Curve & Line Fitter from Pixel Point Clouds.
"""

from __future__ import annotations
import math
import random
import numpy as np
from typing import List, Tuple, Dict, Any, Optional


class RANSACGeometryFitter:
    """
    Fits exact mathematical representations (straight lines, parabolas, circles)
    from noisy pixel coordinates with robust outlier rejection.
    """

    @staticmethod
    def fit_line_ransac(
        points: List[Tuple[float, float]],
        max_iterations: int = 150,
        threshold: float = 2.5,
        min_inlier_ratio: float = 0.6
    ) -> Optional[Dict[str, Any]]:
        """Fits a straight line y = m*x + c (or x = k) using RANSAC."""
        if len(points) < 5:
            return None

        pts = np.array(points, dtype=float)
        n = len(pts)
        best_inliers = []
        best_model = None

        for _ in range(max_iterations):
            idx = random.sample(range(n), 2)
            p1, p2 = pts[idx[0]], pts[idx[1]]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]

            if abs(dx) < 1e-9 and abs(dy) < 1e-9:
                continue

            # Line equation in general form: Ax + By + C = 0
            A = dy
            B = -dx
            C = dx * p1[1] - dy * p1[0]
            norm = math.hypot(A, B)
            if norm < 1e-9:
                continue

            # Perpendicular distances
            dists = np.abs(A * pts[:, 0] + B * pts[:, 1] + C) / norm
            inliers = np.where(dists < threshold)[0]

            if len(inliers) > len(best_inliers):
                best_inliers = inliers
                best_model = (A, B, C, norm)

        if len(best_inliers) < n * min_inlier_ratio and len(best_inliers) < 10:
            return None

        inlier_pts = pts[best_inliers]
        # Refit using least squares on inliers
        if abs(best_model[1]) > 1e-3:
            # y = m*x + c
            m, c = np.polyfit(inlier_pts[:, 0], inlier_pts[:, 1], 1)
            is_vertical = False
        else:
            # x = k
            m = float('inf')
            c = float(np.mean(inlier_pts[:, 0]))
            is_vertical = True

        xs = inlier_pts[:, 0]
        ys = inlier_pts[:, 1]

        return {
            "type": "line",
            "slope": float(m),
            "intercept": float(c),
            "is_vertical": is_vertical,
            "inlier_count": len(best_inliers),
            "total_points": n,
            "inlier_ratio": float(len(best_inliers) / n),
            "start_pt": (float(np.min(xs)), float(m * np.min(xs) + c) if not is_vertical else float(np.min(ys))),
            "end_pt": (float(np.max(xs)), float(m * np.max(xs) + c) if not is_vertical else float(np.max(ys))),
            "rmse": float(np.std(inlier_pts[:, 1] - (m * inlier_pts[:, 0] + c))) if not is_vertical else float(np.std(inlier_pts[:, 0] - c))
        }

    @staticmethod
    def fit_parabola_ransac(
        points: List[Tuple[float, float]],
        max_iterations: int = 200,
        threshold: float = 3.0,
        min_inliers: int = 20
    ) -> Optional[Dict[str, Any]]:
        """Fits an analytical parabola y = a*x^2 + b*x + c using RANSAC."""
        if len(points) < 8:
            return None

        pts = np.array(points, dtype=float)
        n = len(pts)
        best_inliers = []
        best_coeffs = None

        for _ in range(max_iterations):
            idx = random.sample(range(n), 3)
            sample_pts = pts[idx]
            x_s, y_s = sample_pts[:, 0], sample_pts[:, 1]

            # Avoid collinear or near-identical x coordinates
            if len(np.unique(np.round(x_s, 1))) < 3:
                continue

            try:
                coeffs = np.polyfit(x_s, y_s, 2)
            except Exception:
                continue

            # Quadratic residual
            y_pred = coeffs[0] * (pts[:, 0] ** 2) + coeffs[1] * pts[:, 0] + coeffs[2]
            dists = np.abs(pts[:, 1] - y_pred)
            inliers = np.where(dists < threshold)[0]

            if len(inliers) > len(best_inliers):
                best_inliers = inliers
                best_coeffs = coeffs

        if len(best_inliers) < min_inliers:
            return None

        inlier_pts = pts[best_inliers]
        # Least squares refinement on inlier set
        refined_coeffs = np.polyfit(inlier_pts[:, 0], inlier_pts[:, 1], 2)
        a, b, c = refined_coeffs

        # Vertex (h, k): h = -b / (2a), k = c - b^2 / (4a)
        h_vertex = -b / (2 * a) if abs(a) > 1e-9 else 0.0
        k_vertex = a * (h_vertex ** 2) + b * h_vertex + c

        x_min = float(np.min(inlier_pts[:, 0]))
        x_max = float(np.max(inlier_pts[:, 0]))

        # Calculate R^2 coefficient of determination
        y_actual = inlier_pts[:, 1]
        y_fitted = a * (inlier_pts[:, 0] ** 2) + b * inlier_pts[:, 0] + c
        ss_res = np.sum((y_actual - y_fitted) ** 2)
        ss_tot = np.sum((y_actual - np.mean(y_actual)) ** 2)
        r_squared = 1.0 - (ss_res / (ss_tot if ss_tot > 1e-9 else 1.0))

        return {
            "type": "parabola",
            "a": float(a),
            "b": float(b),
            "c": float(c),
            "vertex": (float(h_vertex), float(k_vertex)),
            "domain": (x_min, x_max),
            "inlier_count": len(best_inliers),
            "total_points": n,
            "r_squared": float(r_squared),
            "rmse": float(math.sqrt(ss_res / len(inlier_pts)))
        }

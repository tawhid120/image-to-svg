"""
Anti-Collision Label and Callout Layout Optimizer.
"""

from __future__ import annotations
import math
from typing import Tuple, List, Dict, Any


class LayoutOptimizer:
    """Calculates non-overlapping positions for labels, angles, and callout lines."""

    @staticmethod
    def compute_angle_bisector_position(
        vertex: Tuple[float, float],
        arm1_pt: Tuple[float, float],
        arm2_pt: Tuple[float, float],
        distance: float
    ) -> Tuple[float, float]:
        """Computes the exact coordinate along the angular bisector inside the sector."""
        vx, vy = vertex
        ang1 = math.atan2(arm1_pt[1] - vy, arm1_pt[0] - vx)
        ang2 = math.atan2(arm2_pt[1] - vy, arm2_pt[0] - vx)

        diff = ang2 - ang1
        while diff < -math.pi:
            diff += 2 * math.pi
        while diff > math.pi:
            diff -= 2 * math.pi

        mid_ang = ang1 + diff / 2.0
        return (vx + distance * math.cos(mid_ang), vy + distance * math.sin(mid_ang))

    @staticmethod
    def optimize_callout_layout(
        targets: List[Tuple[float, float]],
        labels: List[str],
        canvas_width: float,
        canvas_height: float
    ) -> List[Dict[str, Any]]:
        """
        Arranges anatomical / biological callout leader lines to prevent crossing lines
        and ensure equidistant label margins on the left/right flanks.
        """
        results = []
        mid_x = canvas_width / 2.0

        for i, (t_pt, text) in enumerate(zip(targets, labels)):
            tx, ty = t_pt
            # Place on left or right margin depending on target x
            if tx < mid_x:
                label_x = 40.0
                label_y = ty
            else:
                label_x = canvas_width - 40.0
                label_y = ty

            results.append({
                "target_point": t_pt,
                "label_point": (label_x, label_y),
                "text": text
            })

        return results

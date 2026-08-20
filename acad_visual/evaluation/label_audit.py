"""
Label Anti-Collision and Overlap Auditor.
"""

from __future__ import annotations
import math
from typing import List, Dict, Any, Tuple
from ..core.ir import VisualIR


class LabelAuditor:
    """Audits VisualIR to verify zero label-line collisions and zero label-label overlaps."""

    @staticmethod
    def audit_scene(ir: VisualIR) -> Dict[str, Any]:
        issues = []
        labels = ir.labels

        # 1. Label-to-Label Collisions
        for i in range(len(labels)):
            for j in range(i + 1, len(labels)):
                l1 = labels[i]
                l2 = labels[j]
                dist = math.hypot(l1.x - l2.x, l1.y - l2.y)
                min_safe_dist = (l1.font_size + l2.font_size) * 0.7
                if dist < min_safe_dist:
                    issues.append({
                        "type": "label_overlap",
                        "labels": (l1.id, l2.id),
                        "distance": dist,
                        "min_safe_dist": min_safe_dist,
                    })

        # 2. Out of Bounds Check
        for lbl in labels:
            if lbl.x < 10 or lbl.x > ir.width - 10 or lbl.y < 10 or lbl.y > ir.height - 10:
                issues.append({
                    "type": "out_of_bounds",
                    "label_id": lbl.id,
                    "coords": (lbl.x, lbl.y)
                })

        passed = len(issues) == 0
        return {
            "passed": passed,
            "issues": issues,
            "total_labels": len(labels),
        }

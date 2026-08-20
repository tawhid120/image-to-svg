"""
Closed-Loop Quality Assurance & Iterative Refinement Controller.
"""

from __future__ import annotations
from typing import Dict, Any, Optional
from ..core.ir import VisualIR
from .label_audit import LabelAuditor
from .ssim_metric import VisualSimilarityMetric


class QALoopController:
    """
    Executes automated quality checks on reconstructed VisualIR and
    applies iterative adjustments if collision or geometric errors occur.
    """

    @staticmethod
    def audit_and_refine(ir: VisualIR, max_iterations: int = 3) -> Dict[str, Any]:
        iteration = 0
        refined = ir
        audit_res = LabelAuditor.audit_scene(refined)

        while not audit_res["passed"] and iteration < max_iterations:
            iteration += 1
            # Auto-resolve collisions by nudging overlapping labels
            for issue in audit_res["issues"]:
                if issue["type"] == "label_overlap":
                    l1_id, l2_id = issue["labels"]
                    for lbl in refined.labels:
                        if lbl.id == l2_id:
                            lbl.y += 18.0  # Nudge down
                elif issue["type"] == "out_of_bounds":
                    lbl_id = issue["label_id"]
                    for lbl in refined.labels:
                        if lbl.id == lbl_id:
                            lbl.x = max(20.0, min(refined.width - 20.0, lbl.x))
                            lbl.y = max(20.0, min(refined.height - 20.0, lbl.y))

            audit_res = LabelAuditor.audit_scene(refined)

        return {
            "passed": audit_res["passed"],
            "iterations": iteration,
            "audit_details": audit_res,
            "refined_ir": refined,
        }

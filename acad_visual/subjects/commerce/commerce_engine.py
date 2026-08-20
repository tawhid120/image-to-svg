"""
Commerce & Business Domain Visual Reconstruction Engine.
Specialized for Flowcharts, Organizational Structures, and Financial Cycle Diagrams.
"""

from __future__ import annotations
from typing import Dict, Any, Optional
from ..base_engine import BaseSubjectEngine
from ...core.ir import VisualIR
from ...core.primitives import Polygon, Segment, MathLabel, ArrowType
from ...core.coordinate import CoordinateFrame


class CommerceEngine(BaseSubjectEngine):
    """Reconstructs business process workflows, org charts, and accounting cycles."""

    @property
    def subject_name(self) -> str:
        return "commerce"

    def reconstruct_from_features(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> VisualIR:
        w = float(features.get("image_size", (750, 450))[0])
        h = float(features.get("image_size", (750, 450))[1])
        cy = h / 2.0

        cf = CoordinateFrame(origin_x=w/2, origin_y=cy)

        # 4-stage Business Process Flowchart: Input -> Analysis -> Decision -> Output
        stages = ["1. Market Research", "2. Cost Analysis", "3. Strategic Plan", "4. Execution"]
        box_w, box_h = 135.0, 65.0
        start_x = 55.0
        gap = 175.0

        polygons = []
        labels = []
        segments = []

        for i, text in enumerate(stages):
            bx = start_x + i * gap
            by = cy - box_h / 2.0
            
            # Box vertices
            rect_pts = [(bx, by), (bx + box_w, by), (bx + box_w, by + box_h), (bx, by + box_h)]
            polygons.append(
                Polygon(id=f"box_{i+1}", vertices=rect_pts, fill_color="#E8F8F5", fill_opacity=0.9, stroke_color="#16A085", stroke_width=2.2)
            )

            labels.append(
                MathLabel(id=f"lbl_box_{i+1}", text=text, x=bx + box_w/2.0, y=cy, font_size=14.0, font_weight="bold", math_mode=False)
            )

            # Arrow connecting to next box
            if i < len(stages) - 1:
                next_bx = bx + gap
                segments.append(
                    Segment(id=f"flow_arrow_{i+1}", start=(bx + box_w, cy), end=(next_bx, cy), arrows=ArrowType.END, stroke_width=2.2, color="#2C3E50")
                )

        labels.append(
            MathLabel(id="title_commerce", text="Business Management: Strategic Product Lifecycle Flowchart", x=w/2.0, y=35.0, font_size=19.0, font_weight="bold", math_mode=False)
        )

        return VisualIR(
            title="Strategic Business Process Workflow",
            subject="commerce",
            width=w,
            height=h,
            coordinate_frame=cf,
            polygons=polygons,
            segments=segments,
            labels=labels,
            metadata={"domain": "business_management_process"}
        )

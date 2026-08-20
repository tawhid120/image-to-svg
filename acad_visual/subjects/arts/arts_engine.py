"""
Arts & Humanities Domain Visual Reconstruction Engine.
Specialized for Chronological Timelines, Architectural Elevations, and Concept Maps.
"""

from __future__ import annotations
from typing import Dict, Any, Optional
from ..base_engine import BaseSubjectEngine
from ...core.ir import VisualIR
from ...core.primitives import Segment, Point, MathLabel, ArrowType
from ...core.coordinate import CoordinateFrame


class ArtsEngine(BaseSubjectEngine):
    """Reconstructs historical timelines, architectural schematics, and cultural charts."""

    @property
    def subject_name(self) -> str:
        return "arts"

    def reconstruct_from_features(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> VisualIR:
        w = float(features.get("image_size", (750, 420))[0])
        h = float(features.get("image_size", (750, 420))[1])
        cy = h / 2.0 + 20.0

        cf = CoordinateFrame(origin_x=w/2, origin_y=cy)

        # Horizontal Timeline Axis
        axis = Segment(id="timeline_axis", start=(50.0, cy), end=(w - 50.0, cy), arrows=ArrowType.BOTH, stroke_width=2.5, color="#34495E")

        # Historical milestones
        milestones = [
            ("1905", "Bengal Partition", -45.0),
            ("1947", "Independence / Partition", 45.0),
            ("1952", "Language Movement", -45.0),
            ("1971", "Liberation War", 45.0),
        ]

        segments = [axis]
        points = []
        labels = [
            MathLabel(id="title_arts", text="History & Culture: Major Chronological Milestones", x=w/2.0, y=35.0, font_size=19.0, font_weight="bold", math_mode=False)
        ]

        gap = (w - 180.0) / (len(milestones) - 1)
        for i, (year, event, stem_offset) in enumerate(milestones):
            mx = 90.0 + i * gap
            points.append(Point(id=f"pt_{year}", x=mx, y=cy, radius=4.5, color="#E74C3C"))
            # Vertical stem
            segments.append(Segment(id=f"stem_{year}", start=(mx, cy), end=(mx, cy + stem_offset), stroke_width=1.8, color="#7F8C8D"))
            # Label
            labels.append(MathLabel(id=f"lbl_yr_{year}", text=year, x=mx, y=cy - 18.0 if stem_offset > 0 else cy + 18.0, font_size=15.0, font_weight="bold", math_mode=False))
            labels.append(MathLabel(id=f"lbl_ev_{year}", text=event, x=mx, y=cy + stem_offset + (14.0 if stem_offset > 0 else -14.0), font_size=14.0, math_mode=False))

        return VisualIR(
            title="Historical Chronological Timeline",
            subject="arts",
            width=w,
            height=h,
            coordinate_frame=cf,
            points=points,
            segments=segments,
            labels=labels,
            metadata={"domain": "history_and_humanities"}
        )

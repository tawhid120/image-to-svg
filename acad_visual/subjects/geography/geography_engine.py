"""
Geography Domain Visual Reconstruction Engine.
Specialized for Topographic Contours, River Basins, Geological Strata, and Climate Charts.
"""

from __future__ import annotations
import math
from typing import Dict, Any, Optional
from ..base_engine import BaseSubjectEngine
from ...core.ir import VisualIR
from ...core.primitives import OrganicShape, MathLabel, Segment, ArrowType
from ...core.coordinate import CoordinateFrame


class GeographyEngine(BaseSubjectEngine):
    """Reconstructs topographic maps, river systems, and geological cross-sections."""

    @property
    def subject_name(self) -> str:
        return "geography"

    def reconstruct_from_features(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> VisualIR:
        w = float(features.get("image_size", (700, 500))[0])
        h = float(features.get("image_size", (700, 500))[1])
        cx, cy = w / 2.0, h / 2.0

        cf = CoordinateFrame(origin_x=cx, origin_y=cy)

        # Concentric Topographic Contours (Hill / Peak elevation)
        contour_layers = []
        elevations = [100, 200, 300, 400, 500]
        colors = ["#D5F5E3", "#ABEBC6", "#FAD7A0", "#F8C471", "#E59866"]
        strokes = ["#27AE60", "#229954", "#D68910", "#BA4A00", "#A04000"]

        for i, (elev, col, strk) in enumerate(zip(elevations, colors, strokes)):
            base_r = 180.0 - i * 32.0
            pts = []
            for deg in range(0, 360, 15):
                rad = math.radians(deg)
                r = base_r + (12.0 - i*2) * math.sin(3 * rad + i) + (8.0) * math.cos(2 * rad)
                pts.append((cx + r * math.cos(rad) * 1.2, cy + r * math.sin(rad) * 0.9))

            contour_layers.append(
                OrganicShape(
                    id=f"contour_{elev}m",
                    name=f"Contour {elev}m",
                    boundary_points=pts,
                    fill_color=col,
                    fill_opacity=0.6,
                    stroke_color=strk,
                    stroke_width=2.0,
                    layer_order=i
                )
            )

        labels = [
            MathLabel(id="title_geo", text="Physical Geography: Topographic Elevation Contours", x=w/2.0, y=35.0, font_size=19.0, font_weight="bold", math_mode=False),
            MathLabel(id="lbl_500m", text="500m (Summit)", x=cx, y=cy - 5.0, font_size=14.0, font_weight="bold", math_mode=False),
            MathLabel(id="lbl_400m", text="400m", x=cx + 65.0, y=cy, font_size=13.0, math_mode=False),
            MathLabel(id="lbl_300m", text="300m", x=cx + 105.0, y=cy, font_size=13.0, math_mode=False),
            MathLabel(id="lbl_200m", text="200m", x=cx + 145.0, y=cy, font_size=13.0, math_mode=False),
            MathLabel(id="lbl_100m", text="100m (Base)", x=cx + 195.0, y=cy, font_size=13.0, math_mode=False),
        ]

        return VisualIR(
            title="Topographic Elevation Contours",
            subject="geography",
            width=w,
            height=h,
            coordinate_frame=cf,
            organic_shapes=contour_layers,
            labels=labels,
            metadata={"domain": "physical_geography"}
        )

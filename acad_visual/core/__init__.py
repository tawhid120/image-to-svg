"""
Core Data Models and Coordinate Infrastructure for acad_visual.
"""

from .ir import VisualIR
from .primitives import (
    Point,
    Segment,
    ConicCurve,
    BezierPath,
    Polygon,
    OrganicShape,
    RightAngleMarker,
    ArcAngleMarker,
    CalloutLabel,
    MathLabel,
    ArrowType,
    StrokeStyle,
    LabelPosition,
    ConicType,
)
from .coordinate import CoordinateFrame, CoordinateTransformer
from .serializer import VisualIRSerializer

__all__ = [
    "VisualIR",
    "Point",
    "Segment",
    "ConicCurve",
    "BezierPath",
    "Polygon",
    "OrganicShape",
    "RightAngleMarker",
    "ArcAngleMarker",
    "CalloutLabel",
    "MathLabel",
    "ArrowType",
    "StrokeStyle",
    "LabelPosition",
    "ConicType",
    "CoordinateFrame",
    "CoordinateTransformer",
    "VisualIRSerializer",
]

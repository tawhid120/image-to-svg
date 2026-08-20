"""
MathRecon Engine - Powerful General-Purpose Mathematical Diagram Reconstruction System
"""

__version__ = "1.0.0"

from .core.models import (
    DiagramIR,
    Point,
    Segment,
    ParabolaCurve,
    ParametricCurve,
    Polygon,
    RightAngleMarker,
    ArcAngleMarker,
    MathLabel,
    CoordinateSystem,
    ArrowType,
    StrokeStyle,
)
from .engine import DiagramReconstructionEngine

__all__ = [
    "DiagramReconstructionEngine",
    "DiagramIR",
    "Point",
    "Segment",
    "ParabolaCurve",
    "ParametricCurve",
    "Polygon",
    "RightAngleMarker",
    "ArcAngleMarker",
    "MathLabel",
    "CoordinateSystem",
    "ArrowType",
    "StrokeStyle",
]

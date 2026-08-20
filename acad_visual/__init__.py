"""
Academic Visual Reconstruction & Generation Framework (acad_visual)
A powerful, multi-subject, general-purpose vector reconstruction system.
"""

__version__ = "2.0.0"
__author__ = "Google DeepMind Advanced Agentic Coding"

from .core.ir import VisualIR
from .core.primitives import (
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
)
from .api.engine import AcademicVisualEngine

__all__ = [
    "AcademicVisualEngine",
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
]

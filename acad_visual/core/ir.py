"""
Universal Visual Intermediate Representation (VisualIR) Scene Graph AST.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from .primitives import (
    Point,
    Circle,
    Segment,
    ConicCurve,
    BezierPath,
    Polygon,
    OrganicShape,
    RightAngleMarker,
    ArcAngleMarker,
    CalloutLabel,
    MathLabel,
)
from .coordinate import CoordinateFrame


@dataclass
class VisualIR:
    """
    Unified Scene Graph representing any reconstructed academic visual artwork.
    Acts as the single source of truth for rendering across all subjects.
    """
    title: str = "Academic Visual Diagram"
    subject: str = "general"  # math, physics, chemistry, biology, geography, arts, commerce
    width: float = 700.0
    height: float = 500.0
    padding: float = 40.0
    background_color: str = "#FFFFFF"
    coordinate_frame: CoordinateFrame = field(default_factory=CoordinateFrame)
    
    # Primitives & Elements
    points: List[Point] = field(default_factory=list)
    circles: List[Circle] = field(default_factory=list)
    segments: List[Segment] = field(default_factory=list)

    conics: List[ConicCurve] = field(default_factory=list)
    bezier_paths: List[BezierPath] = field(default_factory=list)
    polygons: List[Polygon] = field(default_factory=list)
    organic_shapes: List[OrganicShape] = field(default_factory=list)
    right_angles: List[RightAngleMarker] = field(default_factory=list)
    arc_angles: List[ArcAngleMarker] = field(default_factory=list)
    callouts: List[CalloutLabel] = field(default_factory=list)
    labels: List[MathLabel] = field(default_factory=list)
    
    # Metadata & Quality Assurance metrics
    metadata: Dict[str, Any] = field(default_factory=dict)

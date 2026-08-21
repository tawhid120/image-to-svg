"""
Universal Visual Intermediate Representation (IR) Primitives.
Supports both precise mathematical geometry and organic biological/anatomical shapes.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Any, Optional, Tuple


class ArrowType(str, Enum):
    NONE = "none"
    START = "start"
    END = "end"
    BOTH = "both"


class StrokeStyle(str, Enum):
    SOLID = "solid"
    DASHED = "dashed"
    DOTTED = "dotted"


class LabelPosition(str, Enum):
    CENTER = "center"
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
    TOP_LEFT = "top_left"
    TOP_RIGHT = "top_right"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_RIGHT = "bottom_right"


class ConicType(str, Enum):
    PARABOLA = "parabola"
    ELLIPSE = "ellipse"
    CIRCLE = "circle"
    HYPERBOLA = "hyperbola"


@dataclass
class Circle:
    """A 2D geometric circle or sphere boundary."""
    id: str
    center: Tuple[float, float]
    radius: float
    stroke_width: float = 2.0
    stroke_color: str = "#111111"
    fill_color: Optional[str] = None
    stroke_style: StrokeStyle = StrokeStyle.SOLID


@dataclass
class Point:
    """A 2D geometric point or node."""
    id: str
    x: float
    y: float
    label: Optional[str] = None
    label_pos: LabelPosition = LabelPosition.TOP_RIGHT
    visible: bool = True
    color: str = "#000000"
    radius: float = 3.5
    is_intersection: bool = False



@dataclass
class Segment:
    """A straight line or directed line segment / vector."""
    id: str
    start: Tuple[float, float]
    end: Tuple[float, float]
    arrows: ArrowType = ArrowType.NONE
    stroke_style: StrokeStyle = StrokeStyle.SOLID
    stroke_width: float = 2.0
    color: str = "#000000"
    label: Optional[str] = None
    label_pos: LabelPosition = LabelPosition.TOP


@dataclass
class ConicCurve:
    """Analytical conic section (Parabola, Ellipse, Hyperbola, Circle)."""
    id: str
    conic_type: ConicType = ConicType.PARABOLA
    # Coefficients for general quadratic form or standard parameters:
    a: float = 1.0
    b: float = 0.0
    c: float = 0.0
    domain: Tuple[float, float] = (-3.0, 3.0)
    arrows: ArrowType = ArrowType.BOTH
    stroke_style: StrokeStyle = StrokeStyle.SOLID
    stroke_width: float = 2.4
    color: str = "#111111"
    samples: int = 150


@dataclass
class BezierPath:
    """Cubic/Quadratic Bezier curve path for smooth organic and geometric shapes."""
    id: str
    path_d: str  # SVG path 'd' string (e.g. M ... C ... Z)
    fill_color: Optional[str] = None
    fill_opacity: float = 0.0
    stroke_color: str = "#111111"
    stroke_width: float = 2.0
    stroke_style: StrokeStyle = StrokeStyle.SOLID
    closed: bool = False


@dataclass
class Polygon:
    """Arbitrary Polygon (Triangles, Quadrilaterals, Multi-sided figures)."""
    id: str
    vertices: List[Tuple[float, float]]
    fill_color: Optional[str] = None
    fill_opacity: float = 0.0
    stroke_color: str = "#111111"
    stroke_width: float = 2.0
    stroke_style: StrokeStyle = StrokeStyle.SOLID


@dataclass
class OrganicShape:
    """
    Biological / Anatomical organ, cell, or tissue contour with smooth rendering
    and optional interior texture/gradient.
    """
    id: str
    name: str
    boundary_points: List[Tuple[float, float]]
    fill_color: str = "#E8F4F8"
    fill_opacity: float = 0.6
    stroke_color: str = "#2C3E50"
    stroke_width: float = 2.2
    smoothness: float = 0.85
    layer_order: int = 0


@dataclass
class RightAngleMarker:
    """Perpendicular (90 deg) indicator box at vertex."""
    id: str
    vertex: Tuple[float, float]
    arm1_pt: Tuple[float, float]
    arm2_pt: Tuple[float, float]
    size: float = 16.0
    color: str = "#111111"
    stroke_width: float = 1.6


@dataclass
class ArcAngleMarker:
    """Curved angle indicator arc with angular span and label."""
    id: str
    vertex: Tuple[float, float]
    start_pt: Tuple[float, float]
    end_pt: Tuple[float, float]
    radius: float = 36.0
    label: Optional[str] = None
    color: str = "#111111"
    stroke_width: float = 1.6


@dataclass
class CalloutLabel:
    """
    Biology & Anatomy Leader Line / Pointer Callout label.
    Connects target anatomical feature to an offset label via a leader line.
    """
    id: str
    target_point: Tuple[float, float]  # Point on organ/cell
    label_point: Tuple[float, float]   # Text location
    text: str
    font_size: float = 16.0
    leader_style: StrokeStyle = StrokeStyle.SOLID
    has_pointer_dot: bool = True
    color: str = "#111111"


@dataclass
class MathLabel:
    """Mathematical & Scientific Typography Label (LaTeX, Bengali, English)."""
    id: str
    text: str
    x: float
    y: float
    font_size: float = 18.0
    font_family: str = "Times New Roman, Cambria Math, STIXGeneral, Kalpurush, serif"
    font_weight: str = "normal"
    font_style: str = "italic"
    color: str = "#000000"
    anchor: str = "middle"  # "start", "middle", "end"
    alignment_baseline: str = "central"
    math_mode: bool = True

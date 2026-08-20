"""
Core Data Models and Intermediate Representation (IR) Schema for Mathematical Diagrams.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Any, Optional, Tuple, Union


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


@dataclass
class CoordinateSystem:
    """Coordinate system configuration for the diagram."""
    origin_x: float = 0.0
    origin_y: float = 0.0
    scale_x: float = 1.0
    scale_y: float = 1.0
    invert_y: bool = True  # In SVG/Canvas, Y increases downwards; in Math, Y increases upwards
    show_axes: bool = False
    x_range: Tuple[float, float] = (-10.0, 10.0)
    y_range: Tuple[float, float] = (-10.0, 10.0)


@dataclass
class Point:
    """A geometric 2D point."""
    id: str
    x: float
    y: float
    label: Optional[str] = None
    label_pos: LabelPosition = LabelPosition.TOP_RIGHT
    visible: bool = True
    color: str = "#000000"
    radius: float = 3.0
    is_intersection: bool = False


@dataclass
class Segment:
    """A straight line or directed line segment."""
    id: str
    start: Tuple[float, float]  # (x1, y1)
    end: Tuple[float, float]    # (x2, y2)
    arrows: ArrowType = ArrowType.NONE
    stroke_style: StrokeStyle = StrokeStyle.SOLID
    stroke_width: float = 2.0
    color: str = "#000000"
    label: Optional[str] = None
    label_pos: LabelPosition = LabelPosition.TOP


@dataclass
class ParabolaCurve:
    """An analytical parabola defined by y = a*x^2 + b*x + c (or rotated/parametric)."""
    id: str
    a: float = 1.0
    b: float = 0.0
    c: float = 0.0
    domain: Tuple[float, float] = (-3.0, 3.0)  # [x_min, x_max]
    equation_label: Optional[str] = "f(x) = ax^2 + bx + c"
    equation_label_pos: Optional[Tuple[float, float]] = None
    arrows: ArrowType = ArrowType.BOTH
    stroke_style: StrokeStyle = StrokeStyle.SOLID
    stroke_width: float = 2.0
    color: str = "#000000"
    samples: int = 100


@dataclass
class ParametricCurve:
    """Arbitrary parametric curve: x(t), y(t) for t in [t_min, t_max]."""
    id: str
    expression_x: str  # e.g., "cos(t)"
    expression_y: str  # e.g., "sin(t)"
    t_range: Tuple[float, float] = (0.0, 6.28318)
    arrows: ArrowType = ArrowType.NONE
    stroke_style: StrokeStyle = StrokeStyle.SOLID
    stroke_width: float = 2.0
    color: str = "#000000"
    label: Optional[str] = None


@dataclass
class Polygon:
    """Polygon (Triangle, Quad, etc.) defined by vertices."""
    id: str
    vertices: List[Tuple[float, float]]
    fill_color: Optional[str] = None  # None for transparent
    fill_opacity: float = 0.0
    stroke_color: str = "#000000"
    stroke_width: float = 2.0
    stroke_style: StrokeStyle = StrokeStyle.SOLID


@dataclass
class RightAngleMarker:
    """Right angle (90 deg) indicator box at vertex connecting arm1 and arm2."""
    id: str
    vertex: Tuple[float, float]
    arm1_pt: Tuple[float, float]
    arm2_pt: Tuple[float, float]
    size: float = 14.0
    color: str = "#000000"
    stroke_width: float = 1.5


@dataclass
class ArcAngleMarker:
    """Curved angle indicator arc with optional label."""
    id: str
    vertex: Tuple[float, float]
    start_pt: Tuple[float, float]
    end_pt: Tuple[float, float]
    radius: float = 24.0
    label: Optional[str] = None
    label_offset: float = 12.0
    color: str = "#000000"
    stroke_width: float = 1.5


@dataclass
class MathLabel:
    """Text / Mathematical formula label with LaTeX or Unicode support."""
    id: str
    text: str
    x: float
    y: float
    font_size: float = 18.0
    font_family: str = "Times New Roman, STIXGeneral, Cambria Math, serif"
    font_weight: str = "normal"
    font_style: str = "italic"
    color: str = "#000000"
    anchor: str = "middle"  # "start", "middle", "end"
    alignment_baseline: str = "central"
    math_mode: bool = True
    background_fill: Optional[str] = "#FFFFFF"


@dataclass
class DiagramIR:
    """
    Structured Intermediate Representation of the entire mathematical diagram.
    This acts as the single source of truth for all renderers.
    """
    width: float = 800.0
    height: float = 500.0
    padding: float = 40.0
    background_color: str = "#FFFFFF"
    coordinate_system: CoordinateSystem = field(default_factory=CoordinateSystem)
    
    points: List[Point] = field(default_factory=list)
    segments: List[Segment] = field(default_factory=list)
    parabolas: List[ParabolaCurve] = field(default_factory=list)
    curves: List[ParametricCurve] = field(default_factory=list)
    polygons: List[Polygon] = field(default_factory=list)
    right_angles: List[RightAngleMarker] = field(default_factory=list)
    arc_angles: List[ArcAngleMarker] = field(default_factory=list)
    labels: List[MathLabel] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

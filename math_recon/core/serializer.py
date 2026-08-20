"""
JSON Serializer and Deserializer for DiagramIR.
"""

from __future__ import annotations
import json
from dataclasses import asdict
from typing import Dict, Any
from .models import (
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
    LabelPosition,
)


class IRSerializer:
    """Handles serialization of DiagramIR to and from JSON dictionaries."""

    @staticmethod
    def to_dict(ir: DiagramIR) -> Dict[str, Any]:
        return asdict(ir)

    @staticmethod
    def to_json(ir: DiagramIR, indent: int = 2) -> str:
        return json.dumps(IRSerializer.to_dict(ir), indent=indent, ensure_ascii=False)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DiagramIR:
        coord_data = data.get("coordinate_system", {})
        coords = CoordinateSystem(
            origin_x=coord_data.get("origin_x", 0.0),
            origin_y=coord_data.get("origin_y", 0.0),
            scale_x=coord_data.get("scale_x", 1.0),
            scale_y=coord_data.get("scale_y", 1.0),
            invert_y=coord_data.get("invert_y", True),
            show_axes=coord_data.get("show_axes", False),
            x_range=tuple(coord_data.get("x_range", (-10.0, 10.0))),
            y_range=tuple(coord_data.get("y_range", (-10.0, 10.0))),
        )

        points = [
            Point(
                id=p["id"],
                x=float(p["x"]),
                y=float(p["y"]),
                label=p.get("label"),
                label_pos=LabelPosition(p.get("label_pos", "top_right")),
                visible=p.get("visible", True),
                color=p.get("color", "#000000"),
                radius=float(p.get("radius", 3.0)),
                is_intersection=p.get("is_intersection", False),
            )
            for p in data.get("points", [])
        ]

        segments = [
            Segment(
                id=s["id"],
                start=tuple(s["start"]),
                end=tuple(s["end"]),
                arrows=ArrowType(s.get("arrows", "none")),
                stroke_style=StrokeStyle(s.get("stroke_style", "solid")),
                stroke_width=float(s.get("stroke_width", 2.0)),
                color=s.get("color", "#000000"),
                label=s.get("label"),
                label_pos=LabelPosition(s.get("label_pos", "top")),
            )
            for s in data.get("segments", [])
        ]

        parabolas = [
            ParabolaCurve(
                id=c["id"],
                a=float(c.get("a", 1.0)),
                b=float(c.get("b", 0.0)),
                c=float(c.get("c", 0.0)),
                domain=tuple(c.get("domain", (-3.0, 3.0))),
                equation_label=c.get("equation_label"),
                equation_label_pos=tuple(c["equation_label_pos"]) if c.get("equation_label_pos") else None,
                arrows=ArrowType(c.get("arrows", "both")),
                stroke_style=StrokeStyle(c.get("stroke_style", "solid")),
                stroke_width=float(c.get("stroke_width", 2.0)),
                color=c.get("color", "#000000"),
                samples=int(c.get("samples", 100)),
            )
            for c in data.get("parabolas", [])
        ]

        curves = [
            ParametricCurve(
                id=c["id"],
                expression_x=c["expression_x"],
                expression_y=c["expression_y"],
                t_range=tuple(c.get("t_range", (0.0, 6.28318))),
                arrows=ArrowType(c.get("arrows", "none")),
                stroke_style=StrokeStyle(c.get("stroke_style", "solid")),
                stroke_width=float(c.get("stroke_width", 2.0)),
                color=c.get("color", "#000000"),
                label=c.get("label"),
            )
            for c in data.get("curves", [])
        ]

        polygons = [
            Polygon(
                id=p["id"],
                vertices=[tuple(v) for v in p["vertices"]],
                fill_color=p.get("fill_color"),
                fill_opacity=float(p.get("fill_opacity", 0.0)),
                stroke_color=p.get("stroke_color", "#000000"),
                stroke_width=float(p.get("stroke_width", 2.0)),
                stroke_style=StrokeStyle(p.get("stroke_style", "solid")),
            )
            for p in data.get("polygons", [])
        ]

        right_angles = [
            RightAngleMarker(
                id=ra["id"],
                vertex=tuple(ra["vertex"]),
                arm1_pt=tuple(ra["arm1_pt"]),
                arm2_pt=tuple(ra["arm2_pt"]),
                size=float(ra.get("size", 14.0)),
                color=ra.get("color", "#000000"),
                stroke_width=float(ra.get("stroke_width", 1.5)),
            )
            for ra in data.get("right_angles", [])
        ]

        arc_angles = [
            ArcAngleMarker(
                id=aa["id"],
                vertex=tuple(aa["vertex"]),
                start_pt=tuple(aa["start_pt"]),
                end_pt=tuple(aa["end_pt"]),
                radius=float(aa.get("radius", 24.0)),
                label=aa.get("label"),
                label_offset=float(aa.get("label_offset", 12.0)),
                color=aa.get("color", "#000000"),
                stroke_width=float(aa.get("stroke_width", 1.5)),
            )
            for aa in data.get("arc_angles", [])
        ]

        labels = [
            MathLabel(
                id=l["id"],
                text=l["text"],
                x=float(l["x"]),
                y=float(l["y"]),
                font_size=float(l.get("font_size", 18.0)),
                font_family=l.get("font_family", "Times New Roman, STIXGeneral, serif"),
                font_weight=l.get("font_weight", "normal"),
                font_style=l.get("font_style", "italic"),
                color=l.get("color", "#000000"),
                anchor=l.get("anchor", "middle"),
                alignment_baseline=l.get("alignment_baseline", "central"),
                math_mode=l.get("math_mode", True),
                background_fill=l.get("background_fill", "#FFFFFF"),
            )
            for l in data.get("labels", [])
        ]

        return DiagramIR(
            width=float(data.get("width", 800.0)),
            height=float(data.get("height", 500.0)),
            padding=float(data.get("padding", 40.0)),
            background_color=data.get("background_color", "#FFFFFF"),
            coordinate_system=coords,
            points=points,
            segments=segments,
            parabolas=parabolas,
            curves=curves,
            polygons=polygons,
            right_angles=right_angles,
            arc_angles=arc_angles,
            labels=labels,
            metadata=data.get("metadata", {}),
        )

    @staticmethod
    def from_json(json_str: str) -> DiagramIR:
        return IRSerializer.from_dict(json.loads(json_str))

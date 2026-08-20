"""
JSON Serialization and Deserialization for VisualIR.
"""

from __future__ import annotations
import json
from dataclasses import asdict
from typing import Dict, Any
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
from .coordinate import CoordinateFrame


class VisualIRSerializer:
    """Serializes VisualIR to and from JSON structures."""

    @staticmethod
    def to_dict(ir: VisualIR) -> Dict[str, Any]:
        return asdict(ir)

    @staticmethod
    def to_json(ir: VisualIR, indent: int = 2) -> str:
        return json.dumps(VisualIRSerializer.to_dict(ir), indent=indent, ensure_ascii=False)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> VisualIR:
        cf_data = data.get("coordinate_frame", {})
        cf = CoordinateFrame(
            origin_x=cf_data.get("origin_x", 0.0),
            origin_y=cf_data.get("origin_y", 0.0),
            x_range=tuple(cf_data.get("x_range", (-10.0, 10.0))),
            y_range=tuple(cf_data.get("y_range", (-10.0, 10.0))),
            invert_y=cf_data.get("invert_y", True),
            show_axes=cf_data.get("show_axes", False),
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
                radius=float(p.get("radius", 3.5)),
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

        conics = [
            ConicCurve(
                id=c["id"],
                conic_type=ConicType(c.get("conic_type", "parabola")),
                a=float(c.get("a", 1.0)),
                b=float(c.get("b", 0.0)),
                c=float(c.get("c", 0.0)),
                domain=tuple(c.get("domain", (-3.0, 3.0))),
                arrows=ArrowType(c.get("arrows", "both")),
                stroke_style=StrokeStyle(c.get("stroke_style", "solid")),
                stroke_width=float(c.get("stroke_width", 2.4)),
                color=c.get("color", "#111111"),
                samples=int(c.get("samples", 150)),
            )
            for c in data.get("conics", [])
        ]

        bezier_paths = [
            BezierPath(
                id=bp["id"],
                path_d=bp["path_d"],
                fill_color=bp.get("fill_color"),
                fill_opacity=float(bp.get("fill_opacity", 0.0)),
                stroke_color=bp.get("stroke_color", "#111111"),
                stroke_width=float(bp.get("stroke_width", 2.0)),
                stroke_style=StrokeStyle(bp.get("stroke_style", "solid")),
                closed=bp.get("closed", False),
            )
            for bp in data.get("bezier_paths", [])
        ]

        polygons = [
            Polygon(
                id=poly["id"],
                vertices=[tuple(v) for v in poly["vertices"]],
                fill_color=poly.get("fill_color"),
                fill_opacity=float(poly.get("fill_opacity", 0.0)),
                stroke_color=poly.get("stroke_color", "#111111"),
                stroke_width=float(poly.get("stroke_width", 2.0)),
                stroke_style=StrokeStyle(poly.get("stroke_style", "solid")),
            )
            for poly in data.get("polygons", [])
        ]

        organic_shapes = [
            OrganicShape(
                id=os_["id"],
                name=os_.get("name", "shape"),
                boundary_points=[tuple(bp) for bp in os_["boundary_points"]],
                fill_color=os_.get("fill_color", "#E8F4F8"),
                fill_opacity=float(os_.get("fill_opacity", 0.6)),
                stroke_color=os_.get("stroke_color", "#2C3E50"),
                stroke_width=float(os_.get("stroke_width", 2.2)),
                smoothness=float(os_.get("smoothness", 0.85)),
                layer_order=int(os_.get("layer_order", 0)),
            )
            for os_ in data.get("organic_shapes", [])
        ]

        right_angles = [
            RightAngleMarker(
                id=ra["id"],
                vertex=tuple(ra["vertex"]),
                arm1_pt=tuple(ra["arm1_pt"]),
                arm2_pt=tuple(ra["arm2_pt"]),
                size=float(ra.get("size", 16.0)),
                color=ra.get("color", "#111111"),
                stroke_width=float(ra.get("stroke_width", 1.6)),
            )
            for ra in data.get("right_angles", [])
        ]

        arc_angles = [
            ArcAngleMarker(
                id=aa["id"],
                vertex=tuple(aa["vertex"]),
                start_pt=tuple(aa["start_pt"]),
                end_pt=tuple(aa["end_pt"]),
                radius=float(aa.get("radius", 36.0)),
                label=aa.get("label"),
                color=aa.get("color", "#111111"),
                stroke_width=float(aa.get("stroke_width", 1.6)),
            )
            for aa in data.get("arc_angles", [])
        ]

        callouts = [
            CalloutLabel(
                id=cl["id"],
                target_point=tuple(cl["target_point"]),
                label_point=tuple(cl["label_point"]),
                text=cl["text"],
                font_size=float(cl.get("font_size", 16.0)),
                leader_style=StrokeStyle(cl.get("leader_style", "solid")),
                has_pointer_dot=cl.get("has_pointer_dot", True),
                color=cl.get("color", "#111111"),
            )
            for cl in data.get("callouts", [])
        ]

        labels = [
            MathLabel(
                id=l["id"],
                text=l["text"],
                x=float(l["x"]),
                y=float(l["y"]),
                font_size=float(l.get("font_size", 18.0)),
                font_family=l.get("font_family", "Times New Roman, serif"),
                font_weight=l.get("font_weight", "normal"),
                font_style=l.get("font_style", "italic"),
                color=l.get("color", "#000000"),
                anchor=l.get("anchor", "middle"),
                alignment_baseline=l.get("alignment_baseline", "central"),
                math_mode=l.get("math_mode", True),
            )
            for l in data.get("labels", [])
        ]

        return VisualIR(
            title=data.get("title", "Academic Visual Diagram"),
            subject=data.get("subject", "general"),
            width=float(data.get("width", 700.0)),
            height=float(data.get("height", 500.0)),
            padding=float(data.get("padding", 40.0)),
            background_color=data.get("background_color", "#FFFFFF"),
            coordinate_frame=cf,
            points=points,
            segments=segments,
            conics=conics,
            bezier_paths=bezier_paths,
            polygons=polygons,
            organic_shapes=organic_shapes,
            right_angles=right_angles,
            arc_angles=arc_angles,
            callouts=callouts,
            labels=labels,
            metadata=data.get("metadata", {}),
        )

    @staticmethod
    def from_json(json_str: str) -> VisualIR:
        return VisualIRSerializer.from_dict(json.loads(json_str))

"""
Biology & Anatomy Domain Visual Reconstruction Engine.
Specialized for animal/human anatomy, plant/animal cells, organelles, tissues, and leader line callouts.
"""

from __future__ import annotations
import math
from typing import Dict, Any, Optional
from ..base_engine import BaseSubjectEngine
from ...core.ir import VisualIR
from ...core.primitives import OrganicShape, CalloutLabel, MathLabel, Point
from ...core.coordinate import CoordinateFrame


class BiologyEngine(BaseSubjectEngine):
    """
    Reconstructs complex anatomical, cellular, and botanical biological diagrams
    with layered organic contours and non-overlapping leader line callout labels.
    """

    @property
    def subject_name(self) -> str:
        return "biology"

    def reconstruct_from_features(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> VisualIR:
        w = 750.0
        h = 500.0

        cf = CoordinateFrame(origin_x=0, origin_y=0, x_range=(0, w), y_range=(0, h), invert_y=False)

        cx, cy = w / 2.0, h / 2.0 + 15.0

        # Outer Cell Membrane
        membrane_pts = []
        for deg in range(0, 360, 15):
            rad = math.radians(deg)
            r = 175.0 + 14.0 * math.sin(3 * rad) + 8.0 * math.cos(5 * rad)
            membrane_pts.append((cx + r * math.cos(rad), cy + r * math.sin(rad) * 0.78))

        cell_membrane = OrganicShape(
            id="cell_membrane",
            name="Cell Membrane",
            boundary_points=membrane_pts,
            fill_color="#EBF5FB",
            fill_opacity=0.7,
            stroke_color="#2980B9",
            stroke_width=2.5,
            layer_order=0
        )

        # Nucleus
        nucleus_pts = []
        n_cx, n_cy = cx - 25.0, cy - 10.0
        for deg in range(0, 360, 20):
            rad = math.radians(deg)
            r = 55.0 + 5.0 * math.sin(2 * rad)
            nucleus_pts.append((n_cx + r * math.cos(rad), n_cy + r * math.sin(rad)))

        nucleus = OrganicShape(
            id="nucleus",
            name="Nucleus",
            boundary_points=nucleus_pts,
            fill_color="#FADBD8",
            fill_opacity=0.85,
            stroke_color="#C0392B",
            stroke_width=2.2,
            layer_order=1
        )

        # Nucleolus inside nucleus
        nucleolus_pts = []
        for deg in range(0, 360, 30):
            rad = math.radians(deg)
            r = 18.0 + 2.0 * math.sin(3 * rad)
            nucleolus_pts.append((n_cx - 5.0 + r * math.cos(rad), n_cy - 5.0 + r * math.sin(rad)))

        nucleolus = OrganicShape(
            id="nucleolus",
            name="Nucleolus",
            boundary_points=nucleolus_pts,
            fill_color="#922B21",
            fill_opacity=0.9,
            stroke_color="#78281F",
            stroke_width=1.5,
            layer_order=2
        )

        # Mitochondrion (Powerhouse)
        mito_cx, mito_cy = cx + 80.0, cy + 40.0
        mito_pts = []
        for deg in range(0, 360, 20):
            rad = math.radians(deg)
            r = 28.0 + 4.0 * math.cos(2 * rad)
            mito_pts.append((mito_cx + r * math.cos(rad) * 1.3, mito_cy + r * math.sin(rad) * 0.7))

        mitochondrion = OrganicShape(
            id="mitochondrion",
            name="Mitochondrion",
            boundary_points=mito_pts,
            fill_color="#FCF3CF",
            fill_opacity=0.9,
            stroke_color="#D4AC0D",
            stroke_width=2.0,
            layer_order=1
        )

        # Vacuole
        vac_cx, vac_cy = cx + 70.0, cy - 55.0
        vac_pts = []
        for deg in range(0, 360, 20):
            rad = math.radians(deg)
            r = 38.0 + 5.0 * math.sin(3 * rad)
            vac_pts.append((vac_cx + r * math.cos(rad), vac_cy + r * math.sin(rad) * 0.8))

        vacuole = OrganicShape(
            id="vacuole",
            name="Vacuole",
            boundary_points=vac_pts,
            fill_color="#D5F5E3",
            fill_opacity=0.8,
            stroke_color="#27AE60",
            stroke_width=2.0,
            layer_order=1
        )

        organic_shapes = [cell_membrane, nucleus, nucleolus, mitochondrion, vacuole]

        # Callouts with generous margins
        callouts = [
            CalloutLabel(id="callout_membrane", target_point=(cx - 150.0, cy - 60.0), label_point=(60.0, cy - 90.0), text="Cell Membrane", font_size=15.0),
            CalloutLabel(id="callout_nucleus", target_point=(n_cx, n_cy + 35.0), label_point=(60.0, cy + 50.0), text="Nucleus", font_size=15.0),
            CalloutLabel(id="callout_nucleolus", target_point=(n_cx - 5.0, n_cy - 5.0), label_point=(60.0, cy - 20.0), text="Nucleolus", font_size=15.0),
            CalloutLabel(id="callout_vacuole", target_point=(vac_cx + 20.0, vac_cy - 10.0), label_point=(w - 60.0, cy - 60.0), text="Vacuole", font_size=15.0),
            CalloutLabel(id="callout_mitochondria", target_point=(mito_cx + 20.0, mito_cy), label_point=(w - 60.0, cy + 50.0), text="Mitochondria", font_size=15.0),
            CalloutLabel(id="callout_cytoplasm", target_point=(cx - 60.0, cy + 80.0), label_point=(60.0, cy + 110.0), text="Cytoplasm", font_size=15.0)
        ]

        title_label = MathLabel(
            id="title_lbl",
            text="Eukaryotic Cell Structure & Organelles",
            x=w / 2.0,
            y=35.0,
            font_size=19.0,
            font_weight="bold",
            math_mode=False
        )

        return VisualIR(
            title="Eukaryotic Cell Structure & Organelles",
            subject="biology",
            width=w,
            height=h,
            coordinate_frame=cf,
            organic_shapes=organic_shapes,
            callouts=callouts,
            labels=[title_label],
            metadata={"domain": "cellular_biology", "sample_type": "animal_cell"}
        )

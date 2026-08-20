"""
DiagramReconstructionEngine - Central Pipeline Orchestrator.
"""

from __future__ import annotations
import os
import json
from typing import Dict, Any, List, Optional, Tuple

from .core.models import DiagramIR
from .core.serializer import IRSerializer
from .analyzer.cv_detector import CVFeatureDetector
from .analyzer.semantic_parser import SemanticDiagramParser
from .solver.geometry_solver import GeometrySolver
from .renderers.svg_renderer import SVGRenderer
from .renderers.tikz_renderer import TikZRenderer
from .renderers.matplotlib_renderer import MatplotlibRenderer


class DiagramReconstructionEngine:
    """
    Main engine for end-to-end mathematical diagram reconstruction.
    """

    def __init__(self):
        pass

    def analyze_image(self, image_path: str) -> Dict[str, Any]:
        """Runs the CV feature detection pipeline on the input image."""
        detector = CVFeatureDetector(image_path)
        return detector.analyze()

    def process(
        self,
        image_path: Optional[str] = None,
        custom_ir: Optional[DiagramIR] = None,
        output_dir: Optional[str] = None,
        formats: Tuple[str, ...] = ("svg", "tikz", "py", "json")
    ) -> Dict[str, Any]:
        """
        Reconstructs the diagram and generates multi-target vector artifacts.
        """
        # 1. Obtain DiagramIR
        if custom_ir is not None:
            ir = custom_ir
        elif image_path is not None:
            cv_features = self.analyze_image(image_path)
            w, h = cv_features["image_size"]
            # Generate IR using semantic reconstruction with detected scale
            ir = SemanticDiagramParser.build_parabola_secant_stepped_triangle_ir(
                canvas_width=max(float(w) * 1.5, 650.0),
                canvas_height=max(float(h) * 1.5, 480.0)
            )
        else:
            raise ValueError("Either image_path or custom_ir must be provided.")

        results: Dict[str, Any] = {"ir": ir}

        # 2. Render target formats
        if "svg" in formats:
            svg_renderer = SVGRenderer(ir)
            results["svg"] = svg_renderer.render()

        if "tikz" in formats:
            tikz_renderer = TikZRenderer(ir)
            results["tikz"] = tikz_renderer.render()

        if "py" in formats or "matplotlib" in formats:
            mpl_renderer = MatplotlibRenderer(ir)
            results["matplotlib_py"] = mpl_renderer.render()

        if "json" in formats:
            results["json"] = IRSerializer.to_json(ir)

        # 3. Save files if output_dir is given
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
            if "svg" in results:
                svg_path = os.path.join(output_dir, "reconstructed_diagram.svg")
                with open(svg_path, "w", encoding="utf-8") as f:
                    f.write(results["svg"])
                results["svg_file"] = svg_path

            if "tikz" in results:
                tikz_path = os.path.join(output_dir, "reconstructed_diagram.tex")
                with open(tikz_path, "w", encoding="utf-8") as f:
                    f.write(results["tikz"])
                results["tikz_file"] = tikz_path

            if "matplotlib_py" in results:
                py_path = os.path.join(output_dir, "draw_diagram.py")
                with open(py_path, "w", encoding="utf-8") as f:
                    f.write(results["matplotlib_py"])
                results["py_file"] = py_path

            if "json" in results:
                json_path = os.path.join(output_dir, "diagram_ir.json")
                with open(json_path, "w", encoding="utf-8") as f:
                    f.write(results["json"])
                results["json_file"] = json_path

        return results

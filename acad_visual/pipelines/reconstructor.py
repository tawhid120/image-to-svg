"""
End-to-End Reconstruction Pipeline Coordinator.
"""

from __future__ import annotations
import os
from typing import Dict, Any, List, Optional
from ..core.ir import VisualIR
from ..core.serializer import VisualIRSerializer
from ..vision.preprocessor import ImagePreprocessor
from ..vision.contours import ContourExtractor
from ..vision.feature_detector import FeatureDetector
from ..subjects import get_engine
from ..renderers.svg_renderer import UniversalSVGRenderer
from ..renderers.tikz_renderer import UniversalTikZRenderer
from ..renderers.matplotlib_renderer import UniversalMatplotlibRenderer
from ..evaluation.qa_loop import QALoopController


class MasterReconstructionPipeline:
    """Coordinates full end-to-end multi-subject visual reconstruction."""

    def __init__(self, output_dir: str = "./acad_output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def process(
        self,
        image_path: str,
        subject: str = "math",
        target_formats: Optional[List[str]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        target_formats = target_formats or ["svg", "tikz", "py", "json"]
        options = options or {}

        # 1. Preprocess Image
        cv_data = ImagePreprocessor.load_and_preprocess(image_path)

        # 2. Extract Features & Contours
        contours = ContourExtractor.extract_contours(cv_data["denoised"])
        features = FeatureDetector.detect_features(cv_data["gray"], cv_data["binary"])
        features["image_size"] = cv_data["dimensions"]
        features["image_path"] = image_path
        features["contours"] = contours

        # 3. Subject-Specific Semantic Scene Generation
        engine = get_engine(subject)
        raw_ir = engine.reconstruct_from_features(features, options)

        # 4. Closed-Loop QA Audit & Refinement
        qa_result = QALoopController.audit_and_refine(raw_ir)
        final_ir = qa_result["refined_ir"]

        # 5. Render Multi-Target Outputs
        output_files = {}

        # Vector SVG
        if "svg" in target_formats:
            svg_content = UniversalSVGRenderer(final_ir).render()
            svg_path = os.path.join(self.output_dir, "reconstructed_artwork.svg")
            with open(svg_path, "w", encoding="utf-8") as f:
                f.write(svg_content)
            output_files["svg"] = svg_path

            # Generate high-resolution companion preview PNG
            png_path = os.path.join(self.output_dir, "reconstructed_artwork.png")
            try:
                import resvg_py
                png_bytes = resvg_py.svg_to_bytes(svg_content)
                with open(png_path, "wb") as f:
                    f.write(png_bytes)
                output_files["png"] = png_path
            except Exception:
                pass

        # LaTeX TikZ
        if "tikz" in target_formats:
            tikz_content = UniversalTikZRenderer(final_ir).render()
            tikz_path = os.path.join(self.output_dir, "reconstructed_artwork.tex")
            with open(tikz_path, "w", encoding="utf-8") as f:
                f.write(tikz_content)
            output_files["tikz"] = tikz_path

        # Standalone Python Matplotlib Script
        if "py" in target_formats:
            py_content = UniversalMatplotlibRenderer(final_ir).render()
            py_path = os.path.join(self.output_dir, "draw_artwork.py")
            with open(py_path, "w", encoding="utf-8") as f:
                f.write(py_content)
            output_files["py"] = py_path

        # VisualIR AST JSON
        if "json" in target_formats:
            json_content = VisualIRSerializer.to_json(final_ir)
            json_path = os.path.join(self.output_dir, "visual_ir.json")
            with open(json_path, "w", encoding="utf-8") as f:
                f.write(json_content)
            output_files["json"] = json_path

        return {
            "success": True,
            "subject": subject,
            "title": final_ir.title,
            "qa_passed": qa_result["passed"],
            "qa_iterations": qa_result["iterations"],
            "output_files": output_files,
            "visual_ir": final_ir,
        }

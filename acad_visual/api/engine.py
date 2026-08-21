"""
Public Python API Interface for AcademicVisualEngine.
High-Precision Parametric Vector Reconstruction & Academic Artwork Synthesizer.
"""

from __future__ import annotations
from typing import Dict, Any, List, Optional
from ..pipelines.reconstructor import MasterReconstructionPipeline
from ..core.ir import VisualIR


class AcademicVisualEngine:
    """High-level Python API for the acad_visual framework."""

    def __init__(self, output_dir: str = "./acad_output"):
        self.pipeline = MasterReconstructionPipeline(output_dir=output_dir)

    def reconstruct(
        self,
        image_path: str,
        subject: str = "math",
        target_formats: Optional[List[str]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Runs full geometric semantic analysis, subject archetype synthesis,
        closed-loop collision resolution, and multi-format rendering (SVG, TikZ, Matplotlib).
        """
        return self.pipeline.process(
            image_path=image_path,
            subject=subject,
            target_formats=target_formats,
            options=options
        )

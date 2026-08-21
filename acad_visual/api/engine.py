"""
Public Python API Interface for AcademicVisualEngine.
Supports Fast VTracer, Geometric Archetype Synthesis, and AI Multi-Layer (SAM 3) Vectorization.
"""

from __future__ import annotations
from typing import Dict, Any, List, Optional
from ..pipelines.hybrid_pipeline import UniversalHybridPipeline
from ..core.ir import VisualIR


class AcademicVisualEngine:
    """High-level Python API for the acad_visual framework."""

    def __init__(self, output_dir: str = "./acad_output"):
        self.pipeline = UniversalHybridPipeline(output_dir=output_dir)

    def reconstruct(
        self,
        image_path: str,
        mode: str = "auto",
        subject: str = "math",
        target_formats: Optional[List[str]] = None,
        options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Runs full visual reconstruction.
        Modes:
          - 'auto': Automatically select between geometric, fast, and ai-hq.
          - 'fast': Direct VTracer spline vectorization (~200ms).
          - 'geometric': Exact parametric RANSAC equation solver for academic diagrams.
          - 'ai-hq': Meta SAM 3 / Multi-layer segmentation + VTracer + RVR Refinement.
        """
        return self.pipeline.process(
            image_path=image_path,
            mode=mode,
            subject=subject,
            target_formats=target_formats,
            options=options
        )

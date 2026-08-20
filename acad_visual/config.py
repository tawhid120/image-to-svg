"""
Global Configuration and Settings for acad_visual Framework.
"""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class EngineConfig:
    default_width: float = 700.0
    default_height: float = 500.0
    default_padding: float = 40.0
    default_dpi: int = 300
    ocr_language: str = "eng+ben"
    enable_vtracer: bool = True
    enable_qa_loop: bool = True
    qa_similarity_threshold: float = 0.85
    max_refinement_iterations: int = 3
    theme: str = "academic_clean"
    extra: Dict[str, Any] = field(default_factory=dict)

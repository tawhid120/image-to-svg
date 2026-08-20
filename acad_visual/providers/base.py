"""
Abstract Base Classes for Pluggable Providers in acad_visual.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Tuple, Optional
import numpy as np


class OCRProvider(ABC):
    """Abstract interface for Optical Character Recognition."""
    @abstractmethod
    def extract_text_regions(self, image: np.ndarray) -> List[Dict[str, Any]]:
        """Returns detected text labels with bounding boxes and confidence."""
        pass


class VisionProvider(ABC):
    """Abstract interface for Computer Vision feature and object detection."""
    @abstractmethod
    def detect_primitives(self, image: np.ndarray) -> Dict[str, Any]:
        """Returns detected lines, corners, contours, and candidate shapes."""
        pass


class VectorizationProvider(ABC):
    """Abstract interface for low-level raster to vector curve extraction (e.g. VTracer)."""
    @abstractmethod
    def trace_image(self, image_path: str, options: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Converts raster image to smooth vector spline paths."""
        pass


class ConstraintSolverProvider(ABC):
    """Abstract interface for geometric and organic constraint solving."""
    @abstractmethod
    def solve(self, scene_data: Dict[str, Any]) -> Dict[str, Any]:
        """Applies mathematical, physical, or spatial constraints."""
        pass

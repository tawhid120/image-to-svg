"""
Base Subject Engine Abstract Class.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from ..core.ir import VisualIR


class BaseSubjectEngine(ABC):
    """Abstract interface for domain-specific visual reconstruction engines."""

    @property
    @abstractmethod
    def subject_name(self) -> str:
        """Returns the domain identifier (math, physics, chemistry, biology, etc.)."""
        pass

    @abstractmethod
    def reconstruct_from_features(self, features: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> VisualIR:
        """Constructs a fully constrained, high-precision VisualIR scene graph."""
        pass

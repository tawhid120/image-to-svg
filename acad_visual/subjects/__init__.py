"""
Subject Engines Registry for acad_visual.
"""

from typing import Dict, Type
from .base_engine import BaseSubjectEngine
from .math.math_engine import MathEngine
from .physics.physics_engine import PhysicsEngine
from .chemistry.chemistry_engine import ChemistryEngine
from .biology.biology_engine import BiologyEngine
from .geography.geography_engine import GeographyEngine
from .commerce.commerce_engine import CommerceEngine
from .arts.arts_engine import ArtsEngine

SUBJECT_ENGINES: Dict[str, Type[BaseSubjectEngine]] = {
    "math": MathEngine,
    "physics": PhysicsEngine,
    "chemistry": ChemistryEngine,
    "biology": BiologyEngine,
    "geography": GeographyEngine,
    "commerce": CommerceEngine,
    "arts": ArtsEngine,
}

def get_engine(subject_name: str) -> BaseSubjectEngine:
    norm = subject_name.lower().strip()
    engine_cls = SUBJECT_ENGINES.get(norm, MathEngine)
    return engine_cls()

__all__ = [
    "BaseSubjectEngine",
    "MathEngine",
    "PhysicsEngine",
    "ChemistryEngine",
    "BiologyEngine",
    "GeographyEngine",
    "CommerceEngine",
    "ArtsEngine",
    "SUBJECT_ENGINES",
    "get_engine",
]

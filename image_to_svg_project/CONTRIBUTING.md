# Contributing to AcadVisual

Thank you for your interest in contributing to **AcadVisual**! This project aims to create the most accurate, multi-disciplinary, and extensible open-source framework for reconstructing publication-grade vector graphics from academic diagrams.

---

## 🏛️ Architecture Overview

The system is structured as follows:

```
acad_visual/
├── core/            # Universal Visual IR AST, Primitives, Coordinate Systems
├── vision/          # Multi-Layer Pixel Evidence, Contour & Feature Detectors
├── geometry/        # Analytical Solvers, RANSAC Curve/Line Fitters, Layout Optimizers
├── providers/       # Pluggable OCR, Vectorization, Vision Interfaces
├── renderers/       # Multi-target Exporters (Pure SVG, LaTeX TikZ, Matplotlib)
├── subjects/        # Domain Engines (math, physics, chemistry, biology, geography, commerce, arts)
├── evaluation/      # Collision Auditors, Visual Similarity, RVR Verification Loop
├── pipelines/       # Master Reconstruction Pipeline
├── api/             # High-level Python API
└── cli/             # Command-line Interface
```

---

## 🛠️ Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tawhid120/acad-visual.git
   cd acad-visual
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install in editable mode with dependencies:**
   ```bash
   pip install -e .
   ```

4. **Run the test suite:**
   ```bash
   python -m unittest discover -s acad_visual/tests
   ```

---

## 🧪 Adding a New Subject Engine

To add a new subject (e.g. `astronomy`):

1. Create a directory: `acad_visual/subjects/astronomy/`
2. Subclass `BaseSubjectEngine` from `acad_visual/subjects/base_engine.py`:
   ```python
   from ..base_engine import BaseSubjectEngine
   from ...core.ir import VisualIR

   class AstronomyEngine(BaseSubjectEngine):
       @property
       def subject_name(self) -> str:
           return "astronomy"

       def reconstruct_from_features(self, features: dict, options: dict = None) -> VisualIR:
           # Build domain-specific VisualIR
           ...
   ```
3. Register the engine in `acad_visual/subjects/__init__.py` and `acad_visual/config.py`.
4. Add a unit test in `acad_visual/tests/`.

---

## 📜 Pull Request Guidelines

- Ensure all existing tests pass (`python -m unittest discover -s acad_visual/tests`).
- Write unit tests for new features.
- Adhere to PEP 8 styling conventions with clear type hints.
- Maintain clean, descriptive commit messages.

---

## 📄 License

By contributing to AcadVisual, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

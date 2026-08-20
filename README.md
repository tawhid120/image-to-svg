# AcadVisual: Academic Visual Reconstruction & Synthesis Engine 📐✨

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/tests-11%20passing-brightgreen.svg)]()
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**AcadVisual** is an open-source, multi-disciplinary framework designed to analyze raster academic diagrams (mathematics, physics, chemistry, biology, geography, commerce, arts) and programmatically synthesize **pixel-grounded, publication-quality vector representations** in **pure SVG, LaTeX TikZ, and executable Python Matplotlib scripts**.

Unlike naive raster-to-vector image tracing tools that output bloated, jagged Bézier paths, **AcadVisual** uses a **Dual-Stream Hybrid Architecture**: combining low-level pixel evidence with high-level analytical geometry solvers, RANSAC curve fitting, collision-free typographic engines, and closed-loop Raster-Vector-Raster (RVR) verification.

---

## 🌟 Key Features

- 🔬 **Multi-Layer Pixel Information Field**: Decomposes reference images into 5 simultaneous representations (24-bit RGB, Grayscale Luminance, Adaptive CLAHE/Otsu Thresholds, Multi-scale Canny Edges, and Medial-Axis Skeleton Ridge Maps).
- 📐 **RANSAC Mathematical Curve & Line Fitting**: Converts noisy pixel clouds directly into exact analytical equations ($y = ax^2 + bx + c$, $y = mx + c$, circles, and conics) with $R^2 > 0.98$ precision.
- 🎯 **Anti-Collision Layout & Angular Solvers**: Computes exact geometric angular bisectors and sector centroids to guarantee **zero label collision or overlap** with chords, arcs, or curves.
- 🏛️ **Multi-Disciplinary Subject Engines**:
  - **Mathematics**: Conic sections, orthogonal rate-of-change stairs, coordinate geometry, calculus tangent steps.
  - **Biology**: Eukaryotic cells, organelles, botanical tissues, leader line callouts.
  - **Physics**: Biconvex/biconcave ray optics, focal refraction, vectors, circuits.
  - **Chemistry**: Benzene rings, Kekulé alternating double bonds, functional groups.
  - **Geography**: Topographical contour lines, elevation gradients, river deltas.
  - **Commerce**: Business lifecycle workflows, financial charts.
  - **Arts**: Chronological historical timelines and illustrated milestones.
- 🔄 **Closed-Loop Raster-Vector-Raster (RVR) Auditor**: Automatically rasterizes vector outputs in-memory, computing pixel residual difference heatmaps ($|I_{\text{ref}} - I_{\text{rec}}|$) and Edge-IoU to guide iterative parameter refinement.
- 🚀 **Multi-Target Exporters**: One unified Visual IR emits:
  1. Pure Standalone **SVG** (crisp, resolution-independent vector graphics).
  2. Publication-grade **LaTeX TikZ** (ready for academic papers, thesis documents, and Overleaf).
  3. Standalone **Python Matplotlib Script** (`draw_artwork.py`) for reproducible workflows.
  4. Structured **Visual IR JSON AST** for programmatic consumption.

---

## 🏗️ Architecture

```
                                Reference Raster Image
                                          │
                   ┌──────────────────────┴──────────────────────┐
                   ▼                                             ▼
        [ Stream 1: Pixel Evidence ]                  [ Stream 2: Semantic Domain ]
        • 5-Layer Spectral Decomposition              • OCR & Math Regex Tokenizer
        • Medial Axis Ridge Skeleton                  • Subject Classification
        • Connected-Component Clusters                • Geometric Graph Topology
                   │                                             │
                   └──────────────────────┬──────────────────────┘
                                          ▼
                            [ Hybrid Constraint Fusion ]
                            • RANSAC Conic & Line Fitting
                            • Exact Analytical Intersections
                            • Angular Bisector Typography
                                          │
                                          ▼
                              [ Universal Visual IR AST ]
                                          │
                   ┌──────────────────────┼──────────────────────┐
                   ▼                      ▼                      ▼
             [ Pure SVG ]          [ LaTeX TikZ ]       [ Matplotlib Py ]
                   │
                   ▼
       [ Closed-Loop RVR Verification ]
       • In-Memory Vector Rasterization
       • Pixel Residual Difference Heatmap
       • Edge-IoU Quality Score (Passed >= 0.70)
```

---

## ⚡ Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/tawhid120/acad-visual.git
cd acad-visual

# Install dependencies and package in editable mode
pip install -e .
```

### Command Line Interface (CLI)

```bash
# Reconstruct a mathematics diagram with all export formats
acad_visual --input path/to/diagram.png --subject math --output-dir ./output --formats svg,tikz,py,json

# Reconstruct a biology or physics diagram
acad_visual --input path/to/cell.png --subject biology --output-dir ./bio_output
acad_visual --input path/to/lens.png --subject physics --output-dir ./phys_output
```

### Python API

```python
from acad_visual import AcadVisualEngine

# Initialize framework
engine = AcadVisualEngine()

# Reconstruct diagram from reference image
result = engine.reconstruct(
    image_path="downloaded_diagrams/hsc_math2_HSC_math_2nd_paper_panjeeri_guide_part2_chapter_7_23_.png",
    subject="math",
    output_dir="./reconstruction_output",
    formats=["svg", "tikz", "py", "json"]
)

print(f"Status: {result.status}")
print(f"SVG saved to: {result.artifacts['svg']}")
print(f"TikZ saved to: {result.artifacts['tikz']}")
```

---

## 📁 Repository Structure

```
acad-visual/
├── acad_visual/
│   ├── api/                 # High-level Python API (AcadVisualEngine)
│   ├── cli/                 # CLI entrypoint (acad_visual command)
│   ├── core/                # VisualIR AST, Primitives, Coordinate Systems
│   ├── evaluation/          # Collision Auditor, RVR Verifier, Similarity Metrics
│   ├── geometry/            # Analytical Solvers, RANSAC Curve Fitters, Layout Optimizers
│   ├── pipelines/           # Master Reconstruction Pipeline Orchestrator
│   ├── providers/           # OCR, Vision, and Vector Provider Adapters
│   ├── renderers/           # SVG, TikZ, and Matplotlib Renderers
│   ├── subjects/            # Domain Engines (Math, Physics, Chem, Bio, Geo, etc.)
│   ├── tests/               # Comprehensive automated test suite
│   └── vision/              # Pixel Field, Skeletons, Contours, Preprocessors
├── downloaded_diagrams/     # Reference benchmark academic diagrams
├── CONTRIBUTING.md          # Guide for open-source contributors
├── LICENSE                  # MIT License
├── pyproject.toml           # Modern Python packaging configuration
├── requirements.txt         # Package dependencies
└── setup.py                 # Setuptools installer
```

---

## 🧪 Testing

Run the full automated test suite:

```bash
python -m unittest discover -s acad_visual/tests
```

All 11 unit & integration tests pass with 100% success.

---

## 🤝 Contributing

Contributions are warmly welcomed! Please read our [Contributing Guide](CONTRIBUTING.md) for details on adding new subject engines, submitting bug fixes, and proposing enhancements.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

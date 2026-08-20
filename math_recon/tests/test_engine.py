"""
Unit and Integration Tests for MathRecon Engine.
"""

import unittest
import os
import json
from math_recon.core.models import DiagramIR, Point, Segment, ParabolaCurve, ArrowType, RightAngleMarker, ArcAngleMarker, MathLabel
from math_recon.core.serializer import IRSerializer
from math_recon.solver.geometry_solver import GeometrySolver
from math_recon.renderers.svg_renderer import SVGRenderer
from math_recon.renderers.tikz_renderer import TikZRenderer
from math_recon.renderers.matplotlib_renderer import MatplotlibRenderer
from math_recon.engine import DiagramReconstructionEngine


class TestMathReconEngine(unittest.TestCase):

    def test_ir_serialization(self):
        """Test IR to JSON and back."""
        ir = DiagramIR(width=500, height=400)
        ir.points.append(Point(id="p1", x=100.0, y=150.0, label="P"))
        ir.segments.append(Segment(id="s1", start=(0.0, 0.0), end=(100.0, 100.0), arrows=ArrowType.BOTH))
        
        json_str = IRSerializer.to_json(ir)
        deserialized = IRSerializer.from_json(json_str)
        
        self.assertEqual(deserialized.width, 500)
        self.assertEqual(len(deserialized.points), 1)
        self.assertEqual(deserialized.points[0].id, "p1")
        self.assertEqual(len(deserialized.segments), 1)
        self.assertEqual(deserialized.segments[0].arrows, ArrowType.BOTH)

    def test_parabola_intersection(self):
        """Test mathematical solver for parabola-line intersections."""
        # Parabola y = x^2, Line y = 4 (passing through (-2, 4) and (2, 4))
        intersections = GeometrySolver.solve_parabola_line_intersection(
            a=1.0, b=0.0, c=0.0,
            line_pt1=(-10.0, 4.0),
            line_pt2=(10.0, 4.0)
        )
        self.assertEqual(len(intersections), 2)
        self.assertAlmostEqual(intersections[0][0], -2.0)
        self.assertAlmostEqual(intersections[1][0], 2.0)

    def test_right_angle_geometry(self):
        """Test 90-degree orthogonal corner computation."""
        vertex = (0.0, 0.0)
        arm1 = (10.0, 0.0)
        arm2 = (0.0, 10.0)
        box = GeometrySolver.compute_right_angle_box(vertex, arm1, arm2, size=10.0)
        self.assertEqual(len(box), 3)
        self.assertAlmostEqual(box[0][0], 10.0)
        self.assertAlmostEqual(box[0][1], 0.0)
        self.assertAlmostEqual(box[1][0], 10.0)
        self.assertAlmostEqual(box[1][1], 10.0)
        self.assertAlmostEqual(box[2][0], 0.0)
        self.assertAlmostEqual(box[2][1], 10.0)

    def test_renderers_output(self):
        """Test SVG, TikZ, and Matplotlib code generation."""
        engine = DiagramReconstructionEngine()
        test_img = "downloaded_diagrams/hsc_math2_HSC_math_2nd_paper_panjeeri_guide_part2_chapter_7_23_.png"
        
        if os.path.exists(test_img):
            results = engine.process(image_path=test_img, formats=("svg", "tikz", "py", "json"))
            self.assertIn("svg", results)
            self.assertTrue(results["svg"].startswith("<svg"))
            self.assertTrue(results["svg"].endswith("</svg>"))
            self.assertIn("tikz", results)
            self.assertIn("\\begin{tikzpicture}", results["tikz"])
            self.assertIn("matplotlib_py", results)
            self.assertIn("import matplotlib.pyplot as plt", results["matplotlib_py"])
            self.assertIn("json", results)


if __name__ == "__main__":
    unittest.main()

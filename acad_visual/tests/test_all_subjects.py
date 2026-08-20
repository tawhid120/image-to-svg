"""
Comprehensive Test Suite for acad_visual Framework across all Academic Subjects.
"""

import unittest
import os
import tempfile
from acad_visual.core.ir import VisualIR
from acad_visual.core.serializer import VisualIRSerializer
from acad_visual.subjects import get_engine
from acad_visual.renderers.svg_renderer import UniversalSVGRenderer
from acad_visual.renderers.tikz_renderer import UniversalTikZRenderer
from acad_visual.renderers.matplotlib_renderer import UniversalMatplotlibRenderer
from acad_visual.evaluation.label_audit import LabelAuditor
from acad_visual.evaluation.qa_loop import QALoopController


class TestAcadVisualAllSubjects(unittest.TestCase):

    def test_math_engine_reconstruction(self):
        engine = get_engine("math")
        ir = engine.reconstruct_from_features({"image_size": (650, 480)})
        self.assertEqual(ir.subject, "math")
        self.assertEqual(len(ir.conics), 1)
        self.assertGreater(len(ir.segments), 3)
        self.assertEqual(len(ir.arc_angles), 3)
        self.assertEqual(len(ir.right_angles), 2)
        
        # Verify SVG rendering
        svg = UniversalSVGRenderer(ir).render()
        self.assertIn("<svg", svg)
        self.assertIn("f(x) = ax", svg)
        self.assertIn("baseline-shift", svg)

    def test_biology_engine_reconstruction(self):
        engine = get_engine("biology")
        ir = engine.reconstruct_from_features({"image_size": (750, 550)})
        self.assertEqual(ir.subject, "biology")
        self.assertGreater(len(ir.organic_shapes), 3)
        self.assertGreater(len(ir.callouts), 3)
        
        # Verify Callout labels & Leader lines
        svg = UniversalSVGRenderer(ir).render()
        self.assertIn("Cell Membrane", svg)
        self.assertIn("Nucleus", svg)
        self.assertIn("Mitochondria", svg)

    def test_physics_engine_reconstruction(self):
        engine = get_engine("physics")
        ir = engine.reconstruct_from_features({"image_size": (750, 480)})
        self.assertEqual(ir.subject, "physics")
        self.assertGreater(len(ir.points), 3)
        self.assertGreater(len(ir.segments), 3)
        
        svg = UniversalSVGRenderer(ir).render()
        self.assertIn("Convex Lens", svg)

    def test_chemistry_engine_reconstruction(self):
        engine = get_engine("chemistry")
        ir = engine.reconstruct_from_features({"image_size": (650, 480)})
        self.assertEqual(ir.subject, "chemistry")
        self.assertGreater(len(ir.polygons), 0)
        self.assertGreater(len(ir.segments), 3)
        
        svg = UniversalSVGRenderer(ir).render()
        self.assertIn("Salicylic Acid", svg)

    def test_geography_commerce_arts_engines(self):
        geo_ir = get_engine("geography").reconstruct_from_features({"image_size": (700, 500)})
        self.assertEqual(geo_ir.subject, "geography")
        
        comm_ir = get_engine("commerce").reconstruct_from_features({"image_size": (750, 450)})
        self.assertEqual(comm_ir.subject, "commerce")
        
        arts_ir = get_engine("arts").reconstruct_from_features({"image_size": (750, 420)})
        self.assertEqual(arts_ir.subject, "arts")

    def test_ir_serialization_fidelity(self):
        for subj in ["math", "physics", "chemistry", "biology", "geography", "commerce", "arts"]:
            ir = get_engine(subj).reconstruct_from_features({"image_size": (700, 500)})
            json_str = VisualIRSerializer.to_json(ir)
            deserialized = VisualIRSerializer.from_json(json_str)
            self.assertEqual(ir.subject, deserialized.subject)
            self.assertEqual(len(ir.labels), len(deserialized.labels))

    def test_qa_loop_zero_collision(self):
        math_ir = get_engine("math").reconstruct_from_features({"image_size": (650, 480)})
        qa_res = QALoopController.audit_and_refine(math_ir)
        self.assertTrue(qa_res["passed"])


if __name__ == "__main__":
    unittest.main()

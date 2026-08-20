"""
Unit & Integration Tests for Pixel Evidence Field, RANSAC Fitting, and RVR Verification.
"""

import unittest
import os
import numpy as np
import cv2
from acad_visual.vision.pixel_field import PixelEvidenceField
from acad_visual.geometry.ransac_fitter import RANSACGeometryFitter
from acad_visual.evaluation.rvr_verifier import RVRVerifier


class TestPixelReconstruction(unittest.TestCase):

    def setUp(self):
        self.benchmark_img = "downloaded_diagrams/hsc_math2_HSC_math_2nd_paper_panjeeri_guide_part2_chapter_7_23_.png"

    def test_pixel_evidence_field_layers(self):
        pef = PixelEvidenceField(self.benchmark_img)
        summary = pef.get_summary()
        
        self.assertIn("rgb", pef.layers)
        self.assertIn("gray", pef.layers)
        self.assertIn("threshold_map", pef.layers)
        self.assertIn("edge_map", pef.layers)
        self.assertIn("skeleton_map", pef.layers)
        
        self.assertGreater(summary["total_clusters"], 0)
        self.assertGreater(pef.width, 100)
        self.assertGreater(pef.height, 100)

    def test_ransac_line_fitting_synthetic(self):
        # Generate synthetic noisy line: y = 2x + 5
        xs = np.linspace(0, 100, 100)
        ys = 2.0 * xs + 5.0 + np.random.normal(0, 0.5, 100)
        # Add 20 random outliers
        outlier_xs = np.random.uniform(0, 100, 20)
        outlier_ys = np.random.uniform(0, 200, 20)
        all_pts = list(zip(xs, ys)) + list(zip(outlier_xs, outlier_ys))

        fit_res = RANSACGeometryFitter.fit_line_ransac(all_pts)
        self.assertIsNotNone(fit_res)
        self.assertAlmostEqual(fit_res["slope"], 2.0, delta=0.2)
        self.assertAlmostEqual(fit_res["intercept"], 5.0, delta=2.0)

    def test_ransac_parabola_fitting_synthetic(self):
        # Generate synthetic noisy parabola: y = 0.5 * x^2 - 2 * x + 3
        xs = np.linspace(-10, 10, 150)
        ys = 0.5 * (xs ** 2) - 2.0 * xs + 3.0 + np.random.normal(0, 0.4, 150)
        outlier_xs = np.random.uniform(-10, 10, 30)
        outlier_ys = np.random.uniform(0, 100, 30)
        all_pts = list(zip(xs, ys)) + list(zip(outlier_xs, outlier_ys))

        fit_res = RANSACGeometryFitter.fit_parabola_ransac(all_pts)
        self.assertIsNotNone(fit_res)
        self.assertAlmostEqual(fit_res["a"], 0.5, delta=0.08)
        self.assertAlmostEqual(fit_res["b"], -2.0, delta=0.4)
        self.assertAlmostEqual(fit_res["c"], 3.0, delta=1.5)
        self.assertGreater(fit_res["r_squared"], 0.95)

    def test_rvr_verification_metrics(self):
        res = RVRVerifier.compute_rvr_metrics(
            original_image_path=self.benchmark_img,
            reconstructed_image_path="math_artwork.png",
            diff_output_path="rvr_difference_map.png"
        )
        self.assertIn("alignment_score", res)
        self.assertIn("edge_iou", res)
        self.assertGreater(res["alignment_score"], 0.0)


if __name__ == "__main__":
    unittest.main()

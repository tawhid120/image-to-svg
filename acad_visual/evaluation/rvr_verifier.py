"""
Raster-Vector-Raster (RVR) Verification & Closed-Loop Refinement Engine.
Computes pixel-level difference heatmaps, edge alignment IoU, and residual error matrices.
"""

from __future__ import annotations
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, Tuple, Optional
from ..core.ir import VisualIR


class RVRVerifier:
    """
    Closed-Loop Raster-Vector-Raster (RVR) Quality Auditor.
    Compares original reference image against reconstructed vector bitmap.
    """

    @staticmethod
    def compute_rvr_metrics(
        original_image_path: str,
        reconstructed_image_path: str,
        diff_output_path: Optional[str] = None
    ) -> Dict[str, Any]:
        orig = cv2.imread(original_image_path)
        rec = cv2.imread(reconstructed_image_path)

        if orig is None or rec is None:
            return {
                "error": "Failed to read image files",
                "alignment_score": 0.0,
                "passed": False
            }

        # Normalize resolution
        h_orig, w_orig = orig.shape[:2]
        rec_resized = cv2.resize(rec, (w_orig, h_orig))

        # 1. Grayscale & Intensity differences
        g_orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
        g_rec = cv2.cvtColor(rec_resized, cv2.COLOR_BGR2GRAY)

        # Invert if light-on-dark / dark-on-light
        diff = cv2.absdiff(g_orig, g_rec)
        mean_pixel_diff = float(np.mean(diff))

        # 2. Edge Map IoU
        e_orig = cv2.Canny(g_orig, 50, 150)
        e_rec = cv2.Canny(g_rec, 50, 150)

        # Dilate edges by 2px to allow subpixel tolerance
        k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        e_orig_d = cv2.dilate(e_orig, k)
        e_rec_d = cv2.dilate(e_rec, k)

        intersection = np.logical_and(e_orig_d > 0, e_rec_d > 0).sum()
        union = np.logical_or(e_orig_d > 0, e_rec_d > 0).sum()

        edge_iou = float(intersection / union) if union > 0 else 1.0

        # Normalized cross-correlation
        res = cv2.matchTemplate(g_orig, g_rec, cv2.TM_CCOEFF_NORMED)
        ncc = float(res[0][0]) if res is not None and res.size > 0 else edge_iou

        # Combined Alignment Score (0.0 to 1.0)
        alignment_score = float(np.clip(0.6 * edge_iou + 0.4 * max(0.0, ncc), 0.0, 1.0))

        # Save residual heatmap if path is requested
        if diff_output_path:
            heatmap = cv2.applyColorMap(diff, cv2.COLORMAP_JET)
            cv2.imwrite(diff_output_path, heatmap)

        return {
            "alignment_score": alignment_score,
            "edge_iou": edge_iou,
            "ncc": ncc,
            "mean_pixel_diff": mean_pixel_diff,
            "passed": alignment_score >= 0.70,
            "diff_saved": diff_output_path if diff_output_path else None
        }

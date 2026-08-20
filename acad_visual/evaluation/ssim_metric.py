"""
Structural Similarity (SSIM) and Perceptual Metrics for Diagram Evaluation.
"""

from __future__ import annotations
import cv2
import numpy as np
from typing import Dict, Any


class VisualSimilarityMetric:
    """Computes edge-based structural similarity and IoU between raster assets."""

    @staticmethod
    def compute_edge_similarity(img1: np.ndarray, img2: np.ndarray) -> float:
        # Resize img2 to img1 shape if necessary
        if img1.shape[:2] != img2.shape[:2]:
            img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

        g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) if len(img1.shape) == 3 else img1
        g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) if len(img2.shape) == 3 else img2

        # Canny edge maps
        e1 = cv2.Canny(g1, 50, 150)
        e2 = cv2.Canny(g2, 50, 150)

        # Dilate slightly to allow subpixel tolerance
        k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        e1_d = cv2.dilate(e1, k)
        e2_d = cv2.dilate(e2, k)

        intersection = np.logical_and(e1_d > 0, e2_d > 0).sum()
        union = np.logical_or(e1_d > 0, e2_d > 0).sum()

        iou = float(intersection / union) if union > 0 else 1.0
        return iou

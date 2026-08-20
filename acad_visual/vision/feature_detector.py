"""
Geometric and Anatomical Feature Detector.
"""

from __future__ import annotations
import cv2
import numpy as np
from typing import List, Dict, Any, Tuple


class FeatureDetector:
    """Detects line segments, corner hubs, and potential arrowheads."""

    @staticmethod
    def detect_features(gray_img: np.ndarray, binary_img: np.ndarray) -> Dict[str, Any]:
        # 1. Hough Lines
        edges = cv2.Canny(gray_img, 50, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=30, minLineLength=20, maxLineGap=10)
        
        detected_lines = []
        if lines is not None:
            for l in lines:
                pts = l.reshape(-1)
                if len(pts) == 4:
                    detected_lines.append(((float(pts[0]), float(pts[1])), (float(pts[2]), float(pts[3]))))

        # 2. Corner / Junction detection
        corners = cv2.goodFeaturesToTrack(gray_img, maxCorners=60, qualityLevel=0.01, minDistance=12)
        corner_pts = []
        if corners is not None:
            for c in corners:
                pts = c.reshape(-1)
                if len(pts) >= 2:
                    corner_pts.append((float(pts[0]), float(pts[1])))

        return {
            "lines": detected_lines,
            "corners": corner_pts,
        }

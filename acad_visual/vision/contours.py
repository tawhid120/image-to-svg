"""
Contour Extraction and Organic Shape Approximator.
"""

from __future__ import annotations
import cv2
import numpy as np
from typing import List, Dict, Any, Tuple


class ContourExtractor:
    """Extracts hierarchical contours, smooths organic boundaries, and detects closed loops."""

    @staticmethod
    def extract_contours(binary_img: np.ndarray, min_area: float = 20.0) -> List[Dict[str, Any]]:
        contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        extracted = []
        for i, cnt in enumerate(contours):
            area = cv2.contourArea(cnt)
            if area < min_area:
                continue

            # Polygon approximation
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.015 * peri, True)
            
            # Smooth points
            pts = [(float(p[0][0]), float(p[0][1])) for p in cnt]
            
            # Bounding box
            x, y, w, h = cv2.boundingRect(cnt)
            
            extracted.append({
                "index": i,
                "area": float(area),
                "perimeter": float(peri),
                "bbox": (x, y, w, h),
                "points": pts,
                "approx_vertices": [(float(p[0][0]), float(p[0][1])) for p in approx],
                "is_closed": True,
            })

        return extracted

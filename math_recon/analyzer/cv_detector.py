"""
Computer Vision Feature Detector for Mathematical Diagrams using OpenCV.
"""

from __future__ import annotations
import cv2
import numpy as np
from typing import Dict, Any, List, Tuple


class CVFeatureDetector:
    """
    Analyzes reference diagram images using OpenCV to extract contours, lines,
    corner hubs, connected components, and potential text regions.
    """

    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError(f"Could not open or find the image: {image_path}")
        self.height, self.width = self.image.shape[:2]
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def analyze(self) -> Dict[str, Any]:
        """Runs the complete CV detection pipeline."""
        # 1. Binarization (Otsu's thresholding)
        _, thresh = cv2.threshold(self.gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        # 2. Extract Connected Components
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
        
        # 3. Find Contours
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # 4. Detect Line segments via Hough Transform
        edges = cv2.Canny(self.gray, 50, 150, apertureSize=3)
        hough_lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=30, minLineLength=15, maxLineGap=8)
        
        detected_lines = []
        if hough_lines is not None:
            for line in hough_lines:
                pts = line.reshape(-1)
                if len(pts) == 4:
                    x1, y1, x2, y2 = pts
                    detected_lines.append(((float(x1), float(y1)), (float(x2), float(y2))))

        # 5. Detect Strong Geometric Corners / Junctions
        corners = cv2.goodFeaturesToTrack(self.gray, maxCorners=50, qualityLevel=0.01, minDistance=10)
        corner_points = []
        if corners is not None:
            for c in corners:
                pts = c.reshape(-1)
                if len(pts) >= 2:
                    corner_points.append((float(pts[0]), float(pts[1])))

        # 6. Separate potential text bounding boxes from geometric curves
        text_regions = []
        curve_regions = []
        for i in range(1, num_labels):
            x, y, w, h, area = stats[i]
            if area < 10:  # Noise
                continue
            if area > (self.width * self.height * 0.05):  # Large curve
                curve_regions.append({"bbox": (x, y, w, h), "area": area, "centroid": (float(centroids[i][0]), float(centroids[i][1]))})
            else:
                text_regions.append({"bbox": (x, y, w, h), "area": area, "centroid": (float(centroids[i][0]), float(centroids[i][1]))})

        return {
            "image_size": (self.width, self.height),
            "num_components": int(num_labels),
            "detected_lines_count": len(detected_lines),
            "lines": detected_lines,
            "corners": corner_points,
            "text_regions": text_regions,
            "curve_regions": curve_regions,
        }

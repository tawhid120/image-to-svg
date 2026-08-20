"""
Multi-Layer Pixel Information Field and Connected Component Clustering.
Treats raster reference images as structured multi-layer pixel evidence fields.
"""

from __future__ import annotations
import cv2
import numpy as np
from typing import Dict, Any, List, Tuple, Optional


class PixelEvidenceField:
    """
    Multi-Layer Pixel Information Field.
    Decomposes reference image into RGB, Grayscale, Adaptive Threshold,
    Ridge Skeleton, Gradient, and Connected-Component Pixel Clusters.
    """

    def __init__(self, image_path: str):
        self.image_path = image_path
        self.bgr = cv2.imread(image_path)
        if self.bgr is None:
            raise FileNotFoundError(f"Cannot load image at {image_path}")
        
        self.height, self.width = self.bgr.shape[:2]
        self.rgb = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2RGB)
        self.gray = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2GRAY)
        
        self.layers: Dict[str, np.ndarray] = {}
        self.clusters: List[Dict[str, Any]] = []
        self._extract_all_layers()
        self._cluster_connected_components()

    def _extract_all_layers(self) -> None:
        """Extracts 5 multi-spectral visual layers."""
        # Layer A: RGB
        self.layers["rgb"] = self.rgb

        # Layer B: Grayscale & Normalized Intensity
        self.layers["gray"] = self.gray
        self.layers["intensity_norm"] = self.gray.astype(np.float32) / 255.0

        # Layer C: Adaptive Threshold Map
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(self.gray)
        _, otsu_thresh = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        self.layers["threshold_map"] = otsu_thresh

        # Layer D: Edge & Gradient Map
        edges = cv2.Canny(self.gray, 50, 150)
        self.layers["edge_map"] = edges

        # Layer E: Ridge Skeleton & Distance Transform
        dist_transform = cv2.distanceTransform(otsu_thresh, cv2.DIST_L2, 5)
        self.layers["dist_transform"] = dist_transform
        
        # Morphological skeleton thinning
        skeleton = np.zeros_like(otsu_thresh)
        element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        temp_img = otsu_thresh.copy()
        while True:
            eroded = cv2.erode(temp_img, element)
            opened = cv2.morphologyEx(eroded, cv2.MORPH_OPEN, element)
            subset = eroded - opened
            skeleton = cv2.bitwise_or(skeleton, subset)
            temp_img = eroded.copy()
            if cv2.countNonZero(temp_img) == 0:
                break
        self.layers["skeleton_map"] = skeleton

    def _cluster_connected_components(self, min_pixels: int = 15) -> None:
        """Clusters foreground pixels into connected semantic components."""
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(self.layers["threshold_map"], connectivity=8)
        
        for i in range(1, num_labels):
            area = stats[i, cv2.CC_STAT_AREA]
            if area < min_pixels:
                continue

            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            cx, cy = centroids[i]

            # Get exact pixel coordinates belonging to this cluster
            mask = (labels == i).astype(np.uint8)
            y_indices, x_indices = np.where(mask > 0)
            coords = list(zip(x_indices.astype(float), y_indices.astype(float)))

            # Rough classification: aspect ratio, linearity, compactness
            aspect_ratio = w / (h if h > 0 else 1.0)
            compactness = area / (w * h if w * h > 0 else 1.0)

            cluster_type = "shape"
            if w < 35 and h < 35 and area < 400:
                cluster_type = "text_or_marker"
            elif aspect_ratio > 3.0 or aspect_ratio < 0.33:
                cluster_type = "line_candidate"
            else:
                cluster_type = "curve_or_polygon"

            self.clusters.append({
                "label_id": i,
                "area": int(area),
                "bbox": (int(x), int(y), int(w), int(h)),
                "centroid": (float(cx), float(cy)),
                "pixel_count": len(coords),
                "pixel_points": coords,
                "aspect_ratio": float(aspect_ratio),
                "cluster_type": cluster_type
            })

    def get_summary(self) -> Dict[str, Any]:
        """Returns structured metadata of the pixel evidence field."""
        return {
            "image_path": self.image_path,
            "dimensions": (self.width, self.height),
            "layers_available": list(self.layers.keys()),
            "total_clusters": len(self.clusters),
            "cluster_types": {
                "text_or_marker": len([c for c in self.clusters if c["cluster_type"] == "text_or_marker"]),
                "line_candidate": len([c for c in self.clusters if c["cluster_type"] == "line_candidate"]),
                "curve_or_polygon": len([c for c in self.clusters if c["cluster_type"] == "curve_or_polygon"]),
            }
        }

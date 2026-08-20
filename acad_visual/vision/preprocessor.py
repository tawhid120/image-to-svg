"""
Image Preprocessing Pipeline using OpenCV.
"""

from __future__ import annotations
import cv2
import numpy as np
from typing import Tuple, Dict, Any


class ImagePreprocessor:
    """Handles contrast enhancement, adaptive thresholding, and denoising."""

    @staticmethod
    def load_and_preprocess(image_path: str) -> Dict[str, Any]:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Image not found at {image_path}")

        h, w = img.shape[:2]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Contrast enhancement via CLAHE
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)

        # Otsu binarization
        _, binary = cv2.threshold(enhanced, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Denoise small salt-and-pepper noise
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        denoised = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

        return {
            "original": img,
            "gray": gray,
            "enhanced": enhanced,
            "binary": binary,
            "denoised": denoised,
            "dimensions": (w, h),
        }

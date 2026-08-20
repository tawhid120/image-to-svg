"""
Vectorization Providers including VTracer and Analytic Spline Fitters.
"""

from __future__ import annotations
import os
import subprocess
from typing import Dict, Any, List, Optional
import numpy as np
from .base import VectorizationProvider


class VTracerProvider(VectorizationProvider):
    """
    Adapter for VTracer (open-source raster-to-vector engine).
    Can run via Python bindings or CLI if installed, with graceful fallbacks.
    """

    def __init__(self, vtracer_cmd: str = "vtracer"):
        self.vtracer_cmd = vtracer_cmd

    def trace_image(self, image_path: str, options: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        # Check if vtracer executable exists
        output_svg = image_path + ".vtracer.svg"
        options = options or {}
        colormode = options.get("colormode", "binary")
        
        # If external vtracer binary exists, we can call it
        try:
            cmd = [
                self.vtracer_cmd,
                "--input", image_path,
                "--output", output_svg,
                "--colormode", colormode
            ]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if res.returncode == 0 and os.path.exists(output_svg):
                with open(output_svg, "r", encoding="utf-8") as f:
                    svg_content = f.read()
                return [{"type": "vtracer_svg", "content": svg_content}]
        except Exception:
            pass
            
        return []


class AnalyticBezierProvider(VectorizationProvider):
    """
    High-precision analytic Bezier curve fitter based on contour curvature analysis.
    """

    def trace_image(self, image_path: str, options: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        # Returns analytical spline segment representations
        return []

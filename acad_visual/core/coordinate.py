"""
Coordinate Systems and Geometric Transformations.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Tuple


@dataclass
class CoordinateFrame:
    """Mathematical world coordinate space mapping to screen pixels."""
    origin_x: float = 0.0
    origin_y: float = 0.0
    x_range: Tuple[float, float] = (-10.0, 10.0)
    y_range: Tuple[float, float] = (-10.0, 10.0)
    invert_y: bool = True  # SVG/Canvas has Y increasing downwards
    show_axes: bool = False


class CoordinateTransformer:
    """Transforms coordinates between mathematical world space and screen pixels."""

    @staticmethod
    def world_to_screen(
        pt: Tuple[float, float],
        frame: CoordinateFrame,
        width: float,
        height: float,
        padding: float = 40.0
    ) -> Tuple[float, float]:
        x_w, y_w = pt
        x_min, x_max = frame.x_range
        y_min, y_max = frame.y_range

        drawable_w = width - 2 * padding
        drawable_h = height - 2 * padding

        norm_x = (x_w - x_min) / (x_max - x_min) if abs(x_max - x_min) > 1e-9 else 0.5
        norm_y = (y_w - y_min) / (y_max - y_min) if abs(y_max - y_min) > 1e-9 else 0.5

        screen_x = padding + norm_x * drawable_w
        if frame.invert_y:
            screen_y = height - padding - norm_y * drawable_h
        else:
            screen_y = padding + norm_y * drawable_h

        return (screen_x, screen_y)

    @staticmethod
    def screen_to_world(
        pt: Tuple[float, float],
        frame: CoordinateFrame,
        width: float,
        height: float,
        padding: float = 40.0
    ) -> Tuple[float, float]:
        s_x, s_y = pt
        x_min, x_max = frame.x_range
        y_min, y_max = frame.y_range

        drawable_w = width - 2 * padding
        drawable_h = height - 2 * padding

        norm_x = (s_x - padding) / drawable_w if drawable_w > 0 else 0.5
        if frame.invert_y:
            norm_y = (height - padding - s_y) / drawable_h if drawable_h > 0 else 0.5
        else:
            norm_y = (s_y - padding) / drawable_h if drawable_h > 0 else 0.5

        x_w = x_min + norm_x * (x_max - x_min)
        y_w = y_min + norm_y * (y_max - y_min)
        return (x_w, y_w)

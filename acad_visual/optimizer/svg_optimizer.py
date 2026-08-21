"""
SVG Path Simplification and DOM Optimization Engine.
Prunes redundant precision, cleans up path attributes, and structures semantic <g> groups.
"""

from __future__ import annotations
import re
import xml.etree.ElementTree as ET
from typing import Optional


class SVGOptimizer:
    """
    Optimizes and structures raw SVG outputs.
    """

    @classmethod
    def optimize_svg(
        cls,
        svg_content: str,
        decimal_places: int = 2,
        remove_empty_paths: bool = True
    ) -> str:
        """
        Cleans and optimizes SVG markup.
        """
        # 1. Round decimal numbers in path commands
        def round_floats(match):
            num = float(match.group(0))
            if num.is_integer():
                return str(int(num))
            return f"{num:.{decimal_places}f}".rstrip("0").rstrip(".")

        # Regex to match floating point numbers
        optimized = re.sub(r'[-+]?\d*\.\d+', round_floats, svg_content)

        # 2. Clean empty groups or empty d attributes if requested
        if remove_empty_paths:
            optimized = re.sub(r'<path\s+[^>]*d=["\']\s*["\'][^>]*/>', '', optimized)
            optimized = re.sub(r'<g\s*>\s*</g>', '', optimized)

        # 3. Ensure proper XML namespace and headers
        if not optimized.strip().startswith("<?xml") and not optimized.strip().startswith("<svg"):
            optimized = f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n{optimized}\n</svg>'

        return optimized

    @classmethod
    def wrap_in_semantic_groups(
        cls,
        layer_svg_snippets: list[tuple[str, str]],
        width: int,
        height: int
    ) -> str:
        """
        Wraps multiple SVG layer snippets into labeled <g id="..."> semantic groups.
        """
        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
            '  <defs>',
            '    <style>',
            '      .layer-bg { fill-rule: evenodd; }',
            '      .layer-fg { fill-rule: nonzero; }',
            '    </style>',
            '  </defs>',
        ]

        for layer_name, snippet in layer_svg_snippets:
            parts.append(f'  <g id="{layer_name}">')
            # Indent snippet
            for line in snippet.strip().splitlines():
                if not line.startswith("<svg") and not line.startswith("</svg") and not line.startswith("<?xml"):
                    parts.append(f'    {line}')
            parts.append('  </g>')

        parts.append('</svg>')
        return "\n".join(parts)

"""
Command-Line Interface (CLI) for MathRecon Engine.
"""

from __future__ import annotations
import argparse
import sys
import os
from .engine import DiagramReconstructionEngine


def main():
    parser = argparse.ArgumentParser(
        description="MathRecon - Powerful General-Purpose Mathematical Diagram Reconstruction Engine"
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the input reference image (e.g. diagram.png)"
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="./output_diagrams",
        help="Directory to save reconstructed artifacts (SVG, TikZ, Python, JSON)"
    )
    parser.add_argument(
        "--formats", "-f",
        default="svg,tikz,py,json",
        help="Comma-separated list of output formats: svg,tikz,py,json"
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)

    format_list = tuple(fmt.strip().lower() for fmt in args.formats.split(","))

    print(f"[*] Initializing MathRecon Engine...")
    print(f"[*] Input reference: {args.input}")
    print(f"[*] Target formats: {', '.join(format_list)}")
    print(f"[*] Output directory: {args.output_dir}")

    engine = DiagramReconstructionEngine()
    results = engine.process(
        image_path=args.input,
        output_dir=args.output_dir,
        formats=format_list
    )

    print("\n[+] Reconstruction Completed Successfully!")
    if "svg_file" in results:
        print(f"  -> Vector SVG:  {results['svg_file']}")
    if "tikz_file" in results:
        print(f"  -> LaTeX TikZ:  {results['tikz_file']}")
    if "py_file" in results:
        print(f"  -> Python Code: {results['py_file']}")
    if "json_file" in results:
        print(f"  -> IR JSON:     {results['json_file']}")


if __name__ == "__main__":
    main()

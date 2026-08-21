"""
Command Line Interface for acad_visual Framework.
High-Precision Parametric Vector Reconstruction & Academic Artwork Synthesizer.
"""

from __future__ import annotations
import argparse
import sys
import os
from ..api.engine import AcademicVisualEngine


def main():
    parser = argparse.ArgumentParser(
        prog="acad_visual",
        description="Academic Visual Reconstruction & High-Precision Vector Generation Framework"
    )
    parser.add_argument("--input", "-i", required=True, help="Path to reference image (PNG, JPG, etc.)")
    parser.add_argument("--subject", "-s", default="math", choices=["math", "physics", "chemistry", "biology", "geography", "commerce", "arts"], help="Academic domain subject")
    parser.add_argument("--output-dir", "-o", default="./acad_output", help="Directory to save reconstructed artifacts")
    parser.add_argument("--formats", "-f", default="svg,tikz,py,json", help="Comma-separated output formats (svg,tikz,py,json)")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"[-] Error: Input file not found at {args.input}", file=sys.stderr)
        sys.exit(1)

    formats = [fmt.strip().lower() for fmt in args.formats.split(",")]

    print("==================================================================")
    print("      ACADEMIC VISUAL RECONSTRUCTION & GENERATION FRAMEWORK       ")
    print("==================================================================")
    print(f"[*] Input image:   {args.input}")
    print(f"[*] Subject:       {args.subject.upper()}")
    print(f"[*] Target format: {', '.join(formats)}")
    print(f"[*] Output dir:    {args.output_dir}")
    print("------------------------------------------------------------------")

    engine = AcademicVisualEngine(output_dir=args.output_dir)
    res = engine.reconstruct(
        image_path=args.input,
        subject=args.subject,
        target_formats=formats
    )

    if res.get("success", False):
        print("\n[+] RECONSTRUCTION SUCCESSFUL!")
        print(f"  -> Title:         {res.get('title', 'Academic Artwork')}")
        print(f"  -> QA Loop Audit: {'PASSED (0 collisions)' if res.get('qa_passed', False) else 'REFINED'}")
        for fmt, fpath in res.get("output_files", {}).items():
            print(f"  -> {fmt.upper():<6}: {fpath}")
        print("==================================================================")
    else:
        print("[-] Reconstruction failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()

import cairosvg
import os

svg_path = 'acad_output/benchmark_math/reconstructed_artwork.svg'
png_path = 'acad_output/benchmark_math/reconstructed_artwork.png'

if os.path.exists(svg_path):
    try:
        cairosvg.svg2png(url=svg_path, write_to=png_path, dpi=300)
        print("Rendered SVG to PNG via CairoSVG")
    except Exception as e:
        print("CairoSVG error:", e)

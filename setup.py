from setuptools import setup, find_packages

setup(
    name="img2svg",
    version="3.0.0",
    description="High-Fidelity AI Image to SVG Converter & Vector Reconstruction Engine.",
    packages=find_packages(include=["acad_visual", "acad_visual.*"]),
    install_requires=[
        "numpy>=1.22.0",
        "opencv-python>=4.6.0",
        "matplotlib>=3.5.0",
        "scipy>=1.8.0",
        "sympy>=1.10.0"
    ],
    entry_points={
        "console_scripts": [
            "img2svg=acad_visual.cli.main:main",
            "image-to-svg=acad_visual.cli.main:main",
            "acad_visual=acad_visual.cli.main:main",
        ]
    },
)

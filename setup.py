from setuptools import setup, find_packages

setup(
    name="acad-visual",
    version="2.5.0",
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
            "acad_visual=acad_visual.cli.main:main",
            "acad-visual=acad_visual.cli.main:main",
        ]
    },
)

from pathlib import Path
from setuptools import setup

# read the contents of the README file
cwd = Path(__file__).parent
long_description = (cwd / "README.md").read_text()

setup(
    name="actr",
    # version is the actr pip package (this is different from the python_actr version)
    version="1.0.0",
    description="Python implementation of the ACT-R cognitive architecture",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Carleton Cognitive Modelling Lab",
    maintainer="Andy Maloney (fork)",
    url="https://github.com/asmaloney/python_actr",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
    license="MIT",
    keywords=[
        "ACT-R",
        "cognitive architecture",
        "cognitive modelling",
        "cognitive science",
        "CogSci",
    ],
    packages=[
        "python_actr",
        "python_actr.display",
        "python_actr.actr",
        "python_actr.ui",
    ],
    python_requires=">=3.0",
)

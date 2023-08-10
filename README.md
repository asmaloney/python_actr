# Python ACT-R (fork)

A Python implementation of the ACT-R cognitive architecture developed at the Carleton Cognitive Modelling (CCM) Lab.

The original pip package is called [python_actr](https://pypi.org/project/python-actr/).

## Fork

This fork of [python_actr](https://github.com/CarletonCognitiveModelingLab/python_actr) by Andy Maloney is not affiliated with the CCM lab.

I created it because the main repository isn't being updated and I need a stable, running version via pip for my [gactar](https://github.com/asmaloney/gactar) project.

Changes are noted in the [CHANGELOG](CHANGELOG.md).

The pip package for this fork is named [actr](https://pypi.org/project/actr/).

## Compatibility

Although this pip package is named `actr`, it still uses `python_actr` as its package name.

This keeps this pip package compatible with the official `python_actr` one, however **_you should only have one of them installed at a time_**. As far as I can tell, there's no way to enforce this using pip, so if the `python_actr` package is already installed, run:

```bash
pip uninstall python_actr
```

## Install

(Before installing, please see note above about compatibility with the `python_actr` package.)

```bash
pip3 install actr
```

## Use

When writing code, you use it the same way you use the `python_actr` package:

```python
from python_actr import *
```

To run a file, make sure the package is installed with pip (see above), then you can just run it like this:

```bash
python3 tutorials/hello_world.py
```

## Run Tests

```bash
make test
```

I know there are a bunch of failures - these exist in `python_actr` as well & I am not planning to investigate at this time...

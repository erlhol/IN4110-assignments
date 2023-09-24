# The `in3110-instapy` module

## Summary of the package

This package can be used to apply filters (gray scale and sepia) on images.
It also conatins a CLI that can be run by the command: `instapy`

## Install package

To install this package run

```
python3 -m pip install . in the code directory
```

To make this package editable (development mode) run in the same location:

```
pip install --editable .
```

Whenever you need a module from the package, write for instance:

```python
import in3110_instapy

```

To check if the package has been installed correctly, run:

```
python3 -m pytest -v test/test_package.py
```

which imports the `in3110_instapy` module.

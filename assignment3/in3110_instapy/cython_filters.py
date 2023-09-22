"""Cython implementation of filter functions"""
from __future__ import annotations

import cython as C
import numpy as np
from cython.cimports.libc.stdint import uint8_t # type: ignore

if not C.compiled:
    raise ImportError(
        "Cython module not compiled! Check setup.py and make sure this package has been installed, not just imported in-place."
    )

# we may need a 'const uint8_t' type to make sure we accept 'read-only' arrays
const_uint8_t = C.typedef("const uint8_t")
float64_t = C.typedef(C.double)


def cython_color2gray(image):
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    # iterate through the pixels, and apply the grayscale transform
    
    # The grayscale transform will have the weights 0.21, 0.72 and 0.07
    shape = gray_image.shape
    h: C.int = shape[0]
    w: C.int = shape[1]
    r_weight: C.float = 0.21
    g_weight: C.float = 0.72
    b_weight: C.float = 0.07

    for i in range(h):
        for j in range(w):
            pixel = gray_image[i][j]
            pixel_real = image[i][j]
            r_p: C.int = pixel_real[0]
            g_p: C.int = pixel_real[1]
            b_p: C.int = pixel_real[2]

            gray_scale: C.int = int(r_p * r_weight + g_p * g_weight + b_p * b_weight)
            pixel[0] = gray_scale
            pixel[1] = gray_scale
            pixel[2] = gray_scale

    return gray_image


def cython_color2sepia(image):
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    ...

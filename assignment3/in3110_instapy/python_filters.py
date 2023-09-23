"""pure Python implementation of image filters"""
from __future__ import annotations

import numpy as np

def python_color2gray(image: np.array) -> np.array:
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
    for i in range(shape[0]):
        for j in range(shape[1]):
            pixel = gray_image[i][j]
            pixel_real = image[i][j]
            gray_scale = pixel_real[0] * 0.21 + pixel_real[1] * 0.72 + pixel_real[2] * 0.07
            pixel[0] = gray_scale
            pixel[1] = gray_scale
            pixel[2] = gray_scale

    gray_image = gray_image.astype("uint8")
    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix

    sepia_matrix = [
    [ 0.393, 0.769, 0.189], # R
    [ 0.349, 0.686, 0.168], # G
    [ 0.272, 0.534, 0.131], # B
    ]

    shape = sepia_image.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            pixel = sepia_image[i][j]
            pixel_real = image[i][j]
            pixel[0] = min(255,pixel_real[0] * sepia_matrix[0][0] + pixel_real[1] * sepia_matrix[0][1] + pixel_real[2] * sepia_matrix[0][2])
            pixel[1] = min(255,pixel_real[0] * sepia_matrix[1][0] + pixel_real[1] * sepia_matrix[1][1] + pixel_real[2] * sepia_matrix[1][2])
            pixel[2] = min(255,pixel_real[0] * sepia_matrix[2][0] + pixel_real[1] * sepia_matrix[2][1] + pixel_real[2] * sepia_matrix[2][2])

    # Return image
    # don't forget to make sure it's the right type!
    sepia_image = sepia_image.astype("uint8")
    return sepia_image
"""numpy implementation of image filters"""
from __future__ import annotations

import numpy as np

def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    gray_image = np.empty_like(image)
    # Hint: use numpy slicing in order to have fast vectorized code
    gray_scale = image[:,:,0] * 0.21 + image[:,:,1] * 0.72 + image[:,:,2] * 0.07
    gray_image[:,:,0] = gray_scale
    gray_image[:,:,1] = gray_scale
    gray_image[:,:,2] = gray_scale
    # Return image (make sure it's the right type!)
    gray_image = gray_image.astype("uint8")
    return gray_image


def numpy_color2sepia(image: np.array, k: float = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
        you may ignore it)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = np.empty_like(image)

    # define sepia matrix (optional: with stepless sepia changes)
    sepia_matrix = [
    [ 0.393, 0.769, 0.189], # R
    [ 0.349, 0.686, 0.168], # G
    [ 0.272, 0.534, 0.131], # B
    ]

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter

    sepia_image[:,:,0] = np.minimum(255,image[:,:,0] * sepia_matrix[0][0] + image[:,:,1] * sepia_matrix[0][1] + image[:,:,2] * sepia_matrix[0][2])
    sepia_image[:,:,1] = np.minimum(255,image[:,:,0] * sepia_matrix[1][0] + image[:,:,1] * sepia_matrix[1][1] + image[:,:,2] * sepia_matrix[1][2])
    sepia_image[:,:,2] = np.minimum(255,image[:,:,0] * sepia_matrix[2][0] + image[:,:,1] * sepia_matrix[2][1] + image[:,:,2] * sepia_matrix[2][2])

    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255

    # Return image (make sure it's the right type!)
    sepia_image = sepia_image.astype("uint8")
    return sepia_image
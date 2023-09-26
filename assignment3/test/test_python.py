from in3110_instapy.python_filters import python_color2gray, python_color2sepia
import pytest
import in3110_instapy.io as io

def test_color2gray(image):
    # run color2gray
    res = python_color2gray(image)
    # check that the result has the right shape, type
    assert type(res) == type(image)
    assert res.shape == image.shape

    height = res.shape[0]
    width = res.shape[1]

    # assert uniform r,g,b values
    checking_indices = [(height // 2, width // 2), (height // 3, width // 3), (height// 4, width // 4)]
    for i, j in checking_indices:
        r_color = res[i][j][0]
        g_color = res[i][j][1]
        b_color = res[i][j][2]
        assert r_color == g_color == b_color

        # Assert graycolor
        img_r_color = image[i][j][0]
        img_g_color = image[i][j][1]
        img_b_color = image[i][j][2]

        color = int(img_r_color * 0.21 + img_g_color * 0.72 + img_b_color * 0.07)
        assert color == r_color == g_color == b_color

def test_color2sepia(image):
    # run color2sepia
    res = python_color2sepia(image)
    # check that the result has the right shape, type
    assert type(res) == type(image)
    assert res.shape == image.shape
    # verify some individual pixel samples
    # according to the sepia matrix
    sepia_matrix = [
    [ 0.393, 0.769, 0.189], # R
    [ 0.349, 0.686, 0.168], # G
    [ 0.272, 0.534, 0.131], # B
    ]

    height = res.shape[0]
    width = res.shape[1]

    checking_indices = [(height // 2, width // 2), (height // 3, width // 3), (height// 4, width // 4)]
    for i, j in checking_indices:
        r_color = res[i][j][0]
        g_color = res[i][j][1]
        b_color = res[i][j][2]

        derived_r_color = int(min(255,image[i][j][0] * sepia_matrix[0][0] + image[i][j][1] * sepia_matrix[0][1] + image[i][j][2] * sepia_matrix[0][2]))
        derived_g_color = int(min(255,image[i][j][0] * sepia_matrix[1][0] + image[i][j][1] * sepia_matrix[1][1] + image[i][j][2] * sepia_matrix[1][2]))
        derived_b_color = int(min(255,image[i][j][0] * sepia_matrix[2][0] + image[i][j][1] * sepia_matrix[2][1] + image[i][j][2] * sepia_matrix[2][2]))

        assert r_color == derived_r_color
        assert g_color == derived_g_color
        assert b_color == derived_b_color
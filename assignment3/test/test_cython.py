import numpy.testing as nt
from in3110_instapy.cython_filters import cython_color2gray, cython_color2sepia

def test_color2gray(image, reference_gray):
    # run color2gray
    res = cython_color2gray(image)
    # check that the result has the right shape, type
    assert type(res) == type(image)
    assert res.shape == image.shape
    nt.assert_allclose(res,reference_gray)

def test_color2sepia(image, reference_sepia):
    # run color2sepia
    res = cython_color2sepia(image)
    # check that the result has the right shape, type
    assert type(res) == type(image)
    assert res.shape == image.shape
    nt.assert_allclose(res,reference_sepia)

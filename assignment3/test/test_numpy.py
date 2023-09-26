import numpy.testing as nt
from in3110_instapy.numpy_filters import numpy_color2gray, numpy_color2sepia

import in3110_instapy.io as io

def test_color2gray(image, reference_gray):
    # run color2gray
    res = numpy_color2gray(image)
    # check that the result has the right shape, type
    assert type(res) == type(image)
    assert res.shape == image.shape
    nt.assert_allclose(res,reference_gray)


def test_color2sepia(image, reference_sepia):
    # run color2sepia
    res = numpy_color2sepia(image)
    # check that the result has the right shape, type
    assert type(res) == type(image)
    assert res.shape == image.shape
    nt.assert_allclose(res,reference_sepia)

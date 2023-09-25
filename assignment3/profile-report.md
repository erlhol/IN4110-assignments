# Profiling report

## Questions

A few questions below. We are not asking for lots of detail,
just 1-2 sentences each.

### Question 1

> which profiler produced the most useful output, and why?

I think they are both great ways to measure performance. They
give different ouputs that is relevant depending on what you want.
But to choose one, I would say that line_profiler is more useful,
as it is easy to see where the bottlenecks are - exactly on which line

### Question 2

> Which implementations have the most useful profiling output, and why?

The numpy color2gray implementation is the most useful to me. In the lineprofile
it specifies a huge overhead on line 17 in the slicing.

### Question 3

> Do any profiler+implementations produce seem to not work at all? If so, which?

Yes, the line_profiler + cython and numba does not seem to work. I read about it 
here: https://stackoverflow.com/questions/54545511/using-line-profiler-with-numba-jitted-functions
and this is because these to implementations go through optimization. Therefore, 
we can not line_profile these implementations, as there may be done some optimizations.
(the code have been changed, and therefore we can not profile the correct lines)

## profile output

<details>
<summary>cProfile output</summary>

```
Begin cProfile
Profiling python color2gray with cprofile:
         18 function calls in 2.388 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    2.387    0.796    2.388    0.796 /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/python_filters.py:6(python_color2gray)
        3    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 /opt/homebrew/anaconda3/lib/python3.11/site-packages/numpy/core/multiarray.py:84(empty_like)


Profiling numpy color2gray with cprofile:
         18 function calls in 0.004 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.004    0.001    0.004    0.001 /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/numpy_filters.py:6(numpy_color2gray)
        3    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 /opt/homebrew/anaconda3/lib/python3.11/site-packages/numpy/core/multiarray.py:84(empty_like)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numba color2gray with cprofile:
         9 function calls in 0.002 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.002    0.001    0.002    0.001 /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/numba_filters.py:7(numba_color2gray)
        3    0.000    0.000    0.000    0.000 /opt/homebrew/anaconda3/lib/python3.11/site-packages/numba/core/serialize.py:30(_numba_unpickle)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling cython color2gray with cprofile:
         15 function calls in 0.460 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.460    0.153    0.460    0.153 in3110_instapy/cython_filters.py:18(cython_color2gray)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 /opt/homebrew/anaconda3/lib/python3.11/site-packages/numpy/core/multiarray.py:84(empty_like)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling python color2sepia with cprofile:
         2764818 function calls in 6.752 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    6.532    2.177    6.752    2.251 /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/python_filters.py:32(python_color2sepia)
  2764800    0.220    0.000    0.220    0.000 {built-in method builtins.min}
        3    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 /opt/homebrew/anaconda3/lib/python3.11/site-packages/numpy/core/multiarray.py:84(empty_like)


Profiling numpy color2sepia with cprofile:
         21 function calls in 0.010 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.010    0.003    0.010    0.003 /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/numpy_filters.py:26(numpy_color2sepia)
        3    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.array}
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 /opt/homebrew/anaconda3/lib/python3.11/site-packages/numpy/core/multiarray.py:84(empty_like)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numba color2sepia with cprofile:
         9 function calls in 0.067 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.067    0.022    0.067    0.022 /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/numba_filters.py:31(numba_color2sepia)
        3    0.000    0.000    0.000    0.000 /opt/homebrew/anaconda3/lib/python3.11/site-packages/numba/core/serialize.py:30(_numba_unpickle)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling cython color2sepia with cprofile:
         15 function calls in 0.492 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.492    0.164    0.492    0.164 in3110_instapy/cython_filters.py:53(cython_color2sepia)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 /opt/homebrew/anaconda3/lib/python3.11/site-packages/numpy/core/multiarray.py:84(empty_like)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


End cProfile

```

</details>

<details>
<summary>line_profiler output</summary>

```
Begin line_profiler
Profiling python color2gray with line_profiler:
Timer unit: 1e-09 s

Total time: 2.96507 s
File: /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/python_filters.py
Function: python_color2gray at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           def python_color2gray(image: np.array) -> np.array:
     7                                               """Convert rgb pixel array to grayscale
     8                                           
     9                                               Args:
    10                                                   image (np.array)
    11                                               Returns:
    12                                                   np.array: gray_image
    13                                               """
    14         3      33000.0  11000.0      0.0      gray_image = np.empty_like(image)
    15                                               # iterate through the pixels, and apply the grayscale transform
    16                                               
    17                                               # The grayscale transform will have the weights 0.21, 0.72 and 0.07
    18         3       4000.0   1333.3      0.0      shape = gray_image.shape
    19      1443     169000.0    117.1      0.0      for i in range(shape[0]):
    20    923040   92234000.0     99.9      3.1          for j in range(shape[1]):
    21    921600  199628000.0    216.6      6.7              pixel = gray_image[i][j]
    22    921600  199110000.0    216.0      6.7              pixel_real = image[i][j]
    23    921600 1989667000.0   2158.9     67.1              gray_scale = pixel_real[0] * 0.21 + pixel_real[1] * 0.72 + pixel_real[2] * 0.07
    24    921600  174094000.0    188.9      5.9              pixel[0] = gray_scale
    25    921600  150401000.0    163.2      5.1              pixel[1] = gray_scale
    26    921600  159530000.0    173.1      5.4              pixel[2] = gray_scale
    27                                           
    28         3     198000.0  66000.0      0.0      gray_image = gray_image.astype("uint8")
    29         3       2000.0    666.7      0.0      return gray_image

Profiling numpy color2gray with line_profiler:
Timer unit: 1e-09 s

Total time: 0.004339 s
File: /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/numpy_filters.py
Function: numpy_color2gray at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           def numpy_color2gray(image: np.array) -> np.array:
     7                                               """Convert rgb pixel array to grayscale
     8                                           
     9                                               Args:
    10                                                   image (np.array)
    11                                               Returns:
    12                                                   np.array: gray_image
    13                                               """
    14                                           
    15         3      16000.0   5333.3      0.4      gray_image = np.empty_like(image)
    16                                               # Hint: use numpy slicing in order to have fast vectorized code
    17         3    3019000.0    1e+06     69.6      gray_scale = image[:,:,0] * 0.21 + image[:,:,1] * 0.72 + image[:,:,2] * 0.07
    18         3     349000.0 116333.3      8.0      gray_image[:,:,0] = gray_scale
    19         3     330000.0 110000.0      7.6      gray_image[:,:,1] = gray_scale
    20         3     380000.0 126666.7      8.8      gray_image[:,:,2] = gray_scale
    21                                               # Return image (make sure it's the right type!)
    22         3     244000.0  81333.3      5.6      gray_image = gray_image.astype("uint8")
    23         3       1000.0    333.3      0.0      return gray_image

Profiling python color2sepia with line_profiler:
Timer unit: 1e-09 s

Total time: 7.19666 s
File: /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/python_filters.py
Function: python_color2sepia at line 32

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    32                                           def python_color2sepia(image: np.array) -> np.array:
    33                                               """Convert rgb pixel array to sepia
    34                                           
    35                                               Args:
    36                                                   image (np.array)
    37                                               Returns:
    38                                                   np.array: sepia_image
    39                                               """
    40         3      23000.0   7666.7      0.0      sepia_image = np.empty_like(image)
    41                                               # Iterate through the pixels
    42                                               # applying the sepia matrix
    43                                           
    44         3       1000.0    333.3      0.0      sepia_matrix = [
    45         3       1000.0    333.3      0.0      [ 0.393, 0.769, 0.189], # R
    46         3       1000.0    333.3      0.0      [ 0.349, 0.686, 0.168], # G
    47         3          0.0      0.0      0.0      [ 0.272, 0.534, 0.131], # B
    48                                               ]
    49                                           
    50         3       1000.0    333.3      0.0      shape = sepia_image.shape
    51      1443     138000.0     95.6      0.0      for i in range(shape[0]):
    52    923040   94245000.0    102.1      1.3          for j in range(shape[1]):
    53    921600  203756000.0    221.1      2.8              pixel = sepia_image[i][j]
    54    921600  194462000.0    211.0      2.7              pixel_real = image[i][j]
    55    921600 2293310000.0   2488.4     31.9              pixel[0] = min(255,pixel_real[0] * sepia_matrix[0][0] + pixel_real[1] * sepia_matrix[0][1] + pixel_real[2] * sepia_matrix[0][2])
    56    921600 2220587000.0   2409.5     30.9              pixel[1] = min(255,pixel_real[0] * sepia_matrix[1][0] + pixel_real[1] * sepia_matrix[1][1] + pixel_real[2] * sepia_matrix[1][2])
    57    921600 2189805000.0   2376.1     30.4              pixel[2] = min(255,pixel_real[0] * sepia_matrix[2][0] + pixel_real[1] * sepia_matrix[2][1] + pixel_real[2] * sepia_matrix[2][2])
    58                                           
    59                                               # Return image
    60                                               # don't forget to make sure it's the right type!
    61         3     328000.0 109333.3      0.0      sepia_image = sepia_image.astype("uint8")
    62         3       1000.0    333.3      0.0      return sepia_image

Profiling numpy color2sepia with line_profiler:
Timer unit: 1e-09 s

Total time: 0.010495 s
File: /Users/erlingholte/Documents/UiO-master/IN4110/IN3110-erlinhol/assignment3/in3110_instapy/numpy_filters.py
Function: numpy_color2sepia at line 26

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    26                                           def numpy_color2sepia(image: np.array, k: float = 1) -> np.array:
    27                                               """Convert rgb pixel array to sepia
    28                                           
    29                                               Args:
    30                                                   image (np.array)
    31                                                   k (float): amount of sepia (optional)
    32                                           
    33                                               The amount of sepia is given as a fraction, k=0 yields no sepia while
    34                                               k=1 yields full sepia.
    35                                           
    36                                               (note: implementing 'k' is a bonus task,
    37                                                   you may ignore it)
    38                                           
    39                                               Returns:
    40                                                   np.array: sepia_image
    41                                               """
    42                                           
    43         3       2000.0    666.7      0.0      if not 0 <= k <= 1:
    44                                                   # validate k (optional)
    45                                                   raise ValueError(f"k must be between [0-1], got {k=}")
    46                                           
    47         3       6000.0   2000.0      0.1      sepia_image = np.empty_like(image)
    48                                           
    49         6       6000.0   1000.0      0.1      sepia_matrix = np.array([
    50         3          0.0      0.0      0.0          [ 0.393, 0.769, 0.189],
    51         3       1000.0    333.3      0.0          [ 0.349, 0.686, 0.168],
    52         3          0.0      0.0      0.0          [ 0.272, 0.534, 0.131],
    53                                               ])
    54                                           
    55                                               # define sepia matrix (optional: with stepless sepia changes)
    56                                           
    57                                               # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    58                                               # use Einstein sum to apply pixel transform matrix
    59                                               # Apply the matrix filter
    60                                           
    61         3    3358000.0    1e+06     32.0      sepia_image[:,:,0] = np.minimum(255,image[:,:,0] * sepia_matrix[0][0] + image[:,:,1] * sepia_matrix[0][1] + image[:,:,2] * sepia_matrix[0][2])
    62         3    3417000.0    1e+06     32.6      sepia_image[:,:,1] = np.minimum(255,image[:,:,0] * sepia_matrix[1][0] + image[:,:,1] * sepia_matrix[1][1] + image[:,:,2] * sepia_matrix[1][2])
    63         3    3593000.0    1e+06     34.2      sepia_image[:,:,2] = np.minimum(255,image[:,:,0] * sepia_matrix[2][0] + image[:,:,1] * sepia_matrix[2][1] + image[:,:,2] * sepia_matrix[2][2])
    64                                           
    65                                               # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    66                                           
    67                                               # Return image (make sure it's the right type!)
    68         3     112000.0  37333.3      1.1      sepia_image = sepia_image.astype("uint8")
    69         3          0.0      0.0      0.0      return sepia_image

End line_profiler
```

</details>

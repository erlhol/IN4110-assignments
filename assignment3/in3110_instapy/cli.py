"""Command-line (script) interface to instapy"""
from __future__ import annotations

import argparse
import sys

import in3110_instapy
import numpy as np
from PIL import Image

from . import io


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
) -> None:
    """Run the selected filter"""
    # load the image from a file
    image = Image.open(file)
    if scale != 1:
        # Resize image, if needed
        (width, height) = (round(image.width * scale), round(image.height * scale))
        image = image.resize((width, height))

    # Apply the filter
    filter_fun = in3110_instapy.get_filter(filter,implementation)
    filtered = filter_fun(image)
    if out_file:
        # save the file
        io.write_image(filtered,out_file)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")

    # Add required arguments
    parser.add_argument("-g","--gray",help="Select gray filter",action='store_true')
    parser.add_argument("-se","--sepia",help="Select sepia filter",action='store_true')
    parser.add_argument("-sc","--scale", type=int , help="Scale factor to resize image")
    parser.add_argument("-i","--implementation", choices=["python", "numba", "numpy","cython"],help="The implementation")

    # parse arguments and call run_filter
    args = parser.parse_args()
    if args.gray == True:
        run_filter(args.file,args.out,args.implementation,"color2gray",args.scale)
    if args.sepia == True:
        run_filter(args.file,args.out,args.implementation,"color2sepia",args.scale)
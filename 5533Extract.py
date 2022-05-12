# Solution kindly provided by yut23 (https://stackoverflow.com/questions/72202439/how-can-i-extract-those-bits-from-16bit-le-data/72207797#72207797)

import os
import numpy as np
from PIL import Image
from PIL.ImageChops import invert


# image dimensions
size = 512
# merge components into single rgba image
stack = False
# invert stack alpha for better visibility
invert_alpha = False
# input file type
input_type = ".buffer"
# output file type
output_type = ".png"
# filepath
path = os.getcwd()


def extract_mask(arr, mask):
    shift = int(np.log2(mask & -mask))
    return (arr & mask) >> shift
    

masks = {
    "R": 0b000_000_00000_11111,
    "G": 0b000_000_11111_00000,
    "B": 0b000_111_00000_00000,
    "A": 0b111_000_00000_00000
}

for i in os.listdir(path):
    if i.endswith(input_type):
        print(i + "...")
        data = np.fromfile(i, dtype="<u2").reshape(size, size)
        images = {
            k: Image.fromarray(extract_mask(data, mask).astype(np.uint8))
            for k, mask in masks.items()
        }
        if stack:
            if invert_alpha:
                images['A'] = invert(images['A'])
            RGBA = np.dstack((images['R'], images['G'], images['B'], images['A']))
            Image.fromarray(RGBA).save(i[:-len(input_type)] + "_STACK" + output_type)
        else:
            images['R'].save(i[:-len(input_type)] + "_OL" + output_type)
            images['G'].save(i[:-len(input_type)] + "_BG" + output_type)
            images['B'].save(i[:-len(input_type)] + "_UV" + output_type)
            images['A'].save(i[:-len(input_type)] + "_SL" + output_type)

import os
import numpy as np
from PIL import Image

# Solution kindly provided by Mark Setchell (https://stackoverflow.com/questions/71631519/how-to-specify-a-custom-channel-distribution-in-imagemagick/71645767)

h, w = 512, 512

path = os.getcwd()
# path = 'C:\\optional\\custom\\path'
input_type = '.buffer'
output_type = '.png'
bom = 0

for filename in os.listdir(path):

    if (filename.endswith(input_type)):
        print('Converting ' + filename + '...')

        # Read raw 16-bit file, skipping BOM with offset=2. Reshape.
        raw = np.fromfile(path + '\\' + filename, dtype=np.dtype('>u2'), offset=bom).reshape((h,w))

        # RGBA5533 packed into uint16
        R = (np.bitwise_and(raw, 0xf800) >> 8).astype(np.uint8)
        G = (np.bitwise_and(raw, 0x07c0) >> 3).astype(np.uint8)
        B = (np.bitwise_and(raw, 0x0038) << 2).astype(np.uint8)
        A = (np.bitwise_and(raw, 0x0007) << 5).astype(np.uint8)

        # Stack the individual channels into RGBA
        RGBA = np.dstack((R,G,B,A))

        # Display or save
        Image.fromarray(RGBA).save(path + "\\" + filename[:-len(input_type)] + ".png")


# Alternate way of doing this via ImageMagick:
# FOR /R %a IN (*.buffer) DO magick -size 512x512+0 -endian MSB -depth 16 gray:%~dpna.buffer -write MPR:orig +delete ^
#   ( MPR:orig -evaluate and 63488 ) ^
#   ( MPR:orig -evaluate and 1984  -evaluate leftshift 5  ) ^
#   ( MPR:orig -evaluate and 56    -evaluate leftshift 10 ) ^
#   ( MPR:orig -evaluate and 7     -evaluate leftshift 13 ) ^
#   -combine %~dpna.png
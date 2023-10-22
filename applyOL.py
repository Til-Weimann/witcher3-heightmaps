import os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

dir = os.getcwd()
dir = "C:\\Users\\Til\\Desktop\\workspace\\white orchard"

olMask = np.array(Image.open(os.path.join(dir, "olMask.png"))).astype('bool')
bg = np.array(Image.open(os.path.join(dir, "bg.png"))).astype(np.uint8)
ol = np.array(Image.open(os.path.join(dir, "ol.png"))).astype(np.uint8)

out = Image.fromarray(bg * np.invert(olMask) + ol * olMask)

out.save(os.path.join(dir, "merged.png"))
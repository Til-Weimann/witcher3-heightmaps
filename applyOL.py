import os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

olMask = np.array(Image.open(os.path.join(os.getcwd(), "olM.png"))).astype('bool')
bg = np.array(Image.open(os.path.join(os.getcwd(), "bg.png"))).astype(np.uint8)
ol = np.array(Image.open(os.path.join(os.getcwd(), "ol.png"))).astype(np.uint8)

out = Image.fromarray(bg * np.invert(olMask) + ol * olMask)

out.save(os.path.join(os.getcwd(), "merged.png"))
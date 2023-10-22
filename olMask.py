import os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

dir = os.getcwd()
dir = "C:\\Users\\Til\\Desktop\\workspace\\white orchard"

sm = np.array(Image.open(os.path.join(dir, "sm.png"))) # 0 to 255
bc = np.array(Image.open(os.path.join(dir, "bc.png"))) * 32 # 0 to 7

olM = sm <= bc # where blend control is higher than / equal to slope, choose overlay

out = Image.fromarray(olM.astype('bool'))

out.save(os.path.join(dir, "olMask.png"))

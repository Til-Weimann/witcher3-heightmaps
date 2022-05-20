import os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

sm = np.array(Image.open(os.path.join(os.getcwd, "sm.png")))
sc = np.array(Image.open(os.path.join(os.getcwd, "sc.png"))) * 8192 + 8192

olM = sm < sc

out = Image.fromarray(olM.astype('bool'))

out.save(os.path.join(os.getcwd, "olMask.png"))

import os
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None

dir = os.getcwd()
dir = "C:\\Users\\Til\\Desktop\\workspace\\white orchard"

colors = []

for filename in os.listdir(os.path.join(dir, "texarray")):
    if filename.endswith(".tga"):
        colors.append(np.average(Image.open(os.path.join(dir, "texarray", filename)), axis=(0,1)))



img = Image.open(os.path.join(dir, "merged.png")).convert("RGBA")

data = np.array(img)
newdata = data

red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

i = 1
for color in colors:
    mask = (red == i)
    data[:,:,:4][mask] = color
    i += 1
    
img = Image.fromarray(newdata)
img.save(os.path.join(dir, "preview.png"))
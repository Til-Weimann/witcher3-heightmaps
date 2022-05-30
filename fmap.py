from PIL import Image
import json
import numpy as np
import os

p = os.getcwd()
res = 16384

for f in os.listdir(p):
    if f.endswith(".txt"):
        map = np.zeros((res, res))
        with open(p + f) as data:
            for i in json.load(data):
                map[round(i["PosX"] + res/2), round(i["PosY"] + res/2)] = 1
            Image.fromarray(np.rot90(map).astype(bool)).save(p + f[:-4] + ".png")
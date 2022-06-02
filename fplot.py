from PIL import Image
import json
import numpy as np
import os

path = os.getcwd()
base = 8192
prec = 2

for f in os.listdir(path):
    if f.endswith(".txt"):
        map = np.zeros((base * prec, base * prec))
        with open(os.path.join(path, f)) as data:
            for i in json.load(data):
                map[round((i["PosX"] + base/2) * prec), round((i["PosY"] + base/2) * prec)] = 1
            Image.fromarray(np.rot90(map).astype(bool)).save(os.path.join(path, f[:-4] + ".png"))

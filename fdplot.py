from PIL import Image
import numpy as np
import os

path = os.getcwd()
res = 7475

posX = 0
posY = 0

for f in os.listdir(path):
    if f.endswith(".txt"):
        map = np.zeros((res, res))
        with open(os.path.join(path, f)) as data:
            for line in data.readlines():
                if "Yaw (Float) : " in line and -res/2 < posX < res/2 and -res/2 < posY < res/2:
                    map[round(posX + res/2), round(posY + res/2)] = 1
                if "PositionX (Float) : " in line:
                    posX = float(line.replace("PositionX (Float) : ","").replace("\n","").replace(" ","").replace(",","."))
                if "PositionY (Float) : " in line:
                    posY = float(line.replace("PositionY (Float) : ","").replace("\n","").replace(" ","").replace(",","."))
        
        Image.fromarray(np.rot90(map).astype(bool)).save(os.path.join(path, f[:-4] + ".png"))

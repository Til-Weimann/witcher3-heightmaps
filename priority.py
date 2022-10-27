import os
import numpy as np
from PIL import Image

path = os.getcwd()
res = 7475

full = np.zeros((res, res))
while True:
    fn = input("Enter file name: ") + ".png"
    if fn == "stop.png":
        break
    elif fn == "save.png":
        Image.fromarray(full.astype(bool)).save(os.path.join(path, "p", "_save.png"))
        continue
    elif fn == "load.png":
        full = Image.open(os.path.join(path, "p", "_save.png"))
        continue
    elif not os.path.exists(os.path.join(path, fn)):
        print(fn + " does not exist, try again.")
        continue
    old = Image.open(os.path.join(path, fn))
    new = np.subtract(old,np.minimum(full,old))
    print(str(round(100*(np.sum(new) / (np.sum(old))),2)) + "%...")

    full = np.maximum(full, new)
    Image.fromarray(new.astype(bool)).save(os.path.join(path, "p", fn))
    os.remove(os.path.join(path, fn))

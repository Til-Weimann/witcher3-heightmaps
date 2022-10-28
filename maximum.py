import os
import numpy as np
from PIL import Image

path = os.getcwd()
images = []
format = ""

while True:
    print(images)
    ip = input("> ")
    fn = ip[1:]
    if ip[0] == "+":
        if "." not in fn:
            fn += format
        if os.path.exists(os.path.join(path, fn)):
            images.append(fn)
        else:
            print("Error, " + fn + " does not exist.")
    elif ip[0] == "-":
        if "." not in fn:
            fn += format
        if fn in images:
            images.remove(fn)
    elif ip[0] == "#":
        if fn[0] == "c":
            images = []
            print("Cleared.")
        elif fn[0] == "e":
            exit()
        elif fn[0] == "s":
            fn = fn.split(" ")[-1]
            if "." not in fn:
                fn += format
            out = Image.open(os.path.join(path, images[0]))
            for i in images:
                out = np.maximum(out, Image.open(os.path.join(path, i)))
            Image.fromarray(out).save(os.path.join(path, fn))
            print("Saved.")
            out = None
        elif fn[0] == "d":
            for i in images:
                os.remove(os.path.join(path, i))
            print("Deleted " + len(images) + " images.")
            images = []
        elif fn[0] == "f":
            format = fn.split(" ")[-1]
            print("Format: " + format)
    else:
        print("Bad Operator!")
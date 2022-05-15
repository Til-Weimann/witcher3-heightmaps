import os
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

input_type = ".png"
output_type = ".png"

dir = os.listdir(os.getcwd())

# Gradient Solution by Mark Setchell (https://stackoverflow.com/a/49735873/14450544)

for i in dir:
    if i.endswith(input_type):
        print(i + "...")
        img = plt.imread(i)
        # Define kernel for x differences
        kx = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
        # Define kernel for y differences
        ky = np.array([[1,2,1] ,[0,0,0], [-1,-2,-1]])
        # Perform x convolution
        x=ndimage.convolve(img,kx)
        # Perform y convolution
        y=ndimage.convolve(img,ky)
        sobel=np.hypot(x,y)
        mpimg.imsave(i[:-len(input_type)] + "_slope" + output_type, sobel, cmap=plt.cm.gray)
# image to array
from PIL import Image
from numpy import asarray

# load image
image = Image.open('16x16.png')

# get array of pixels
pixelArray = asarray(image)

for p in pixelArray:
    print(p)
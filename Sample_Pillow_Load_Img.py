#Using Pillow Read a jpeg file to Image Object
from PIL import Image

img = Image.open("./image/black.jpg")

img.show()

#Convert Pillow To Numpy
import numpy

imgarr = numpy.array(img)

print(imgarr.shape)                     #(123, 160, 3)
from ppadb.client import Client
from PIL import Image
import numpy
import time


adb = Client(host='127.0.0.1',port=5037)
devices = adb.devices()


if len(devices) == 0:
    print("No device attached")
    quit()


device = devices[0]

# device.shell('input touchscreen swipe 500 500 500 1000 2000')


image = device.screencap()
with open('screen.png','wb') as f:
    f.write(image)

image = Image.open('screen.png')
image = numpy.array(image, dtype=numpy.uint8)

# print(image[1500])

pixels = [list(i[:3]) for i in image[1500]]

# print(pixels)

transitions = []






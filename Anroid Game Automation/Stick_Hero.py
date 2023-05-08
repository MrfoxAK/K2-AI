from ppadb.client import Client
from PIL import Image
import numpy
import time

def SH():
     
     adb = Client(host='127.0.0.1',port=5037)
     devices = adb.devices()


     if len(devices) == 0:
          print("No device attached")
          quit()


     device = devices[0]

     # device.shell('input touchscreen swipe 500 500 500 1000 2000')

     while True:
          image = device.screencap()
          with open('screen.png','wb') as f:
               f.write(image)

          image = Image.open('screen.png')
          image = numpy.array(image, dtype=numpy.uint8)

          # print(image[1500])

          pixels = [list(i[:3]) for i in image[1500]]

          # print(pixels)

          transitions = []
          ignore = True
          black = True

          for i, pixel in enumerate(pixels):
               r,g,b = [int(i) for i in pixel]
               # print(r,g,b)
               if ignore and (r+g+b) != 0:
                    continue

               ignore = False

               if black and (r+g+b) != 0:
                    black = not black
                    transitions.append(i)
                    continue
               if not black and (r+g+b) == 0:
                    black = not black
                    transitions.append(i)
                    continue

          print(transitions)

          start , targe1, target2 = transitions
          gap = targe1 - start
          target = target2 - targe1
          distance = (gap + target/2) * .98

          print(distance)


          device.shell(f'input touchscreen swipe 500 500 500 500 {int(distance)}')

          time.sleep(2.3)

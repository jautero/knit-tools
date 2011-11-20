#!/usr/bin/python

from PIL import Image, ImageDraw

gridsize=10

def convert_image(image):
  new_image=Image.new(image.mode,tuple(gridsize*i for i in image.size))
  draw=ImageDraw.Draw(new_image)
  pix=image.load()
  for x in range(0,image.size[0]):
    for y in range(0,image.size[1]):
      box=(x*gridsize,y*gridsize,x*gridsize+(gridsize-1),y*gridsize+(gridsize-1))
      if pix[x,y]==255:
        draw.rectangle(box,outline=0,fill=255)
      else:
        draw.rectangle(box,outline=255,fill=0)
  return new_image

import sys
image=Image.open(sys.argv[1])
conversion=convert_image(image)
conversion.save("converted"+sys.argv[1])

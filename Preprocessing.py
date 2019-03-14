from PIL import Image
from PIL import ImageFilter
import pathlib
import time
from datetime import datetime

########################################
#def current_time():
    #return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#print current_time()
#########################################

im = Image.open(r"C:\Users\susu1\Documents\Image processing\hurricane.png")
 # opening image

if im is None:
    print ('no pic')

print (im)

#im = im.crop((0,0,1024,1024))
# crop image, coordinate system L= bottom left corner, uL = upper left, R = upper Right...

im = im.resize((910, 512))
# size is w x h, resizing filter - if none, PIL.Image.NEAREST, box- not needed

im = im.filter(ImageFilter.EDGE_ENHANCE)
#runs image thru filter, edge enhance/ edge enhance more/ find edges

##im = ImageOps.grayscale("hurricane.png")
# greyscale the image

print (im)

im.save("cropped_hurricane.png")

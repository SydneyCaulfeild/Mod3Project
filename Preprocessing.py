from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import pathlib
import time
from datetime import datetime
import requests
import json
import os
import cv2
import glob

##################################################################

send_url = "http://api.ipstack.com/check?access_key=ae5620e07d25c95d8baca860f7fdc0d6"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']
print(latitude, longitude, city)

## test lat
if latitude is None:
    print('no lat')
##test long
if longitude is None:
    print ('no long')
##test city
if city is None:
    print ('no city')
##########################################

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print (current_time())

## test
if current_time() is None:
    print('no datetime')
##########################################
i = 0
im_dir = r"C:\Users\susu1\Documents\Image processing\images"

data_path = os.path.join(im_dir,'*g')
files = glob.glob(data_path)
data = []
for f1 in files:
    im = Image.open(f1)
 # opening image
    if im is None:
        print ('no pic')
    print (im)
    i = i + 1
    im = im.crop((0,0,100,100))
# crop image, coordinate system L= bottom left corner, uL = upper left, R = upper Right...
    #im = im.resize((910, 512))
# size is w x h, resizing filter - 455 x 256?
    im = im.filter(ImageFilter.EDGE_ENHANCE)
#runs image thru filter, edge enhance/ edge enhance more/ find edges
    im = ImageOps.autocontrast(im, cutoff=0, ignore=None)
#normalize !!! CHANGE PERCENTAGE IF YOU KNOW WHATS GOING ON !!
    print (im)
    print (i)
    im.save("cropped dog  " + str(i) + ".jpg")
    continue

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:10:09 2019

@author: bzbri
"""

from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
from datetime import datetime
from keras.models import load_model

import requests
import json
import os
import cv2
import glob

send_url = "http://api.ipstack.com/check?access_key=ae5620e07d25c95d8baca860f7fdc0d6"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

i = 0
j = 0

im_dir = r"images"
data_path = os.path.join(im_dir,'*g')
files = glob.glob(data_path)

model = load_model("model512PRE.h5")

for f in files:
    i += 1
    im = Image.open(f)
    im = im.filter(ImageFilter.EDGE_ENHANCE)
    im = ImageOps.autocontrast(im, cutoff=0, ignore=None)
    
    im.save("temp"+str(i)+".png")

for n in range(i):
    j += 1
    img = cv2.imread("temp"+str(j)+".png",1)
    img = cv2.resize(img,(64,64))
    output = model.predict(img.reshape(-1,64,64,3))

    if output[0][0]==1:
        print("Hurricane:")
        print("Latitude:",latitude)
        print("Longitude:",longitude)
        print("Time:",time)
        
        cv2.imwrite("Hurricanes/Hurricane"+str(j)+".png",img)
    
    elif output[0][1]==1:
        print("Not a Hurricane")
        
    os.remove("temp"+str(j)+".png")
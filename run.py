# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:13:45 2019

@author: bzbri
"""
from PIL import Image
from PIL import ImageFilter
from keras.models import load_model

import os
import cv2
import glob

i = 0
j = 0

yes = 0
no = 0

im_dir = r"dataset/train/Nothing"
data_path = os.path.join(im_dir,'*g')
files = glob.glob(data_path)

model = load_model("model512PRE.h5")

for f in files:
    i += 1
    im = Image.open(f)
    im = im.filter(ImageFilter.EDGE_ENHANCE)
    #im = ImageOps.autocontrast(im, cutoff=0, ignore=None)
    
    im.save("temp"+str(i)+".png")

for n in range(i):
    j += 1
    img = cv2.imread("temp"+str(j)+".png",1)
    img = cv2.resize(img,(64,64))
    output = model.predict(img.reshape(-1,64,64,3))

    if output[0][0]==1:
        yes+=1
    
    elif output[0][1]==1:
        no+=1
        
    os.remove("temp"+str(j)+".png")

print("Hurricanes:",yes)
print("Total Images:",yes+no)
print("Percentage of Hurricanes:",100*yes/(yes+no),"%")

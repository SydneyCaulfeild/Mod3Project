# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 20:13:45 2019

@author: bzbri
"""
import cv2
from keras.models import load_model

model = load_model("model.h5")
image = cv2.imread("cat_or_dog_1.jpg",1)
print(image.shape)
image = cv2.resize(image,(64,64))
output = model.predict(image.reshape(-1,64,64,3))

print(output)

#model.summary()
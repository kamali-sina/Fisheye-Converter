import cv2
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import numpy as np
from math import sqrt
import math
from math import atan2,cos,sin,atan

img = cv2.imread('ut.png',1)
output = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

def convert (i,j,img):
    x = j - (img.shape[1]/2)
    y = ((img.shape[0] - i) - (img.shape[0]/2))
    return x,y

def normalize (x,y,img):
    xn = x/(img.shape[1]/2)
    yn = y/(img.shape[0]/2)
    return xn,yn

def denormalize(xn,yn,img):
    x = xn * (img.shape[1]/2)
    y = yn * (img.shape[0]/2)
    return x,y

def de_convert(x,y,img):
    j = x + (img.shape[1]/2)
    i = img.shape[0] - (y + (img.shape[0]/2))
    return int(i),int(j)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x,y = convert(i,j,img)
        xn,yn = normalize (x,y,img)
        r = sqrt((xn**2) + (yn**2))
        theta = atan2 (yn,xn)
        if (r <= 1):
            r_prime = (r + (1 - sqrt(1 - (r**2))))/2
            xn_new = r_prime*cos(theta)
            yn_new = r_prime*sin(theta)
            x_new,y_new = denormalize(xn_new,yn_new,img)
            new_i,new_j = de_convert(x_new,y_new,img)
            output[new_i][new_j][0] = img[i][j][0]
            output[new_i][new_j][1] = img[i][j][1]
            output[new_i][new_j][2] = img[i][j][2]
        
        
print('ready')
cv2.imshow('image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
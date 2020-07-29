import cv2
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import numpy as np
from math import sqrt
import math
from math import atan2,cos,sin,atan

class fisheye():
    def __init__(self,filepath,con):
        self.img = cv2.imread(filepath,cv2.IMREAD_UNCHANGED)
        self.output = np.zeros((self.img.shape[0], self.img.shape[1], 3), np.uint8)
        self.filepath = filepath
        self.to_from_fisheye(con)

    def _convert (self,i,j,img):
        x = j - (self.img.shape[1]/2)
        y = ((self.img.shape[0] - i) - (self.img.shape[0]/2))
        return x,y

    def _normalize (self,x,y,img):
        xn = x/(self.img.shape[1]/2)
        yn = y/(self.img.shape[0]/2)
        return xn,yn

    def _denormalize(self,xn,yn,img):
        x = xn * (self.img.shape[1]/2)
        y = yn * (self.img.shape[0]/2)
        return x,y

    def _de_convert(self,x,y,img):
        j = int(x + (self.img.shape[1]/2))
        i = int(self.img.shape[0] - (y + (self.img.shape[0]/2)))
        return i,j

    def to_from_fisheye(self,conv):
        cv2.destroyAllWindows()
        cv2.startWindowThread()
        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                x,y = self._convert(i,j,self.img)
                xn,yn = self._normalize (x,y,self.img)
                r = sqrt((xn**2) + (yn**2))
                theta = atan2 (yn,xn)
                if (r <= 1):
                    r_prime = (r + 1 - sqrt(1 - r**2)) / 2
                    xn_new = r_prime*cos(theta)
                    yn_new = r_prime*sin(theta)
                    x_new,y_new = self._denormalize(xn_new,yn_new,self.img)
                    new_i,new_j = self._de_convert(x_new,y_new,self.img)
                    if (conv == 0):
                        self.output[new_i][new_j][0] = self.img[i][j][0]
                        self.output[new_i][new_j][1] = self.img[i][j][1]
                        self.output[new_i][new_j][2] = self.img[i][j][2]
                    else:
                        self.output[i][j][0] = self.img[new_i][new_j][0]
                        self.output[i][j][1] = self.img[new_i][new_j][1]
                        self.output[i][j][2] = self.img[new_i][new_j][2]
        print(self.filepath + ' ready!!')
        cv2.imshow('Output', self.output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

print("from fisheye : 0   ------- to fisheye : 1")
x = int(input().strip())
filepath = input("File Path: ")
fishy = fisheye(filepath,x)
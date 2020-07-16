import cv2
import time
import math
import numpy as np
import pygame
import matplotlib.pyplot as plt
img=cv2.imread('C:\\Users\\Hemant\\Desktop\\data.png', 1)
img=cv2.line(img,(0,0),(100,100),(0,100,0),5)
cap=cv2.VideoCapture(0)
cv2.imshow('image',img)
cv2.waitKey(5000)
while(True):
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',grey)
cv2.release()
cv2.destroyAllWindows()

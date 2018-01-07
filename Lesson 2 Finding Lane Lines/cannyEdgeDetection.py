#Canny Edge Detection 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 
import cv2

#read in the image and convert to grayscale
imgae = mpimg.imread('exit-ramp.jpg')
gray =cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#define a kernel size for Gaussian smoothing / blurring
#note: this step is optional as cv2.Canny() applies a 5x5 Gaussian internally
kernel_size =3
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

#define parameters for Canny and run it
##note: if you try running this code you might wany to change these
low_threshold = 1
high_threshold =10
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

#display the image
plt.imshow(edges, cmap='Greys_r')

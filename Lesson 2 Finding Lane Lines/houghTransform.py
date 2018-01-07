#Hough Transform to Fine Lane Line
#Do relevant imports
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import numpy as np 
import cv2

#Read in and grayscale the imahe
image = mpimg.imread('exit-ramp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#define a kernel size and apply gaussian smoothing
kernel_size =5
blur_gray = cv2.GaussianBLur(gray,(kernel_size, kernel_size),0)

#define our parameters for canny and apply
low_threshold = 50
high_threshold = 150
masked_edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

#define the hough transform parameters
#make a blank the same size as our image to draw on
rho =1
theta =1
threshold =1
min_line_length =10
max_line_length =1
line_image = np.copy(image)*0 #creating a blank to draw lines on

#run hough on edge detected image
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
						min_line_length, max_line_length)

#iterate over the output "lines" as draw lines on the blank
for line in lines
	for x1, y1, x2, y2 in line:
		cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0),10)

#create a "color" binary image to combine with line image
color_edges = np.dstack(masked_edges, masked_edges, masked_edges)

#draw the lines on the edge image
combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
plt.imshow(combo)
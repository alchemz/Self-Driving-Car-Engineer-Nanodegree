import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#read in the image and print some stats
image = mping.imread('test.jpg')
print("This image is:", type(image),
		'with dimensions:', image.shape)

#pull out the x and y sizes and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
region_select = np.copy(image)

#define a triangle region of interest
#keep in mind the origin(x=0, y=0) is in the upper left in image processing
#note: if you rund this code, you'll find tese are not sensible values
#but you'll get a chance to play with them soon in a quiz
left_bottom = [0, 539]
right_bottom =[900, 300]
apex = [400, 0]

#fit lines(y =Ax+ B) to identify the 3 sided region of interest
#np.poly.fit() returns the coefficients[A, B] of the fit
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]),1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]),1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]),(left_bottom[1], right_bottom[1]),1)

#find the region inside the lines
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_threshold = (YY > (XX * fit_left[0]+ fit_left[1])) & \
					(YY > (XX * fit_right[0] + fit_right[1])) & \
					(YY < (XX *fit_bottom[0] + fit_bottom[1]))

#color pixels red which are inside the region of interest
region_threshold =(YY > (XX*fit_left[0] + fit_left[1])) & \
					(YY > (XX*fit_right[0] + fit_right[1])) & \
					(YY > (XX*fit_bottom[0] + fit_bottom[1])) 

#color pixels red which are inside the region of interest
region_select[region_threshold] = [255, 0,0]

#displat the image
plt.imshow(region_select)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#read in the image and print out some stats
image = mpimg.imread('test.jpg')
print('This image is :', type(image), 'with dimensions:', image.shape)

#grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]
#note: always make a copy rather than simply using "="
color_select = np.copy(image)

#define color threshold
#define our color selection criteria
#note: if you run this code, you will find tese are not sensible values
#but you'll get a chance to play with them soon in a quiz
red_threshold = 200
green_threshold =200
blue_threshold =200
rgb_threshold =[red_threshold, green_threshold, blue_threshold]

#identify pixels below the threshold
threshold =(image[:,:,0] < rgb_threshold[0] \
			| (image[:,:,1] < rgb_threshold[1])\
			| (image[:,:,1] < rgb_threshold[2])\
color_select[threshold] = [0,0,0]

#display the image
plt.imshow(color_select)
plt.show()

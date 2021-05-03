#!/usr/bin/env python3

from PIL import Image
from numpy import *
from scipy.ndimage import measurements,morphology
from pylab import *

import drawing_tools

# load image and threshold to make sure it is binary
im = array(Image.open('./data/houses.png').convert('L'))
#im = array(Image.open('../getDataPoints/Figures/h_dataMC_eta_PixelSharedHits.png').convert('L'))
im2 = 1*(im<128)

labels, nbr_objects = measurements.label(im2)
print ("Number of objects:", nbr_objects)

# morphology - openingto separate objects better
im_open = morphology.binary_opening(im2,ones((9,5)),iterations=2)

labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)


# Drawing results
drawing_tools.show_images([im,im2,labels,im_open,labels_open],5,1)
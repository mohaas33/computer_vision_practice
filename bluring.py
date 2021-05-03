#!/usr/bin/env python3

from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

im = array(Image.open('./data/empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)

im_3l = array(Image.open('./data/empire.jpg'))
im3 = zeros(im_3l.shape)
for i in range(3):
  im3[:,:,i] = filters.gaussian_filter(im_3l[:,:,i],10)
im3 = uint8(im3)


#create a new figure
figure()
subplot(1,3,1)
#don't use colors
gray()
axis('equal')
axis('off')

imshow(im)

subplot(1,3,2)
imshow(im2)
axis('equal')
axis('off')

subplot(1,3,3)
imshow(im3)
axis('equal')
axis('off')

show()
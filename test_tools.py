#!/usr/bin/env python3
from PIL import Image
from pylab import *
from numpy import *

import imtools


# read image to array
im = array(Image.open('./data/empire.jpg').convert('L'))

#create a new figure
figure()
subplot(1,2,1)
#don't use colors
gray()
#show contours
contour(im,origin='image')
axis('equal')
axis('off')

subplot(1,2,2)
hist(im.flatten(),128)

def change_image(img_name):
    im = array(Image.open(img_name).convert('L'))
    im2,cdf = imtools.histeq(im)

    # plot
    figure()
    gray()

    subplot(2,3,1)
    hist(im.flatten(),128)
    #axis('equal')
    #axis('off')

    subplot(2,3,2)
    plot(im.flatten()[::50],im2.flatten()[::50], color='green', marker='o', linestyle='dashed',linewidth=.0, markersize=1)
    plt.xlabel('Before')
    plt.ylabel('After')

    subplot(2,3,3)
    hist(im2.flatten(),128)

    subplot(2,3,4)
    imshow(im)
    axis('equal')
    axis('off')

    subplot(2,3,5)
    #imshow(im2)
    axis('equal')
    axis('off')

    subplot(2,3,6)
    imshow(im2)
    axis('equal')
    axis('off')

    

change_image('./data/AquaTermi_lowcontrast.jpg')
change_image('./data/empire.jpg')
show()
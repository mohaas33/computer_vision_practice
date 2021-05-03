from PIL import Image
from pylab import *
from numpy import *

def show_images(images,xN,yN):
    figure()
    gray()
    im_len = len(images)
    for i,im in enumerate(images,start=1):
        subplot(yN,xN,i)
        #don't use colors
        axis('equal')
        axis('off')
        imshow(im)
    show()
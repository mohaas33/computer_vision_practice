import os
from PIL import Image
from pylab import *
from numpy import *

def get_imlist(path):
    """Returns list of all .jpg fileth in the path """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im,sz):
    """Changes array size with PIL"""
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

def histeq(im,nbr_bins=256):
    """ Histogram equalization of a grayscale image. """
    #get histo of image
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255*cdf/cdf[-1] # normalization
    # use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape), cdf

def compute_average(imlist):
    """Calculate average of the images list"""
    #open 1-st image and make it array of floats
    averageim = array(Image.open(imlist[0]),'float')
    
    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print (imname + '...skipped')
    averageim /= len(imlist)
    #return averages as an array of uint8
    return array(averageim, 'uint8') 
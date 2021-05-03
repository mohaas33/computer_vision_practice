#!/usr/bin/env python3

from PIL import Image
from numpy import *
from scipy.ndimage import filters
from pylab import *

import drawing_tools


im = array(Image.open('./data/empire.jpg').convert('L'))
#im = array(Image.open('../getDataPoints/Figures/h_dataMC_eta_PixelSharedHits.png').convert('L'))

# Sobel derivative filters
imx = zeros(im.shape)
filters.sobel(im,1,imx)

imy = zeros(im.shape)
filters.sobel(im,0,imy)

magnitude = sqrt(imx**2+imy**2)

# Gaussian smearing
sigma = 5 # standard deviation

imx_g = zeros(im.shape)
filters.gaussian_filter(im,(sigma,sigma),(0,1),imx_g)

imy_g = zeros(im.shape)
filters.gaussian_filter(im,(sigma,sigma),(1,0), imy_g)

magnitude_g = sqrt(imx_g**2+imy_g**2)
# Drawing results
drawing_tools.show_images([im,imx,imy,magnitude],2,2)
drawing_tools.show_images([im,imx_g,imy_g,magnitude_g],2,2)


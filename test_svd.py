#!/usr/bin/env python3

from PIL import Image
from numpy import *
from pylab import *
from os import listdir
from os.path import isfile, join
import pickle
import pca

mypath = './data/a_thumbs/'
imlist = [mypath+f for f in listdir(mypath) if isfile(join(mypath, f))]
print(imlist[0])
im = array(Image.open(imlist[0])) # open one image to get size
m,n = im.shape[0:2] #get the size of the images
imnbr = len(imlist) # get the number of images

# create matrix to store all flattened images
immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')

# perform PCA
V,S,immean = pca.pca(immatrix)

# save mean and principal components
with open('./files/font_pca_modes.pkl', 'wb') as f:
  pickle.dump(immean,f)
  pickle.dump(V,f)


# load mean and principal components
with open('./files/font_pca_modes.pkl', 'rb') as f:
  immean = pickle.load(f)
  V = pickle.load(f)

# Note that the order of the objects should be the same!


# show some images (mean and 7 first modes)
figure()
gray()
subplot(2,5,1)
imshow(immean.reshape(m,n))
for i in range(9):
  subplot(2,5,i+2)
  imshow(V[i].reshape(m,n))

show()
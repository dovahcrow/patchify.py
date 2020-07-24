##
%load_ext autoreload
%autoreload 2
##
sys.path.append(".")
##
from skimage.io import imread, imshow
from patchify import patchify, unpatchify
##
img = imread("wp2559551.jpg")

##
patches = patchify(img, (900, 256, 3), step=1)

##
imshow(unpatchify(patches, img.shape))
##
patches = patchify(img[:,:,1], (645, 256), step=1)

##
imshow(img[:,:,1])
##
imshow(unpatchify(patches, img[:,:,1].shape))

##

# patchify

patchfy can split images into small overlappable patches by given patch cell size, and merge patches into original image.

This library provides two functions: `patchify`, `unpatchify`.

## Installation
```
pip install patchify
```

## Usage

### Split image to patches

`patchify(image_to_patch, patch_shape, step=1)`

2D image:
```python
#This will split the image into small images of shape [3,3]
patches = patchify(image, (3, 3), step=1)
```

3D image:
```python
#This will split the image into small images of shape [3,3,3]
patches = patchify(image, (3, 3, 3), step=1)
```

### Merge patches into original image

`unpatchify(patches_to_merge, merged_image_size)`

```python
reconstructed_image = unpatchify(patches, image.shape)
```
This will reconstruct the original image that was patchified in previous code.

### Help! `unpatchify` yields distorted images
In order for `unpatchify` to work, patchies should be created with equal step size. 
e.g. if the original image has width 3 and the patch has width 2, you cannot really create equal step size patches with step size 2. 
(first patch [elem0, elem1] and second patch [elem2, elem3], in which elem3 is out of bound).

The required condition to successfully recover the image using unpatchify
is to have `(width - patch_width) mod step_size = 0` when calling `patchify`.

### Full running examples

#### 2D image patchify and merge

```python
import numpy as np
from patchify import patchify, unpatchify

image = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

patches = patchify(image, (2,2), step=1) # split image into 2*3 small 2*2 patches.

assert patches.shape == (2, 3, 2, 2)
reconstructed_image = unpatchify(patches, image.shape)

assert (reconstructed_image == image).all()
```

#### 3D image patchify and merge

```python
import numpy as np
from patchify import patchify, unpatchify

image = np.random.rand(512,512,3)

patches = patchify(image, (2,2,3), step=1) # patch shape [2,2,3]
print(patches.shape) # (511, 511, 1, 2, 2, 3). Total patches created: 511x511x1

assert patches.shape == (511, 511, 1, 2, 2, 3)
reconstructed_image = unpatchify(patches, image.shape)
print(reconstructed_image.shape) # (512, 512, 3)

assert (reconstructed_image == image).all()
```

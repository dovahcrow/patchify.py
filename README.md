# patchify.py


patchfy.py can split images into small overlappable patches by given patch cell size, and merge patches into original image.

This library provides two functions: `patchify`, `unpatchify`.

Usage:
#### `patchify(image_to_patch, windows_shape, step=1)`

Example:
```python
patches = patchify(image, (3, 3), step=1)
```
This will split the image into 3x3 small images, which can be connected to get the original image.


#### `unpatchify(patches_to_merge, merged_image_size)`

Example:
```python
reconstructed_image = unpatchify(patches, image.shape)
```
This will reconstruct the original image that was patchified in previous code.

A full example:
```python
import numpy as np
from patchify import patchify, unpatchify

image = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

patches = patchify(image, (2,2), step=1) # split image into 2*3 small 2*2 patches.

assert patches.shape == (2, 3, 2, 2)
reconstructed_image = unpatchify(patches, image.shape)

assert (reconstructed_image == image).all()
```

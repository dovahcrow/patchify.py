# patchify

patchfy can split images into small overlappable patches by given patch cell size, and merge patches into original image.

This library provides two functions: `patchify`, `unpatchify`.

Usage:

#### `patchify(image_to_patch, patch_shape, step=1)`

Example: <br>
2D images:
```python
#This will split the image into small images of shape [3,3]
patches = patchify(image, (3, 3), step=1)
```
3D images:
```python
#This will split the image into small images of shape [3,3,3]
patches = patchify(image, (3, 3, 3), step=1)
```

Patches can merged using:
#### `unpatchify(patches_to_merge, merged_image_size)`

Example:
```python
reconstructed_image = unpatchify(patches, image.shape)
```
This will reconstruct the original image that was patchified in previous code.

A full example:

##### 2D images
```python
import numpy as np
from patchify import patchify, unpatchify

image = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

patches = patchify(image, (2,2), step=1) # split image into 2*3 small 2*2 patches.

assert patches.shape == (2, 3, 2, 2)
reconstructed_image = unpatchify(patches, image.shape)

assert (reconstructed_image == image).all()
```

##### 3D images
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

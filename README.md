# patchify.py

A library that helps you split image into small, overlappable patches, and merge patches into original image.

This library provides two functions: `patchify`, `unpatchify`.

Usage:

```python
import numpy as np
from patchify import patchify, unpatchify

image = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

patches = patchify(image, (2,2), step=1) # split image into 2*3 small 2*2 patches.

assert patches.shape == (2, 3, 2, 2)

reconstructed_image = unpatchify(patches, image.shape)

assert (reconstructed_image == image).all()
```


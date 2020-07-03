import numpy as np
from .. import patchify, unpatchify


def test_2d() -> None:

    image = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    patches = patchify(image, (2, 2), step=1)  # split image into 2*3 small 2*2 patches.

    assert patches.shape == (2, 3, 2, 2)
    reconstructed_image = unpatchify(patches, image.shape)

    assert (reconstructed_image == image).all()


def test_3d() -> None:

    image = np.random.rand(512, 512, 3)

    patches = patchify(image, (2, 2, 3), step=1)  # patch shape [2,2,3]
    print(patches.shape)  # (511, 511, 1, 2, 2, 3). Total patches created: 511x511x1

    assert patches.shape == (511, 511, 1, 2, 2, 3)
    reconstructed_image = unpatchify(patches, image.shape)
    print(reconstructed_image.shape)  # (512, 512, 3)

    assert (reconstructed_image == image).all()

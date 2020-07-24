import numpy as np
import pytest

from .. import patchify, unpatchify


def test_2d() -> None:

    # 3 x 4 image
    image = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    patches = patchify(image, (2, 2), step=1)  # split image into 2*3 small 2*2 patches.

    assert patches.shape == (2, 3, 2, 2)
    reconstructed_image = unpatchify(patches, image.shape)

    assert (reconstructed_image == image).all()

    patches = patchify(image, (3, 2), step=1)  # split image into 1*3 small 3*2 patches.

    assert patches.shape == (1, 3, 3, 2)
    reconstructed_image = unpatchify(patches, image.shape)

    assert (reconstructed_image == image).all()

    patches = patchify(image, (2, 4), step=1)  # split image into 2*1 small 2*4 patches.

    assert patches.shape == (2, 1, 2, 4)
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


@pytest.mark.xfail
def test_fail() -> None:

    image = np.random.rand(900, 1600, 3)

    patches = patchify(image, (256, 256, 3), step=128)
    assert patches.shape == (6, 11, 1, 256, 256, 3)
    reconstructed_image = unpatchify(patches, image.shape)
    assert (reconstructed_image == image).all()

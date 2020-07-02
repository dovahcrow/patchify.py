import numpy as np
from skimage.util import view_as_windows
from itertools import product
from typing import Tuple

def patchify(patches: np.ndarray, patch_size: Tuple[int, int], step: int = 1):
    return view_as_windows(patches, patch_size, step)

def unpatchify(patches: np.ndarray, imsize):
    if len(patches.shape) == 4:
        return unpatchify2D(patches, imsize)
    elif len(patches.shape) == 6:
        return unpatchify3D(patches, imsize)
    else:
        print("Error in Patches dimension: ", patches.shape)
        return -1

def unpatchify2D(patches: np.ndarray, imsize: Tuple[int, int]):

    assert len(patches.shape) == 4

    i_h, i_w = imsize
    image = np.zeros(imsize, dtype=patches.dtype)
    divisor = np.zeros(imsize, dtype=patches.dtype)

    n_h, n_w, p_h, p_w = patches.shape

    # Calculat the overlap size in each axis
    o_w = (n_w * p_w - i_w) / (n_w - 1)
    o_h = (n_h * p_h - i_h) / (n_h - 1)

    # The overlap should be integer, otherwise the patches are unable to reconstruct into a image with given shape
    assert int(o_w) == o_w
    assert int(o_h) == o_h

    o_w = int(o_w)
    o_h = int(o_h)

    s_w = p_w - o_w
    s_h = p_h - o_h

    for i, j in product(range(n_h), range(n_w)):
        patch = patches[i,j]
        image[(i * s_h):(i * s_h) + p_h, (j * s_w):(j * s_w) + p_w] += patch
        divisor[(i * s_h):(i * s_h) + p_h, (j * s_w):(j * s_w) + p_w] += 1

    return image / divisor

def unpatchify3D(patches: np.ndarray, imsize: Tuple[int, int, int]):

    assert len(patches.shape) == 6

    i_h, i_w, i_c = imsize
    image = np.zeros(imsize, dtype=patches.dtype)
    divisor = np.zeros(imsize, dtype=patches.dtype)

    n_h, n_w, n_c, p_h, p_w, p_c = patches.shape

    # Calculat the overlap size in each axis
    o_w = (n_w * p_w - i_w) / (n_w - 1)
    o_h = (n_h * p_h - i_h) / (n_h - 1)
    o_c = 1 if n_c==1 else (n_c * p_c - i_c) / (n_c - 1)

    # The overlap should be integer, otherwise the patches are unable to reconstruct into a image with given shape
    assert int(o_w) == o_w
    assert int(o_h) == o_h
    assert int(o_c) == o_c

    o_w = int(o_w)
    o_h = int(o_h)
    o_c = int(o_c)

    s_w = p_w - o_w
    s_h = p_h - o_h
    s_c = p_c - o_c

    for i, j, k in product(range(n_h), range(n_w), range(n_c)):
        patch = patches[i,j,k]
        image[(i * s_h):(i * s_h) + p_h, (j * s_w):(j * s_w) + p_w, (k * s_c):(k * s_c) + p_c] += patch
        divisor[(i * s_h):(i * s_h) + p_h, (j * s_w):(j * s_w) + p_w, (k * s_c):(k * s_c) + p_c] += 1

    return image / divisor
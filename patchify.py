import numpy as np
from skimage.util import view_as_windows
from itertools import product
from typing import Tuple

def patchify(patches: np.ndarray, patch_size: Tuple[int, int], step: int = 1):
    return view_as_windows(patches, patch_size, step)

def unpatchify(patches: np.ndarray, imsize: Tuple[int, int]):
    
    assert len(patches.shape) == 4
    
    i_h, i_w = imsize
    image = np.zeros(imsize, dtype=patches.dtype)
    
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
    
    def n_overlap(x: int, y: int):
        """
        Get corresponding patch indices for a specific pixel
        """
        xmin = int(max(np.ceil((x - p_w) / s_w) + ((x - p_w) % s_w == 0), 0))
        xmax = int(min(np.floor(x / s_w), n_w - 1))
        ymin = int(max(np.ceil((y - p_h) / s_h) + ((y - p_h) % s_h == 0), 0))
        ymax = int(min(np.floor(y / s_h), n_h - 1))
        return (xmax - xmin + 1) * (ymax - ymin + 1)
        
    
    for i, j in product(range(n_h), range(n_w)):
        patch = patches[i,j]
        image[(i * s_h):(i * s_h) + p_h, (j * s_w):(j * s_w) + p_w] += patch

    for i, j in product(range(i_h), range(i_w)):
        image[i, j] /= n_overlap(j,i)

    return image

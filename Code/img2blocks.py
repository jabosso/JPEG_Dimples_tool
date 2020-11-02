import numpy as np


def img2blocks(img, t_size):
    h, w = img.shape
    range_h = h // t_size
    range_w = w // t_size
    blk_img = []
    for i in range(range_h):
        for j in range(range_w):
            new_block = img[i * t_size:(i + 1) * t_size, j * t_size:(j + 1) * t_size]
            blk_img.append(new_block)
    blk_img = np.asarray(blk_img)
    blk_img = np.resize(blk_img, (t_size, t_size, range_h * range_w))

    return blk_img

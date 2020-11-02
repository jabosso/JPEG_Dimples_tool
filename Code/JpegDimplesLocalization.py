# ---------------------IMPORT SECTION----------------------------------------#
from scipy.signal.signaltools import wiener
import numpy as np
from img2blocks import img2blocks


# ---------------------------------------------------------------------------#

def JpegDimplesLocalization(img):
    THRESHOLD = 13
    h, w, c = img.shape
    templ_size = min(32, h, w)

    for c_iter in range(c):
        img[:, :, c_iter] = img[:, :, c_iter] - wiener(img[:, :, c_iter], (3, 3))
    img = np.mean(img, axis=2)
    blk_img = img2blocks(img, templ_size)

# ---------------------IMPORT SECTION----------------------------------------#
from scipy.signal.signaltools import wiener
import numpy as np
from img2blocks import img2blocks
from crosscorr import crosscorr
from PCE_noStat import PCE_noStat


# ---------------------------------------------------------------------------#

def JpegDimplesLocalization(img):
    THRESHOLD = 13
    h, w, c = img.shape
    templ_size = min(32, h, w)

    for c_iter in range(c):
        img[:, :, c_iter] = img[:, :, c_iter] - wiener(img[:, :, c_iter], (3, 3))
    img = np.mean(img, axis=2)
    blk_img = img2blocks(img, templ_size)

    blk_img = np.mean(blk_img, axis=2)
    print(blk_img.shape)
# --------------------------------------- Generate Template ---------------------------------------#

    template = np.zeros((templ_size, templ_size))
    for i in range(0, templ_size, 8):
        for j in range(0, templ_size, 8):
            template[i, j] = 1
# -------------------------------------- Compute Correlation --------------------------------------#
    C = crosscorr(template, blk_img)
    detection = PCE_noStat(C, [8, 8], 8)



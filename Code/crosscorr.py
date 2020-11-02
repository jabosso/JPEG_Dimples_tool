import numpy as np
import scipy

def crosscorr(arr_1, arr_2):
    arr_1 = arr_1 - np.mean(arr_1)
    arr_2 = arr_2 - np.mean(arr_2)
    #---------------------------------------#
    tilted_array2 = np.flip(arr_2,1)
    tilted_array2 = np.flip(tilted_array2,0)
    TA = scipy.fft(tilted_array2)
    FA = scipy.fft(arr_1)
    FF = np.multiply(FA, TA)
    ret = scipy.ifft(FF)
    return ret
import numpy as np


def PCE_noStat(C, shift_range=[0,0], squaresize=11):
    if C.all()==0 :
        PCE = 0
        pvalue = 1
        PeakLocation = [0,0]
    else :
        Cinrange = C[0:shift_range[0], 0:shift_range[1]]
        ord = sort(C)
        peakheight, coord = ord[0]
        xpeak, ypeak =coord
        C_without_peak = RemoveNeighborhood(C,[xpeak,ypeak],squaresize)
        PCE_energy = np.mean(np.dot(C_without_peak,C_without_peak))
        PCE = peakheight*peakheight/PCE_energy*np.sign(peakheight)

    return



def keyer(e):
    a, b = e
    return a
def sort(A):
    A_list=[]
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            A_list.append([A[i][j], (i,j)])
    A_list.sort(reverse=True, key= keyer)
    return A_list

def RemoveNeighborhood(X,x,asize):
    m, n =X.shape
    radius =(asize-1)/2
    X_s = np.roll(X,int(radius-x[0])+1, axis=0) #----- ERROR
    X_s = np.roll(X_s, int(radius - x[1]) + 1, axis=1)
    Y =X[asize+1:,0:asize]
    Y= Y.reshape(-1)
    return Y
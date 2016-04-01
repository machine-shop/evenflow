import numpy as np

def DoProduction(T):
    #Extract the dimensions(has to be 3) from matrix T.
    nVars, PPP, nTaus = np.shape(T)

    #Creates two 2D arrays filled with 0s.
    Tplus = np.zeros((nVars, nTaus))
    Tminus = np.zeros((nVars, nTaus))

    #Creates one 3D array filled with NaN.
    TnetBinary = np.empty((nVars, nVars, nTaus))
    TnetBinary.fill(np.NAN)

    #Creates one 3D array filled with 1s.
    nanFlag = np.ones((nVars, nVars, nTaus))

    #Calculation
    for i in range(nVars):
        for j in range(nVars):
            for t in range(nTaus):
                if T[i, j, t] != np.NAN:
                    Tplus[i,t] = Tplus[i,t] + T[i,j,t]
                    Tminus[j,t] = Tminus[j,t] + T[i,j,t]

    Tnet = Tplus - Tminus

    for t in range(nTaus):
        SQRmat = T[:,:,t]
        TnetBinary[:,:,t] = SQRmat - SQRmat.transpose()
        #transpose of non-complex conjugate, but original matlab code uses complex conjugate transpose

    return Tplus, Tminus, Tnet,TnetBinary

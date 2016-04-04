import numpy as np

def DoProduction(T):
    #Extract the dimensions(has to be 3) from matrix T.
    nTaus, nVars, PPP = np.shape(T)

    #Creates two 2D arrays filled with 0s.
    Tplus = np.zeros((nVars, nTaus))
    Tminus = np.zeros((nVars, nTaus))

    #Creates one 3D array filled with NaN.
    Tnet = np.empty((nVars,nTaus))
    Tnet.fill(np.NAN)
    TnetBinary = np.empty((nTaus, nVars, nVars))
    TnetBinary.fill(np.NAN)

    #Creates one 3D array filled with 1s.
    nanFlag = np.ones(( nTaus, nVars, nVars))

    #Calculation



    for i in range(nVars):
        for j in range(nVars):
            for t in range(nTaus):
                if T[t, i, j] != np.NAN:
                    Tplus[i,t] = Tplus[i,t] + T[t, i,j]
                    Tminus[j,t] = Tminus[j,t] + T[t, i,j]

    Tnet = Tplus - Tminus

    for t in range(nTaus):
        SQRmat = T[t, :,:]
        
        TnetBinary[t, :,:] = SQRmat - SQRmat.transpose()
        #transpose of non-complex conjugate, but original matlab code uses complex conjugate transpose

    return Tplus, Tminus, Tnet,TnetBinary

import numpy as np

def getcountmat(tuplemat, nbinmat, sX, sY, nodatacode):
    """

    :param tuplemat: matrix to be processed.
    :param nbinmat: matrix of bin edges
    :param sX: scalar
    :param sY: scalar
    :param nodatacode: indicates field has no data value
    :return: number of valid entries (ncount) and matrix with 1s where there
    are valid entries, and 0 elsewhere.
    """
    ndata, _ = np.shape(tuplemat)
    binmatarr = np.asarray(nbinmat)
    C = np.zeros(shape=(binmatarr[sX-1],binmatarr[sY-1], binmatarr[sY-1]))
    ncounts = 0
    for i in range(ndata):
        dimXt = tuplemat[i, 1]
        dimYw = tuplemat[i, 2]
        dimYf = tuplemat[i, 3]
        if dimXt != nodatacode and dimYw != nodatacode and dimYf != nodatacode:
            C[dimXt, dimYw, dimYf]+= 1
            ncounts += 1
    return C, ncounts



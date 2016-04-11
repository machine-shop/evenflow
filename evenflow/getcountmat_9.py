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
    """
    Notes on implementation:
    1) values of dimXt, dimYw and dimYf are hard-coded and reduced by 1
    to solve indexing issues. Matlab indexes from 1, python indexes from 0.
    2) likewise is done when assigning dimXt, dimYw, dimYf to tuplemat[i,j].
    3) Generalized to an n x n matrix. Might cause compatibility issues
    """
    #Todo: vectorize as much as possible.
    #Todo: generalize to arbitrary sized tuplemat/return matrix.
    # catching faulty parameters.
    assert sX >= 1
    assert sY >= 1
    assert sX-1 < len(nbinmat)
    assert sY-1 < len(nbinmat)
    assert np.size(tuplemat) > 0
    assert np.size(nbinmat) > 0
    tupshape = np.shape(tuplemat)
    assert tupshape[1] == 3

    ndata, _ = np.shape(tuplemat)
    binmatarr = np.asarray(nbinmat)
    c = np.zeros(shape=(binmatarr[sX-1], binmatarr[sY-1], binmatarr[sY-1]))
    ncounts = 0
    for i in range(ndata):
        dimXt = tuplemat[i, 0]
        dimYw = tuplemat[i, 1]
        dimYf = tuplemat[i, 2]
        if dimXt != nodatacode and dimYw != nodatacode and dimYf != nodatacode:
            c[dimXt-1, dimYw-1, dimYf-1] += 1
            ncounts += 1
    return c, ncounts



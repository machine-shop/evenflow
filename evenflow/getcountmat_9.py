import numpy as np


def getcountmat(tuplemat, nbinmat, sx, sy, nodatacode):
    """

    :param tuplemat: matrix to be processed.
    :param nbinmat: matrix of bin edges
    :param sx: scalar
    :param sy: scalar
    :param nodatacode: indicates field has no data value
    :return: number of valid entries (ncount) and matrix with 1s where there
    are valid entries, and 0 elsewhere.
    """
    """
    Notes on implementation:
    1) values of dimXt, dimYw and dimYf are hard-coded and reduced by 1
    to solve indexing issues. Matlab indexes from 1, python indexes from 0.
    2) likewise is done when assigning dimXt, dimYw, dimYf to tuplemat[i,j].
    3) Generalized to an n x n matrix. Might cause compatibility issues with
    getShannonBits.
    """
    # catching faulty parameters.
    assert sx >= 1
    assert sy >= 1
    assert sx-1 < len(nbinmat)
    assert sy-1 < len(nbinmat)
    assert np.size(tuplemat) > 0
    assert np.size(nbinmat) > 0

    # function begins
    rownum, colnum = np.shape(tuplemat)
    binmatarr = np.asarray(nbinmat)
    dimlist = []
    # constructing matrix of required proportions
    for i in range(colnum):
        if i == 0:
            dimlist.append(binmatarr[sx - 1][0])
        else:
            dimlist.append(binmatarr[sy - 1][0])
    c = np.zeros(shape=tuple(dimlist))
    ncounts = 0
    for i in range(rownum):
        row = tuplemat[i, :]
        row[row == nodatacode] = np.nan
        if np.isfinite(row).all():
            coords = tuple(row.astype(int) - 1)
            c[coords] += 1
            ncounts += 1
    return c, ncounts


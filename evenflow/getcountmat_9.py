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
    tuplematarr = np.asarray(tuplemat)
    binmatarr = np.asarray(nbinmat)
    C = np.zeros(shape=(binmatarr(sX-1),binmatarr(sY-1), binmatarr(sY-1)))


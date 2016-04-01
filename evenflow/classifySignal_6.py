import numpy as np


def classifysignal(samplemat, binedges, nbinmat, nodatacode):
    """
    :param samplemat:result from removePeriodicMean.
    :param binedges: matrix of bin edges (i.e. start and end points for intervals)
    :param nbinmat: a column vector where every entry
    is the number of bins used for this sample
    :param nodatacode: indicates no data value at this position
    :return:
    """
    # TODO: vectorize, write tests.
    ndata, nsignals = np.shape(samplemat)
    classifiedmat = np.zeros(shape=(ndata, nsignals))
    ncounts = 0
    """
    add in a bunch of assert statements to ensure that the dimensions
    of the matrices passed in all line up.
    """
    # assert
    # assert
    # assert
    # assert
    for i in range(ndata):
        for j in range(nsignals):
            classifiedmat[i,j] = nbinmat[j]
            for e in range(nbinmat[j]):
                if samplemat[i,j] == nodatacode:
                    classifiedmat[i,j] == nodatacode
                    break
                elif samplemat[i,j] <= binedges[j, e]:
                    classifiedmat[i,j] = e
                    ncounts += 1
                    break
    ncounts = float(ncounts/nsignals)
    return classifiedmat, ncounts


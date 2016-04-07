import numpy as np


def classifysignal(samplemat, binedges, nbinmat, nodatacode):
    """
    :param samplemat:result from removePeriodicMean.
    :param binedges: matrix of bin edges (i.e. start and end points for intervals)
    :param nbinmat: a column vector where every entry
    is the number of bins used for this sample
    :param nodatacode: indicates no data value at this position
    :return: matrix of classified data, and the number of assigned entries.
    """
    """
    notes explaining the implementation:
     1) nbinmat in the original matlab is a column vector with every entry the same. So instead of
     looping through I just assigned the entire classifiedmat to the value of the first entry.

     2) maintained the initial triple loop, no neat way to vectorize.

     3) IMPORTANT: classifiedmat features e+1 instead of e as entries so as to
     line up with matlab implementation. MIGHT WANNA CHANGE THIS, but code functionality
     is intact regardless.

    """
    # asserts that the arguments are of the right dimensions.
    assert samplemat.shape[1] == nbinmat.shape[0]
    assert np.amax(nbinmat) == binedges.shape[1]


    ndata, nsignals = np.shape(samplemat)
    print("Ndata: " + str(ndata))
    print("NSignals: " + str(nsignals))
    ncounts = 0
    classifiedmat = np.zeros(shape=(ndata, nsignals))
    for i in range(ndata):
        for j in range(nsignals):
            classifiedmat[i, j] = nbinmat[j]
            for e in range(nbinmat[j]):
                if samplemat[i, j] == nodatacode:
                    classifiedmat[i, j] = nodatacode
                    break
                elif samplemat[i, j] <= binedges[j, e]:
                    classifiedmat[i, j] = e + 1
                    ncounts += 1
                    break
    ncounts = float(ncounts/nsignals)
    return classifiedmat, ncounts

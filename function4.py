import numpy as np
def getSkipMean(vector, NoDataCode):
    """
    :param vector: vector of values.
    :param NoDataCode: indicates value to be ignored
    :return: average of the values in the vector ignoring NoData values
    """
    N, _ = np.shape(vector)
    sum = 0
    nVals = 0
    for i in range(N):
        if vector(i) != NoDataCode:
            sum+=vector(i)
            nVals += 1
    if nVals > 0:
        avg = sum/nVals
    else:
        avg = NoDataCode

    return avg
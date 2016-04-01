import numpy as np


def getskipmean(vector, nodatacode):

    """
    :param vector: vector of values.
    :param nodatacode: indicates value to be ignored
    :return: average of the values in the vector ignoring NoData values
    """
    vector[vector == nodatacode] = np.nan
    # checks to see if edited vector has any finite values left.
    containsdata = np.isfinite(vector).any()
    if containsdata:
        return np.nanmean(vector)
    else:
        return nodatacode

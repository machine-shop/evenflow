import numpy as np
from evenflow import getSkipMean_4 as gsm


def removeperiodicmean(signalmat, period, sliderwidth, nodatacode):

    """
    :param signalmat: n - column matrix where variables represent timeseries
    :param period: length of repeating pattern of data (i.e. seasons, years, etc).
    :param sliderwidth: Number of periods to base the anomaly on.
    :param nodatacode: data value to be ignored
    :return: matrix of values that accounts for periodic averages
    """
    ndata, nsignals = np.shape(signalmat)
    newlength = ndata - period * (sliderwidth - 1)
    anomalymat = np.nan * np.zeros(shape=(newlength, nsignals))
    avg = np.nan * np.zeros(shape=(ndata, nsignals))

    for i in range(newlength):
        for j in range(nsignals):
            end = i + (sliderwidth*period) - 1
            avg[i, j] = gsm.getskipmean(signalmat[i:end:period, j], nodatacode)

        if avg[i, j] == nodatacode or signalmat[i, j] == nodatacode:
            anomalymat[i, j] = nodatacode
        else:
            anomalymat[i, j] = signalmat[i, j] - avg[i, j]

    return anomalymat

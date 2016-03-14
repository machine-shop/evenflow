import numpy as np
from function4 import getSkipMean
def removePeriodicMean(signalMat, period, sliderWidth, NoDataCode):
    """
    :param signalMat: n - column matrix where variables represent timeseries
    :param period: length of repeating pattern of data (i.e. seasons, years, etc).
    :param sliderWidth: Number of periods to base the anomaly on.
    :param NoDatCode: data value to be ignored
    :return: matrix of values that accounts for periodic averages
    """
    nData, nSignals = np.shape(signalMat)   
    newLength = nData - period * (sliderWidth - 1)
    anomalyMat = np.nan * np.zeros(shape = (newLength, nSignals))
    avg = np.nan * np.zeros(shape=(nData, nSignals))

    for i in range(newLength):
        for j in range(nSignals):
            end = i + (sliderWidth*period) - 1
            avg[i,j] = getSkipMean(signalMat[i:end:period, j], NoDataCode)

        if avg[i,j] == NoDataCode or signalMat[i,j] == NoDataCode:
            anomalyMat[i,j] = NoDataCode
        else:
            anomalyMat[i,j] = signalMat[i,j]

    return anomalyMat


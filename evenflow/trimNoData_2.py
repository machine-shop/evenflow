import numpy as np


def trimnodata(rawdata, nodatacode):
    """
    :param rawdata: matrix of values, some of which are nodata values
    :param nodatacode: code specifying that given entry in rawdata has no data value
    :return: a matrix where the entire row containing a nodata entry is filled with nodata entries
    """
    # TODO: vectorize this even more. Currently relies on one loop and one
    # TODO (cont'd): set of vectorized ops

    row, col = np.shape(rawdata)
    trimmeddata = np.zeros(shape=(row, col))
    for i in range(row):
        row = rawdata[i, :].copy()
        row[row == nodatacode] = np.nan
        containsdata = np.isfinite(row).all()
        if containsdata:
            trimmeddata[i, :] = row
        else:
            trimmeddata[i, :] = nodatacode
    return trimmeddata

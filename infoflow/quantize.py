import numpy as np
import sys


def quantize(sig, partition, varargin):

    if sig.size == 0 or not np.isreal(sig).all() or sig.shape[0] != 1:
        sys.exit("comm:quantize:invalid_Sig")

    if len(partition) == 0 or not np.isreal(partition).all() or type(partition) != list:
        sys.exit("comm:quantize:invalid_Partition")

    nrows, ncols = np.shape(sig)
    indx = np.zeros((nrows, ncols))

    for i in range(len(partition)):
        indx += (sig > partition[i])

    return indx

import numpy as np
from math import pi, exp, sqrt


def multidimensionalkde(x, xi, bw_coeff):
    """
    :param x: data matrix, rows are observations and columns are dimensions.
    :param xi: coordinates at which joint probabilities are to be estimated.
    :param bw_coeff:
    :return: joint probability at xi
    """
    n, d = np.shape(x)
    # pick the bandwidth for each dimension
    h = np.zeros(shape=(1, d))
    for i in range(d):
        h[0, i] = float(bw_coeff * 1.06 * n**(-1/5) *np.std(x[:, i]))
    # estimating probability at xi
    p = np.zeros(shape=(np.shape(xi)[0], 1))
    for k in range(len(p)):
        for i in range(n):
            prod = 1
            for j in range(d):
                u = float((xi[j] - x[i, j])/h[0][j])
                prod = float(prod * 1/sqrt(2*pi) * exp(-0.5*(u**2)) / h[0][j])
            p[k] += prod
    p = p/n
    return p

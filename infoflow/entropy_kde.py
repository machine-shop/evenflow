import numpy as np
from infoflow import multidimkde as mdkde
from math import log


def kerneldensityestimation(source, target, timelagx, timelagy, n, bw_coeff):
    """
    :param source: source time series, 1-D vector
    :param target: target time series, 1-D vector
    :param timelagx: time lag in x from present
    :param timelagy: time lag in y from present
    :param n: number of equally spaced points along each dimension where probabilities are to be estimated
    :param bw_coeff: multiplier that adjusts Gaussian bandwidth
    :return: transfer entropy in bits.
    """

    """ All code written here is based on the transfer entropy
     toolbox, Copyright 2011 Joon Lee. Use protected under GNU."""

    # fixing block lengths to 1
    l, k = 1, 1

    sourcearr = source.flatten()
    targetarr = target.flatten()

    # go through source and target timeseries, and populate source_pat, target_pat and target_t
    source_pat = []
    target_pat = []
    target_t = []

    for i in range(max(l+timelagx, k+timelagy)-1, min(len(sourcearr), len(targetarr))):
        source_pat.append(sourcearr[i - l - timelagx+1: i - timelagx+1][0])
        target_pat.append(targetarr[i - k - timelagy+1: i - timelagy+1][0])
        target_t.append(targetarr[i])

    # reassigning to numpy arrays
    source_pat = np.array(source_pat).reshape(len(source_pat), 1)
    target_pat = np.array(target_pat).reshape(len(target_pat), 1)
    target_t = np.array(target_t).reshape(len(target_t), 1)

    # establishing values
    source_pat_i = np.linspace(np.amin(source_pat) - 0.1*(np.amax(source_pat) - np.amin(source_pat)),
                               np.amax(source_pat) + 0.1*(np.amax(source_pat) - np.amin(source_pat)), n)

    target_pat_i = np.linspace(np.amin(target_pat) - 0.1*(np.amax(target_pat) - np.amin(target_pat)),
                               np.amax(target_pat) + 0.1*(np.amax(target_pat) - np.amin(target_pat)), n)

    target_t_i = np.linspace(np.amin(target_t)-0.1*(np.amax(target_t)-np.amin(target_t)),
                            np.amax(target_t)+0.1*(np.amax(target_t)-np.amin(target_t)), n)

    # reshaping the resultant arrays
    source_pat_i = np.array(source_pat_i)
    target_pat_i = np.array(target_pat_i)
    target_t_i = np.array(target_t_i)

    # initializing the probability density function matrix
    pdf = np.zeros(shape=(len(target_t_i), len(source_pat_i), len(target_pat_i)))

    # bookkeeping
    source_pat = source_pat.transpose()
    target_pat = target_pat.transpose()
    target_t = target_t.transpose()

    # populating the pdf matrix
    x = np.vstack((source_pat, target_pat, target_t)).transpose()
    for i in range(len(source_pat_i)):
        for j in range(len(target_pat_i)):
            for k in range(len(target_t_i)):
                xi = np.hstack((source_pat_i[i], target_pat_i[j], target_t_i[k]))
                ans = mdkde.multidimensionalkde(x, xi, bw_coeff)
                pdf[k, i, j] = ans[0]

    # normalizing probabilities
    pdf = pdf/np.sum(pdf)

    # computing transfer entropy
    transferentropy = 0
    for i in range(len(source_pat_i)):
        for j in range(len(target_pat_i)):
            for k in range(len(target_t_i)):
                a = pdf[k, i, j]
                b = np.sum(pdf[:, i, j])
                c = np.sum(pdf[k, :, j])
                d = np.sum(sum(pdf[:, :, j]))
                transferentropy += a * log(((a * d) / (b * c)), 2)
    return transferentropy

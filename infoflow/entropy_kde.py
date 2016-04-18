import numpy as np
from infoflow import multidimkde as mdkde

def kerneldensityestimation(source, target, timelagx, timelagy, n, bw_coeff):
    """
    :param source: source time series
    :param target: target time series
    :param timelagx: time lag in x from present
    :param timelagy: time lag in y from present
    :param N: number of equally spaced points along each dimension where probabilities are to be estimated
    :param bw_coeff: multiplier that adjusts Gaussian bandwidth
    :return: transfer entropy in bits.
    """

    """ All code written here is based on the transfer entropy
     toolbox, Copyright 2011 Joon Lee. Use protected under GNU."""

    # fixing block lengths to 1
    l, k = 1, 1

    sourcearr = source.flatten()
    targetarr = target.flatten()

    # go through the timeseries source and target, and populate source_pat, target_pat and target_t
    source_pat = []
    target_pat = []
    target_t = []
    for i in range(max(l+timelagx, k+timelagy), min(len(source), len(target)), 1):
       # print(sourcearr[i - l - timelagx:i - timelagx + 1])
        source_pat.append(sourcearr[i - l - timelagx:i - timelagx ][0])
        target_pat.append(targetarr[i - k - timelagy:i - timelagy ][0])
        target_t.append(targetarr[i])

    # reassigning to numpy arrays
    source_pat = np.array(source_pat).reshape(len(source_pat), 1)
    target_pat = np.array(target_pat).reshape(len(target_pat), 1)
    target_t = np.array(target_t).reshape(len(target_t), 1)

    # computing transfer entropy
    #print(source_pat)
    source_pat_i = np.linspace(np.amin(source_pat) - 0.1*(np.amax(source_pat) - np.amin(source_pat)),
                               np.amax(source_pat)+ 0.1*(np.amax(source_pat) - np.amin(source_pat)), n)

    target_pat_i = np.linspace(np.amin(target_pat) - 0.1*(np.amax(target_pat)- np.amin(target_pat)),
                               np.amax(target_pat) + 0.1*(np.amax(target_pat) - np.amin(target_pat)), n)

    target_t_i = np.linspace(np.amin(target_t)-0.1*(np.amax(target_t)-np.amin(target_t)),
                np.amax(target_t)+0.1*(np.amax(target_t)-np.amin(target_t)), n)

    # reshaping the resultant arrays
    source_pat_i = np.array(source_pat_i).reshape(len(source_pat_i),1)
    target_pat_i = np.array(target_pat_i).reshape(len(target_pat_i),1)
    target_t_i = np.array(target_t_i).reshape(len(target_t_i),1)
    #initializing the probability density function matrix
    pdf = np.zeros(shape=(len(target_t_i), len(source_pat_i), len(target_pat_i)))


    for i in range(len(source_pat_i)):
        for j in range(len(target_pat_i)):
            for k in range(len(target_t_i)):
                x = np.hstack((source_pat, target_pat, target_t))
                xi = np.hstack((source_pat_i[i], target_pat_i[j], target_t_i[k]))
                ans = mdkde.multidimensionalkde(x, xi, bw_coeff)
                pdf[i, j, k]=ans[0]

    # normalizing
    pdf = pdf/np.sum(pdf)
    transferentropy = 0
    for i in range(len(source_pat_i)):
        for j in range(len(target_pat_i)):
            for k in range(len(target_t_i)):
                a = pdf[i, j, k]
                b = sum(pdf[:, i, j])
                c = sum(pdf[i, j, :])
                d = sum(sum(pdf[:, j, :]))
                transferentropy = transferentropy + a * np.log2((a * d) / (b * c))

    return transferentropy

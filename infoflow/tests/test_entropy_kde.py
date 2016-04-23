from infoflow import entropy_kde as kde
from infoflow import multidimkde as multkde
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))


# tests first case of matlab demo script.
def test_basic():
    x = np.genfromtxt(path + '\input files\entropykdeinputx.txt', delimiter="\t")
    y = np.genfromtxt(path + '\input files\entropykdeinputy.txt', delimiter='\t')
    n = 10
    timelagx = 2
    timelagy = 2
    bw_coeff = 1
    ans = kde.kerneldensityestimation(x, y, timelagx, timelagy, n, bw_coeff)
    result = 0.798553577280728
    print(ans)
    assert np.isclose(ans, result,rtol=10e-20,atol=10e-15)


# test all cases of matlab demo script.
def test_all():
    n = 10
    timelagx = 2
    timelagy = 2
    bw_coeff = 1
    resultarr = [0.798553577280728, 0.845537518582966, 0.879353564494117, 0.862343316961739,
                 0.946161823385283, 0.967731331557469, 0.971018899881274, 0.991938112384209,
                 0.997664153887389, 1.00943865954647, 1.03324658910437]
    for i in range(1, 12):
        x = np.genfromtxt(path + '\input files\entropykdeinputx' + str(i) + '.txt', delimiter='\t')
        y = np.genfromtxt(path + '\input files\entropykdeinputy' + str(i) + '.txt', delimiter='\t')
        result = resultarr[i-1]
        ans = kde.kerneldensityestimation(x, y, timelagx, timelagy, n, bw_coeff)
        assert np.isclose(ans, result, rtol=10e-20, atol=10e-15)

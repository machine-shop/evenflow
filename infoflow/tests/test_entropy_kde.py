from infoflow import entropy_kde as kde
from infoflow import multidimkde as multkde
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))

def test_basic():
    x = np.genfromtxt(path + '\entropykdeinputx.txt', delimiter="\t")
    y = np.genfromtxt(path + '\entropykdeinputy.txt', delimiter='\t')
    n = 10
    timelagx = 2
    timelagy = 2
    bw_coeff = 1
    ans = kde.kerneldensityestimation(x,y,timelagx,timelagy,n,bw_coeff)
    result = 0.798553577280728
    print(ans)
    assert np.isclose(ans, result,rtol=10e-20,atol=10e-15)





def test_inputs():
    return 0


def test_outputs():
    return 0


def test_all():
    return 0

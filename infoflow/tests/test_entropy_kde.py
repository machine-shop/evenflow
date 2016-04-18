from infoflow import entropy_kde as kde
from infoflow import multidimkde as multkde
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))

def test_basic():
    x = np.genfromtxt(path + '\entropykdeinputx.txt', delimiter=",")
    print(np.shape(x))
    y = np.genfromtxt(path + '\entropykdeinputy.txt', delimiter=',')
    print(np.shape(y))
    n = 10
    timelagx = 2
    timelagy = 2
    bw_coeff = 1
    ans = kde.kerneldensityestimation(x,y,timelagx,timelagy,n,bw_coeff)
    result = 0.0086
    print(ans)
    assert ans == result





def test_inputs():
    return 0


def test_outputs():
    return 0


def test_all():
    return 0

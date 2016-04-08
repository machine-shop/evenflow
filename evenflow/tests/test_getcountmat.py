import numpy as np
from evenflow import getcountmat_9 as gcm
import os

path = os.path.dirname(os.path.realpath(__file__))
def test_basic():
    nsignals = 3
    nbinmat = np.array([11,11,11]).reshape(3,1)
    tuplemat = np.genfromtxt(path + '\mat.txt',delimiter=',')
    nodatacode = -9999
    sX, sY = 3,3
    result = np.genfromtxt(path + '\getcountresult.txt', delimiter=',')
    print(result)
    print(np.shape(result))
    print(np.size(result))
    result.reshape((11,11,11))
    for matrix in result:
        matrix = np.transpose(matrix)
    final, count = gcm.getcountmat(tuplemat, nbinmat, sX, sY, nodatacode)
    assert final.all() == result.all()

def test_1():
    return 0


def test_2():
    return 0


def test_3():
    return 0


def test_4():
    return 0

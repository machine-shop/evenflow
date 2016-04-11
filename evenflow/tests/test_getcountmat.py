import numpy as np
from evenflow import getcountmat_9 as gcm
import os

path = os.path.dirname(os.path.realpath(__file__))


def test_basic():
    nbinmat = np.array([11, 11, 11]).reshape(3, 1)
    tuplemat = np.genfromtxt(path + '\mat.txt', delimiter=',')
    nodatacode = -9999
    sx, sy = 3, 3
    result = np.genfromtxt(path + '\getcountresult.txt', delimiter=',')
    result.reshape((11, 11, 11))
    for matrix in result:
        matrix = np.transpose(matrix)
    final, count = gcm.getcountmat(tuplemat, nbinmat, sx, sy, nodatacode)
    assert final.all() == result.all()


def test_assignment():
    nbinmat = np.array([3, 3, 3]).reshape(3, 1)
    tuplemat = np.zeros(shape=(4, 4))

    return 0


def test_indices():
    return 0


def test_ncounts():
    return 0


def test_all():
    return 0

#check to see if only valid inputs are processed. insert random inputs
# to check if everything is being caught.
def test_random_inputs():
    return 0
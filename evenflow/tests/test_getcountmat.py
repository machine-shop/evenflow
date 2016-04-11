import numpy as np
from evenflow import getcountmat_9 as gcm
import os

path = os.path.dirname(os.path.realpath(__file__))


def test_basic():
    nbinmat = np.array([11, 11, 11]).reshape(3, 1)
    tuplemat = np.genfromtxt(path + '/mat.txt', delimiter=',')
    nodatacode = -9999
    sx, sy = 3, 3
    result = np.genfromtxt(path + '/getcountresult.txt', delimiter=',')
    result.reshape((11, 11, 11))
    for matrix in result:
        matrix = np.transpose(matrix)
    final, count = gcm.getcountmat(tuplemat, nbinmat, sx, sy, nodatacode)
    assert final.all() == result.all()


def test_shape():
    nbinmat = np.array([3, 3, 3, 3]).reshape(4, 1)
    tuplemat = np.zeros(shape=(4, 4))
    nodatacode = - 9999
    sx, sy = 3, 3
    result, counts = gcm.getcountmat(tuplemat, nbinmat, sx, sy, nodatacode)
    assert np.shape(result) == (3, 3, 3, 3)


def test_indices():
    nbinmat = np.array([3, 3, 3, 3]).reshape(4, 1)
    tuplemat = np.ones(shape=(4, 4))
    nodatacode = -9999
    sx, sy = 3, 3
    result, count = gcm.getcountmat(tuplemat, nbinmat, sx, sy, nodatacode)
    assert count == 4
    assert result[0, 0, 0, 0] == 4
    result[0, 0, 0, 0] = np.nan
    assert np.nanmean(result) == 0


def test_ncounts():
    nbinmat = np.array([3, 3, 3, 3, 3]).reshape(5, 1)
    tuplemat = np.ones(shape=(5, 5))
    nodatacode = -9999
    sx, sy = 3, 3
    result, count = gcm.getcountmat(tuplemat, nbinmat, sx, sy, nodatacode)
    assert count == 5


def test_varied_bins():
    nbinmat = np.array([2, 3, 4, 5]).reshape(4, 1)
    tuplemat = np.ones(shape=(4, 4))
    nodatacode = -9999
    sx, sy = 3, 3
    result, count = gcm.getcountmat(tuplemat, nbinmat, sx, sy, nodatacode)
    assert np.shape(result) == (4, 4, 4, 4)
    assert result[0, 0, 0, 0] == count
    assert count == 4
    dx, dy = 4, 4
    result2, count2 = gcm.getcountmat(tuplemat, nbinmat, dx, dy, nodatacode)
    assert np.shape(result2) == (5, 5, 5, 5)
    assert result2[0, 0, 0, 0] == count2
    assert count2 == 4
    fx, fy = 2, 4
    result3, count3 = gcm.getcountmat(tuplemat, nbinmat, fx, fy, nodatacode)
    assert np.shape(result3) == (3, 5, 5, 5)
    assert result3[0, 0, 0, 0] == count3
    assert count3 == 4

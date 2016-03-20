import numpy as np


from evenflow import removePeriodicMean_3 as rpm


def test_basicfunctionality():
    a = np.zeros(shape=(3, 4))
    a[a == 0] = -999
    b = np.zeros(shape=(3, 4))
    b[0, 0] = 1
    b[1, 2] = 1
    assert rpm.removeperiodicmean(b, 1, 1, -999).all() == a.all()


def test_2():
    return 0


def test_3():
    return 0


def test_4():
    return 0


def test_5():
    return 0

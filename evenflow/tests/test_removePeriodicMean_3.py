import numpy as np


from evenflow import removePeriodicMean_3 as rpm


def test_basicfunctionality():
    a = np.zeros(shape=(3, 4))
    a[a == 0] = -999
    b = np.zeros(shape=(3, 4))
    b[0, 0] = 1
    b[1, 2] = 1
    assert rpm.removeperiodicmean(b, 1, 1, -999).all() == a.all()


def test_allones():
    a = np.zeros(shape=(50,50))
    a[a==0] = 1
    b = np.zeros(shape=(50,50))
    assert rpm.removeperiodicmean(a,1, 1, 0).all() == b.all()



import numpy as np
# import sys
# import os
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from evenflow import getSkipMean_4 as gsm



def test_basicfunctionality():

    a = np.nan * np.zeros(shape=(3, 4))
    a[1, 1] = 1
    b = np.zeros(shape=(3, 4))
    b[2, 1] = 4
    b[2, 2] = 5
    assert gsm.getskipmean(a, np.nan) == 1.0


def test_first():
    a = np.nan * np.zeros(shape=(3, 4))
    a[1, 1] = 1
    b = np.zeros(shape=(3, 4))
    b[2, 1] = 4
    b[2, 2] = 5
    assert gsm.getskipmean(a, np.nan) == 1.0


def test_skipvalue2():
    b = np.zeros(shape=(3, 4))
    b[2, 1] = 4
    b[2, 2] = 5
    assert gsm.getskipmean(b, 0) == 4.5


def test_computation():
    c = np.random.rand(3, 4)
    assert gsm.getskipmean(c, np.nan) == np.nanmean(c)


def test_aggregatemean():
    d = np.zeros(shape=(3, 4))
    d[d == 0] = 1
    assert gsm.getskipmean(d, 1) == 1

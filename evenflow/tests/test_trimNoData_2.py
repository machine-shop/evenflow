import numpy as np
from evenflow import trimNoData_2 as tnd


def test_basicfunctionality():
    a = np.ones(shape=(3,4))
    a[1,1] = 0
    b = np.matrix([[1,1,1,1],[0,0,0,0],[1,1,1,1]])
    assert b.all() == tnd.trimnodata(a,0).all()


def test_2():
    a = np.ones(shape=(50,50))
    a[1,:] = 0
    b = np.zeros(shape=(50,50))
    assert b.all() == a.all()


def test_3():
    a = np.ones(shape = (4, 4))
    np.fill_diagonal(a, 5)
    b = np.ones(shape = (4, 4))
    np.fill_diagonal(b, 5)
    a[0, 3] = np.nan
    b[0, 2] = np.nan
    assert tnd.trimnodata(a, np.nan).all() == tnd.trimnodata(b, np.nan).all()

def test_nancase():
    a = np.ones(shape =(4, 4))
    np.fill_diagonal(a, np.nan)
    result = tnd.trimnodata(a, np.nan)
    assert np.isnan(result).all() == True


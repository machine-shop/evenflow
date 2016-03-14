import numpy as np
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import trimNoData_2

def function2GeneralTest():
    tnd = trimNoData_2.trimNoData
    a = np.zeros(shape=(3,4))
    a[0,0] = 1
    a[1,0] = 1
    a[2,1] = 1
    b = tnd(a, 1)
    x = np.zeros(shape=(3,4))
    x[:] = 1
    assert x == b
    y = np.zeros(shape=(3,4))
    c = tnd(a, 0)
    assert c==y



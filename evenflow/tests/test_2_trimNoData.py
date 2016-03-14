import numpy as np, nose
from function2 import trimNoData

def function2GeneralTest():
    a = np.zeros(shape=(3,4))
    a[0,0] = 1
    a[1,0] = 1
    a[2,1] = 1
    b = trimNoData(a, 1)
    x = np.zeros(shape=(3,4))
    x[:] = 1
    print(x == b)
    y = np.zeros(shape=(3,4))
    c = trimNoData(a, 0)
    print(c==y)



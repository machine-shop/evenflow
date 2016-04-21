from infoflow import multidimkde as multkde
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))

def test_basic():
    """
    Note about test: ans[0][0] - result ~ 10^-34. If system is chaotic, could cause errors. Double check
    floating point bs.
    """
    x = np.genfromtxt(path + '\mdkde_input.txt', delimiter='\t')
    xi = np.array([6.921252431034000, -18.53087722427270, 37.295725015630570])
    bw_coeff = 1
    result = 4.67184882019e-22
    ans = multkde.multidimensionalkde(x, xi, bw_coeff).reshape(1,3)
    assert np.isclose(ans[0,0], result)


from infoflow import multidimkde as multkde
import numpy as np
import os

path = os.path.dirname(os.path.realpath(__file__))

def test_basic():
    x = np.genfromtxt(path + '\mdkde_input.txt', delimiter='\t')
    xi = np.array([6.921252431034000, -18.53087722427270, 37.295725015630570])
    bw_coeff = 1
    result = 4.67184882019107e-22
    ans = multkde.multidimensionalkde(x, xi, bw_coeff)
    assert np.isclose(ans, result).all()

def test_inputs():
    return 0


def test_outputs():
    return 0


def test_all():
    return 0


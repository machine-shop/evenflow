import numpy as np
import os
from evenflow import classifySignal_6 as csig



path = os.path.dirname(os.path.realpath(__file__))
def test_basic():
    binedges = np.array([-15.188183272727272,-11.711953545454545,-8.2357238181818158,
                      -4.7594940909090884,-1.2832643636363628,2.1929653636363682,
                      5.6691950909090956,9.145424818181823,12.621654545454547,16.097884272727274,
                      19.574114000000005,-20.639158272727272,-15.856375545454545,
                      -11.073592818181819,-6.2908100909090905,-1.5080273636363657,
                      3.2747553636363627,8.0575380909090875,12.840320818181819,
                      17.623103545454544,22.405886272727269,27.188669,
                      5.2275687181818178,9.4928182463636368,13.758067774545454,
                      18.023317302727271,22.288566830909087,26.553816359090906,
                      30.819065887272725,35.084315415454547,39.349564943636359,
                      43.614814471818178,47.880064]).reshape(3,11)
    samplemat = np.genfromtxt(path + '\classifySignalTestFile.txt', delimiter=",")
    nodatacode = -9999
    nbinmat = np.array([11,11,11]).reshape(3,1)
    ans = np.genfromtxt(path + '\classifySignalTestFile2.txt', delimiter=",")
    result, count = csig.classifysignal(samplemat, binedges, nbinmat, nodatacode)
    assert np.allclose(result, ans)


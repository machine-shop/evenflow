import sys
import os
import numpy as np
from infoflow import quantize as qtz
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

in_path = 'in_quantize/'
out_path = 'out_quantize/'

x = np.genfromtxt(in_path+'x.csv', delimiter=',').reshape((1, 202))
partition = np.genfromtxt(in_path+'partition.csv', delimiter=',').tolist()
xquant = np.genfromtxt(out_path+'xquant.csv', delimiter=',').reshape((1, 202))

assert np.all((xquant == qtz.quantize(x, partition, 0)))

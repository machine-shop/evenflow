import sys
import os
import numpy as np
from infoflow import quantize as qtz
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ''))
print(sys.path[0])

in_path = 'in_quantize/'
out_path = 'out_quantize/'

x = np.genfromtxt(sys.path[0]+in_path+'x.csv', delimiter=',').reshape((1, 202))
partition = np.genfromtxt(sys.path[0]+ in_path+'partition.csv', delimiter=',').tolist()
xquant = np.genfromtxt(sys.path[0]+out_path+'xquant.csv', delimiter=',').reshape((1, 202))

assert np.all((xquant == qtz.quantize(x, partition, 0)))

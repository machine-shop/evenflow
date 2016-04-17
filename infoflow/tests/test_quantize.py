import sys
import os
import numpy as np
import scipy.io as sio
from infoflow import quantize as qtz
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

in_path = 'in_quantize/'
out_path = 'out_quantize/'

x = sio.loadmat(in_path+'x.mat')['x']
partition = sio.loadmat(in_path+'partition.mat')['partition']
xquant = sio.loadmat(out_path+'xquant.mat')['xquant']

assert np.all((xquant == qtz.quantize(x, partition[0].tolist(), 0)))

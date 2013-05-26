#!/usr/bin/env python2

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import matplotlib
import matplotlib.pyplot as plt
import numpy as np



returns = matplotlib.mlab.csv2rec('./returns_calculated.csv',delimiter=b',')

#from IPython import embed; embed()

x = returns['date']
y = returns['yhoo']
fig = plt.figure()
fig.add_subplot(111).plot(x, y)
plt.show()


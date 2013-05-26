#!/usr/bin/env python2

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import datetime


returns = matplotlib.mlab.csv2rec('./returns_calculated.csv',delimiter=b',')
news = matplotlib.mlab.csv2rec('./news.csv',delimiter=b',')


#from IPython import embed; embed()

x = returns['date']
y = returns['yhoo']
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y)

print('Footnotes (headline text):')
for i, (time, headline) in enumerate(news):
	print('[{0}] {1} "{2}"'.format(i, time, headline))
	ax.annotate('[{0}]'.format(i), xy=(time, 0),
		xytext=(time, 0.1),
		arrowprops={'facecolor': 'black', 'shrink': 0.05, 'width': 0},
		horizontalalignment='center', verticalalignment='top',
	)

plt.show()


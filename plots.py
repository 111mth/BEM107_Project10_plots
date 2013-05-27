#!/usr/bin/env python2

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime


returns = matplotlib.mlab.csv2rec('./returns_calculated.csv',delimiter=b',')
news = matplotlib.mlab.csv2rec('./news.csv',delimiter=b',')



x = returns['date']
y = returns['yhoo']
fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlim((datetime(2008, 01, 01), datetime(2008, 03, 01)))

ax.plot(x, y)
#from IPython import embed; embed()

print('Footnotes (headline text):')
(ymin, ymax) = ax.get_ybound()
for i, (time, headline) in enumerate(news):
	print('[{0}] {1} "{2}"'.format(i, time, headline))
	ax.annotate('[{0}]'.format(i),
		xy=(time, ymin),
		xytext=(time, ymax + 0.02 * (ymax - ymin) * (i % 5)),
		arrowprops={
			'arrowstyle': '-', #'shrink': 0.05,
			#'width': 0,
			#'linestyle': 'dotted',
			'edgecolor': 'black', 'alpha': 0.2
		},
		horizontalalignment='center', verticalalignment='bottom',
	)

plt.show()


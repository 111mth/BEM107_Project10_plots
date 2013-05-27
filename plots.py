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

print('Footnotes (headline text):')
for i, (time, headline) in enumerate(news):
	print('[{0}] {1} "{2}"'.format(i, time, headline))

def annotate_news(axis):
	'Annotates the plot axis with news events.'
	(ymin, ymax) = axis.get_ybound()
	for i, (time, headline) in enumerate(news):
		axis.annotate('[{0}]'.format(i),
			xy=(time, ymin),
			xytext=(time, ymax + 0.02 * (ymax - ymin) * (i % 5)),
			arrowprops={'arrowstyle': '-', 'edgecolor': 'black', 'alpha': 0.2,},
			horizontalalignment='center', verticalalignment='bottom',
		)	

#ax.set_xlim((datetime(2008, 01, 01), datetime(2008, 03, 01)))

call = lambda f: f()

@call
def figure2a():
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.plot(returns['date'], returns['cumexcret_yhoo'])
	ax.plot(returns['date'], returns['cumexcret_msft'])
	annotate_news(ax)
	fig.tight_layout()
	return fig


#from IPython import embed; embed()



plt.show()


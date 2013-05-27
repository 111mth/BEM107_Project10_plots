#!/usr/bin/env python2

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import matplotlib
import matplotlib.pyplot as plt
import numpy

from datetime import datetime


returns = matplotlib.mlab.csv2rec('./returns_calculated.csv',delimiter=b',')
news = matplotlib.mlab.csv2rec('./news.csv',delimiter=b',')

def cumulate_returns(series):
	'''Takes a time-series of daily returns and calculates the cumulative returns.'''
	return (1 + numpy.array(series)).cumprod() - 1

print('Footnotes (headline text):')
for i, (time, headline) in enumerate(news):
	print('[{0}] {1} "{2}"'.format(i, time, headline))

def annotate_news(axes):
	'Annotates the plot axes with news events.'
	news_axes = axes.twiny()
	news_axes.set_xlim(axes.get_xlim())
	news_axes.set_xticks(news['date'])
	news_axes.set_xticklabels(map('[{0}]'.format,xrange(len(news))))
	news_axes.xaxis.grid(True, linestyle='-', linewidth=1, color='black', alpha=0.2)

#ax.set_xlim((datetime(2008, 01, 01), datetime(2008, 03, 01)))

call = lambda f: f()

@call
def figure2a():
	fig = plt.figure()
	axes = fig.add_subplot(1, 1, 1)
	axes.plot(returns['date'], returns['excret_yhoo'])
	axes.plot(returns['date'], returns['excret_msft'])
	annotate_news(axes)
	fig.tight_layout()
	return fig

	#plt.ion()
	#plt.show()
	#from IPython import embed; embed()

#from IPython import embed; embed()



plt.show()


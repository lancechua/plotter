import matplotlib.pyplot as plt
import numpy as np
import collections

class plotter:
	def __init__(self, x_min, x_max, step=1):
		self.domain = np.arange(x_min, x_max, step)

	def add_linfns(self, m_list, b_list):
		"""add linear functions as defined by their slopes and intercepts"""
		assert (isinstance(m_list, list) or isinstance(m_list, tuple)) \
			and (isinstance(b_list, list) or isinstance(b_list, tuple)), \
			'Please enter arguments as lists or tuples' 
		[plt.plot(self.domain, (lambda x: m * x + b)(self.domain)) for m, b in zip(m_list,b_list)]

	def add_fns(self, f_list):
		"""add any function; note order is not important now"""
		assert isinstance(f_list, collections.Iterable), 'Please enter argument as an iterable object' 
		[plt.plot(self.domain, f(self.domain)) for f in f_list] 

	def show(self):
		plt.show()

### --- SAMPLE USAGE --- ###
graph = plotter(1,50)
graph.add_linfns((10,20,30,40),[0,0,0,0])
graph.add_fns({lambda x: x ** 1.5, lambda x: x ** 2})
graph.show()
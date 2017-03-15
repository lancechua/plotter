import matplotlib.pyplot as plt
import numpy as np
import collections
import math

class plotter:
	def __init__(self, x_min, x_max, num=200):
		self.domain = np.linspace(x_min, x_max, num)

	def add_linfns(self, m_list, b_list):
		"""add linear functions as defined by their slopes and intercepts"""
		if not (isinstance(m_list, list) or isinstance(m_list, tuple)) and (isinstance(b_list, list) or isinstance(b_list, tuple)):
			raise Exception('Please enter arguments as lists or tuples')

		[plt.plot(self.domain, (lambda x: m * x + b)(self.domain)) for m, b in zip(m_list,b_list)]

	def add_fn(self, f, f_kwargs={} ):
		"""add a function, with optional keyword arguments in dict format.
		"""
		if not isinstance(f_kwargs, dict):
			raise Exception('f_kwargs must be a dictionary.')	
		f_param = lambda x: f(x, **f_kwargs)
		plt.plot(self.domain, [f_param(a) for a in self.domain])	

	def add_fns(self, f_list):
		"""add any function; note order is not important now
		functions are assumed to take in only x as a parameter; please specify coefficients in advance"""
		if not isinstance(f_list, collections.Iterable):
			raise Exception('Please enter argument as an iterable object') 
		[plt.plot(self.domain, [f(a) for a in self.domain]) for f in f_list] 

	def show(self):
		plt.show()

### --- SAMPLE USAGE --- ###
if __name__ == '__main__':
	def myfunc(x):
		return 100000/(1+math.exp(-x))

	def myf2(x,a):
		return x ** a

	graph = plotter(1,500)
	graph.add_linfns((10,20,30,40),[0,0,0,0])
	graph.add_fns([lambda x: x ** 1.5, lambda x: x ** 2, myfunc])
	graph.add_fn(myfunc)
	
	kwargs = {'a' : -0.5}
	graph.add_fn(myf2, kwargs)


	graph.show()
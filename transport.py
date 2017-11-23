import numpy as np
import time

from threading import Thread
from abc import ABCMeta, abstractmethod


class Transport(Thread):

	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self, name, delay, boundary, **gauss_parameters):
		Thread.__init__(self)
		self.name = name
		self.gauss_parameters = gauss_parameters
		self.delay = delay
		self.correction = 0.5
	
		self.orientation = np.random.uniform(-boundary, boundary)


class Plane(Transport):
	def __init__(self, name, delay, boundary, **gauss_parameters):
		Transport.__init__(self, name, delay, boundary, **gauss_parameters)
		
	def run(self):
		print 'Launched %s - orientation: %f' % (self.name, self.orientation)
		self.fly()
		print 'Stabilized %s' % (self.name)

	def fly(self):
		while True:
			time.sleep(self.delay)
			turbulation = np.random.normal(self.gauss_parameters['mu'], self.gauss_parameters['sigma'])
			self.orientation += turbulation
			self.orientation = self.orientation - self.correction if self.orientation > 0 else self.orientation + self.correction
			if abs(self.orientation) < 1.:
				break
			
	def __str__(self):
		return str(self.orientation)

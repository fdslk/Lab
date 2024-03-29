import numpy as np
import random
import fun.test_function as tf

class second_order_PSO():
	def __init__(self, pN, dim, max_iter):
		self.w = 0.8
		self.c1 = 2
		self.c2 = 2
		self.r1 = 0.6
		self.r2 = 0.3
		self.pN = pN
		self.dim = dim
		self.max_iter = max_iter
		self.X = np.zeros((self.pN, self.dim))
		self.V = np.zeros((self.pN, self.dim))
		self.pbest = np.zeros((self.pN, self.dim))
		self.gbest = np.zeros((1, self.dim))
		self.p_fit = np.zeros(self.pN)
		self.fit = 1e10 
		
	def init_Population(self):
		fun = tf.Test_fun()
		for i in range(self.pN):
			for j in range(self.dim):
				self.X[i][j] = random.uniform(0, 1)
				self.V[i][j] = random.uniform(0, 1)
			self.pbest[i] = self.X[i]
			tmp = fun.Sphere_function(self.X[i])
			self.p_fit[i] = tmp
			if(tmp < self.fit):
				self.fit = tmp
				self.gbest = self.X[i]
				
	def iterator(self):
		fitness = []
		fun = tf.Test_fun()
		for t in range(self.max_iter):
			tempX = np.zeros((1, self.dim))
			for i in range(len(tempX)):
				tempX[i] = random.uniform(0, 1)
			for i in range(self.pN):
				temp = fun.Sphere_function(self.X[i])
				if(temp < self.p_fit[i]):
					self.p_fit[i] = temp
					self.pbest[i] = self.X[i]
					if(self.p_fit[i] < self.fit):
						self.gbest = self.X[i]
						self.fit = self.p_fit[i]
			for i in range(self.pN):
				self.V[i] = self.w*self.V[i] + self.c1*self.r1*(self.pbest[i] - 2*self.X[i] + tempX)+\
							self.c2*self.r2*(self.gbest - 2*self.X[i] + tempX)
				tempX = self.X[i]
				self.X[i] = self.V[i] + self.X[i]
			fitness.append(self.fit)
			print(self.fit)
		return fitness
		
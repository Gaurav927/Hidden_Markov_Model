import numpy as np
class problem3:
	def __init__(self,emission,transition,observation,initial):
		self.emission = emission
		self.transition = transition
		self.observation = observation
		self.initial = initial
		self.T = len(self.observation)
		self.N = len(transition)
		self.M = len(emission)

	def compute_alpha(self):
		forward = np.zeros(shape=(self.N,self.T))
		N = len(self.transition)
		T = len(self.observation)

		for i in range(N):
			forward[i,0] = self.intial[i]*self.emission[i][self.observation[0]]

		prob =0.0

		for t in range(1,T):
			for j in range(N):
				sol =0.0
				for i in range(N):
					sol +=forward[i,t-1]*A[i][j]*B[j][observation[t]]
				forward[j,t] =sol

		for i in range(N):
			prob+=forward[i][T-1]

		return forward,prob
		

	def compute_beta(self):
		backward = np.zeros(shape=(len(self.N),len(self.T)))

		N = len(self.transition)
		T = len(self.observation)

		for i in range(N):
			backward[i][T-1] = 1.0

		for t in reversed(range(0,T-1)):
			for i in range(N):
				sol =0.0
				for j in range(N):
					sol +=backward[t+1][j]*self.transition[i][j]*self.emission[j][self.observation[t+1]]
				backward[t][i] = sol

		return backward

	def E_step(self):
		forward,prob = self.compute_alpha()
		backward = self.compute_beta()

		gamma = np.zeros(shape=(self.T,self.N))

		estimate =np.zeros(shape=(self.T,self.N,self.N))
        
        for t in range(self.T-1):
        	for i in range(self.N):
        		for j in range(self.N):
        			estimate[t,i,j] = (forward[i][t]*backward[j][self.observation[t+1]]*self.transition[i][j]*self.emission[j][self.observation[t+1]])/prob

        for t in range(self.T-1):
        	for i in range(self.N):
        		gamma[t][i] = (forward[i][t]*backward[i][t])/prob
        for i in range(self.N):
        	gamma[self.T-1][i] = forward[self.T-1][i]

		return gamma , estimate

	def M_step(self):
		gamma , estimate = self.E_step()

		for i in range(self.N):
			self.initial[i] = gamma[0,i]

		for i in range(self.N):
			for j in range(self.N):
				sol =0.0
				for t in range(self.T-1):
					sol += estimate[t,i,j]
				self.transition[i,j] = sol


		for i in range(self.N):
			denom = 0.0

			for t in range(self.T):
				denom+=gamma[t,i]

			for j in range(self.M):
				numer =0.0
				for t in range(self.T):
					if(self.obsevation[t]==j):
						numer +=gamma[t,i]
				self.emission[i][j] = numer/denom

	def initialize(self):
		for i in range(self.N):
			for j in range(self.N):
				self.transition[i][j] = 1.0/self.N

		for i in range(self.N):
			for j in range(self.M):
				self.emission[i][j] = 1.0/self.M

		for i in range(self.N):
			self.emission[i] = 1.0/self.N

	def train(self,num_iter):
		self.initialize()
		for epoch in range(num_iter):
			self.E_step()
			self.M_step()
		return self.initial ,self.transition,self.emission

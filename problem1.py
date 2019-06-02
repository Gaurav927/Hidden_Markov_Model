import numpy as np
def Solve_problem1(A,B,intial,observation):
	"""
	A: transition probablity matrix (N X N)
		aij represent probablity of transition from state i to state j
	B: Emission Matrix
		bij represent probablity of emitting jth observation state from ith
		hidden state
	intial = probablity of hidden state as being the first 

	Observation : Sequence of obsevation

	"""
	# forward[t][j] = P(o1,o2. . .ot,qt = j|λ)
	# forward[t][j] = sum(forward[t-1][i]*aij*bj(ot))

	forward = np.zeros(shape=(len(A),len(observation)))
	N = len(A)
	T = len(observation)

	for i in range(N):
		forward[i,0] = intial[i]*B[i][observation[0]]

	prob =0.0

	for t in range(1,T):
		for j in range(N):
			sol =0.0
			for i in range(N):
				sol +=forward[i,t-1]*A[i][j]*B[j][observation[t]]
			forward[j,t] =sol

	for i in range(N):
		prob+=forward[i][T-1]

	return prob

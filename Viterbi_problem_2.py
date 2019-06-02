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


	for t in range(1,T):
		for j in range(N):
			sol =0.0
			for i in range(N):
				sol +=forward[i,t-1]*A[i][j]*B[j][observation[t]]
			forward[j,t] =sol

	state = []

	for t in range(T):
		step =0
		maxi = -99

		for i in range(N):
			if(forward[t][i]>maxi):
				maxi = forward[t][i]
				step =i
		state.append(step)

	return state

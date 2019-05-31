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

	forward = [[0 for i in range(len(A))] for j in range(len(obsevation))]
	N = len(A)
	T = len(obsevation)

	for i in range(N):
		forward[i][0] = intial[i]*B[i][obsevation[0]]

	prob =0

	for t in range(1,T):
		for j in range(N):
			sol =0
			for i in range(N):
				sol +=forward[t-1][i]*A[i][j]*B[j][obsevation[t]]
			forward[t][j] =sol

	for i in range(N):
		prob+=forward[T-1][i]

	return prob


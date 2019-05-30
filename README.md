# Hidden_Markov_Model
HMM from scratch 

The example for implementing HMM is inspired from GeoLife Trajectory Dataset. The data consist of 180 users and their GPS data of during the stay of 4 years. After Data Cleaning and running some algorithms we got users and their place of interest with some probablity distribution i.e. transition probablity, observation probablity and instial state probablity distribution

The data is based on above condition
### Derivation of Equations
Let :

    Q = q1 q2 . . . qN a set of N states
        
    A = a11 . . . aij . . . aNN a transition probability matrix A, each aij representing the probability
                     Pij of moving from state i to state j, s.t.  N j=1 aij = 1 ∀i
                                        
    O = o1,o2,oT a sequence of T observations, each one drawn from a vocabulary V =v1 , v2 ,..., vV
        
    B = bi(ot) a sequence of observation likelihoods, also called emission probabili-ties, each expressing 
                     the probability of an observation ot being generated from a state i
                                        
    π = π1 , π2 , ..., πN an initial probability distribution over states. πi is the probability that the 
                      Markov chain will start in state i. Some states Pj may have πj = 0, 
                      meaning that they cannot be initial states. Also, ni=1 π i = 1
        
        
        

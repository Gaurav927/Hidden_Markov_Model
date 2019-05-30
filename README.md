# Hidden_Markov_Model
HMM from scratch 

The example for implementing HMM is inspired from GeoLife Trajectory Dataset. The data consist of 180 users and their GPS data during the stay of 4 years. After Data Cleaning and running some algorithms we got users and their place of interest with some probablity distribution i.e. transition probablity, observation probablity and instial state probablity distribution

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
        
        
        
We solve 3 types of problem in HMM

    Problem 1:
        Given the model λ = (A, B, π) and a sequence of observations O, find P (O | λ). Here, we
        want to determine a score for the observed sequence O with respect to the given model λ.
        
    Problem 2:
        Given λ = (A, B, π) and an observation sequence O, find an optimal state sequence for the
        underlying Markov process.
        
    Problem 3:
        Given an observation sequence O and the dimensions N and M , find the model λ = (A, B, π)
        that maximizes the probability of O.
#### Problem 1
Note that a given observation can be come from any of the hidden states that is we have N possiblity similiary <br />
a observation of length T can have total N <sup> T </sup> possible option each taking O(T) for computaion, therefore <br />
time complexity for the problem is O(TN<sup>T</sup>)


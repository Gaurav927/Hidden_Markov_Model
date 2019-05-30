# Hidden_Markov_Model
HMM from scratch 

The example for implementing HMM is inspired from GeoLife Trajectory Dataset. The data consist of 180 users and their GPS data of during the stay of 4 years. After Data Cleaning and running some algorithms we got users and their place of interest with some probablity distribution i.e. transition probablity, observation probablity and instial state probablity distribution

I am just assuming some data based on the above condition.

Let :

        T = length of the observation sequence
        N = number of states in the model
        M = number of observation symbols
        Q = {q0; q1; : : : ; qN−1} = distinct states of the Markov process
        V = {0; 1; : : : ; M − 1} = set of possible observations
        A = state transition probabilities
        B = observation probability matrix
        π = initial state distribution
        O = (O0; O1; : : : ; OT −1) = observation sequence
        
        



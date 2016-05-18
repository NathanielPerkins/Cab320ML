#!/usr/bin/env python

# Solutions to Chris McCool Prac

# Created on the 11th May by f.maire@qut.edu.au

import pickle
import numpy as np


#### Load the data
fp            = open('two_cluster_example.pickle','r')
(X1,X2)       = pickle.load(fp);
fp.close();

# X1 and X2 are points of two clusters
X = np.vstack((X1, X2))

# Shuffle the rows
np.random.shuffle(X)

# X  = X[:5,:]  # debug

#### Set the initial guess for the cluster centers 
C  = np.array([[-2.,0.],[1.,-1]])


# will stop when the centers move less than this threshold
change_thr = 0.001

N = X.shape[0] # number of examples in the data set

R = np.zeros((N,2)) # membership
# R[i] is the cluster index of ith element 

while True:
    # E-step

    # compute the distance to center 0
    d0 = C[0]-X
    sd0 = np.sum(d0*d0,1)  # sum along axis 1
    sd0 = sd0.reshape((N,1)) # ensure sd0 is 2D

    # compute the distance to center 1
    d1 = C[1]-X
    sd1 = np.sum(d1*d1,1)
    sd1 = sd1.reshape((N,1))    
    #print 'sd1 = ', sd1 # debug

    D = np.hstack( (sd0,sd1) )
    # D is 2 by N
    
    R = np.argmin(D,axis=1)
    # R[i] is the index of the cluster of the ith input

    # M-step

    # recompute the centers of the clusters
    C0 = np.sum((1-R).reshape(N,1)*X,axis=0) /(1e-6+np.sum(1-R))
    C1 = np.sum(R.reshape(N,1)*X,axis=0) /(1e-6+np.sum(R))
    

    # measure how much the centers have moved
    change = np.sum(np.abs(C[0]-C0)+np.abs(C[1]-C1))
    print change

    C[0] = C0
    C[1] = C1
    print C 

    if change<change_thr:
        break
    #print C0

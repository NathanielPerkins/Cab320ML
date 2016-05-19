import numpy as np
import time
import matplotlib

def computeNeuron(x,w):
    assert x.shape == w.shape
    assert not np.isnan(w).any()
    return np.sign(np.dot(x,w))

def train(training,w=None):
    print "Entered train"
    if w is None:
        w = np.zeros(len(training[0])-1)
    trained = False
    iteration = 0
    while not trained:
        count = 0
        trained = True
        np.random.shuffle(training)
        for row in training:
            y = computeNeuron(row[0:len(row)-1],w)
            if y != np.sign(row[-1]): #check that output is the same as expected
                trained = False
                w = np.add(w,row[-1]*row[:-1])
            else:
                count += 1
        w = w/max(w) #normalize weights
        iteration += 1
    return w

f = open('iris.txt', 'r')
x = f.read().split()
x = [float(a) for a in x]
x = np.array(x)
x = x.reshape((100,5))
np.random.shuffle(x)

test = np.zeros((20,5))
training = np.zeros((80,6))
for i in range(20):
    test[i] = x[i]
for i in range(20,100):
    training[i-20] = np.hstack((1,x[i]))
assert training.shape == (80,6)

w = train(training)

xMax = np.amax(x[1:3])
print xMax
print xLine

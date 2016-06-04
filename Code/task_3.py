'''
Determine the information gain of each attribute, then use that information
to traverse the tree at each decision using the most information
Relevant information:
H((P(-),P(+))) = -P(-)*log(P(-)) - P(+)*log(P(+))

Entropy Calcualtion check challenge 2 in week 12 prac
'''
import math  # will need for log and entropy


def testFullDataEntropy():
    data1 = [[1, 2, 0], [1, 2, 1], [1, 3, 0]]
    attribute_types1 = [1, 2, 2]
    Hp1 = entropy(2, 3) + entropy(1, 3)
    print "Test Hp1 = ",
    print Hp1 == fullDataEntropy(data1, attribute_types1)
    data2 = [[1, 0], [1, 1], [1, 0], [1, 1], [1, 2]]
    attribute_types2 = [1, 2, 3]
    Hp2 = entropy(2, 5) + entropy(2, 5) + entropy(1, 5)
    print "Test Hp2 = ",
    print Hp2 == fullDataEntropy(data2, attribute_types2)


def entropy(x, total):
    return -float(x)/(total)*math.log(float(x)/total)


def fullDataEntropy(data, attribute_types):
    '''
    Caclulate and return the entropy of the data set, assume the last attribute
    is the class attribute.
    Return: Float, Entropy of data set.
    '''
    total = 0
    P = [0 for x in xrange(attribute_types[-1])]
    for row in data:
        for x in xrange(attribute_types[-1]):
            if row[-1] is x:
                P[x] += 1
                total += 1
    Hp = 0
    for x in xrange(attribute_types[-1]):
        Hp += entropy(P[x], total)
    return Hp

testFullDataEntropy()

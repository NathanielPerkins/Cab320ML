'''
Determine the information gain of each attribute, then use that information
to traverse the tree at each decision using the most information
Relevant information:
H((P(-),P(+))) = -P(-)*log(P(-)) - P(+)*log(P(+))

Entropy Calcualtion check challenge 2 in week 12 prac
'''
import math  # will need for log and entropy


def testFullDataEntropy():
    '''
    Test function for collecting the full entropy of data, only considering
    the last element, the class attribute
    '''
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
    '''
    Calculates and returns the entropy of a probability.
    x = frequency of occurence in dataset
    total = total number of entries
    return: x/total * log_2(x/total)
    '''
    if x == 0:  # division by 0 error if not implemented
        return 0
    else:
        return -float(x)/(total)*math.log(float(x)/total, 2)


# yes, no for particular attribute value
def E(row):
    '''
    Computes and returns the entropy of the row
    row = row of data
    return summation of entropy of every value of row
    '''
    total = sum(row)
    e_value = 0
    for value in row:
        e_value += entropy(value, total)
    return e_value


# yes, no for all attribute's values
def P(valueCount, totalAttributeCount):
    '''
    Computes and returns the probabilty in float form
    valueCount = discrete number of occurences of element
    totalAttributeCount = total number of all elements in an attribute_types
    returns float value of valueCount/totalAttributeCount
    '''
    return float(valueCount)/float(totalAttributeCount)


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


# Sorts data into useable form
def conditionalSummary(attribute, dataset):
    summary = []
    conditionalSet = zip(zip(*dataset)[attribute], zip(*dataset)[-1])
    attributeArray = splitAttribute(conditionalSet)
    for i in range(len(attributeArray)):
        temp = []
        values = zip(*attributeArray[i])[-1]
        temp.append(values.count(0))
        temp.append(values.count(1))
        summary.append(temp)
    return summary


# Split a dataset pair (2 columns) by the number of unique attributes
def splitAttribute(dataset):
    attributeSet = zip(*dataset)[0]
    uniqueAttributes = list(set(attributeSet))
    numUnique = len(set(attributeSet))

    final = []
    for i in range(numUnique):
        temp = []
        for row in dataset:
            if row[0] == uniqueAttributes[i]:
                temp.append(row)
        final.append(temp)
    return final


def conditionalEntropy(dataset):
    ce = 0  # conditional Entropy
    totalAtt = sum([sum(row) for row in dataset])
    for row in dataset:
        ce += P(sum(row), totalAtt)*E(row)
    return ce


# Information Gain for given attribute
def gain(attribute, dataset):
    conditionalSet = zip(zip(*dataset)[attribute], zip(*dataset)[-1])

    classValues = [sum(zip(*conditionalSet)[0]), sum(zip(*conditionalSet)[1])]
    ce = conditionalEntropy(dataset)
    return E(classValues)-ce


def ID3(examples, target_Attributes, attributes):
    '''
    Attempted implmentation of ID3 algorithm. Psuedocode included below
    '''
    root = {}
    return root


myData = [[0, 0, 0],
          [1, 0, 1],
          [0, 0, 0],
          [0, 0, 0],
          [0, 1, 1],
          [1, 0, 0],
          [0, 1, 0],
          [0, 1, 1],
          [1, 0, 0],
          [1, 0, 0]]

theirData = [[0, 1],
             [0, 1],
             [0, 1],
             [0, 0],
             [0, 0],
             [1, 1],
             [1, 1],
             [1, 1],
             [1, 1],
             [2, 1],
             [2, 1],
             [2, 0],
             [2, 0],
             [2, 0]]

# testFullDataEntropy()
# data = [[3,2],[4,0],[2,3]]
data = [[3, 1], [4, 2]]

ce1 = conditionalEntropy(data)

print ce1

sortedData = conditionalSummary(1, myData)
print sortedData

ce2 = conditionalEntropy(sortedData)
print ce2

print gain(0, sortedData)

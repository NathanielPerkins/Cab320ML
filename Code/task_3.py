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


def classAttributeSummary(attribute, dataset):
    '''
    Given a dataset of discrete values, a list summary for a certain
    attribute and its relation to the class variable is returned.
    Basically an attribute is split up into its discrete values
    and for each unique value, the number of class successes and
    fails are counted. With the data in this form, it makes it
    easier to calculate probabilties and entropies.
    Input:
        attribute: The attribute's index, being summarised
        dataset: Dataset of discrete values
    Output:
        2D arrray summarising the number of class value pass/fails
        for each unqiue discrete value.
    '''
    summary = []
    attributeColumn = zip(*dataset)[attribute]
    classColumn =  zip(*dataset)[-1]

    classAttributeSet = zip(attributeColumn,classColumn)
    attributesArray = splitAttributes(classAttributeSet)

    for i in range(len(attributesArray)):
        discreteValue = []
        #  Get the list of class pass/fails for a particular attribute
        values = zip(*attributesArray[i])[-1]
    
        discreteValue.append(values.count(0))  # Count number of 0's(fail)
        discreteValue.append(values.count(1))  # Count number of 1's (pass)
        summary.append(discreteValue)
    return summary


# Split a dataset pair (2 columns) by the number of unique attributes
def splitAttributes(attribute_summary):
    '''
    When given a paired attribute summary dataset, this function
    will return a list the data split up by all the unique values
    from the attributes column. So for simple attribute types with
    a binary value, the dataset is split into 2. For more complex
    attributes with 3 or more, it will return an array with lots
    of splits equal to the number of unique values for that
    attribute.
    Input:
        attribute_summary: Output from classAttributeSummary
    Output:
        2D array of split data by unqiue attribute values
    '''
    attributeSet = zip(*attribute_summary)[0]

    # List of all unique attribute values
    uniqueAttributes = list(set(attributeSet))
    numUnique = len(set(attributeSet)) # Count of this list

    splits = []
    for i in range(numUnique):
        splitData = []
        for row in attribute_summary:
            #Loop through dataset and save only rows with
            #a particular attribute value
            if row[0] == uniqueAttributes[i]:
                splitData.append(row)
        splits.append(splitData)
    return splits


def classAttributeEntropy(attribute_summary):
    '''
    Calculates the entropy for the class attribute pair. Simply
    the entropy for the class value given a certain attribute.
    For each row in the data the probability and entropy is
    calculated and added to the total.
    Input:
        attribute_summary: Output from classAttributeSummary
    Output:
        Class attribute entropy for the given data.
    '''
    ce = 0  # class attribute entropy
    totalAttributeCount = sum([sum(row) for row in attribute_summary])
    for row in attribute_summary:
        ce += P(sum(row), totalAttributeCount)*E(row)
    return ce



def informationGain(attribute_summary):
    '''
    Calculate the information gain for a given attribute.
    By calculating the class attribute entropy and subtracting
    that from the entropy for the class values, the information
    gain for the attribute can be calculated
    Input:
        attribute_summary: Output from classAttributeSummary
    Output:
        Information gain for given data      
    '''
    attributeColumn = zip(*attribute_summary)[0]
    classColumn =  zip(*attribute_summary)[-1]

    classAttributeSet = zip(attributeColumn,classColumn)
 
    classValues = [sum(zip(*classAttributeSet)[0]),
                   sum(zip(*classAttributeSet)[1])]
    ce = classAttributeEntropy(attribute_summary)
    return E(classValues)-ce


def ID3(examples, target_Attributes, attributes):
    '''
    Attempted implmentation of ID3 algorithm. Psuedocode included below
    '''
    root = {}
    return root



if __name__ == "__main__":
    # Dataset can be simplified down to success count
    # pairs for a given attribute

    # Expected output of classAttributeSummary
    simplifiedDataset1A1 = [[3, 1], [4, 2]]
    dataset1 = [[0, 0, 0],
               [1, 0, 1],
               [0, 0, 0],
               [0, 0, 0],
               [0, 1, 1],
               [1, 0, 0],
               [0, 1, 0],
               [0, 1, 1],
               [1, 0, 0],
               [1, 0, 0]]

    # Expected output of classAttributeSummary
    simplifiedDataset2 = [[2,3],[0,4],[3,2]]
    dataset2 =  [[0, 1],
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



    sortedDataset1 = classAttributeSummary(0, dataset1)
    print 'Sorted Dataset 1:',sortedDataset1
    print 'Expected Dataset 1:',simplifiedDataset1A1
    print 'Class Entropy: ',classAttributeEntropy(sortedDataset1)
    print 'Information Gain: ',informationGain(sortedDataset1)
    print '\n'

    sortedDataset2 = classAttributeSummary(0, dataset2)
    print 'Sorted Dataset 2:',sortedDataset2
    print 'Expected Dataset 2:',simplifiedDataset2
    print 'Class Entropy: ',classAttributeEntropy(sortedDataset2)
    print 'Information Gain: ',informationGain(sortedDataset2)

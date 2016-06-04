from task_1 import *
import math

'''
Things to note:
need to find the following
P(a1:+)*P(a2:+)...*P(a15:+)*P(+)
P(a1:-)*P(a2:-)...*P(a15:-)*P(-)
where a1-15 are the attributes, and +/- are the outcome.
Whichever of the above 2 equations is the prediction
for continuous attributes, need to either discretize it if it's linearly
distributed or use a probability function if non linearly distributed
calculate the mean and variance of data, then convert new data point to
probability with that
'''


def getProbabilities(test_data, summaries):
    '''
    This function gets the probabilities of each element occuring given a data
    set. For instance, given a data set of type [A1... An], where A1 can take
    the following values, 'a' and 'b'. If 'a' occurs k times, and 'b' occurs j
    times, the probability of 'a' occuring is k/(j+k). If An takes a continous
    value, the mean and variance need to be inputted for that type, and the
    guassian probability density function is calculated to return that
    probability. Returns a list of probabilities corresponding to each element.
    Eg, if A1 has 2 possible values,
    Return = [prob(A1_1), prob(A1_2),
              prob(A2_1)... prob(A2_numAttributes)),
              ...
              prob(An_1)...prob(An_numAttributes)]
    '''
    probabilities = ([],[])
    for i in range(len(summaries)):
        classSummary = summaries[i]["Statistics"]
        classLength = summaries[i]["Length"]
        for row in test_data:  # Loop through each row in data
            testProb = 1  # Initialise probability to 1
            for j in range(len(classSummary)):  # Loop through each attribute
                if(mapping[j] == {}):  # Continuous attribute
                   mean = classSummary[j]["Mean"]
                   std = classSummary[j]["StdDev"]
                   testProb *= contProbability(row[j],mean,std)
                else:   # Discrete attribute
                   testProb *= discreteProbability(row[j],classSummary[j],classLength)
            probabilities[i].append(testProb)
    return probabilities


def makePredictions(test_data, summaries):
    '''
    Makes predictions about the test data by getting the highest probability
    between the class values. Whichever class value has the highest probabbility
    will be the prediction for that test data.
    Input:
        test_data: The data which will be predicted on.
        summaries: a summary of the stastics for the training data
    Output:
        predictions: a list of predictions for all test data.
    '''
    p = getProbabilities(test_data, summaries)
   
    predictions = []  # Initialise predictions list
    for i in range(len(p[0])):  # Loop through all probabilities
        bestProbability = -1
        bestClass = -1
        for j in range(len(p)):  # For each class value
            # Find greatest probability between different classes
            if(p[j][i] > bestProbability):  
                bestProbability = p[j][i]
                bestClass = j
        predictions.append(bestClass)
    return predictions



def determineAccuracy(predictions, test_data):
    '''
    Given the predictions made and the test_data, the accuracy of the classifier
    will be returned. 
    Input:
        predictions: List of preditions for the corresponding data.
        test_data: The data that was predicted upon.
    Output:
        Accuracy: The accuracy precentage of the classifer.
    '''
    numCorrect = 0
    for i in range(len(test_data)):
        if test_data[i][-1] == predictions[i]:
            numCorrect += 1
    return (numCorrect/float(len(test_data))) * 100.0

    
def dataSummary(dataset):
    '''
    Creates a dictionary summary of the dataset for use in calcuating
    probabilities and making predictions.
    '''
    summary = {'Length':len(dataset)}
    stats_summary = []
    for i in range(len(mapping)-1):  # Loop through attributes, minus last
        if(mapping[i] == {}):  # Continuous attribute
            values = zip(*dataset)[i]
            mean = np.mean(values)
            std = np.std(values)
            stats_summary.append({"Mean":mean,"StdDev":std})
        else:  # Discrete attribute
            discreteSummary = []  # Initialise list
            for j in range(len(mapping[i])):
                discreteSummary.append(zip(*dataset)[i].count(j))
            stats_summary.append(discreteSummary)

    summary["Statistics"] = stats_summary
    return summary
        

def classDataSummaries(train_data):
    '''
    Splits data by class and returns the dataset summaries for both class values.
    Input:
        train_data: Training data to be summarised
    Output:
        summaries of the data split by class
    '''
    classData = splitByClass(train_data)
    print "\nLength of class 0:",len(classData[0])
    print "Length of class 1:",len(classData[1])
    return tuple((dataSummary(classData[0]),dataSummary(classData[1])))



def contProbability(X, mean, std):
    '''
    Computes the guassian probability of a continous variable given a mean and
    variance. Returns the probability of value x happening.
    '''
    if(mean == 0 or std == 0):  # If either mean or std is 0, probability 0.
        return 0
    else:
        exponent = math.exp(-(math.pow(X-mean,2)/(2*math.pow(std,2))))
        return (1 / (math.sqrt(2*math.pi) * std)) * exponent




def discreteProbability(X, discreteSummary, length):
    '''
    Computes the probability of a discrete variable given a summary
    of the attribute, with counts of all possible values.
    Returns the probability of value x happening.
    '''
    return float(discreteSummary[int(X)])/float(length)

    

def splitByClass(dataset):
    '''
    Splits the dataset by its class variables.
    Returns a tuple of the two split datasets.
    '''
    class0 = []
    class1 = []
    for row in dataset:
        if row[-1] == 0:
            class0.append(row)
        elif row[-1] == 1:
            class1.append(row)
    return tuple((class0,class1))




if __name__ == "__main__":
    splitRatio = 0.8 #  Define the split of training data to testing data

    filename, ndtype, mapping, attribute_type = setup_task_1()
    loaded_data = loadData(filename, ndtype, mapping, attribute_type)
    
    #  Randomise and split into two datasets
    train_data, test_data = splitDataSets(loaded_data,splitRatio)
    #train_data = train_data[:50]
    #test_data = test_data[:50]
    print "Length of Test Data:",len(test_data)
    print "Length of Train Data:",len(train_data)

    # Create Summary of training data split by class
    summaries = classDataSummaries(train_data)

    #  Make predictions about test data and report its accuracy
    test_predictions = makePredictions(test_data, summaries)
    test_accuracy = determineAccuracy(test_predictions,test_data)
    print "\nAccuracy of Test Data Classification:",test_accuracy
    print "Error of Test Data Classification:",100-test_accuracy
    
    #  Make predictions about test data and report its accuracy
    train_predictions = makePredictions(train_data, summaries)
    train_accuracy = determineAccuracy(train_predictions, train_data)
    print "\nAccuracy of Training Data Classification:",train_accuracy
    print "Error of Training Data Classification:",100-train_accuracy
    
##    mapping = [{}, {'+': 0, '-': 1}] 
##    summaries = ({'Length':1, 'Statistics':[{"Mean":1, "StdDev":0.5}]},
##                 {'Length':1, 'Statistics':[{"Mean":20, "StdDev":5.0}]})
##    inputVector = [[1.1, '?']]   
##    p = getProbabilities(inputVector, summaries)
    
    

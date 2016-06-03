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
    times, the probabilit of 'a' occuring is k/(j+k). If An takes a continous
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
        for row in test_data:
            testProb = 1
            for j in range(len(classSummary)):
                if(mapping[j] == {}):  # Continuous
                   mean = classSummary[j]["Mean"]
                   std = classSummary[j]["StdDev"]
                   testProb *= contProbability(row[j],mean,std)
                else:
                   testProb *= discreteProbability(row[j],classSummary[j],classLength)
            probabilities[i].append(testProb)
    return probabilities


def makePredictions(test_data, summaries):
    p = getProbabilities(test_data, summaries)
   
    predictions = []
    for i in range(len(p[0])):  # Loop through all probabilities
        bestProbability = -1
        bestClass = -1
        for j in range(len(p)):  # For each class value
            if(p[j][i] > bestProbability):
                bestProbability = p[j][i]
                bestClass = j
        predictions.append(bestClass)
    return predictions


#Straight copy pasted for quick testing
def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
    
def dataSummary(dataset):
    summary = {'Length':len(dataset)}
    stats_summary = []
    for i in range(len(mapping)-1):
        if(mapping[i] == {}):  # Continuous
            values = zip(*dataset)[i]
            mean = np.mean(values)
            std = np.std(values)
            stats_summary.append({"Mean":mean,"StdDev":std})
        else:  # Discrete
            discreteSummary = []
            for j in range(len(mapping[i])):
                discreteSummary.append(zip(*dataset)[i].count(j))
            stats_summary.append(discreteSummary)

    summary["Statistics"] = stats_summary
    return summary
        

def classDataSummaries(train_data):
    classData = splitByClass(train_data)
    print "\nLength of class 0:",len(classData[0])
    print "Length of class 1:",len(classData[1])
    return tuple((dataSummary(classData[0]),dataSummary(classData[1])))

#Issue with dividing by 0
def contProbability(X, mean, std):
    '''
    Computes the guassian probability of a continous variable given a mean and
    variance. Returns the probability of value x happening.
    '''
    exponent = math.exp(-(math.pow(X-mean,2)/(2*math.pow(std,2))))
    return (1 / (math.sqrt(2*math.pi) * std)) * exponent

def discreteProbability(X, discreteSummary, length):
    return float(discreteSummary[int(X)])/float(length)
    
    


def splitByClass(dataset):
    class0 = []
    class1 = []
    for row in dataset:
        if row[-1] == 0:
            class0.append(row)
        elif row[-1] == 1:
            class1.append(row)
    return tuple((class0,class1))






if __name__ == "__main__":
    splitRatio = 0.8

    
    loaded_data = test_loadData()
    
    train_data, test_data = splitDataSets(loaded_data,splitRatio)
    print "Length of Test Data:",len(test_data)
    print "Length of Train Data:",len(train_data)
    
    summaries = classDataSummaries(train_data)
    predictions = makePredictions(test_data, summaries)

    accuracy = getAccuracy(test_data, predictions)

    print "\nAccuracy of Classification:",accuracy
    
##    mapping = [{}, {'+': 0, '-': 1}] 
##    summaries = ({'Length':1, 'Statistics':[{"Mean":1, "StdDev":0.5}]},
##                 {'Length':1, 'Statistics':[{"Mean":20, "StdDev":5.0}]})
##    inputVector = [[1.1, '?']]
    
##    p = getProbabilities(inputVector, summaries)
    
    


    #pass_summary = summarise(pass_data)

import numpy as np
from StringIO import StringIO
import time
def mapData(mapping,data,averages):
    '''
    Takes some input data, a mapping table and row averages and returns a 2d
    array of data that has been mapped to new values, and any missing values
    replaced with the average of each element, row wise
    In:
    mapping: List of dictionaries corresponding to each row element of data
    data: 2d List or numpy array of data, with each row being a seperate instance
    of collected results
    averages: the average element of each element in a row.
    Out:
    data: 2d list of processed data, with all values mapped to new values, and
    all missing data replaced with averages
    '''
    data = list(data)
    for i in range(len(data)):
        if data[i] == '?':
            data[i] = averages[i]
        if mapping[i] != {}:
            data[i] = mapping[i][data[i]]
    return data

def getAverages(data,mapping):
    '''
    WORK IN PROGRESS: Continous variables appear to be working, nominal needs more
    testing as not sure if working correctly
    In:
    data: 2d list of data, each row represents seperate instance of variables
    mapping: mapping function from collected data to integers for nominal variables
    Out:
    aveData: return a row vector, with each element corresponding to the average results
    of the entire data for each element. If the variable in data is continious,
    returns the mean of the data. Else if the variable is nominal, it returns the
    most occuring element.
    '''
    aveData = []
    x,y = len(data),len(data[0])
    assert type(x) is int
    assert type(y) is int
    assert y == len(mapping)
    for i in range(y): # for every row element
        count = 0.0 #used for continous variable
        aveC = 0 #used for continious variable
        currentAve = [0 for a in mapping[i]]
        for j in range(x): # every element i of every instance of data, get average of that column
            if data[j][i] != '?':
                if mapping[i] == {}: #means it's continuous variable
                    aveC += data[j][i]
                    count += 1.0
                else: #else it's a nominal variable and counts each instance seperately
                    assert data[j][i] in mapping[i]
                    currentAve[mapping[i][data[j][i]]] += 1
        print "Current Average for element ",i,
        print currentAve
        if mapping[i] == {}: #if the value was a continoues one, calculate the mean
            aveC = aveC/count
            aveData.append(aveC)
        else: # If the variable was nominal, take the largest
            index = currentAve.index(max(currentAve))
            largest = currentAve[0]

            # for k in range(1,len(currentAve)-1):
            #     if currentAve[k] > largest:
            #         largest = k
            #         index = k
            aveData.append(index)
    return aveData
def processData(ndtype,tdtype,relation,filename):
    '''
    WORK IN PROGRESS
    '''
    array = np.genfromtxt(filename,dtype=ndtype,delimiter=',')
    NUM_ATTRIBUTES = len(ndtype)
    processed = np.zeros((NUM_ATTRIBUTES,len(array)),dtype=ndtype)

    proper = True
    for line in array:
        temp = list(line)
        end = len(temp) - 1
        if temp[end] not in ['+','-'] or end+1 is not NUM_ATTRIBUTES:
            proper = False
    assert proper

    data = np.zeros((1,16),dtype=tdtype)
    print data.dtype
    i = 0
    for char in temp:
        data[i] = char
        i+=1
    print data

'''
NEEDED SETUP: DO NOT REMOVE ----------------------------------------------------
For clarification look into dtype in numpy: [('Item1 Name','Item1 type')...], used
for reading in the data from numpy to tell it that each element has a different
type
'''
ndtype  = [('A1','S1'),('A2','f4'),('A3','f4'),('A4','S2'),('A5','S2'),('A6','S2'),('A7','S2'),('A8','f4'),('A9','S1')]
ndtype += [('A10','S1'),('A11','f4'),('A12','S1'),('A13','S1'),('A14','f4'),('A15','f4'),('A16','S1')]

tdtype = [('a','i2'),('b','f4'),('c','f4'),('d','i2'),('e','i2'),('f','i2'),('g','i2'),('h','f4'),('i','i2')]
tdtype += [('j','i2'),('k','f4'),('l','i2'),('m','i2'),('n','f4'),('o','f4'),('p','i2')]
#list of dictionaries mapping[0] corresponds to possible values in data[all][0] etc
mapping = [{'b':0,'a':1},
           {},
           {},
           {'u':0,'y':1,'l':2,'t':3},
           {'g':0,'p':1,'gg':2},
           {'c':0,'d':1,'cc':2,'i':3,'j':4,'k':5,'m':6,'r':7,'q':8,'w':9,'x':10,'e':11,'aa':12,'ff':13},
           {'v':0,'h':1,'bb':2,'j':3,'n':4,'z':5,'dd':6,'ff':7,'o':8},
           {},
           {'t':0,'f':1},
           {'t':0,'f':1},
           {},
           {'t':0,'f':1},
           {'g':0,'p':1,'s':2},
           {},
           {},
           {'+':0,'-':1}]
#-------------------------------------------------------------------------------
array = np.genfromtxt('records.txt',dtype=ndtype,delimiter=',')

# print array.shape
temp = []
temp = [list(line) for line in array]
for line in temp[0:4]:
    print line
ave = getAverages(temp[0:4],mapping)
print ave

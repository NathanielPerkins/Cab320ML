import numpy as np
import math
import csv


def test_loadData():
    filename = 'records.txt'
    ndtype = [('A1', 'S1'), ('A2', 'f8'), ('A3', 'f8'), ('A4', 'S1'),
              ('A5', 'S2'),
              ('A6', 'S2'), ('A7', 'S2'), ('A8', 'f8'), ('A9', 'S1'),
              ('A10', 'S1'), ('A11', 'f8'), ('A12', 'S1'), ('A13', 'S1'),
              ('A14', 'f8'), ('A15', 'f8'), ('A16', 'S1')]
    mapping = [{'b': 0, 'a': 1},
               {},
               {},
               {'u': 0, 'y': 1, 'l': 2, 't': 3},
               {'g': 0, 'p': 1, 'gg': 2},
               {'c': 0, 'd': 1, 'cc': 2, 'i': 3, 'j': 4, 'k': 5, 'm': 6,
                'r': 7,
                'q': 8, 'w': 9, 'x': 10, 'e': 11, 'aa': 12, 'ff': 13},
               {'v': 0, 'h': 1, 'bb': 2, 'j': 3, 'n': 4, 'z': 5, 'dd': 6,
               'ff': 7, 'o': 8},
               {},
               {'t': 0, 'f': 1},
               {'t': 0, 'f': 1},
               {},
               {'t': 0, 'f': 1},
               {'g': 0, 'p': 1, 's': 2},
               {},
               {},
               {'+': 0, '-': 1}]
    attribute_type = []
    for line in mapping:
        if line != {}:
            attribute_type.append(len(line))
        else:
            attribute_type.append(-1)
    # attribute_type = np.array(attribute_type)
    return np.array(loadData(filename, ndtype, mapping, attribute_type))


def loadData(filename, ndtype, mapping, attribute_type):

    data = np.genfromtxt(filename, dtype=ndtype, delimiter=',')

    data = [list(line) for line in data]

    averages = getAverages(data, mapping, attribute_type)

    return mapData(mapping, data, averages)


def test_mapData():
    '''
    Tests the mapData function for accuracy with expected results given a
    known set of inputs
    '''
    # partial mapping partial unknown
    test1D = [['?', 2, '?', 'zz'], ['a', '?', 4.2, '?']]
    test1M = [{'b': 0, 'a': 1}, {}, {}, {'zz': 6, 'tz': 17}]
    test1A = ['b', 13, 6.5, 'tz']
    test1E = [[0, 2, 6.5, 6], [1, 13, 4.2, 17]]
    test1R = mapData(test1M, test1D, test1A)
    # full mapping all unknown
    test2D = [['?', '?', '?', '?'], ['?', '?', '?', '?']]
    test2M = [{'b': 0, 'a': 1}, {'b': 0, 'a': -1}, {'b': 73}, {'tz': 17}]
    test2A = ['b', 'a', 'b', 'tz']
    test2E = [[0, -1, 73, 17], [0, -1, 73, 17]]
    test2R = mapData(test2M, test2D, test2A)
    # No mapping
    test3D = [[1, 2, 3, 4], [5, 6, 7, 8]]
    test3M = [{}, {}, {}, {}]
    test3A = [1, 2, 3, 4]
    test3E = [[1, 2, 3, 4], [5, 6, 7, 8]]
    test3R = mapData(test3M, test3D, test3A)
    # data contains NaN
    test4D = [[np.nan, 2, 3, np.nan], [5, 6, 7, 8]]
    test4M = [{}, {}, {}, {}]
    test4A = [-5, 2, 3, -1]
    test4E = [[-5, 2, 3, -1], [5, 6, 7, 8]]
    test4R = mapData(test4M, test4D, test4A)

    print "Test 1: ", test1R == test1E
    print "Test 2: ", test2R == test2E
    print "Test 3: ", test3R == test3E
    print "Test 4: ", test4R == test4E


def mapData(mapping, data, averages):
    '''
    Takes some input data, a mapping table and row averages and returns a 2d
    array of data that has been mapped to new values, and any missing values
    replaced with the average of each element, row wise
    In:
    mapping: List of dictionaries corresponding to each row element of data
    data: 2d List or numpy array of data, with each row being a seperate
    instance of collected results. # of rows >= 2
    averages: the average element of each element in a row.
    Out:
    data: 2d list of processed data, with all values mapped to new values, and
    all missing data replaced with averages
    '''
    mapped = []
    count = 0
    for row in data:
        for i in xrange(len(row)):
            try:
                if(np.isnan(row[i])):  # continuous (?)
                    row[i] = averages[i]
            except:
                if row[i] == '?':  # discrete (?)
                    row[i] = averages[i]
                    continue  # continues through for loop if it was a (?)
            if(mapping[i] != {}):
                row[i] = mapping[i][row[i]]

        mapped.append(row)
        count += 1
    return mapped


def splitDataSets(data,splitRatio):
    '''
    Shuffles the input data and splits the shuffled data into two arrays
    of different lengths dependent on the ratio of train data to test data.
    In:
    data: 2d list of data, each row represents seperate instance of variables
    mapping: mapping function from collected data to integers for nominal
    variables
    Out:
    train_data: set of data for training purposes
    test_data: set of data for testing purposes
    '''
    N = len(data)

    trainDataLength = int(round(N*splitRatio))

    np.random.shuffle(data)

    return data[:trainDataLength], data[trainDataLength:]


def getAverages(data, mapping, attribute_type):
    '''
    WORK IN PROGRESS: Continous variables appear to be working, nominal needs
    more testing as not sure if working correctly
    In:
    data: 2d list of data, each row represents seperate instance of variables
    mapping: mapping function from collected data to integers for nominal
    variables Out:
    aveData: return a row vector, with each element corresponding to the
    average results of the entire data for each element. If the variable in
    data is continious,returns the mean of the data. Else if the variable is
    nominal, it returns the most occuring element.
    '''
    aveData = []
    x, y = len(data), len(data[0])
    assert type(x) is int
    assert type(y) is int
    assert y == len(mapping)
    for i in xrange(y):  # for every row element
        count = 0.0  # used for continous variable
        aveC = 0  # used for continious variable
        currentAve = [0 for a in mapping[i]]
        for j in xrange(x):  # get average of column i of data
            if attribute_type[i] == -1:  # -1 indicates continuous variable
                if not math.isnan(data[j][i]):
                    aveC += data[j][i]
                    count += 1.0
            else:  # else it's a nominal value and need to count each instance
                if data[j][i] != '?':
                    assert data[j][i] in mapping[i]
                    currentAve[mapping[i][data[j][i]]] += 1

        if mapping[i] == {}:  # if value was continuous, calculate mean
            assert count > 0
            aveC = aveC/count
            aveData.append(aveC)
        else:  # If the variable was nominal, take the largest
            index = currentAve.index(max(currentAve))
            aveData.append(index)
    return aveData


def processData(ndtype, relation, attribute_type, filename):
    '''
    WORK IN PROGRESS
    '''
    array = np.genfromtxt(filename, dtype=ndtype, delimiter=',')
    NUM_ATTRIBUTES = len(ndtype)
    # processed = np.zeros((NUM_ATTRIBUTES, len(array)), dtype=ndtype)
    proper = True
    for line in array:
        temp = list(line)
        end = len(temp) - 1
        if temp[end] not in ['+', '-'] or end+1 is not NUM_ATTRIBUTES:
            proper = False
    assert proper

'''
NEEDED SETUP: DO NOT REMOVE ---------------------------------------------------
For clarification look into dtype in numpy: [('Item1 Name','Item1 type')...],
used for reading in the data from numpy to tell it that each element has a
different type
'''
ndtype = [('A1', 'S1'), ('A2', 'f4'), ('A3', 'f4'), ('A4', 'S1'), ('A5', 'S2'),
          ('A6', 'S2'), ('A7', 'S2'), ('A8', 'f4'), ('A9', 'S1'),
          ('A10', 'S1'), ('A11', 'f4'), ('A12', 'S1'), ('A13', 'S1'),
          ('A14', 'f4'), ('A15', 'f4'), ('A16', 'S1')]

# list of dictionaries mapping[0] corresponds to possible values in
# data[all][0] etc
mapping = [{'b': 0, 'a': 1},
           {},
           {},
           {'u': 0, 'y': 1, 'l': 2, 't': 3},
           {'g': 0, 'p': 1, 'gg': 2},
           {'c': 0, 'd': 1, 'cc': 2, 'i': 3, 'j': 4, 'k': 5, 'm': 6, 'r': 7,
            'q': 8, 'w': 9, 'x': 10, 'e': 11, 'aa': 12, 'ff': 13},
           {'v': 0, 'h': 1, 'bb': 2, 'j': 3, 'n': 4, 'z': 5, 'dd': 6,
           'ff': 7, 'o': 8},
           {},
           {'t': 0, 'f': 1},
           {'t': 0, 'f': 1},
           {},
           {'t': 0, 'f': 1},
           {'g': 0, 'p': 1, 's': 2},
           {},
           {},
           {'+': 0, '-': 1}]
# Set up attribute_type vector
attribute_type = []
for line in mapping:
    if line != {}:
        attribute_type.append(len(line))
    else:
        attribute_type.append(-1)
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # test = np.array([np.nan])
    # test2 = np.array(['?'])
    # print np.isnan(test2)
    # print np.isnan(test)
    # test_mapData()
    # data = np.genfromtxt('records.txt', dtype=ndtype, delimiter=',')
    # print data[0]
    # test = np.array(list(data[0]), dtype=ndtype)
    # print test.shape
    # print test
    # print mapping[3]['u']
    print np.array(attribute_type)
    array = test_loadData()
    splitRatio = 0.8
    train_data, test_data = splitDataSets(array,splitRatio)
    # array = np.genfromtxt('records.txt', dtype=ndtype, delimiter=',')
    # print [row[1] for row in fullArray],

import numpy as np
from StringIO import StringIO
import time

def processData(ndtype,relation):

    array = np.genfromtxt('records.txt',dtype=ndtype,delimiter=',')
    NUM_ATTRIBUTES = len(ndtype)
    processed = np.zeros((NUM_ATTRIBUTES,len(array)),dtype=ndtype)

    i,j = 0,0
    temp = list(array[0])
    print temp
    tdtype = [('a','i2'),('b','f4'),('c','f4'),('d','i2'),('e','i2'),('f','i2'),('g','i2'),('h','f4'),('i','i2')]
    tdtype += [('j','i2'),('k','f4'),('l','i2'),('m','i2'),('n','f4'),('o','f4'),('p','i2')]
    data = np.zeros((1,16),dtype=tdtype)
    print data.dtype
    i = 0
    for char in temp:
        data[i] = char
        i+=1
    print data

    # for row in array:
    #     temp = list(row)
    #     for char in temp:
    #         processed[j,i] = char
    #         j += 1
    #     j = 0
    #     i += 1
    # print processed[0]

    #
    # print array.dtype
    # print array[0]
    # print list(array[0])
    # for char in list(array[0]):
    #     print char.dtype
    # print array.dtype

ndtype  = [('A1','S1'),('A2','f4'),('A3','f4'),('A4','S2'),('A5','S2'),('A6','S2'),('A7','S2'),('A8','f4'),('A9','S1')]
ndtype += [('A10','S1'),('A11','f4'),('A12','S1'),('A13','S1'),('A14','f4'),('A15','f4'),('A16','S1')]
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
           {'-':0,'+':1}]

array = np.genfromtxt('records.txt',dtype=ndtype,delimiter=',')

work = array[0]
# print work.dtype
lWork = list(work)
# print mapping[0] == {}
for i in range(len(lWork)):
    print lWork[i],
    if mapping[i] != {}:
        print mapping[i][lWork[i]],
        lWork[i] = mapping[i][lWork[i]]
    print
print lWork
# print mapping

# listDict = [{'A':2},{'Two':4}]
# print listDict
# listDict[0].update({'B':4})
# print listDict
# print listDict[0]['A']
# weightMatrix = np.zeros((3,2)
# for k in range(3):
#     weightMatrix[k,0] = ({'A':k})
#     weightMatrix[k,1] = ({'B':k*k})
#     print weightMatrix[k]




# processData(ndtype)

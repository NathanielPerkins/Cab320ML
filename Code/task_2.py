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


def getProbabilities(Put_Some_Inputs_Here):
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
    return None


def contProbability(Put_Some_Inputs_Here):
    '''
    Computes the guassian probability of a continous variable given a mean and
    variance. Returns the probability of value x happening.
    '''
    return None

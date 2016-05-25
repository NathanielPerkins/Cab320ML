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

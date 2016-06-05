CAB320 Machine Learning Assignment
Authors:
Nathan Perkins - n7291035
Lachlan Cesca - n8580413

Statement of Completeness:
task_1:
All required functions for task_1 have been implemented. No errors with
functionality have been encountered.

Specific case variables needed, including attribute_type are generated
automatically using the setup_task_1 function.

Loading data is achieved through the loadData function, taking the following
filename - name of file to load data from
ndtype - expected types of data to be inputted
mapping - conversion function for inputted data
attribute_type - list of number of possible values each attribute can take

Missing values in the data are replaced with the average result of each
attribute. For nominal values, it is the most frequently occurring type, for
continuous values, the average value is used.

Data is shuffled via the splitDataSets function using a split ratio.


task_2:
Everything required to complete task_2 has been implemented. No errors with 
functionality have been encountered.

Once all data is loaded in and split. A summary of the training data is
generated so predictions can be calculated without having to pass all the 
data in every time. This summary is just a set of mean and standard deviations
for continuous variables, while for discrete values a count of all their
unique values are saved. These values are then used to calculate probabilities 
for new test data and make predictions. These summaries are split by class 
values, so that the two classes can be compared for their probabilities and 
make predictions on which class the test data likely correlates to.

Predictions are made for both test and training data and their accuracy and
error rates are displayed.


task_3:

Decision tree not fully functional. No recursive based algorithm has been
implemented.

Functions to calculate entropy, data entropy, conditional entropy and
information gain have been implemented. 

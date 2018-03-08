from sklearn import datasets, metrics
from scipy import sparse
from sklearn.cross_validation import train_test_split
#Choose one of the dataset using the datasets features in the scikit-learn
from sklearn import svm
from sklearn.datasets import load_boston,load_digits
import numpy as np

k = 1.0
#getting the information and reaction from the data set
numericals=load_digits()

#loading the dataset
L=numericals.data
M=numericals.target

#As indicated by your dataset, split the information to 20% testing information, 80% preparing data(you can likewise utilize some other number)
x_train,x_test,y_train,y_test=train_test_split(L, M, test_size=0.2)

#applying svc with linear kernel
model = svm.SVC(kernel='linear plot')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("Finding Accuracy for the SVC linear kernel " + str(metrics.accuracy_score(y_test,y_pred)))

#Applying SVC with RBF kernel
model = svm.SVC(kernel='rbf model')
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

#printing the accuarcy
print("Accuracy for the SVC with rbf kernel " + str(metrics.accuracy_score(y_test,y_pred)))
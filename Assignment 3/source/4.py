from sklearn.model_selection import train_test_split
from sklearn import datasets, metrics
from sklearn.neighbors import KNeighborsClassifier
#Loading the dataset
irsdataset=datasets.load_iris()

#getting the data and response of the dataset
L=irsdataset.data
M=irsdataset.target

a_train, a_test, b_train, b_test=train_test_split(L, M, tst_sz=0.2)

#split the data for training and testing
md= KNeighborsClassifier(n_neighbors=5)
md.fit(a_train, b_train)

y_dt=md.predict(a_test)

#printing the accuracy
print("Accuracy is : ", metrics.accuracy_score(b_test, y_dt))
kvalue_range=range(1, 20)
#range value
scores=[]

for k in kvalue_range:
    knn=KNeighborsClassifier(n_neighbors=k)
    #knn field
    knn.fit(a_train, b_train)
    y_dt=knn.predict(a_test)
    #appending the scores
    scores.append(metrics.accuracy_score(b_test, y_dt))


import matplotlib.pyplot as plt
#ploting the k,range,scores
plt.plot(kvalue_range, scores)
#ploting the value of k
plt.xlabel("value of k")
#ploting the testing accuracy
plt.ylabel("testing accuracy")
plt.show()
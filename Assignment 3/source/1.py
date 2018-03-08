import matplotlib.pyplot as plt
import LinearDiscriminantAnalysis
from sklearn import datasets
from sklearn.discriminant_analysis\


irisfile = datasets.load_iris()
#loading & importing files
L = irisfile.data
M = irisfile.target
tt_names = irisfile.target_names

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(L, M, test_size=0.30)

from sklearn.neighbors import KNeighborsClassifier
class1 = KNeighborsClassifier(n_neighbors=5)
class1.fit(X_train, y_train)

y_pred = class1.predict(X_test)

#linear discriminat analysis
lda = LinearDiscriminantAnalysis(n_components=2)
X_r2 = lda.fit(X_test, y_pred).transform(L)
#ploting figure
plt.figure()
colors = ['orange', 'red', 'blue']
lenghtw = 2


for color, i, target_name in zip(colors, [0, 1, 2], tt_names):
    plt.scatter(X_r2[M == i, 0], X_r2[M == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of IRIS dataset')
#To plot the figure
plt.show()
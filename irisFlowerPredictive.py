## Source: https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset

import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv('irisflower.csv');
##---------------Preview of Data------------

##print(data.shape)
##print(data.describe())
##print(data.head())
##print(data.info())
#print(data['species'].value_counts());
##print(data.describe())

##----------------Data Visualization---------

##tmp = data.drop('Id', axis=1)
##tmp = data
##g = sns.pairplot(tmp, hue='species', markers='+')
##plt.show()

##g = sns.violinplot(y='species', x='sepal_length', data=data, inner='quartile')
##plt.show()
##g = sns.violinplot(y='species', x='sepal_width', data=data, inner='quartile')
##plt.show()
##g = sns.violinplot(y='species', x='petal_length', data=data, inner='quartile')
##plt.show()
##g = sns.violinplot(y='species', x='petal_width', data=data, inner='quartile')
##plt.show()

##------------------Modeling with scikit-learn-------

X = data
y = data['species']
### print(X.head())
##print(X.shape)
### print(y.head())
##print(y.shape)

##------------------Train and test on the same dataset------

# experimenting with different n values
X = data.drop(['species'], axis=1)
k_range = list(range(1,26))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)
    y_pred = knn.predict(X)
    scores.append(metrics.accuracy_score(y, y_pred))
    
##plt.plot(k_range, scores)
##plt.xlabel('Value of k for KNN')
##plt.ylabel('Accuracy Score')
##plt.title('Accuracy Scores for Values of k of k-Nearest-Neighbors')
##plt.show()

logreg = LogisticRegression()
logreg.fit(X, y)
y_pred = logreg.predict(X)
print(metrics.accuracy_score(y, y_pred))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=5)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

# experimenting with different n values
k_range = list(range(1,26))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))
    
##plt.plot(k_range, scores)
##plt.xlabel('Value of k for KNN')
##plt.ylabel('Accuracy Score')
##plt.title('Accuracy Scores for Values of k of k-Nearest-Neighbors')
##plt.show()

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

##---------------Choosing KNN to Model Iris Species Prediction with k = 12-------

knn = KNeighborsClassifier(n_neighbors=12)
knn.fit(X, y)

# make a prediction for an example of an out-of-sample observation
predict = knn.predict([[2, 1, 1, 6]])
print(predict)

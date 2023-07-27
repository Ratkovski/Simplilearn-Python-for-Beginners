# Classification -> identify which category an object belongsbto : Application -: Spam detection

# Regression -> Predicting an attribute associated with an object: Application -> Stock prices prediction

# Dimensionality reduction -> Reducing the number of random variables to consider
# -> Application: to increase model efficiency

# Pre-processing -> Feature extration and normalization -> Application: transforming
# input data such as text for use with machine learning algorithms

import pandas as pd
import rfc
import seaborn as sns
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

# %matplotlib inline

# Loading dataset
wine = pd.read_csv('winequality2.csv', sep=',')
print(wine.head)
print(wine.info())
print(wine.isnull().sum())

# Preprocessing Data

bins = (2, 6.5, 8)
group_names = ['bad', 'good']
wine['quality'] = pd.cut(wine['quality'], bins=bins, labels=group_names)
wine['quality'].unique()
label_quality = LabelEncoder()
wine['quality'] = label_quality.fit_transform(wine['quality'])
print(wine.head(20))
print(wine['quality'].value_counts())
print(sns.countplot(wine['quality']))

# Now separate the dataset as response variable and feature variables
X = wine.drop('quality', axis=1)
y = wine['quality']

# Train and Test splitting of data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train)
print(X_test)

# Applying Standart scaling to get optimized results
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print(X_train[:10])

# Random Forest Classifier
rcf = RandomForestClassifier(n_estimators=200)
rcf.fit(X_train, y_train)
pred_rfc = rcf.predict(X_test)
# print(pred_rfc[:10])


# Let's see how our model performed
print(classification_report(y_test, pred_rfc))
print(confusion_matrix(y_test, pred_rfc))

# SVM classifier
clf = svm.SVC()
clf.fit(X_train, y_train)
pred_rfc = clf.predict(X_test)

# Let's see how our model performed
print(classification_report(y_test, pred_rfc))
print(confusion_matrix(y_test, pred_rfc))

# Neural Network

mlpc = MLPClassifier(hidden_layer_sizes=(11, 11, 11), max_iter=500)
mlpc.fit(X_train, y_train)
pred_mlpc = mlpc.predict(X_test)

# Let's see how our model performed
print(classification_report(y_test, pred_mlpc))
print(confusion_matrix(y_test, pred_rfc))

from sklearn.metrics import accuracy_score

cm = accuracy_score(y_test, pred_rfc)
print(cm)
print(wine.head(10))

# Xnew = [[7.3, 0.58, 0.00, 2.0, 0.065, 15.0, 21.0, 0.9946, 3.36, 0.47, 10.0]]
# Xnew = sc.transform(Xnew)
# ynew = rfc.predict(Xnew)
# print(ynew)

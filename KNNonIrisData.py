import pandas as pd
from pandas import DataFrame
from sklearn import datasets
from sklearn.model_selection import train_test_split
df_iris = datasets.load_iris()
X = df_iris.data
y = df_iris.target
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state = 100)
print(y_test)
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=5)
#train the model using training data 
model.fit(X_train,y_train)
predicted = model.predict(X_test) #0:Overcast, 2:Mild
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predicted))
print(classification_report(y_test,predicted))
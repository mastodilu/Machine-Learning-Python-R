# XGBoost

# Install xgboost following the instructions on this link: http://xgboost.readthedocs.io/en/latest/build.html#

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting XGBoost to the Training set
from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
accuracies.mean()
accuracies.std()

# PROVO A OTTIMIZZARE CON GRID SEARCH

# Applying Grid Search to find the best model and the best parameters
from sklearn.model_selection import GridSearchCV
# parameters è una lista di dizionari
parameters = [{
        'max_depth,': [1, 3,],
        'learning_rate': [0.2, 0.5],
        'n_estimators': [1, 50, 100, 500],
        }]
grid_search = GridSearchCV(estimator = classifier, # model
                           param_grid = parameters,
                           scoring = 'accuracy',   # accuracy, precision, recall, ...
                                                   # è il criterio che decise perchè un modello scelto è migliore di un altro
                           cv = 10, # corrisponde a K di cross_validation. Dice quanti subset del training set creare e testare
                           n_jobs = 1) # -1
grid_search = grid_search.fit(X_train, y_train)
best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_ #### <-- CONTIENE I PARAMETRI DA USARE!
# conviene settare XGBClassifier(learning_rate=0.1)
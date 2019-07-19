# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

"""
Si vuole capire perchè la gente ha cominciato a lasciare la banca negli ultimi 6 mesi.

E' un problema di classificazione.
"""

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')

# Encoding categorical data
country_dummies = pd.get_dummies(dataset.Geography, prefix="Country", drop_first = True)
gender_dummies = pd.get_dummies(dataset.Gender, prefix="is", drop_first =True)
dataset = pd.DataFrame.drop(dataset, columns=["RowNumber", "CustomerId", "Surname"])
dataset = pd.DataFrame.drop(dataset, columns=["Geography", "Gender"])
dataset = pd.concat([country_dummies, gender_dummies, dataset], axis = 1)

# Create X and y
X = dataset.iloc[:, 0:11].values
y = dataset.iloc[:, 11].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN as sequence of layers
classifier = Sequential() # linear stack of layers

# Adding the input layer and the first hidden layer
classifier.add(Dense(activation="relu", input_dim=11, units=6, kernel_initializer="uniform"))   ### LAYER
# relu è la rectifier function
# output_dim = 6 indica il numero di nodi nell'hidden layer
# input_dim = 11 numero di variabili indipendenti fornite in input

# Adding the second hidden layer
classifier.add(Dense(activation="relu", units=6, kernel_initializer="uniform"))                 ### LAYER

# Adding the output layer
classifier.add(Dense(activation="sigmoid", units=1, kernel_initializer="uniform"))              ### LAYER
# la sigmoide per l'output è ottima perchè consente di vedere le probabilità dell'output
# units = 1 perchè abbiamo un solo nodo di output

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']) 
# binary output                                 --> usa binary_crossentropy
# se l'output ha più di due possibili classi    --> usa categorical_crossentropy

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 5, epochs = 100)
# epochs = 100 dice di fare 100 "epoche", cioè 100 cicli
# batch_size = 10 numero di osservazioni da eseguire prima di aggiornare i pesi

# Part 3 - Making the predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
# y_pred contiene tanti numeri float che indicano la probabilità di quel determinato cliente di lasciare la banca
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

accuracy = evaluateAccuracy(cm)

def evaluateAccuracy(cm):
    total = 0
    diagonal = 0
    
    for r in range(len(cm)):
        for c in range(len(cm[r])):
            total += cm[r][c]
            if r == c:
                diagonal += cm[r][c]
                
    return diagonal/total
    
    
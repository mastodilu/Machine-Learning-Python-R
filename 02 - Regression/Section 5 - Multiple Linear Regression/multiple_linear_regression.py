# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')

# dummy variables
dummy_states = pd.get_dummies(data = dataset.iloc[:, 3], drop_first = True, prefix = "State")
dataset = pd.DataFrame.drop(dataset, columns=['State'])
dataset = pd.concat([dummy_states, dataset], axis = 1)

# variabili indipendenti e dipendenti
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 5].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# non serve fare feature scaling pernchè viene fatto automaticamente dalla libreria

# Fitting Multiple Linear Regression to the Training set
# applica il modello di regressione lineare ai miei dati
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
# stima le y corrispondenti alle X fornite usando le equazioni che il modello
# si è preparato. Così confrontiamo se il modello è buono oppure no.
y_pred = regressor.predict(X_test)

##################################
###### BACKWARD ELIMINATION ######
##################################

import statsmodels.formula.api as sm
# Aggiungiamo una colonna in grado di rappresentare la costante b0 dell'equazione
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)

# begin Backward Elimination #####

# crea la matrice di featuers ottimale: contiene le X molto influenti al calcolo (prima le mettiamo tutte e poi le rimuoviamo una per volta)
X_opt = X[:, [0,1,2,3,4,5]]
# fit the full model with all possible predictors
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
# Considera le Xi con i P-value maggiori. Se P>SL rimuovilo Xi, altrimenti hai finito.
regressor_OLS.summary() # restituisce un botto di info utili sulle variabili del modello

# rimuovo X2
X_opt = X[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# rimuovo X1
X_opt = X[:, [0,3,4,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# rimuovo X4
X_opt = X[:, [0,3,5]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# rimuovo X5
X_opt = X[:, [0,3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# L'array di Xi che ha un impatto significativo nel calcolo delle y (profitto)
# è la colonna X3 (perchè la prima colonna è formato da soli 1)

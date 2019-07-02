# Data Preprocessing Template

# Importing the libraries
import numpy as np # contiene le funzioni matematiche
import matplotlib.pyplot as plt # permette di fare i grafici
import pandas as pd # per importare e maneggiare dataset

# Importing the dataset
dataset = pd.read_csv('Data.csv')

# Categorical data
country_dummies = pd.get_dummies(dataset.Country, prefix="Country", drop_first=True)
purchased_dummies = pd.get_dummies(dataset.Purchased, prefix="Purchased", drop_first=True)
dataset = pd.concat([country_dummies, dataset], axis = 1)
dataset = pd.DataFrame.drop(dataset, columns=["Country"])
dataset = pd.concat([dataset, purchased_dummies], axis = 1)
dataset = pd.DataFrame.drop(dataset, columns=["Purchased"])

# Variabili dipendenti e indipendenti
X = dataset.iloc[:, :-1].to_numpy()
y = dataset.iloc[:, -1].to_numpy()

# Taking care of missing data
from sklearn.impute import SimpleImputer
simple_imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
simple_imputer.fit(X[:, 2:4]) # simple_imputer viene fatto lavorare solo nelle colonne dove ci sono dati mancanti
X[:, 2:4] = simple_imputer.transform(X[:, 2:4])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
stdscaler_X = StandardScaler()
X_train = stdscaler_X.fit_transform(X_train)
X_test = stdscaler_X.transform(X_test)
# sc_y = StandardScaler()
# y_train = sc_y.fit_transform(y_train)
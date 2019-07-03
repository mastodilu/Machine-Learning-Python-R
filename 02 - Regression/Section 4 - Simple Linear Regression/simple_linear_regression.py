# Simple Linear Regression

# Importing the libraries
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values # var indipendenti (matrice di Features X)
y = dataset.iloc[:, 1].values   # var dipendenti

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0) # circa il 33%

# QUA AVVIENE IL MACHINE LEARNING

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train) # si specifica tutto il training set

# con il fitting della regressione lineare abbiamo creato un modello che si è
# calcolato la funzione y = a+bx per stimare ogni possibile salario.

# Predicting the Test set results
y_predictions = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')                  # traccia tutti i punti: coordinata X; coordinata Y; colore
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # traccia la retta: coordinata X; coordinata Y; colore
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
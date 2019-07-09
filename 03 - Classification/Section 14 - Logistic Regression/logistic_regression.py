# Logistic Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values # usiamo solo age e salary
y = dataset.iloc[:, 4].values # purchased or not

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

"""
la matrice di confusione contiene le decisione corrette
calcolate dalla macchina e quelle sbagliate.
Si crea una matrice di 2 righe e 2 colonne: C[i][j] contiene
il numero di osservazioni del gruppo i previste come gruppo j.
    C00: chi non l'ha comperata ed è stato previsto che non la comperasse
    C01: chi non l'ha comperata ma è stato previsto che la comperasse
    C10: chi l'ha comperata ma non è stato previsto che la comperasse
    C11: chi l'ha comperata proprio come previsto
"""
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('pink', 'green'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
"""
SPIEGAZIONE DEL GRAFICO OTTENUTO
I punti rappresentano tutte le osservazioni del training set: sull'asse X c'è l'età e sull'asse Y il reddito.
I punti rosa rappresentano le osservazioni del training set la cui y vale 0 (non hanno comperato), mentre
i punti verdi rappresentano le osservazioni del training set la cui y vale 1 (hanno comperato).
Generalmente chi è giovane e con poco salario è in basso a sinistra, quindi non ha comperato.
Chi è più vecchio e più ricco l'ha comperato più frequentemente.

Lo scopo è creare un classificatore in grado di posizionare gli utenti nella regione di previsione
- compra: verde
- non compra: rosso
la linea che separa le due regioni si chiama "prediction boundary"
Se questa riga è retta (come in questo caso) è perchè il classificatore creato è LINEARE,
infatti è stata usata la libreria 'sklearn.linear_model'

Il grafico ottenuto mostra dei cluster di dati classificati male perchè
la popolazione non è distribuita linearmente e andrebbe usato un altro classificatore.
"""

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('pink', 'green'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
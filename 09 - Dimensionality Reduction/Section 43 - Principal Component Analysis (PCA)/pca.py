# PCA

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
Il csv contiene informazioni chimiche su molti vini raccolti da un vinicoltore.

Var indipendenti: Xi. Le colonne dalla prima alla penultima.
y: colonna customer_segment

La y rappresenta la tipologia di cliente (1, 2 o 3).
Grazie a questa informazione diventa possibile raccomandare una determinata categoria
di vini ad una categoria di cliente.

Le Xi sono troppe, dobbiamo averne al massimo 2 per poterle rappresentare graficamente.
Servono le Xi più rilevanti, a costo di una lieve perdita di informazione.
"""
# Importing the dataset
dataset = pd.read_csv('Wine.csv')
X = dataset.iloc[:, 0:len(dataset.columns)-1].values # tutte tranne l'ultima
y = dataset.iloc[:, -1].values # solo l'ultima

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""
PCA riduce le dimensioni del problema, cioè il numero di Xi, creandone di nuove!
"""
# Applying PCA
from sklearn.decomposition import PCA
pca_temp = PCA(n_components = None) # numero di variabili che vogliamo (le feature che meglio descrivono la varianza)
X_train_temp = pca_temp.fit_transform(X_train)
X_test_temp = pca_temp.transform(X_test)
explained_variance = pca_temp.explained_variance_ratio_  # array che mostra come ogni componente influisce sulla varianza
                                                    # da qua possiamo vedere che scegliendo n_components = 2 possiamo
                                                    # possiamo rappresentare 0.369+0.193 = 56% della varianza
                                                    # (quindi le due variabili più significative influenzano il 56% della varianza)
pca_temp = None
X_train_temp = None
X_test_temp = None

# Uso due variabili indipendenti per il modello
pca = PCA(n_components = 2)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
"""
è una matrice 3x3 ma comunque sulla diagonale abbiamo i risultati positivi.
Grazie a PCA abbiamo due variabili in grado di comportarsi molto bene nel modello.
"""

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('pink', 'yellow', 'black'))(i), label = j)
plt.title('Logistic Regression (Training set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green', 'blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('pink', 'yellow', 'black'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()
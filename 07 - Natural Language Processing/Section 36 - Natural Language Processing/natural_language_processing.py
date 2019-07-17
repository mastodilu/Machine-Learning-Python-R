# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# Usiamo i tsv perchè sono delimitati da \t invece che da ;
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)
# quoting = 3 è un codice che permette di ignorare i simboli " leggendo il csv

"""
Nel modello BAG OF WORDS vogliamo soltanto estrarre le parole rilevanti.

ad esempio si tolgono gli articoli, alcuni numeri, si sistemano i tempi verbali,
la punteggiatura inutile. Ecc...

Stemming: tiene solo la radice delle parole (tipo i verbi) in modo da ridurre le
parole totali mantenendo però il senso generale.

Si tolgono le maiuscole.
"""

# Cleaning the texts
import re
import nltk # libreria natural language toolkit
nltk.download('stopwords')  # scarica la lista di parole che genericamente
                            # sono irrilevanti per classificare un testo
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = [] # variabile tipicamente usata per collezionare testo generico
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) # sostituisce con uno spazio bianco
                                                            # tutto quello che non è una lettera maiuscola o minuscola
    review = review.lower() # porta a minuscolo
    review = review.split() # trasforma ogni riga in una lista
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review) # riporta la lista di parole ad una stringa sensata separata da uno spazio
    corpus.append(review)
   
"""
dall'elenco di stopwords conviene non eliminare le negazioni tipo "no", "not"
per non invertire il senso del testo
"""

"""
BAG OF WORDS
1. prende ogni singola parola una sola volta senza ripetizioni e crea una
colonna ciascuna.
2. le colonne vengono scritte in una tabella dove le righe sono le righe classificate
3. alla riga N c'è la recensione X, e in ogni colonna un numero che corrisponde
a quante volte quella parola era presenta nella recensione X

le recensioni sono corte e contengono pochissime parole del totale, quindi si ottiene
una matrice sparsa.
Una MATRICE SPARSA è una matrice in cui la maggior parte delle celle è occupata da 0.

Ottenuta la matrice sparsa ci possiamo ricondurre ai classificatori della sezione 3
"""

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500) # tiene le 1500 parole più frequenti (quindi crea 1500 colonne)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

total_predictions = 0
for r in cm:
    for c in r:
        total_predictions += c
accuracy = (cm[0][0] + cm[1][1]) / total_predictions
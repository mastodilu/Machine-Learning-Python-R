# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Data.csv')

# Taking care of missing values
dataset$Age[is.na(dataset$Age)] <- mean(dataset$Age, na.rm=TRUE)
dataset$Salary[is.na(dataset$Salary)] <- mean(dataset$Salary, na.rm=TRUE)

# Encode categorical data
dataset$Country = factor(dataset$Country, # i dati da codificare
                         levels = c('France', 'Spain', 'Germany'), # c(..) specifica un vettore
                         labels = c(1, 2, 3)) # label assegnati a France, Spain, Germany
dataset$Purchased = factor(dataset$Purchased,
                           levels = c('Yes', 'No'),
                           labels = c(1, 0))
# in R dopo l'encoding non è vero che 1, 2, 3 hanno pesi diversi

# Splitting the dataset into the Training set and Test set
install.packages('caTools')
library(caTools)
set.seed(123) # inizializza il generatore di numeri random
split = sample.split(dataset$Purchased, SplitRatio = 0.8) # si scrive la funzione split per poterla usare dopo
                                                          # bisogna passare come parametro solo le var DIPENDENTI
                                                          # splitratio indica la percentuale dedicata al training set
training_set = subset(dataset, split == TRUE)     # il training set si compone dei valori agli indici di 'split' che valgono True (stampa 'split' nel terminale per capire che sto dicendo)
test_set = subset(dataset, split == FALSE)        # il test set si compone dei valori agli indici false dell'array 'split'

# Feature Scaling
training_set[, 2:3] = scale(training_set[, 2:3]) # applicachiamo il rescaling solo dove è necessario
test_set[, 2:3] = scale(test_set[, 2:3])
# se si verifica questo errore:
#   Error in colMeans(x, na.rm = TRUE) : 'x' must be numeric
# è perchè abbiamo inserito dummy value in colonne che contenevano del testo, e questi numeri sono rimasti testo.
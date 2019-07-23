# Principal Component Analysin (PCA)

E' l'**algoritmo non supervisionato** (non considera le variabili indipendenti) più utilizzato, ed anche il più popolare per **ridurre la dimensionalità** del problema.

A differenza della regressione lineare, non si vuole prevedere un valore, ma la correlazione tra i valori costruendo la lista degli **assi principali**.

Utilizzi:

1. filtro dei rumori
2. Visualizzazione
3. Estrazione di feature
4. Previsioni stock market
5. Analisi dei geni

## Tipi di riduzione della dimensionalità del problema

1. **feature selection**:
   1. `Backward elimination` (vedi sezione 2) per selezionare le feature più rilevanti dalla matrice di feature (quelle che meglio spiegano la variabile dipendente)
   2. `Forward selection`
   3. `Bidirectional elimination`
   4. `Score comparison`
2. **feature extraction**:
   1. `PCA`

## Scopo di PCA

Lo scopo di PCA è identificare la correlazione tra variabili. Se viene trovata una forte correlazione tra due variabili diventa possibile ridurre la dimensione del problema.
Un problema n-dimensionale viene proiettato in un sotto spazio k-dimensionale.

Step:

1. standardizza i dati
2. ottieni
   - Eigenvector
   - Eigenvalues
3. riordina gli Eigenvalues
4. costruisci la matrice di proiezioni $W$ dai k Eigenvectors selezionati
5. trasforma il dataset originale

## Problema

PCA è altamente influenzato dagli outliers.

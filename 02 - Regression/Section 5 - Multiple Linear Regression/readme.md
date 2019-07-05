- [Multiple linear regression](#Multiple-linear-regression)
  - [Problema](#Problema)
  - [Dummy variables](#Dummy-variables)
  - [Come costruire un modello](#Come-costruire-un-modello)
    - [1. All in](#1-All-in)
    - [2. Backward elimination](#2-Backward-elimination)
  - [3. Forward selection](#3-Forward-selection)
    - [4. Bidirectional elimination](#4-Bidirectional-elimination)
    - [5. All possible models](#5-All-possible-models)

# Multiple linear regression

![multiple linear regression formula](img/001.png)

- ***y*** è la **variabile dipendente**
- le ***Xi*** soono le **variabili indipendenti**
- le ***b*** sono i **coefficienti**

Un problema di Regressione Lineare deve soddisfare dei requisiti:

1. Linearità
2. omoschedasticità: tutte le variabili hanno uguale varianza<br>![omoschedasticità](img/003.png)
3. le variabili segueono la distribuzione Normale Multivariata: cioè ogni loro combinazione lineare segue la distribuzione Normale.<br>![formula distribuzione normale](img/002.png)
4. errori indipendenti: se i punti seguono un andamento strano è possibile che ci siano delle influenze<br>![errori indipendenti](img/004.png)
5. mancanza di multicollinearità: La multicollinearità sorge quando c’è un’elevata correlazione tra due o più variabili esplicative.

## Problema

Dato un csv con informazioni su 50 startup, si vuole capire quale chi e perchè performa meglio degli altri: dove sono, come spendono e in cosa investono.

## Dummy variables

![errori indipendenti](img/005.png)

CI sono due possibili caategorie nel colonna State, quindi si usa una Dummy Variable e si continua l'equazione:

![errori indipendenti](img/006.png)

Non puoi mai aggiungere tutte le DUmmy Variables: per rappresentare N variabili bastano N-1 colonne.

## Come costruire un modello

### 1. All in

Usa tutte le variabili, perchè **sai già che tutte sono importanti per la stima finale** oppure perchè stai preparando il campo per **applicare backward elimination**.

### 2. Backward elimination

1. seleziona un livello di significatività per restare nel modello ($SL = 0,05$)
2. aggiungi al modello tutti le variabili dipendenti X
3. si considera la variabile $X_i$ che ha il P-value più alto
   - se $P-value > SL$ vai allo step **4.**
   - **altrimenti hai finito e il modello è pronto**
4. rimuovi quella variabile
5. fai il fit del modello senza usare questa variabile (*in pratica rifai il modello senza quella variabile*)
6. ritorna al punto **3.**

## 3. Forward selection

1. seleziona un livello di significatività ($SL = 0.05$)
2. fai il fit di ogni possibile regressione lineare semplice $y \sim X_n$ e seleziona quella con $SL$  minore
3. tieni questa variabile e fai il fit di ogni possibile modello usando questa variabile e una variabile alla volta tra le altre di cui disponi.<br>In pratica si tenta ogni altro possibile modello calcolato da una coppia di variabili.<br>**Esempio**: ho le variabili A, B, C, D, E e scelgo A. Costruisco ogni modello di regressione lineare semplice usando le coppie AB, AC, AD, AE.
4. Tra tutte le coppie, considera quella dove la variabile aggiunta ha il P-value minore.
   - Se il P-value è minore di SL allora si torna al punto 3
   - altrimenti **hai finito, ma tieni il modello precedente**, cioè senza l'ultima variabile aggiunta.

### 4. Bidirectional elimination

1. seleziona un livello di significatività per entrare nel modello $SL_{ENTER}=0.05$ e uno per restare nel modello $SL_{STAY} = 0.05$
2. esegui il passo successivo di **Forward selection**
   - la variabile entrante deve avere $P_{VALUE}<SL_{ENTER}$
3. esegui tutti i passi di **backward elimination**
   - le vecchie variabili vengono rimosse se hanno $P_{VALUE}>SL_{STAY}$
4. se ci sono variabili che possono entrare o uscire:
   - torna al punto **2.**
   - altrimenti hai finito, il modello è pronto

### 5. All possible models

1. seleziona un criterio di bontà del fit (es: criterio Akaike)
2. costruisci tutti i possibili modelli di regressione: $2^{N-1}$ combinazioni totali
3. seleziona quella che riflette meglio il criterio scelto al punto 1.
4. hai finito.

# Clustering gerarchico

Tipi:

1. agglomerativo
2. divisivo

#### Step 1

ogni punto diventa un cluster: si formano N clusters.

![step 1](img/001.png)

#### Step 2

I due **punti** più vicini vengono raggruppati in un singolo cluster (N-1) cluster

![step 2](img/002.png)

#### Step 3

I due **cluster più vicini** vengono raggruppati in un singolo cluster (N-1) cluster

![step 3](img/003.png)

> come si calcola la distanza tra due cluster?

#### Step 4

ripeti step 3 fino ad ottenere un unico cluster

![step 4.1](img/004.png)

![step 4.2](img/005.png)

![step 4.3](img/006.png)

FINE.

## Dendogramma

### Esempio di dendogramma

![dendogramma](img/dendogramma_esempio.jpg)

### step 1

Ogni punto è un cluster a sè stante.

### step 2

I punti P2 e P3 sono in uno stesso cluster e quindi si collegano con una linea orizzontale. L'altezza tra la linea orizzontale che li collega e l'asse orizzontale rapppresenta la distanza (ad esempio euclidea) tra i due punti/cluster.

![step 2](img/007.png)

### step 3

![step 3](img/008.png)

P5 e P6 sono collegati e hanno un'altezza maggiore rispetto alla coppia precedente perchè la loro distanza è maggiore.

### step 4

![step 4.1](img/009.png)

![step 4.2](img/010.png)

![step 4.3](img/011.png)

## Soglia di diversità

![threshold](img/012.png)

Le altezze rappresentano le distanze tra i cluster, quindi le *diversità* rispetto ai cluster. Maggiore è la distanza e più sono diversi.

E' utile stabilire una soglia, threshold, graficamente rappresentata da una linea orizzontale nel dendogramma, che stoppa il raggruppamento in cluster di cluster minori evitando così di formare gruppi troppo eterogenei.

Nella foto abbiamo due cluster, perchè l'ultimo supera la soglia definita.

![threshold e cluster](img/013.png)

Esempio con 4 clusters:

![threshold e 4 cluster](img/014.png)

## Come trovare un numero di cluster ottimale

Come si setta un threshold adeguato?

Immaginando di prolungare ogni linea orizzontale fino all'asse verticale, si taliga dal threashold la linea verticale più lunga che non è tagliata da alcuna linea orizzontale.

![thresthold per il numero di cluster ottimale](img/015.png)

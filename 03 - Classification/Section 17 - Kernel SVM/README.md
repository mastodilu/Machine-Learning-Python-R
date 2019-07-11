# Kernel SVM

Sono stati visti alcuni classificatori lineari che classificano dei punti dividendoli in due aree grazie ad una retta.

Cosa succede quando non è possibile tracciare una retta?

![kernel svm](img/001.png)

Ogni retta tracciabile non è in grado di separare le due classi: **i dati non sono linearmente separabili**.

## Idee

Una possibilità è aggiungere una terza dimensione ai dati (ad esempio una profondità) per poter rendere separabili linearmente i dati.

Il metodo Kernel invece è più semplice e risolve questo problema senza coinvolgere ulteriori dimensioni.

### Come mappare i dati ad una dimensione in più

Le osservazioni riportate in questa figura mostrano che questi dati non sono linearmente separabili perchè in una dimensione possiamo tracciare solo un punto. Tracciando un singolo punto non siamo in grado di separare tutti i verdi dai rossi.

![dati sul solo asse X](img/002.png)

La seguente funzione può essere trasformata:

1. ad ogni $Xi$ si toglie una stessa quantità, diciamo 5, in modo da shiftare tutti i punti a sinistra fino ad avere i rossi dietro a $X=0$
2. si eleva al quadrato e si proiettano i punti su una parabola
3. ora i punti sono separabili da una retta

![dati trasposti sulla parabola](img/003.png)

### Lo stesso principio da 2D a 3D

![da 2D a 3D](img/004.png)

Al termine del calcolo si riproietta eliminando la dimensione aggiunta:

![da 3D a 2D](img/005.png)

Problema:

aggiungere una dimensione può diventare FOTTUTAMENTE costoso in termini di computazione.

Per risolvere questo problema si usa il metodo Kernel così si evita di mappare ad una dimensione maggiore.

## Il Kernel RBF Gaussiano

![kernel RBF Gaussiano](img/006.png)

Il punto rosso sotto al cono rappresenta il centro della base e si chiama **landmark**.

![kernel RBF Gaussiano](img/007.png)

Tutte le osservazioni all'interno della circonferenza vengono proiettate sul cono: lungo l'asse dell'altezza i punti hanno valore maggiore di 0 se sono all'interno della circonferenza, altrimenti uguale a 0.

![kernel RBF Gaussiano](img/008.png)

$\sigma$ determina l'ampiezza della circonferenza: al crescere di $\sigma$ cresce anche la circonferenza.

Un problema complesso può essere rappresentato come somma algebrica di più kernel RBF gaussiani:

![doppio kernel RBF Gaussiano](img/009.png)

## Tipi di funzioni Kernel

Alcune delle più usate sono:

1. Kernel RBF Gaussiano
2. Kernel sigmoide
3. Kernel polinomiale

![doppio kernel RBF Gaussiano](img/010.png)

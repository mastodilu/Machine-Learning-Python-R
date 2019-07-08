# Random Forest

E' una versione di Ensamble Learning, in cui si prendono molti algoritmi, oppure lo stesso più volte, e si mettono assieme per ottenere qualcosa di migliore rispetto all'originale.

1. partendo dal dataset, si prendono K punti a caso
2. costruisci un albero decisionale in base a quei K punti
3. costruisci N alberi applicando lo stesso procedimento
4. ogni volta che si vuole stimare una y, usa la stima calcolata per ogni albero di decisione

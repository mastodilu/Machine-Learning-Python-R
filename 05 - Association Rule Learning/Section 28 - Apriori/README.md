# Apriori

*Chi fa qualcosa ha fatto pure qualcos'altro.*

L'algoritmo Apriori è diviso in 3 parti:

*SUPPORT($M_1$) = numero di persone che ha compiuto M / totale*.

*CONFIDENCE($M_1 \rArr M_2$) = numero di persone che ha compiuto $M_1$ ed $M_2$ / numero di persone che ha compiuto $M_1$*

$LIFT(M_1 \rArr M_2) = \frac{CONFIDENCE(M_1 \rArr M_2)}{SUPPORT(M_2)}$

## Step by step

1. setta supporto e confidenza minimi
2. prendi tutti i subset in cui *SUPPORT* è più alto di SUPPORT minimo
3. prendi tutti i subset che hanno *CONFIDENCE* più alta di quella minima
4. riordina le regole facendo diminuire *LIFT*

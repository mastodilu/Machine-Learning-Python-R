# Random forest classification

**Ensemble learning**:

- Vengono usati più algoritmi machine learning per farne uno solo.
- random forest usa più alberi decisionali per comporre l'algoritmo finale

Step:

1. prendi K osservazioni random dal dataset
2. costruisci l'albero di decisione associato a quei K punti
3. scegli il numero di alberi da costruire e ripeti gli step 1 e 2
4. per predire in quale categoria deve risiedere un punto, fa predire la classificazione ad ogni albero e assegna il punto alla categoria che ha preso più voti

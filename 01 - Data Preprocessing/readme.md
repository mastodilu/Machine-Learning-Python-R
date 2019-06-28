# Data preprocessing

Prima di cominciare, tutti i file usati sono disponibili [qua](https://www.superdatascience.com/pages/machine-learning).

## 1. Ottieni il dataset

Nel dataset ci sono due tipi di variabili, v. dipendenti e indipendenti.

| Country | Age | Salary | Purchased |
| ------- | --- | ------ | --------- |
| France  | 44  | 72000  | No        |
| Spain   | 27  | 48000  | Yes       |
| Germany | 30  | 54000  | No        |
| Spain   | 38  | 61000  | No        |
| Germany | 40  | ,      | es        |
| France  | 35  | 58000  | Yes       |
| Spain   |     | 2000   | No        |
| France  | 48  | 79000  | Yes       |
| Germany | 50  | 83000  | No        |
| France  | 37  | 67000  | Yes       |

Nel file, le variabili **indipendenti** sono:

- country
- age
- salary

In ogni modello di ML vengono usate variabili indipendenti per predire variabili dipendenti.

In pratica: `F(country, age, salary) -> Purchased`.

## 2. Importa le librerie

### In spyder

```python
# numpy contiene le funzioni matematiche
import numpy as np
# matplotlib.pyplot permette di fare i grafici
import matplotlib.pyplot as plt
# pandas serve a importare e maneggiare dataset
import pandas as pd
```

### In RStudio

Le librerie sono scaricabili dalla finestra dedicata ai package, dove si possono selezionare e deselezionare.

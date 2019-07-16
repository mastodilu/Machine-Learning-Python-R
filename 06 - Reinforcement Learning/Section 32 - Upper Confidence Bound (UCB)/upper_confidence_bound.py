# Upper Confidence Bound

"""
Immaginando di dover proporre dieci diverse pubblicità di un suv da vendere su
un social network otteniamo il dataset corrente.
Per ogni utente (l'indice della riga) abbiamo scoperto che ha cliccato solo su
determinati spot, non sugli altri.
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implementing UCB
import math
N = 10000 # numero di utenti
d = 10 # numero di versioni dello spot
ads_selected = []
numbers_of_selections = [0] * d # lista grossa d inizializzata a 0
sums_of_rewards = [0] * d       # lista grossa d inizializzata a 0
total_reward = 0
for n in range(0, N): # per ogni utente
    ad = 0
    max_upper_bound = 0
    for i in range(0, d): # per ogni spot mostrato all'utente
        if (numbers_of_selections[i] > 0):
            average_reward = sums_of_rewards[i] / numbers_of_selections[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    reward = dataset.values[n, ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + reward
    total_reward = total_reward + reward

# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
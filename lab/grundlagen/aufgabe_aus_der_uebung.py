# %% Pakete

import numpy as np

# %% Aufgaben aus der Uebung

z1 = 3+4j
z2 = 5-2j

w1 = z1+z2
w2 = z1+np.conj(z1)
w3 = z1-np.conj(z1)
print(f'w1 = {w1}')
print(f'w2 = {w2}')
print(f'w3 = {w3}')

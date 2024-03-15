# T3ES2003
# Labor 01
# 15. Maerz 2024

#
# Live Einfuehrung in Python
#

# %% Pakete importieren

import numpy as np # Numpy importieren
from numpy import cos, sin

# %% Start

# Variablen zuweisen
a = 5
b = 7

def addition(x, y):
    '''
    

    Parameters
    ----------
    x : float
        Erster summand.
    y : float
        Zweiter summand.

    Returns
    -------
    s : float
        Summe.

    '''
    s = x + y
    return s

def auswahl(x):
    if x == 10:
        print('x ist 10')

# %% Weiter

for idx in range(5):
    print(idx)

# %%

for c in ['a', 'b', 'c']:
    print(c)


# %% OOP


class Zahl():
    
    def __init__(self):
        self.wert = 5
        # Entspricht in C++
        # this->wert = 5;
        # wert = 5;

    def __str__(self):
        s = f'Wert ist {self.wert}'
        return s

# %%

zahl = Zahl()
print(zahl)




















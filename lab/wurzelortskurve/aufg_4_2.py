# %% Aufgabe 4.2

# %% Packages

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# %% System Definition

# Nullstelle bei -2, wie in der urspruenglichen Aufgabenstellung
s = ctrl.TransferFunction.s

# (a)
L = (s+2)/((s+1)*s)
# (b)
L = (s+2)/(s**2 + s + 4.25)
print(L.poles())
print(L.zeros())

print(L)

# %% WOK

plt.figure('WOK')
plt.clf()
ctrl.rlocus(L)
plt.show()


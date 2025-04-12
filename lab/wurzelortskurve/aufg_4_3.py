# %% Aufgabe 4.3
# Entnommen aus Franklin Aufg. 5.12

# %% Packages

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# %% System definition

# Nullstelle bei -2, wie in der urspruenglichen Aufgabenstellung
L = ctrl.tf([1, 2], [1, 10, 0, 0])

print(L)

# %% WOK

plt.figure('WOK')
plt.clf()
ctrl.rlocus(L)
plt.show()

# %% Einzelne Aeste

roots_on_branches, gains = ctrl.rlocus(L, plot=False)

plt.figure('Branches')
plt.clf()

for branch_idx in range(3):
    re, im = np.real(roots_on_branches[:,branch_idx]), np.imag(roots_on_branches[:,branch_idx])
    plt.plot(re, im, label=f'Ast {branch_idx+1}')

plt.grid(True)
plt.xlim(-15,2)
plt.ylim(-8,8)
plt.legend()
plt.show()

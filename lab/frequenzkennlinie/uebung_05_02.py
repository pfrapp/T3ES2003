# %% Uebung 5: Frequenzkennlinienverfahren
# Aufgabe 2

# %% Pakete

import matplotlib.pyplot as plt
import control as ctrl
import numpy as np

# %% Teil (a) Definition der Uebetragungsfunktion

s = ctrl.tf('s')
L = 6000/(s*(s+300))
print(L)

print(L.poles())

# %% Teil (a) Darstellung des Bode Diagramms

plt.figure('Bode')
plt.clf()
ctrl.bode(L, dB=True, omega_limits=[1, 1000])
plt.show()

# %% Teil (a) Nyquist plot

plt.figure('Nyquist')
plt.clf()
ctrl.nyquist(L)
plt.show()

# %% Teil (a) Contour die zur Auswertung genutzt wurde

N, contour = ctrl.nyquist(L, plot=False, return_contour=True)

print(f'N = {N}')

plt.figure('Contour')
plt.clf()
plt.plot(np.real(contour), np.imag(contour), '-x')
plt.grid(True)
plt.xlim(-0.0003,0.0003)
plt.ylim(-0.0003,0.0003)
plt.show()


# %% Teil (b) Definition der Uebetragungsfunktion

s = ctrl.tf('s')
L = (11*s-7)/(s**2)
print(L)

print(L.poles())

# %% Teil (b) Darstellung des Bode Diagramms

plt.figure('Bode')
plt.clf()
ctrl.bode(L, dB=True, omega_limits=[0.1, 100])
plt.show()

# %% Teil (b) Nyquist plot

plt.figure('Nyquist')
plt.clf()
ctrl.nyquist(L)
plt.show()

# %% Teil (b) Contour die zur Auswertung genutzt wurde

N, contour = ctrl.nyquist(L, plot=False, return_contour=True)

print(f'N = {N}')

plt.figure('Contour')
plt.clf()
plt.plot(np.real(contour), np.imag(contour), '-x')
plt.grid(True)
plt.xlim(-0.0003,0.0003)
plt.ylim(-0.0003,0.0003)
plt.show()

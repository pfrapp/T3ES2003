# %% Beantwortung einer Frage

# Was passiert wenn man 1/((j*omega)**2) vereinfacht zu
# 1/(j**2 * omega**2) = 1/(-omega**2)?


# %% Pakete

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# %% Referenz Bode Diagramm

s = ctrl.tf([1, 0], [1])
print(s)

G = 1/(s**2)

fig = plt.figure('Referenz Bode')
plt.clf()
ctrl.bode(G, dB=True)
plt.show()

# %% Berechnung nach Vereinfachung


# Betrag
# 20*log10(1/(omega**2)) = 20*log10(omega**(-2)) = -40*log10(omega)

# Phase
# Phase von 1/(-omega**2) ist 180 Grad

# Fazit:
# --> Das Bode Diagramm bleibt gleich, aber man kann es nicht mehr
# so einfach anhand der Regeln zeichnen

def G_simplified(omega):
    G_value = 1/(-omega**2)
    return 20*np.log10(np.abs(G_value)), np.rad2deg(np.angle(G_value))

omega = np.logspace(-1.2, 1.2)
betrag, phase = G_simplified(omega)

fig = plt.figure('Bode')
plt.clf()

ax = fig.add_subplot(2,1,1)
ax.plot(omega, betrag)
ax.grid()
ax.set_xscale('log')
ax.set(xlabel='Kreisfrequenz (rad/s)')
ax.set(ylabel='Betrag (dB)')

ax = fig.add_subplot(2,1,2)
ax.plot(omega, phase)
ax.grid()
ax.set_xscale('log')
ax.set(xlabel='Kreisfrequenz (rad/s)')
ax.set(ylabel='Phase (Grad)')

plt.show()

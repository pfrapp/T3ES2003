# Aufgabe 4.4 -- Dynamische Kompensation mit Lag Element
# Angelehnt an Franklin Aufg. 5.27
# Lag Compensation

# %%

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# %%

s = ctrl.TransferFunction.s

G = 1/((s+1)*(s+2))

# %%

plt.figure('WOK')
plt.clf()
ctrl.rlocus(G, plot=True)
plt.show()

# %%

K = 2.5

G_closed_loop = ctrl.feedback(K*G)

print('Polstellen geschl. Kreis')
print(G_closed_loop.poles())

plt.figure('Sprungantwort')
plt.clf()

t, h = ctrl.step_response(G_closed_loop)
plt.plot(t,h)
plt.grid()
plt.show()

print(f'Regelabw. Sprungantwort: {1.0-h[-1]}')

# %% Mit Lag Compensation


z = 0.02
p = 0.0025

D_c = (s+z)/(s+p)

plt.figure('WOK mit lag')
plt.clf()
ctrl.rlocus(D_c*G, plot=True)
plt.show()


G_closed_loop = ctrl.feedback(K*D_c*G)

print('Polstellen geschl. Kreis mit lag')
print(G_closed_loop.poles())

plt.figure('Sprungantwort mit lag')
plt.clf()

t, h = ctrl.step_response(G_closed_loop)
plt.plot(t,h)
plt.grid()
plt.show()

print(f'Regelabw. Sprungantwort mit lag: {1.0-h[-1]}')

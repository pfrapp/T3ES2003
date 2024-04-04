# Philipp Rapp
# fuer Veranstaltung T3ES2003 "Regelungstechnik"
# Labor 02: Systemdynamik
#
# Aufgabe 2.8: Uebertragungsverhalten
#

# %% Packages
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

# %% Plant

s = ctrl.tf('s')
# G = 1/(s*(s+1))

G = ctrl.tf([1], [1, 1, 0], inputs='u', outputs='y')

# %% Controller

# K = 10*(s+2)/(s+10)

K = ctrl.tf([10, 20], [1, 10], inputs='e', outputs='u')


# %% Gesamtsystem

sum_junction = ctrl.summing_junction(inputs=['w', '-y'], outputs='e')

closed_loop = ctrl.interconnect([G, K, sum_junction], inputs='w', outputs='y')

print(closed_loop)

closed_loop = ctrl.tf(closed_loop)

# %% Sprungantworten

t, y = ctrl.step_response(G)


plt.figure('Open loop step response')
plt.clf()
plt.plot(t, y)
plt.grid()
plt.show()



t, y = ctrl.step_response(closed_loop)


plt.figure('Closed loop step response')
plt.clf()
plt.plot(t, y)
plt.grid()
plt.show()



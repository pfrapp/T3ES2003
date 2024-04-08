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
from scipy.integrate import solve_ivp

# %% Plant (Strecke)

s = ctrl.tf('s')
# G = 1/(s*(s+1))

G = ctrl.tf([1], [1, 1, 0], inputs='u', outputs='y')

# %% Controller (Regler)

# K = 10*(s+2)/(s+10)

K = ctrl.tf([10, 20], [1, 10], inputs='e', outputs='u')


# %% Gesamtsystem

sum_junction = ctrl.summing_junction(inputs=['w', '-y'], outputs='e')

closed_loop = ctrl.interconnect([G, K, sum_junction], inputs='w', outputs='y')

print(closed_loop)

closed_loop_tf = ctrl.tf(closed_loop)

# %% Sprungantworten

t, y = ctrl.step_response(G)


plt.figure('Open loop step response')
plt.clf()
plt.plot(t, y)
plt.grid()
plt.show()



t, y = ctrl.step_response(closed_loop_tf)


plt.figure('Closed loop step response')
plt.clf()
plt.plot(t, y)
plt.grid()
plt.show()


# %% Simulation

def ode(t, x):
    # Rechte Seite u
    # Hier 1, da wir die Sprungantwort suchen
    rhs = 1.0
    return closed_loop.dynamics(t, x, rhs)

x_0 = np.zeros((3,))
sol = solve_ivp(ode, [0.0, 7.0], x_0)

t2 = sol.t
y2 = np.dot(closed_loop.C, sol.y).flatten()


# %% Plot the solution

plt.figure('Closed loop step response via integration with scipy')
plt.clf()
plt.plot(t2, y2, label='Solution via scipy')
plt.plot(t, y, label='Solution via control toolbox', linestyle='--')
plt.grid()
plt.legend()
plt.show()

# %%

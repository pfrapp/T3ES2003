# Philipp Rapp
# fuer Veranstaltung T3ES2003 "Regelungstechnik"
# Labor 02: Systemdynamik
#
# Aufgabe 2.7: Zeitbereichsverhalten PT2
#

# %% Packages

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import jet
import control as ctrl

# %% Definition der Uebertragungsfunktion

params = { 'omega_n': 1.0,
           'zeta': 0.3 }

H = ctrl.tf([params['omega_n']**2], [1.0, 2*params['zeta']*params['omega_n'], params['omega_n']**2])

# %% Berechnung der Impulsantwort

t_eval = np.linspace(0,10,200)
t, imp_response = ctrl.impulse_response(H, t_eval)

# Vergleich mit inverser Laplace Transformation
params['sigma'] = params['zeta']*params['omega_n']
params['omega_d'] = params['omega_n'] * np.sqrt(1.0 - params['zeta']**2)
imp_response_analytical = params['omega_n']/np.sqrt(1.0-params['zeta']**2) * \
                            np.exp(-params['sigma']*t_eval) * \
                            np.sin(params['omega_d'] * t_eval)

fig = plt.figure('Impulsantwort')
plt.clf()
plt.plot(t*params['omega_n'], imp_response)
plt.plot(t_eval*params['omega_n'], imp_response_analytical, linestyle='--')
plt.grid()
plt.xlabel('t*omega_n')
plt.show()



# %% Berechnung der Sprungantwort

t, step_response = ctrl.step_response(H, t_eval)

fig = plt.figure('Sprungantwort')
plt.clf()
plt.plot(t*params['omega_n'], step_response)
plt.grid()
plt.xlabel('t*omega_n')
plt.show()

# %% Parameter zeta

zeta_range = np.arange(0.0, 1.1, 0.1)

fig = plt.figure('Impuls- und Sprungantworten fuer verschiedene zeta')
plt.clf()

ax = fig.add_subplot(1,2,1)
for idx, zeta in enumerate(zeta_range):
    H = ctrl.tf([params['omega_n']**2], [1.0, 2*zeta*params['omega_n'], params['omega_n']**2])
    t, imp_response = ctrl.impulse_response(H, t_eval)
    ax.plot(t*params['omega_n']/np.pi, imp_response, label=f'zeta = {zeta:2.1f}', color=jet(zeta))

ax.set(xlabel='t*omega_n/pi')
ax.grid()
ax.legend()
ax.set(title='Impulsantworten')

ax = fig.add_subplot(1,2,2)
for idx, zeta in enumerate(zeta_range):
    H = ctrl.tf([params['omega_n']**2], [1.0, 2*zeta*params['omega_n'], params['omega_n']**2])
    t, step_response = ctrl.step_response(H, t_eval)
    ax.plot(t*params['omega_n']/np.pi, step_response, label=f'zeta = {zeta:2.1f}', color=jet(zeta))

ax.set(xlabel='t*omega_n/pi')
ax.grid()
ax.legend()
ax.set(title='Sprungantworten')

plt.show()



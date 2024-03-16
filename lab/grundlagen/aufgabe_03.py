#!/usr/bin/env python3
#
# Philipp Rapp
# fuer Veranstaltung T3ES2003 Regelungstechnik, 2024
# Labor 01: Grundlagen Laboruebung
#

# Aufgabe 2: Numerische Loesung von Differentialgleichungen

#%% Pakete

import matplotlib.pyplot as plt
from numpy import exp, linspace
from numpy import array, matmul, pi, eye, sin
from numpy.linalg import inv
from scipy.integrate import solve_ivp

#%% Euler vorwaerts fuer die erste Differentialgleichung

# Rechte Seite der Differenzengleichung
def next_x(x_k, step_size):
    x_k_plus_1 = (1.0 - step_size) * x_k
    return x_k_plus_1

# Anfangsbedingung
x_0 = 1.0

# Schrittweite festlegen
delta_t = 0.1

# Ende der Integration (in s)
t_f = 8.0

x = []
t = []

# Numerische Integration durchfuehren
current_t = 0.0
current_x = x_0
while current_t <= t_f:
    t.append(current_t)
    x.append(current_x)
    current_x = next_x(current_x, delta_t)
    current_t += delta_t

#%% Analytische Loesung
t_analytic = linspace(0.0, t_f, 1000)
x_analytic = [exp(-tau) for tau in t_analytic]

#%% Numerische Integration mit SciPy

# Definition der rechten Seite (right hand side, rhs) der
# Differentialgleichung (ordinary differential equation, ODE)
# dx/dt = f(t, x)
def ode_rhs(t, x):
    x_dot = -x
    return x_dot

scipy_integration_result = solve_ivp(ode_rhs, [0, t_f], array([x_0]))

#%% Ergebnisse darstellen
plt.figure(1)
plt.clf()
plt.plot(t, x, '-x', label=f'Euler vorwaerts Approximation (Schrittweite: {delta_t})')
plt.plot(t_analytic, x_analytic, '--', label='Analytische Loesung')
plt.plot(scipy_integration_result.t, scipy_integration_result.y.flatten(), '-.x', label='Numerische Loesung durch SciPy')
plt.grid(True)
plt.legend()
plt.xlabel('t')
plt.show()


#%% Euler vorwaerts fuer die zweite Differentialgleichung
# Hier benoetigen wir die Zustandsraumdarstellung

# Parameter omega und Systemmatrix definieren
omega = 2.0*pi
A = array([[0.0, 1.0], [-omega**2, 0.0]])

# Rechte Seite der Differenzengleichung
def next_x(x_k, step_size):
    B = A*step_size + eye(2)
    x_k_plus_1 = matmul(B, x_k)
    return x_k_plus_1

# Schrittweite festlegen
delta_t = 0.01

# Anfangsbedingung
x_0 = array([0.0, omega])

# Ende der Integration (in s)
t_f = 8.0

x = []
t = []

# Numerische Integration durchfuehren
current_t = 0.0
current_x = x_0
while current_t <= t_f:
    t.append(current_t)
    x.append(current_x)
    current_x = next_x(current_x, delta_t)
    current_t += delta_t

#%% Analytische Loesung
t_analytic = linspace(0.0, t_f, 1000)
x_analytic = [sin(omega*tau) for tau in t_analytic]


#%% Numerische Integration mit SciPy

# Definition der rechten Seite (right hand side, rhs) der
# Differentialgleichung (ordinary differential equation, ODE)
# dx/dt = f(t, x)
def ode_rhs(t, x):
    x_1 = x[0]
    x_2 = x[1]
    x_1_dot = x_2
    x_2_dot = -omega**2 * x_1
    x_dot = array([x_1_dot, x_2_dot])
    return x_dot

scipy_integration_result = solve_ivp(ode_rhs, [0, t_f], x_0)


#%% Ergebnisse darstellen
plt.figure(1)
plt.clf()
plt.plot(t, [xi[0] for xi in x], '-x', label=f'Euler vorwaerts Approximation (Schrittweite: {delta_t})')
plt.plot(t_analytic, x_analytic, '--', label='Analytische Loesung')
plt.plot(scipy_integration_result.t, scipy_integration_result.y[0,:], '-.x', label='Numerische Loesung durch SciPy')
plt.grid(True)
plt.legend()
plt.xlabel('t')
plt.show()


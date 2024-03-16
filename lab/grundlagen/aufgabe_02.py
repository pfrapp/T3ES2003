#!/usr/bin/env python3
#
# Philipp Rapp
# fuer Veranstaltung T3ES2003 Regelungstechnik, 2024
# Labor 01: Grundlagen Laboruebung
#

# Aufgabe 2: Erstellung von Plots

#%% Pakete

import matplotlib.pyplot as plt
from numpy import real, imag, arctan2, hypot, cos, sin, pi
from numpy import linspace, array, exp


#%% Teilaufgabe 1.2.1 von Labor 1
# Scatterplot von komplexen Zahlen

r_0 = [2.0, 2.0]
theta_0 = [pi/4.0, pi/2.0]

def polar_to_cartesian(r, theta):
    # Eulerformel
    x, y = cos(theta), sin(theta)
    # Skalieren mit Betrag r
    return [r*x, r*y]

for k, (r, theta) in enumerate(zip(r_0, theta_0)):
    z0 = polar_to_cartesian(r, theta)
    z1 = polar_to_cartesian(r, -theta)
    z2 = polar_to_cartesian(r, 0)
    z3 = polar_to_cartesian(r, theta+pi)
    z4 = polar_to_cartesian(r, -theta+pi)
    z5 = polar_to_cartesian(r, theta+2*pi)

    plt.figure(k)
    plt.clf()
    plt.scatter(z0[0], z0[1], label='z_0')
    plt.scatter(z1[0], z1[1], label='z_1', marker='x')
    plt.scatter(z2[0], z2[1], label='z_2', marker='+')
    plt.scatter(z3[0], z3[1], label='z_3', marker='v')
    plt.scatter(z4[0], z4[1], label='z_4', marker='^')
    plt.scatter(z5[0], z5[1], label='z_5', marker='s')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.xlim(-2.5,2.5)
    plt.ylim(-2.5,2.5)
    plt.title(f'Plot Nr. {k+1} fuer r_0={r}, theta_0={theta}')
    plt.show()

#%% Teilaufgabe 1.2.1 von Labor 1
# Kurven der Loesung von Dgln.

t = linspace(-1,4,1000)
y_1 = exp(-t)
omega = 2*pi
y_2 = sin(omega*t)

plt.figure('Loesung der Dgln.')
plt.clf()
plt.plot(t, y_1, label='y_1(t)')
plt.plot(t, y_2, label='y_2(t)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()



# %% Aufgabe 10 aus der Uebung, entspricht Ex. 3.30 aus Franklin.
# Im Zuge der Aufgabe muss entweder ein Graph abgelesen werden oder eine
# numerische Nullstellensuche durchgefuehrt werden.
# Hier passiert letzteres.

# %% Packages
import numpy as np

# %% Definition der impliziten Gleichung, die zu Null zu setzen ist, und der Jacobi-Matrix.

# phi hiess zuerst theta_1.
# Aber es muss eine andere Variable sein, da theta von der j-Achse aus zaehlt,
# und phi von der 1-Achse aus zaehlt.

# x1 = phi
# x2 = psi
# x3 = q

# Funktion
def f(x):
    x1, x2, x3 = x
    phi = x1
    psi = x2
    q = x3

    f = np.zeros((3,))
    f[0] = -3+np.cos(psi)-q*np.cos(phi)
    f[1] = 2+np.sin(psi)-q*np.sin(phi)
    f[2] = np.cos(phi)*np.cos(psi) + np.sin(phi)*np.sin(psi)

    return f

# Jacobi-Matrix
def jac(x):
    x1, x2, x3 = x
    phi = x1
    psi = x2
    q = x3

    J = np.zeros((3,3))
    J[0,0] = q*np.sin(phi)
    J[0,1] = -np.sin(psi)
    J[0,2] = -np.cos(phi)

    J[1,0] = -q*np.cos(phi)
    J[1,1] = np.cos(psi)
    J[1,2] = -np.sin(phi)

    J[2,0] = -np.sin(phi)*np.cos(psi) + np.cos(phi)*np.sin(psi)
    J[2,1] = -np.cos(phi)*np.sin(psi) + np.sin(phi)*np.cos(psi)
    J[2,2] = 0.0

    return J

# %% Numerische Ueberpruefung der Jacobi-Matrix

# Kleines epsilon
e = 0.0001

# Beliebiger Startpunkt
x0 = np.random.randn(3)
f0 = f(x0)
J = jac(x0)

# Approximation der Jacobi-Matrix durch Differenzenquotient
# in jede Richtung.
E = np.eye(3)
J_approx = [((f(x0 + e*direction) - f(x0))/e).reshape((3,1)) for direction in E]
J_approx = np.hstack(J_approx)

print('Jacobi-Matrix')
print(J)
print('Approximation der Jacobi-Matrix')
print(J_approx)
print('Rel. Fehler')
print(np.linalg.norm(J-J_approx)/np.linalg.norm(J))


# %% Numerische Loesung berechnung

# Startpunkt der Optimierung
# x1 = phi
# x2 = psi
# x3 = q

# Startpunkt fuer die erste Loesung
x0 = np.array([np.pi/2, np.pi/4, 2])

# Startpunkt fuer die zweite Loesung
# x0 = np.array([np.pi, np.pi/4 + np.pi, 2])

xk = x0
for idx in range(10):
    fk = f(xk)
    Jk = jac(xk)
    # Berechnung von x[k+1] anhand von x[k]
    x_next = xk - np.dot(np.linalg.inv(Jk), fk)
    print(x_next)
    xk = x_next

theta = xk[0] - np.pi/2
print(np.rad2deg(theta))

# %%
# %% Pakete

import matplotlib.pyplot as plt
import control as ctrl

# %% Teil (a)

omega_n = 3.0 # exakte Erfuellung der Anforderung
zeta = 0.1 # zwischen 0 und 1

G = ctrl.tf([omega_n**2], [1, 2*zeta*omega_n, omega_n**2])

t, y = ctrl.step_response(G)

plt.figure(1)
plt.clf()
plt.plot(t, y)
plt.grid()
plt.xlim(0,1.0)
plt.show()

# %% Teil (b)

omega_n = 1.0
zeta = 0.49 # exakte Erfuellung der Anforderung

G = ctrl.tf([omega_n**2], [1, 2*zeta*omega_n, omega_n**2])

t, y = ctrl.step_response(G)

plt.figure(1)
plt.clf()
plt.plot(t, y)
plt.grid()
# plt.xlim(0,1.0)
plt.show()

# %% Teil (c)

rho = 0.5 # exakte Erfuellung der Anforderung
zeta = 0.05
omega_n = rho / zeta

G = ctrl.tf([omega_n**2], [1, 2*zeta*omega_n, omega_n**2])

t, y = ctrl.step_response(G)

plt.figure(1)
plt.clf()
plt.plot(t, y)
plt.grid()
# plt.xlim(0,1.0)
plt.show()

# %% Teil (c)


omega_n = 5.0
zeta = 0.7
rho = zeta*omega_n
print(f'rho = {rho}')
assert rho > 0.5

G = ctrl.tf([omega_n**2], [1, 2*zeta*omega_n, omega_n**2])

t, y = ctrl.step_response(G)

plt.figure(1)
plt.clf()
plt.plot(t, y)
plt.grid()
# plt.xlim(0,1.0)
plt.show()



# %%

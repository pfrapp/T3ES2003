# %% Pakete

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# %%

omega_n = 1.0
zeta = 0.5
alpha = 1

G_no_zero = ctrl.tf([1], [1/omega_n**2, 2*zeta/omega_n, 1])

G = ctrl.tf([1/(alpha*zeta*omega_n), 1], [1/omega_n**2, 2*zeta/omega_n, 1])
print(G)

# %%

t_, y_ = ctrl.step_response(G_no_zero)
t, y = ctrl.step_response(G)

fig = plt.figure('Step response')
plt.clf()
plt.plot(t,y)
plt.plot(t_, y_, linestyle='dashed')
plt.grid(True)
plt.show()

plt.figure('Pol-Nullstellen')
ctrl.pzmap(G)


# %%

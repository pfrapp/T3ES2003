# %% Packages

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# %% Draw a heatmap

# Raum R^2
X, Y = np.mgrid[-5:5:0.02, -5:5:0.02]
Z = np.zeros_like(X)

# Raum C
S = X + 1j*Y

def G_fun(s):
    val = 1.0 / s
    # val = s
    s1 = 2+3j
    s2 = 2-3j
    s3 = -3
    val = (s-s3)/((s-s1)*(s-s2))
    return val

G = G_fun(S)

# Z = np.abs(G)
Z = np.rad2deg(np.angle(G))

plt.figure(1)
plt.clf()
plt.contourf(X, Y, Z, levels=64)
plt.colorbar()
plt.show()

# %% Fancy plotting

# View limits
z_min, z_max = -200, 200

fig = plt.figure(1, figsize=(10,8))
plt.clf()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.view_init(elev=20, azim=300)
ax.plot_wireframe(X, Y, Z, color=[0,0,0], linewidth=0.5)
ax.contourf(X, Y, Z, offset=z_min - 20, levels=32)
ax.grid(True)
ax.set(xlabel='x_1'); ax.set(ylabel='x_2')
ax.set(xlim=(-5,5)); ax.set(ylim=(-5,5)); ax.set(zlim=(z_min - 20,z_max))
plt.show()


# %% Uebung 5: Frequenzkennlinienverfahren
# Aufgabe 1

# %% Pakete

import matplotlib.pyplot as plt
import control as ctrl

# %% Definition der Uebetragungsfunktion

s = ctrl.tf('s')
G = 1/(s+7)
print(G)

# %% Darstellung des Bode Diagramms

# Darstellung des Betrags in dB, d.h. Uebergabe
# von dB=True
plt.figure('Bode')
plt.clf()
ctrl.bode(G, dB=True)
plt.show()

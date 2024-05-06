#%% Labor 3: Reglersynthese
#
# Philipp Rapp
# fuer Veranstaltung Regelungstechnik, 2024
#


#%% Pakete

from control import tf, step_response, feedback, series, pole, pzmap
import matplotlib.pyplot as plt
from numpy import linspace


#%% Labor Aufg. 3.1 -- P-Regler

t_eval = linspace(0,10,1000)

s = tf('s')
G = 1/(s**2+2*s+1)

t, h = step_response(G, T=t_eval)

plt.figure(1)
plt.clf()
plt.plot(t, h)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

plt.figure(2)
plt.clf()
plt.plot(t, h, label='Ungeregeltes System')

# Perfekter Sensor: Übertragungsfunktion = 1
G_sensor = tf([1], [1])
    
for k_P in [1,2,5,10,100]:
    K = tf([k_P], [1])
    
    G_sys = feedback(series(K, G), G_sensor)

    t, h_sys = step_response(G_sys, T=t_eval)
    plt.plot(t, h_sys, label=f'k_P={k_P}')
    
plt.grid(True)
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()


#%% Labor Aufg. 3.2 -- Robustheit
# Aufgabenteile (a)-(d): Steuerung
# Oder: Was passiert beim kuerzen instabiler Pole?

s = tf('s')
# Parameter der Strecke
a = 1.0

# Aufgabenteil (c): a sei exakt bekannt
a_K = a

# Aufgabenteil (d)
# Approximation des Streckenparameters 'a' in der Steuerung
a_K = 0.99*a

K = (s-a_K)/(s+1)
G = (s+1)/(s-a)
GK = series(K, G)

# Pole ausgeben: Man sieht: Der Pol bei a = 1.0 besteht weiterhin.
print('Pole der offenen Steuerkette:')
print(pole(GK))

t_eval = linspace(0,100,1000)
t, h = step_response(GK, T=t_eval)
plt.figure(1)
plt.clf()
plt.plot(t, h)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()

#%% Labor Aufg. 3.2 -- Robustheit
# Aufgabenteile (e)-(g): Regelung

# Aufgabenteil (f): a sei exakt bekannt
a_K = a

# Aufgabenteil (g)
# Approximation des Streckenparameters 'a' im Regler
a_K = 0.99*a

# P-Regler
p = -3
k_P = -(p-a_K)/(p+1)

print(f'k_P = {k_P} (fuer a = {a})')

K = k_P
G = (s+1)/(s-a)
GK = series(K, G)
G_cl = feedback(GK, tf([1],[1]))

print('Pole des geschlossenen Kreises:')
print(pole(G_cl))


t_eval = linspace(0,100,1000)
t, h = step_response(G_cl, T=t_eval)
plt.figure(1)
plt.clf()
plt.plot(t, h)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()



#%% Labor Aufg. 3.3 -- Bleibende Regelabweichung
# Entspricht im Wesentlichen der Aufg. 5.2 aus der Uebung 5
#

s = tf('s')
G = 1/s
K = 2*(s+1)/s
H = 100/(s+100)

# Uebertragung von W auf Y (Annahme: Z=0)
G_WY = feedback(series(K, G), H)

# Uebertragung von Z auf Y (Annahme: W=0)
G_ZY = feedback(G, series(H, K))

# Folgeregelungsfehler bei W = Einheitssprung und Z = 0
t_eval = linspace(0,30,3000)
t, h = step_response(G_WY, T=t_eval)

print(f'G_ZY = {G_ZY}')

plt.figure(3)
plt.clf()
plt.plot(t, h, label='y(t) (Regelgroesse)')
plt.plot([0, 0, 10], [0, 1, 1], label='w(t) (Fuehrungsgroesse)')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('w(t), y(t)')
plt.legend()
plt.title('Fuehrungsgroesse: Einheitssprung')
plt.show()

# Folgeregelungsfehler bei W = Rampe und Z = 0
# Um die Rampe zu erzeugen, schalten wir einen Integrator vor das
# Gesamtsystem.
# w_urspruenglich --> (1/s) --> w_integriert
# Sprung          --> (1/s) --> Rampe
G_integrator = 1/s
t, y = step_response(series(G_integrator, G_WY), T=t_eval)

print(f'G_WY = {G_WY}')

# Rampe als Fuehrungsgroesse
w = t
# Regelfehler (e = w - y)
e = w - y

plt.figure(4)
plt.clf()
plt.plot(t, y, label='y(t) (Regelgroesse)')
plt.plot(t, w, label='w(t) (Fuehrungsgroesse)')
plt.plot(t, e, label='e(t) (Regelfehler)')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('w(t), y(t)')
plt.legend()
plt.title('Fuehrungsgroesse: Rampe')
plt.show()


#%% Labor Aufg. 3.4 -- Stabilitaetsbereich

s = tf('s')
G = (10*s+5)/((s+8)*(s-1))

t, h = step_response(G)

#
# Aufgabenteil (a): Ungeregeltes System
#

# Sprungantwort
plt.figure(4)
plt.clf()
plt.plot(t, h, label='Sprungantwort des ungeregelten Systems')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()

# Pol-Nullstellen-Diagramm
plt.figure(5)
plt.clf()
pzmap(G)



#%% Aufg. 3.4 Aufgabenteil (b)

k_P = 1.0
k_P = 2.0
K = k_P
GK = series(G, K)
G_cl = feedback(GK, tf([1], [1]))

t_eval = linspace(0,10,1000)
t, h = step_response(G_cl)

# Sprungantwort
plt.figure(4)
plt.clf()
plt.plot(t, h, label=f'Sprungantwort fuer k_P={k_P}')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()

# Pol-Nullstellen-Diagramm
plt.figure(5)
plt.clf()
pzmap(G_cl)


#%% Aufg. 3.4 Aufgabenteil (c)
# PD-Regler

k_P = 8.0
k_D = 1.0
K = k_P + k_D*s
GK = series(G, K)
G_cl = feedback(GK, tf([1], [1]))

t_eval = linspace(0,10,1000)
t, h = step_response(G_cl)

# Sprungantwort
plt.figure(4)
plt.clf()
plt.plot(t, h, label=f'Sprungantwort fuer PD-Regler mit k_P={k_P}, k_D={k_D}')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()

# Pol-Nullstellen-Diagramm
plt.figure(5)
plt.clf()
pzmap(G_cl)

#%% Aufg. 3.4 Aufgabenteil (d)
# PI-Regler

k_P = 1.0
k_I = 8.0
K = k_P + k_I/s
GK = series(G, K)
G_cl = feedback(GK, tf([1], [1]))

t_eval = linspace(0,10,1000)
t, h = step_response(G_cl)

# Sprungantwort
plt.figure(4)
plt.clf()
plt.plot(t, h, label=f'Sprungantwort fuer PI-Regler mit k_P={k_P}, k_I={k_I}')
plt.grid(True)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()

# Pol-Nullstellen-Diagramm
plt.figure(5)
plt.clf()
pzmap(G_cl)



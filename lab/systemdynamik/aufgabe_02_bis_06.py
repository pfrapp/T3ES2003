#!/usr/bin/env python3
#
# Philipp Rapp
# fuer Veranstaltung T3ES2003 "Regelungstechnik"
# Labor 02: Systemdynamik
#

# Wir arbeiten mit der 'Python Control Systems Library'.
# Eine Dokumentation ist unter
# https://python-control.readthedocs.io/
# verfügbar.


#%% Notwendige Pakete importieren

import matplotlib.pyplot as plt
from numpy import linspace, any, all, unique, real, imag
import control as ctrl

#%% Augabe 02: Sprungantwort
# Der Sprung ist ein mathematisches Modell für einen
# Einschaltvorgang.

# Zuerst definieren wir die Uebertragungsfunktion.
# Die geschieht mit Hilfe der Funktion 'tf' (kurz für: transfer function).
G = ctrl.tf([1], [1, 1])

# Nun berechnen wir die Werte der Sprungantwort.
# Dies geschieht mit Hilfe der Funktion 'step_response'.
# Wir können der Funktion mitteilen, für welche Zeitpunkte 't'
# wir die Sprungantwort ausgewertet (bzw. evaluiert) haben wollen.
t_eval = linspace(0,10,1000)
h = ctrl.step_response(G, t_eval)

plt.figure('Sprungantwort')
plt.clf()
plt.plot(h[0], h[1])
plt.xlabel('t')
plt.ylabel('h(t)')
plt.grid(True)
plt.title('Sprungantwort')
plt.show()

#%% Aufgabe 03: Impulsantwort
# Der Impuls ist ein mathematisches Modell für einen Schlag.

# Die Berechnung der Impulsantwort erfolgt mit Hilfe der
# Funktion 'impulse_response'.
g = ctrl.impulse_response(G, t_eval)

plt.figure('Impulsantwort')
plt.clf()
plt.plot(g[0], g[1])
plt.xlabel('t')
plt.ylabel('g(t)')
plt.grid(True)
plt.title('Impulsantwort')
plt.show()

#%% Aufgabe 04: Blockdiagramme

from control import tf, series, parallel, feedback

# s = tf('s')
s = ctrl.TransferFunction.s

# Im ersten Schritt erstellen wir die Parallelschaltung
# von '2' und '4/s' (wie in der Vorlesung).
G1 = 2
G2 = 4/s
G3 = parallel(G1, G2)

# Im zweiten Schritt berechnen wir die Serienschaltung (Reihenschaltung)
# der eben erhaltenen Parallelschaltung G3 mit '1/s'
# (wie in der VL).
G4 = 1/s
G5 = series(G3, G4)

# Im dritten Schritt fügen wir die negative Rückführung ein.
# Im Rückführpfad findet sich keine Übertragungsfunktion -- das Signal
# wird direkt zum Summationspunkt geführt.
# Dies entspricht einer Multiplikation des Signals mit '1' (dem neutralen
# Element der Multiplikation).
# Wir verwenden also als Übertragungsfunktion im Rückführpfad '1',
# da wir gezwungen sind der Funktion 'feedback' dieses Argument zu
# übergeben.
# Das Vorzeichen der Rückführung kann ebenfalls als Argument übergeben
# werden. Betrachten Sie hierzu die Hilfe zur Funktion, indem Sie
# help(feedback)
# ausführen.
# Standardmäßig wird eine negative Rückführung angenommen.
G_feedback = 1
G_gesamt = feedback(G5, G_feedback, -1)

# Ergebnis ausgeben
print(G_gesamt)

# Wir erhalten das Ergebnis
#    2 s + 4
# -------------
# s^2 + 2 s + 4
#
# Dieses stimmt mit dem Ergebnis aus der VL überein.

#%% Aufgabe 05: Stabilität
# Vgl. Aufgabe 5 aus der Uebung 2 zur Systemdynamik.

#%% Teilaufgabe 1: Untersuchung auf Stabilität

# Definition der Übertragungsfunktionen in Form der Polynomkoeffizienten.
# Wir nutzen eine Liste, und jedes Listenelement besteht aus einem
# Dictionary. Die Keys des Dictionaries sind 'zaehler' und 'nenner'.
uebertragungs_funktionen = ( \
                {'zaehler': [1],     'nenner': [1, 0]},      \
                {'zaehler': [1],     'nenner': [1, 0, 0]},   \
                {'zaehler': [1, 1],  'nenner': [1, 3, 2]},   \
                {'zaehler': [1, -2], 'nenner': [1, -1, -2]}, \
                {'zaehler': [1],     'nenner': [1, 0, 9]},   \
                {'zaehler': [1, 3],  'nenner': [1, 2, 4]},   \
               )

# Wir nutzen eine Schleife, um über alle Übertragungsfunktionen zu
# iterieren. Die Funktion 'enumerate' gibt uns dabei auch den Laufindex.
for idx, ue_funktion in enumerate(uebertragungs_funktionen):
    # Erstellung der Uebertragungsfunktion
    G = ctrl.tf(ue_funktion['zaehler'], ue_funktion['nenner'])
    # Berechnung der Pole der Uebertragungsfunktion
    poles = ctrl.pole(G)
    # Ausgabe der Pole
    print(f'Die Pole der Uebertragungsfunktion G_{idx+1}(s)=\n{G}\nsind')
    print(poles)
    # Alle Pole in der offenen linken Halbebene --> stabil.
    # Ein Pole in der rechten Halbebene --> instabil.
    # Einfache Pole auf der imaginaeren Achse --> grenzstabil.
    # Mehrfache Pole auf der imaginaeren Aches --> instabil.
    if all(real(poles) < 0.0):
        stabilitaet = 'stabil'
    elif any(real(poles) > 0.0):
        stabilitaet = 'instabil'
    else:
        _, vielfachheit = unique(poles, return_counts=True)
        # Hinweis: Der Underscore _ ignoriert den Rueckgabewert (in dem Fall
        # das Array mit eindeutigen Polen).
        # Wir sind nur an der Vielfachheit der Pole interessiert, und
        # nutzen deshalb 'return_counts=True'.
        if vielfachheit[0] > 1:
            stabilitaet = 'instabil'
        else:
            stabilitaet = 'grenzstabil'
    print(f'\nDas System G_{idx+1}(s) ist {stabilitaet}.\n\n')
    print('----------------------------------------------------')

#%% Teilaufgabe 2: Einfluss der Rückführung auf die Stabilität

G1 = ctrl.tf([1], [1,1,1])
# Pole ohne Rueckfuehrung
poles_without_feedback = ctrl.pole(G1)
print(f'Pole der Strecke (ohne Rueckfuehrung): {poles_without_feedback}')
if all(real(poles_without_feedback) < 0.0):
    print('Die Strecke G1 ist stabil.')

# Mit Rueckfuehrung: Variante 1
G2 = ctrl.tf([5] ,[1, 1])
G_feedback = ctrl.feedback(G1, G2)
poles_with_feedback_variant_1 = ctrl.pole(G_feedback)
print(f'Pole des Gesamtsystems mit Rueckfuehrung (Variante 1): {poles_with_feedback_variant_1}')
# --> Das System ist instabil.

# Mit Rueckfuehrung: Variante 2
G2 = ctrl.tf([5] ,[5, 1])
G_feedback = ctrl.feedback(G1, G2)
poles_with_feedback_variant_2 = ctrl.pole(G_feedback)
print(f'Pole des Gesamtsystems mit Rueckfuehrung (Variante 2): {poles_with_feedback_variant_2}')
# --> Das System ist stabil.

# Wir sehen, dass wir durch eine Rückführung (feedback) die
# Stabilität verändern können.
# Dadurch können wir instabile Strecken stabilisieren (die ist eine
# der Kernaufgaben der Regelungstechnik).
# Durch die Rückführung können aber auch bereits von sich aus
# stabile Strecken destabilisiert werden,
# wie wir hier in dieser Teilaufgabe gesehen haben.
# Dies kann sogar dann passieren, wenn wir (wie hier) eine
# negative Rückführung vorliegen haben.

#%% Aufgabe 06: Pol-Nullstellen-Diagramme

# Definition der Übertragungsfunktionen in Form der Polynomkoeffizienten.
# Wir nutzen eine Liste, und jedes Listenelement besteht aus einem
# Dictionary. Die Keys des Dictionaries sind 'zaehler' und 'nenner'.
uebertragungs_funktionen = ( \
                {'zaehler': [1], 'nenner': [1, 0]},       \
                {'zaehler': [1], 'nenner': [1, 0, 0]},    \
                {'zaehler': [1], 'nenner': [2, 1]},       \
                {'zaehler': [1], 'nenner': [2, -1]},      \
                {'zaehler': [1], 'nenner': [8, 1]},       \
                {'zaehler': [1], 'nenner': [8, -1]},      \
                {'zaehler': [1], 'nenner': [1, 0, 1]},    \
                {'zaehler': [1], 'nenner': [1, 0, 9]},    \
                {'zaehler': [1], 'nenner': [1, 0.2, 1]},  \
                {'zaehler': [1], 'nenner': [1, -0.2, 1]}, \
               )


#%% Teilaufgabe 1: Plotten der Pol-Nullstellen-Diagramme
# Dabei überprüfen wir auch gleich auf Stabilität.
# Hinweis: Es gibt hier nur Pole, keine Nullstellen.

for idx, ue_funktion in enumerate(uebertragungs_funktionen):
    G = ctrl.tf(ue_funktion['zaehler'], ue_funktion['nenner'])
    plt.figure(idx+1)
    plt.clf()
    ctrl.pzmap(G)
    plt.grid(True)
    plt.annotate(f'{G}', xy=(0.8, 0.7), xycoords='figure fraction')
    plt.title(f'Pol-Nullstellendiagramm fuer G_{idx+1}(s)')
    # Ueberpruefung auf Stabilitaet.
    # Zuerst erfolgt die Berechnung der Pole.
    poles = ctrl.pole(G)
    print(f'Pole: {poles}\n')
    # Alle Pole in der offenen linken Halbebene --> stabil.
    # Ein Pole in der rechten Halbebene --> instabil.
    # Einfache Pole auf der imaginaeren Achse --> grenzstabil.
    # Mehrfache Pole auf der imaginaeren Aches --> instabil.
    if all(real(poles) < 0.0):
        stabilitaet = 'stabil'
    elif any(real(poles) > 0.0):
        stabilitaet = 'instabil'
    else:
        _, vielfachheit = unique(poles, return_counts=True)
        # Hinweis: Der Underscore _ ignoriert den Rueckgabewert (in dem Fall
        # das Array mit eindeutigen Polen).
        # Wir sind nur an der Vielfachheit der Pole interessiert, und
        # nutzen deshalb 'return_counts=True'.
        if vielfachheit[0] > 1:
            stabilitaet = 'instabil'
        else:
            stabilitaet = 'grenzstabil'
    print(f'Das System G_{idx+1}(s)={G} ist {stabilitaet}\n\n')

#%% Teilaufgabe 2: Darstellung der Impulsantworten mitsamt der Pol-Nullstellen-Diagramme
    
t_eval = linspace(0,20,1000)

for idx, ue_funktion in enumerate(uebertragungs_funktionen):
    G = ctrl.tf(ue_funktion['zaehler'], ue_funktion['nenner'])
    poles = ctrl.pole(G)
    fig = plt.figure(idx+1)
    plt.clf()
    # Pol-Nullstellen-Diagramm (nur Pole hier)
    ax = fig.add_subplot(1, 2, 1)
    ax.scatter(real(poles), imag(poles), marker='x')
    ax.grid(True)
    ax.set(xlabel='Re(s)')
    ax.set(ylabel='Im(s)')
    ax.set(xlim=(-4,4))
    ax.set(ylim=(-4,4))
    # Impulsantwort
    g = ctrl.impulse_response(G, t_eval)
    ax = fig.add_subplot(1, 2, 2)
    ax.plot(g[0], g[1])
    ax.grid(True)
    ax.set(xlabel='t')
    ax.set(ylabel=f'g_{idx+1}(t)')
    ax.set(ylim=(-3,3))
    fig.suptitle(f'G_{idx+1}(s)')

# Die Lage des Realteils der Polstellen beeinflusst die Auf- oder Abklingzeit.
# Je weiter links ein stabiler Pol sich befindet, desto schneller
# klingt die Impulsantwort ab.
# Je weiter rechts sich ein instabiler Pol befindet, desto schneller
# divergiert die Impulsantwort.

# Die Lage des Imaginärteils der Polstellen beeinflusst
# die Schwingungsfrequenz.
# Die Polstellen treten immer als konjugiert komplexe Pole auf.
# Je weiter die Polstellen von der reellen Achse entfernt sind
# (je grösser also der Betrag des Imaginärteils ist),
# desto höher (also schneller) ist die Schwingungsfrequenz.



#%% Teilaufgabe 3: Darstellung der Sprungantworten mitsamt der Pol-Nullstellen-Diagramme
    
t_eval = linspace(0,20,1000)

for idx, ue_funktion in enumerate(uebertragungs_funktionen):
    G = ctrl.tf(ue_funktion['zaehler'], ue_funktion['nenner'])
    poles = ctrl.pole(G)
    fig = plt.figure(idx+1)
    plt.clf()
    # Pol-Nullstellen-Diagramm (nur Pole hier)
    ax = fig.add_subplot(1, 2, 1)
    ax.scatter(real(poles), imag(poles), marker='x')
    ax.grid(True)
    ax.set(xlabel='Re(s)')
    ax.set(ylabel='Im(s)')
    ax.set(xlim=(-4,4))
    ax.set(ylim=(-4,4))
    # Sprungantwort
    h = ctrl.step_response(G, t_eval)
    ax = fig.add_subplot(1, 2, 2)
    ax.plot(h[0], h[1])
    ax.grid(True)
    ax.set(xlabel='t')
    ax.set(ylabel=f'h_{idx+1}(t)')
    ax.set(ylim=(-3,3))
    fig.suptitle(f'G_{idx+1}(s)')

# Die Lage des Realteils der Polstellen beeinflusst die Einschwingzeit
# (bei stabilen Systemen) bzw. die Geschwindigkeit, in der das
# Signal divergiert (bei instabilen Systemen).
# Je weiter links ein stabiler Pol sich befindet, desto schneller
# schwingt sich die Sprungantwort ein.
# Je weiter rechts sich ein instabiler Pol befindet, desto schneller
# divergiert die Sprungantwort.

# Die Lage des Imaginärteils der Polstellen beeinflusst
# die Schwingungsfrequenz.
# Die Polstellen treten immer als konjugiert komplexe Pole auf.
# Je weiter die Polstellen von der reellen Achse entfernt sind
# (je grösser also der Betrag des Imaginärteils ist),
# desto höher (also schneller) ist die Schwingungsfrequenz.



# %%

# T4ES2003

Repository zur Bereitstellung von Code fuer die Laboruebungen.

Urspruenglich fuer T3ES2003 im Fruehjahr 2024, fortgefuehrt fuer T3ES2003 im Fruehjahr 2025
und jetzt T4ES2003 im Fruehjahr 2026.

## Teams Link fuer die Sprechstunde

Fuer die Sprechstunde bzw. hybride oder remote Veranstaltungen nutzen wir ein
[MS Teams Meeting](https://teams.microsoft.com/meet/33449900809047?p=QV0g1vrXS8uWx1j4bh).

## Videos der Vorlesung

Neben den Videos in Moodle (wo die Dateigroesse limitiert ist)
biete ich die Videos der Vorlesung in höherer Auflösung und mit Zeitstempeln
auf [YouTube](https://www.youtube.com/playlist?list=PLzjPCNvpl75TjOh5PryMuv_X21sxSX71V) an.

Interne bzw. organisatorische Inhalte sind herausgeschnitten.

Pro 3h Präsenzblock Block (ein Termin) gibt es zwei Teile zu je ca. 90 Minuten.
Bei den Videos zur Unterstützung des Selbststudiums ist die zeitliche Aufteilung entsprechend flexibler.

| Termin               | Teil          | Link                                         | Modus         |
|----------------------|---------------|----------------------------------------------|---------------|
| 1                    | 1             | [YouTube](https://youtu.be/GeIb4kHuG18)      | Präsenz       |
| 1                    | 2             | [YouTube](https://youtu.be/L6NKCIVpR8o)      | Präsenz       |
| 2                    | 1             | folgt                                        | Präsenz       |
| 2                    | 2             | folgt                                        | Präsenz       |
| 3                    | 1             | folgt                                        | Präsenz       |
| 3                    | 2             | folgt                                        | Präsenz       |
| 4                    | 1             | folgt                                        | Präsenz       |
| 4                    | 2             | folgt                                        | Präsenz       |
| 5                    | 1             | folgt                                        | Präsenz       |
| 5                    | 2             | folgt                                        | Präsenz       |
| 6                    | 1             | folgt                                        | Präsenz       |
| 6                    | 2             | folgt                                        | Präsenz       |
| 7                    |               | [YouTube](https://youtu.be/2kCm9ZS496Q)      | Selbststudium |


## Termine Sprechstunde

Um das Selbststudium zu erleichtern biete ich eine virtuelle Sprechstunde an.

Ich werde jeweils bis zu 5 min. nach Start der Sprechstunde im MS Teams Termin bleiben
aber diesen wieder verlassen, falls bis dahin niemand weiteres beigetreten ist.

Link zum Teams Meeting s. oben.
Die Sprechstunde wird nicht aufgezeichnet.

| Tag                  | Uhrzeit       | Dauer   | Hinweis          |
|----------------------|---------------|---------|------------------|
| Mittwoch, 25.03.2026 | 19.00 Uhr     | 1h      | Keine Teilnehmer |
| Mittwoch, 01.04.2026 | 19.00 Uhr     | 1h      |                  |


## Setup eines virtuellen Python environments

Unter Windows stark empfohlen, unter Linux/macOS optional:
Erstellung eines conda environments.<br/>
Grund: Windows hat per default kein Python, Linux/macOS hat ein Systempython.<br />

```
# Erstellung
$ conda create -n t4es2003 python=3.9

# Ueberpruefen ob es da ist
$ conda env list

# Aktivieren
$ conda activate t4es2003

# Check ob der richtige Interpreter genutzt wird (nur Linux/macOS)
$ which python3
$ which pip3

# Umgebung deaktivieren
$ conda deactivate

# Loeschen der Umgebung
$ conda env remove -n t4es2003
```

Mit conda nicht notwendig, unter Linux/macOS bei Nutzung des Systempythons stark empfohlen:
Erstellung einer virtuellen Umgebung.
```
# Erstellung
$ python3 -m venv ~/venv/t4es2003

# Aktivierung
$ . ~/venv/t4es2003/bin/activate

# Check ob der richtige Interpreter genutzt wird (nur Linux/macOS)
$ which python3
$ which pip3

# Deaktivieren
$ deactivate

# Loeschen
$ rm -r ~/venv/t4es2003
```

Fuer die Nutzung des Interpreters in VS Code empfiehlt es sich, `ipykernel` zu installieren.
Dazu zuerst das venv oder conda env aktivieren!

```
# Installation des Pakets "ipykernel"
$ pip3 install ipykernel
# Installation der kernel specification fuer Jupyter in den user space
$ python3 -m ipykernel install --user (bei Linux)
Installed kernelspec python3 in /Users/XXX/Library/Jupyter/kernels/python3
$ python -m ipykernel install --user (bei Windows)
Installed kernelspec python3 in C:\Users\XXX\AppData\Roaming\jupyter\kernels\python3
```

Installation von numpy via `pip3 install numpy`

In VS Code: Oeffnen der Command Palette via
Cmd+Shift+P (macOS) bzw. Strg+Shift+P (Windows)

Python: Select Interpreter<br />
Dann den "t4es2003" Interpreter auswaehlen.

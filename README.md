# T3ES2003
Code exchange repository for T3ES2003 (originally for spring 2024, updated for spring 2025)

## Setup eines virtuellen Python environments

Unter Windows stark empfohlen, unter Linux/macOS optional:
Erstellung eines conda environments.<br/>
Grund: Windows hat per default kein Python, Linux/macOS hat ein Systempython.<br />

```
# Erstellung
$ conda create -n t3es2003 python=3.9

# Ueberpruefen ob es da ist
$ conda env list

# Aktivieren
$ conda activate t3es2003

# Check ob der richtige Interpreter genutzt wird (nur Linux/macOS)
$ which python3
$ which pip3

# Umgebung deaktivieren
$ conda deactivate

# Loeschen der Umgebung
$ conda env remove -n t3es2003
```

Mit conda nicht notwendig, unter Linux/macOS bei Nutzung des Systempythons stark empfohlen:
Erstellung einer virtuellen Umgebung.
```
# Erstellung
$ python3 -m venv ~/venv/t3es2003

# Aktivierung
$ . ~/venv/t3es2003/bin/activate

# Check ob der richtige Interpreter genutzt wird (nur Linux/macOS)
$ which python3
$ which pip3

# Deaktivieren
$ deactivate

# Loeschen
$ rm -r ~/venv/t3es2003
```

Fuer die Nutzung des Interpreters in VS Code empfiehlt es sich, `ipykernel` zu installieren.
Dazu zuerst das venv oder conda env aktivieren!

```
# Installation des Pakets "ipykernel"
$ pip3 install ipykernel
# Installation der kernel specification fuer Jupyter in den user space
$ python3 -m ipykernel install --user
Installed kernelspec python3 in /Users/XXX/Library/Jupyter/kernels/python3
```

Installation von numpy via `pip3 install numpy`

In VS Code: Oeffnen der Command Palette via
Cmd+Shift+P (macOS) bzw. Strg+Shift+P (Windows)

Python: Select Interpreter<br />
Dann den "t3es2003" Interpreter auswaehlen.

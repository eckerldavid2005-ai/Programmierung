#!/usr/bin/env python
# Praktikum P3 -- Ergaenzung: matplotlib / sin-Plot
# Diese Aufgabe ist bewusst NICHT Teil der pytest-Abnahme (p3.py/test_p3.py):
# geplottet wird visuell, dafuer gibt es hier die Kommentar-Anleitung wie gehabt.
#
# Teil 1: der "klassische" Weg mit Listen (aus der Vorlesung)
# Teil 2: dieselbe Aufgabe mit numpy in (fast) einer Zeile

import math
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Teil 1: sin(x) fuer x = 0..360 Grad mit Listen plotten
# ------------------------------------------------------------

# Werte fuer x in Grad
x_grad = range(360)

# leere Liste fuer y-Werte anlegen
y=[]

for x in x_grad:
    x_bogen = (x / 180 * math.pi)   # optional: math.radians(x)
    # math.sin(x_bogen) an die y-Werte-Liste anhaengen
    y.append(math.sin(x_bogen))

# Hinweis: Das Skript laeuft erst, wenn ALLE pass ersetzt sind
# (sonst: NameError: name 'y' is not defined)
plt.grid()
plt.plot(x_grad, y)
plt.title("Teil 1: sin(x) mit Listen")
plt.show()







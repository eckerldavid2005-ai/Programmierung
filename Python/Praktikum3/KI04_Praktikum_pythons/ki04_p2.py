#!/usr/bin/env python
# Praktikum KI4 -- Teil 2: Lineare Regression "von Hand" + Fehlermasse
# Alle Tests sind zunaechst ROT -- arbeiten Sie die Funktionen von
# oben nach unten ab, bis alles GRUEN ist.
# Danach koennen Sie die Funktionen mit dem Ergebnis von sklearn
# vergleichen (unten im __main__-Block).

import numpy as np
import pandas as pd
import pathlib


datapath = pathlib.Path() / "datasets"


# ------------------------------------------------------------
# Fehlermasse (Messdaten: Modell y_ist, Vorhersage: y_pred)
# ------------------------------------------------------------

def fehler_summe(y_ist, y_pred):
    # Summe der Abweichungen (y_ist - y_pred) zurueckgeben
    return np.sum(y_ist - y_pred)


def fehler_betrags_summe(y_ist, y_pred):
    # Summe der Betraege der Abweichungen zurueckgeben
    return np.sum(np.abs(y_ist-y_pred))


def sse(y_ist, y_pred):
    # Summe der quadrierten Fehler (Sum of Squared Errors) zurueckgeben
    return np.sum((y_ist - y_pred) *(y_ist - y_pred))


def mse(y_ist, y_pred):
    # Mittlerer quadratischer Fehler (Mean Square Error) zurueckgeben
    return np.mean((y_ist - y_pred) *(y_ist - y_pred))


def rmse(y_ist, y_pred):
    # Wurzel aus dem MSE zurueckgeben -- Achtung:
    # erst mitteln, dann die Wurzel ziehen!
    a=np.mean((y_ist - y_pred)*(y_ist - y_pred))
    return np.sqrt(a)


# ------------------------------------------------------------
# Lineare Regression von Hand (geschlossene Form, 2D)
# ------------------------------------------------------------

def steigung_a(x, y):
    # Steigung a nach der Formel aus der Vorlesung:
    #   a = sum((x_i - x_mean) * (y_i - y_mean)) / sum((x_i - x_mean)^2)
    # zurueckgeben. Hinweis: np.mean, np.sum
    return np.sum((x - np.mean(x)) * (y - np.mean(y))) / np.sum((x - np.mean(x)) ** 2)


def achsenabschnitt_b(x, y):
    # Achsenabschnitt b nach der Formel aus der Vorlesung:
    #   b = y_mean - a * x_mean     (wobei a = steigung_a(x, y))
    # zurueckgeben
    a=steigung_a(x, y)
    return np.mean(y) - a * np.mean(x)


def vorhersage(x_neu, x, y):
    # fuer den (einen) neuen x-Wert x_neu die Vorhersage
    #   y = a * x_neu + b
    # mit den oben berechneten Parametern zurueckgeben
    a = steigung_a(x, y)
    b = achsenabschnitt_b(x, y)
    return a * x_neu + b


# ------------------------------------------------------------
# Anwendung auf die Praktikumsdaten (zum Vergleich mit sklearn)
# ------------------------------------------------------------

if __name__ == "__main__":
    full_country_stats = pd.read_csv(datapath / "lifesat_full.csv")
    x = full_country_stats["GDP per capita (USD)"].values
    y = full_country_stats["Life satisfaction"].values

    a = steigung_a(x, y)
    b = achsenabschnitt_b(x, y)
    print(f"Von Hand:  f(x) = {a:.3e} * x + {b:.3}")

    # Vergleich: was liefert sklearn?
    from sklearn import linear_model
    lin1 = linear_model.LinearRegression()
    lin1.fit(x.reshape(-1, 1), y)
    print(f"sklearn:   f(x) = {lin1.coef_[0]:.3e} * x + {lin1.intercept_:.3f}")

    # Fehlermasse fuer unser "von Hand"-Modell:
    y_pred = a * x + b
    print(f"MSE:  {mse(y, y_pred):.4f}")
    print(f"RMSE: {rmse(y, y_pred):.4f}")

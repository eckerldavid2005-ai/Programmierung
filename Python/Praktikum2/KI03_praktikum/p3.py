#!/usr/bin/env python
# Praktikum P3 (pytest-Variante): NumPy und Pandas
# Alle Tests sind zunaechst ROT -- arbeiten Sie die Funktionen von
# oben nach unten ab, bis alles GRUEN ist.
# Die Plot-Aufgabe (matplotlib / sin) liegt AUSSERHALB der Tests
# in der Datei p3_plot.py -- bearbeiten Sie sie dort.

import math
import numpy as np
import pandas as pd


# ------------------------------------------------------------
# NumPy
# ------------------------------------------------------------

def create_array():
    # ein numpy-Array mit den Werten 1, 2, 3 erzeugen und zurueckgeben
    return np.array([1, 2, 3])
    


def create_x_values():
    # 360 x-Werte im Bereich 0 bis 2*pi (Bogenmass) erzeugen
    # -- entweder mit np.arange(0, 2*np.pi, np.pi/180)
    # -- oder mit np.linspace(0, 2*np.pi, 360)
    return np.linspace(0, 2*np.pi, 360)


def create_data(anzahl):
    # drei Arrays zurueckgeben:
    # 1. ein Array mit 'anzahl' Nullen (np.zeros)
    # 2. ein Array mit 'anzahl' Einsen (np.ones)
    # 3. eine Identitaetsmatrix der Groesse anzahl x anzahl (np.eye)
    a= np.zeros(anzahl) 
    b=np.ones(anzahl) 
    c=np.eye(anzahl)
    return a, b, c


def array_info(m):
    # ein Tupel (ndim, shape) fuer das uebergebene Array zurueckgeben
    return m.ndim, m.shape


def reshape_array(m, new_shape):
    # das uebergebene Array in die Form new_shape bringen (reshape)
    return m.reshape(new_shape)


def boolean_mask(a):
    # aus dem uebergebene Array a nur die Werte zurueckgeben,
    # die groesser als 5 sind (a[a > 5])
    return (a[a>5])


def skalarprodukt(u, v):
    # das Skalarprodukt der beiden Vektoren zurueckgeben (np.dot oder @)
    return np.dot(u, v)


# ------------------------------------------------------------
# Pandas: Series
# ------------------------------------------------------------

def create_series():
    # eine Series mit den Werten 42, 44, 45, 47 und dem
    # Index ["w", "x", "y", "z"] erzeugen und zurueckgeben
    my_index=["w", "x", "y", "z"]
    return pd.Series([42, 44, 45, 47], index=my_index)


def series_slice(my_series):
    # den Bereich "x" bis "y" (inklusive!) der Series zurueckgeben
    return my_series["x": "y"]


def series_sum(s1, s2):
    # die Summe der beiden Series zurueckgeben
    return s1+s2


def drop_nan(a):
    # alle NaN-Eintraege aus der Series entfernen (dropna)
    return a.dropna()


def fill_nan(a, wert):
    # alle NaN-Eintraege der Series durch 'wert' ersetzen (fillna)
    return a.fillna(wert)


def is_nan(a):
    # ein boolesches Array zurueckgeben, das True an den NaN-Stellen hat (isna)
    return a.isna()


# ------------------------------------------------------------
# Pandas: DataFrames
# ------------------------------------------------------------

def create_dataframe():
    # ein DataFrame aus den drei Series la, reg, deg (siehe unten) bauen
    # und zurueckgeben
    jahre = range(2018, 2022)
    la = pd.Series([4926, 4796, 4601, 4490], index=jahre, name="HAW")
    reg = pd.Series([11328, 11167, 11020, 11003], index=jahre, name="OTH")
    deg = pd.Series([5928, 6454, 6369, 6809], index=jahre, name="THD")
    return pd.DataFrame([la, reg, deg])


def column_2020(df):
    # die SPALTE 2020 des DataFrames zurueckgeben
    return df[2020]


def row_haw(df):
    # die ZEILE "HAW" des Dataframes zurueckgeben (loc)
    return df.loc["HAW"]


def value_haw_2020(df):
    # den Wert fuer "HAW" in der Spalte 2020 zurueckgeben
    return df.loc["HAW"][2020]


def more_4700(df):
    # alle Werte des DataFrames, die groesser als 4700 sind, zurueckgeben
    # (alle anderen werden NaN)
    return df[df>4700]


if __name__ == "__main__":
    # visuelle Kontrolle (Abnahme erfolgt ueber test_p3.py):
    print(create_array())
    print(create_dataframe())
    print(more_4700(create_dataframe()))
    # die Plot-Aufgabe (sin) liegt in p3_plot.py

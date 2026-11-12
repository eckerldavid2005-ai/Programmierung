import pandas as pd
import matplotlib.pyplot as plt
import pathlib

datapath = pathlib.Path() / "datasets"

# In diesem File gibt es KEINE TODOs:
# Hier werden die Datensaetze geladen, vorbereitet und in die richtige Form gebracht.
# Die print-Ausgaben dienen nur der Kontrolle -- fuehren Sie das Skript 1x aus.

##################################################
# Laden der Datensaetze:
##################################################
oecd_bli = pd.read_csv(datapath / "oecd_bli.csv")
gdp_per_capita = pd.read_csv(datapath / "gdp_per_capita.csv")

# zur Kontrolle: die beiden geladenen Datensaetze ausgeben
print(oecd_bli)
print(gdp_per_capita)

##################################################
# Vorbereiten von gdp_per_capita:
##################################################

# festlegen, was wir untersuchen wollen
gdp_year = 2020
gdppc_col = "GDP per capita (USD)"
lifesat_col = "Life satisfaction"

# das passende Jahr aussuchen (Filtern der Pandas Tabelle)
gdp_per_capita = gdp_per_capita[gdp_per_capita["Year"] == gdp_year]

# loeschen der unnoetigen Spalten:
gdp_per_capita = gdp_per_capita.drop(["Code", "Year"], axis=1)

# umbenennen der beiden Spalten:
gdp_per_capita.columns = ["Country", gdppc_col]

# zur Kontrolle ausgeben
print(gdp_per_capita)

# aus der Country-Spalte den Index des Pandas-DataFrames machen:
gdp_per_capita.set_index("Country", inplace=True)

# zur Kontrolle ausgeben
print(gdp_per_capita)

##################################################
# Vorbereiten von oecd_bli:
##################################################
print(oecd_bli)

# Nur die Zeilen uebernehmen, deren Spalte INEQUALITY auf "TOT" steht
oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
print(oecd_bli)

# Index auf Land-Namen setzen
oecd_bli = oecd_bli.set_index("Country")

# Filtern auf Spalte "Indicator" == lifesat_col und nur die Spalte "Value" auswaehlen
oecd_bli = oecd_bli[oecd_bli["Indicator"] == lifesat_col]["Value"]
oecd_bli.name = lifesat_col
print(oecd_bli)

# Beide Tabellen ueber den Index (Länder) zusammenfuehren
full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                              left_index=True, right_index=True)
full_country_stats.sort_values(by=gdppc_col, inplace=True)

# Ausreisser entfernen (z. B. Luxemburg):
# Werte >= 89000 werden durch den Vergleich zu NaN und von dropna() entfernt
full_country_stats = full_country_stats[full_country_stats < 89000]
full_country_stats.dropna(inplace=True)

# Das ist der Datensatz, mit dem wir im Praktikum weiterarbeiten:
full_country_stats.to_csv(datapath / "lifesat_full.csv")
print(full_country_stats)

# Und noch die Messpunkte als Streudiagramm:
full_country_stats.plot(kind='scatter', figsize=(5, 3), grid=True,
                        x=gdppc_col, y=lifesat_col)
min_life_sat = 4
max_life_sat = 9
plt.axis([None, None, min_life_sat, max_life_sat])
plt.show()

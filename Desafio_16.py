"""Desafío 16: crear la columna poder a partir de nivel."""

import pandas as pd


datos = pd.read_csv("habitantes.csv")
datos["poder"] = datos["nivel"] * 10

print(datos[["nombre", "nivel", "poder"]].to_string(index=False))

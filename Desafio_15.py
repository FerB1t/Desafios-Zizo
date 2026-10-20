"""Desafío 15: filtrar con dos condiciones y exportar a Excel."""

import pandas as pd


datos = pd.read_csv("habitantes.csv")
filtro = datos[(datos["nivel"] > 5) & (datos["activo"] == True)]
filtro.to_excel("avanzados.xlsx", index=False, engine="openpyxl")

print("Habitantes filtrados:")
print(filtro.to_string(index=False))

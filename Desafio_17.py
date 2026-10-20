"""Desafío 17: contar habitantes por valor de activo."""

import pandas as pd


datos = pd.read_csv("habitantes.csv")
conteo = datos["activo"].value_counts()

print("Conteo de habitantes según el valor de 'activo':")
print(conteo)

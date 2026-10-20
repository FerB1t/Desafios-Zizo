"""Desafío 18: corregir la columna edad."""

import pandas as pd


df = pd.read_csv("registro_ancestral.csv")

# Los textos que no representan números se convierten en NaN.
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")
print("Valores ausentes después de la conversión:")
print(df["edad"].isnull())

# El ejercicio pide practicar fillna() usando 0.
df["edad"] = df["edad"].fillna(0).astype(int)

# Se conservan únicamente las edades comprendidas entre 0 y 200.
df = df[(df["edad"] >= 0) & (df["edad"] <= 200)].copy()
df.to_csv("registro_ancestral_limpio.csv", index=False)

print("\nDatos después de corregir la edad:")
print(df.to_string(index=False))

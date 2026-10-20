"""Desafío 21: explorar datos limpios y organizados."""

import pandas as pd


df = pd.read_csv("registro_ancestral.csv")

# Preparación reproducible de los datos aprendida en los desafíos anteriores.
df["edad"] = pd.to_numeric(df["edad"], errors="coerce").fillna(0)
df = df[(df["edad"] >= 0) & (df["edad"] <= 200)].copy()
df["origen"] = df["origen"].astype(str).str.strip().str.lower()
df["origen"] = df["origen"].replace({"bitarea": "bitaria"})
df["nivel"] = pd.to_numeric(df["nivel"], errors="coerce")

print("Registros por origen:")
print(df["origen"].value_counts())

print("\nEdad promedio por origen:")
print(df.groupby("origen")["edad"].mean())

print("\nNivel mínimo y máximo por origen:")
print(df.groupby("origen")["nivel"].agg(["min", "max"]))


# Desafio 21: Explorar los datos
import pandas as pd

df = pd.read_csv("registro_ancestral.csv")

# Asegurar formato de columnas
df["origen"] = df["origen"].astype(str).str.strip().str.lower()
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")

print("👉 Registros por origen:")
print(df["origen"].value_counts())

print("\n👉 Edad promedio por origen:")
print(df.groupby("origen")["edad"].mean().fillna(0))

print("\n👉 Nivel mínimo y máximo por origen:")
print(df.groupby("origen")["nivel"].agg(["min", "max"]))

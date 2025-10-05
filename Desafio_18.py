# Desafio 18: Corregir la columna "edad"
import pandas as pd
import numpy as np

df = pd.read_csv("registro_ancestral.csv")

# Convertir edad a numérico, errores -> NaN
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")

# Eliminar edades inválidas (<0 o >200)
df.loc[(df["edad"] < 0) | (df["edad"] > 200), "edad"] = np.nan

# Rellenar vacíos con 0
df["edad"] = df["edad"].fillna(0).astype(int)

print(df)

# Guardar archivo limpio
df.to_csv("registro_ancestral_limpio.csv", index=False)

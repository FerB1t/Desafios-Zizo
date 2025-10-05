# Desafio 19: Arreglar la columna "origen"
import pandas as pd

df = pd.read_csv("registro_ancestral.csv")

# Convertir a minúsculas y limpiar espacios
df["origen"] = df["origen"].astype(str).str.strip().str.lower()

# Unificar variaciones de 'bitaria'
df["origen"] = df["origen"].replace({
    "bitaria": "bitaria",
    "bitarea": "bitaria",
    "bitAria".lower(): "bitaria",
    "bitaria": "bitaria"
})

# Codificar categorías como números
df["origen_cod"] = df["origen"].astype("category").cat.codes

print(df[["nombre", "origen", "origen_cod"]])

# Guardar resultado
df.to_csv("registro_ancestral_origen_codificado.csv", index=False)

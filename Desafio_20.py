# Desafio 20: Normalizar los niveles
import pandas as pd

df = pd.read_csv("habitantes.csv")

min_n = df["nivel"].min()
max_n = df["nivel"].max()
df["nivel_norm"] = (df["nivel"] - min_n) / (max_n - min_n)

print(df[["nombre", "nivel", "nivel_norm"]])

# Guardar archivo normalizado
df.to_csv("habitantes_normalizados.csv", index=False)

# Desafio 15: Filtrar datos por múltiples condiciones y guardarlos
import pandas as pd

datos = pd.read_csv("habitantes.csv")

# Filtrar: nivel > 5 y activo == True
filtro = datos[(datos["nivel"] > 5) & (datos["activo"] == True)]

# Guardar resultado en Excel
filtro.to_excel("avanzados.xlsx", index=False)

print("Habitantes filtrados:")
print(filtro)

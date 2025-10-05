# Desafio 17: Agrupar y contar elementos por categoría
import pandas as pd

datos = pd.read_csv("habitantes.csv")

conteo = datos["activo"].value_counts()
print("Conteo de habitantes según estado 'activo':")
print(conteo)

# Desafio 16: Crear nueva columna con datos procesados
import pandas as pd

datos = pd.read_csv("habitantes.csv")

# Nueva columna 'poder'
datos["poder"] = datos["nivel"] * 10

print(datos[["nombre", "nivel", "poder"]])

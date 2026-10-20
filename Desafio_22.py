"""Desafío 22: crear cuatro visualizaciones con Matplotlib y Seaborn."""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Ejemplo autocontenido con las cinco columnas descritas en el capítulo.
datos = pd.DataFrame(
    {
        "nombre": ["Zizo", "Bit", "Null", "Lira", "Codarion", "Exelia", "Rex", "Vera"],
        "edad": [18, 22, 35, 27, 40, 31, 24, 29],
        "nivel": [6, 7, 9, 5, 8, 10, 4, 7],
        "origen": ["Bitaria", "Bitaria", "Exilio", "Exilio", "Bitaria", "Exilio", "Bitaria", "Exilio"],
        "estado": ["activo", "activo", "inactivo", "inactivo", "activo", "activo", "inactivo", "activo"],
    }
)

sns.set_theme(style="whitegrid")

# 1. Gráfico univariado numérico: nivel en 6 intervalos.
plt.figure(figsize=(7, 4.5))
plt.hist(datos["nivel"], bins=6, color="skyblue", edgecolor="black")
plt.title("Distribución del nivel")
plt.xlabel("Nivel")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("histograma_nivel_6bins.png", dpi=150)
plt.close()

# 2. Gráfico univariado categórico: conteo por estado.
plt.figure(figsize=(7, 4.5))
sns.countplot(data=datos, x="estado", hue="estado", legend=False, palette="Set2")
plt.title("Personajes por estado")
plt.xlabel("Estado")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.savefig("barras_estado.png", dpi=150)
plt.close()

# 3. Gráfico bivariado: edad en X y nivel en Y.
plt.figure(figsize=(7, 4.5))
sns.scatterplot(data=datos, x="edad", y="nivel", s=80)
plt.title("Relación entre edad y nivel")
plt.xlabel("Edad")
plt.ylabel("Nivel")
plt.tight_layout()
plt.savefig("scatter_nivel_edad.png", dpi=150)
plt.close()

# 4. Gráfico multivariado: color por origen, sin repetir nivel como tamaño.
plt.figure(figsize=(7, 4.5))
sns.scatterplot(data=datos, x="edad", y="nivel", hue="origen", s=80)
plt.title("Edad y nivel según el origen")
plt.xlabel("Edad")
plt.ylabel("Nivel")
plt.legend(title="Origen")
plt.tight_layout()
plt.savefig("multivariado_nivel_edad_origen.png", dpi=150)
plt.close()

print("Se crearon correctamente las cuatro imágenes del desafío 22.")


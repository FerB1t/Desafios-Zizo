# Desafio 22: Gráficos (univariado, bivariado y multivariado)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos (archivos en la misma carpeta que el .py)
hab = pd.read_csv("habitantes.csv")
reg = pd.read_csv("registro_ancestral.csv")

# --- Limpieza mínima para seguridad ---
# Asegurarse de que 'nivel' sea numérico en ambos archivos
hab["nivel"] = pd.to_numeric(hab["nivel"], errors="coerce")
reg["nivel"] = pd.to_numeric(reg["nivel"], errors="coerce")
# Asegurar que 'edad' sea numérica (hay valores como '?' o 'desconocido')
reg["edad"] = pd.to_numeric(reg["edad"], errors="coerce")
# Normalizar texto de 'origen' para el multivariado
if "origen" in reg.columns:
    reg["origen"] = reg["origen"].astype(str).str.strip().str.lower()

# -----------------------
# 1) Univariado: histograma de "nivel" con 6 rangos
# -----------------------
plt.figure()
plt.hist(hab["nivel"].dropna(), bins=6)
plt.title("Histograma de 'nivel' (6 rangos)")
plt.xlabel("Nivel")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("histograma_nivel_6bins.png")   # guarda imagen
plt.show()

# -----------------------
# 2) Univariado: gráfico de barras por "estado"
#    (el libro usa 'estado' — en los CSV está 'activo'; se adapta)
# -----------------------
# Elegimos la columna 'activo' si existe, si no usamos 'estado'
col_estado = "activo" if "activo" in hab.columns else ("estado" if "estado" in hab.columns else None)
if col_estado is None:
    raise RuntimeError("No se encontró columna 'activo' ni 'estado' en habitantes.csv")
counts = hab[col_estado].value_counts()

plt.figure()
counts.plot(kind="bar")
plt.title(f"Número de personajes por '{col_estado}'")
plt.xlabel(col_estado)
plt.ylabel("Cantidad")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("barras_estado.png")
plt.show()

# -----------------------
# 3) Bivariado: scatterplot "nivel" vs "edad"
# -----------------------
# Usamos registro_ancestral.csv (contiene edad). Eliminamos filas con NaN en las columnas usadas.
df_scatter = reg[["nivel", "edad"]].dropna()
plt.figure()
plt.scatter(df_scatter["nivel"], df_scatter["edad"])
plt.title("Scatterplot: nivel vs edad")
plt.xlabel("Nivel")
plt.ylabel("Edad")
plt.tight_layout()
plt.savefig("scatter_nivel_edad.png")
plt.show()

# -----------------------
# 4) Multivariado: nivel vs edad, colores para 'origen', tamaños según 'nivel'
# -----------------------
# Filtramos filas válidas
if "origen" not in reg.columns:
    raise RuntimeError("No hay columna 'origen' en registro_ancestral.csv para el gráfico multivariado.")
df_multi = reg[["nivel", "edad", "origen"]].dropna()

# Para que los puntos no sean demasiado pequeños/grandes:
# definimos tamaño proporcional a 'nivel' (ej: nivel * 5)
sizes = (df_multi["nivel"].astype(float).fillna(0) * 5).clip(lower=10)  # mínimo 10

plt.figure()
# Dibujamos un scatter por cada origen (así matplotlib asigna colores automáticamente)
for origen, grupo in df_multi.groupby("origen"):
    plt.scatter(grupo["nivel"], grupo["edad"], s=(grupo["nivel"] * 5).clip(lower=10), label=origen)

plt.title("Multivariado: Nivel vs Edad (color = origen, tamaño = nivel)")
plt.xlabel("Nivel")
plt.ylabel("Edad")
plt.legend(title="Origen", bbox_to_anchor=(1.05, 1), loc="upper left")  # leyenda a la derecha
plt.tight_layout()
plt.savefig("multivariado_nivel_edad_origen.png", bbox_inches="tight")
plt.show()

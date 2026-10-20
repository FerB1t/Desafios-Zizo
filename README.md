# Desafíos de *Zizo y el algoritmo perdido*

Este repositorio reúne los archivos de apoyo y las soluciones ejecutables de los desafíos del libro *Zizo y el algoritmo perdido*, de  Diego Fernando Aguirre Barahona.

## Cómo usar el repositorio

1. Descarga el repositorio o clónalo:

   ```bash
   git clone https://github.com/FerB1t/Desafios-Zizo.git
   cd Desafios-Zizo
   ```

2. Crea y activa un entorno virtual:

   **Windows (PowerShell)**

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS o Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

4. Ejecuta un desafío desde la carpeta raíz. Por ejemplo:

   ```bash
   python Desafio_15.py
   ```

## Función de los archivos de datos

| Archivo | Función pedagógica |
| --- | --- |
| `habitantes.csv` | Entrada estable y correcta para los desafíos 15, 16 y 17. |
| `registro_ancestral.csv` | Entrada deliberadamente desordenada para practicar limpieza y transformación. |
| `Archivo_Final.csv` | Base de datos extensa con errores intencionales para que el lector la intervenga. |
| `avanzados.xlsx` | Resultado de referencia del desafío 15; contiene solo a Zizo y Bit. |
| `registro_ancestral_limpio.csv` | Resultado de referencia del desafío 18. |

El orden de las filas de una base de datos no determina que esté correcta o incorrecta. En los archivos deliberadamente desordenados, las inconsistencias forman parte del ejercicio. En cambio, las soluciones `Desafio_*.py` y los archivos de resultado muestran una ejecución válida con la que el lector puede comparar su trabajo.

## Archivos de referencia del desafío 22

- `histograma_nivel_6bins.png`
- `barras_estado.png`
- `scatter_nivel_edad.png`
- `multivariado_nivel_edad_origen.png`

El programa `Desafio_22.py` es autocontenido: crea un DataFrame de ejemplo con las columnas descritas en el capítulo y genera las cuatro imágenes sin depender de un archivo adicional.

## Compatibilidad

Las soluciones fueron verificadas con Python 3 y las bibliotecas declaradas en `requirements.txt`. Para que las rutas relativas funcionen, ejecuta los programas desde la carpeta raíz del repositorio.

## Licencia y uso

Material educativo complementario del libro. Conserva los créditos de autoría al reutilizarlo o compartirlo.


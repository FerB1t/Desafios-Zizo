# Desafio 14: El Orbe de Números (NumPy)
import numpy as np
from statistics import mode

lista = [12, 15, 10, 18, 20, 15]
array = np.array(lista)

promedio = np.mean(array)
maximo = np.max(array)
minimo = np.min(array)
moda = mode(lista)

print("Array:", array)
print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Moda:", moda)

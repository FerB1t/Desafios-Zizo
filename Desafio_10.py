# Desafio 10: La Eternidad Condicional
# Elegimos un rango amplio; el primer múltiplo de 7 después de 1 es 7.
for numero in range(1, 100):   # 100 es arbitrario y seguro para encontrar un múltiplo de 7
    if numero % 7 == 0:
        print("¡Encontrado!", numero)
        break

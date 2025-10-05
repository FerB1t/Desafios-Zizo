# Desafio 7: Crear una función para vencer a Lira
def defender(valor):
    if (valor % 3 == 0) and (valor % 5 == 0):
        return "Ataque bloqueado"
    else:
        return "¡Impacto directo!"

# pruebas
print(defender(15))  # Ataque bloqueado
print(defender(8))   # ¡Impacto directo!

# Desafio 3: La Puerta del Juicio (código corregido)
def saludar(nombre):
    print("¡Bienvenido, " + nombre + "!")

def calcular_media(a, b, c):
    return (a + b + c) / 3

def obtener_mayor(lista):
    return max(lista)

def es_par(numero):
    return numero % 2 == 0

saludar("Zizo")
media = calcular_media(10, 20, 30)
mayor = obtener_mayor([4, 9, 2, 15])
par = es_par(80)

print("Mayor número:", mayor)
print("Media:", media)
print("¿Es par?", par)

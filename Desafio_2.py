# Desafio 2: Invoca o serás olvidado
nombre = "Zizo"
edades = [17, 19, 21, 20]
temperaturas = [36.5, 37.2, 35.8, 38.0]
estaturas = [1.70, 1.68, 1.75, 1.80]

print(f"Hola {nombre}, bienvenido a Nestaria.")
print("Tipo de dato de edades:", type(edades))
print("Cantidad de miembros:", len(edades))
print("Edad máxima:", max(edades), "años")
print("Edad mínima:", min(edades), "años")
print("Estatura promedio:", round(sum(estaturas)/len(estaturas), 2), "m")
print("Temperaturas ordenadas:", sorted(temperaturas))

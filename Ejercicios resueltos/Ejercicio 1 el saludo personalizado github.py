# usamos input para pedir datos al usuario
nombre = input("Nombre: ")
edad = int(input("Edad: "))  # int porque es número

# restamos para calcular el año de nacimiento
anio = 2026 - edad

# print para mostrar resultados
print("Hola", nombre)
print("Naciste en", anio)
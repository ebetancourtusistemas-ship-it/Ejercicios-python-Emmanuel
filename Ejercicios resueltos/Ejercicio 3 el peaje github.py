# Primero: pedimos la edad
edad = int(input("Escribe tu edad: "))

# Segundo: verificamos si cumple la edad mínima
if edad >= 18:
    # Tercero: si tiene 18 o más, puede conducir
    print("Puedes conducir")
else:
    # Cuarto: si es menor de 18, no puede
    print("Aún no tienes edad para conducir")
# Primero: pedimos la edad
edad = int(input("Edad: "))

# Segundo: revisamos en qué grupo cae
if edad <= 12:
    # si tiene 12 o menos
    print("Niño")

elif edad <= 17:
    # si tiene hasta 17
    print("Adolescente")

elif edad <= 64:
    # si tiene hasta 64
    print("Adulto")

else:
    # si tiene 65 o más
    print("Adulto mayor")
# Primero: guardamos el PIN correcto
pin_correcto = "1234"

# Segundo: pedimos el PIN al usuario
pin = input("Ingresa el PIN: ")

# Tercero: usamos while para repetir hasta que sea correcto
while pin != pin_correcto:
    # si es incorrecto, vuelve a pedirlo
    print("PIN incorrecto")
    pin = input("Intenta de nuevo: ")

# Cuarto: cuando acierta
print("Acceso permitido")
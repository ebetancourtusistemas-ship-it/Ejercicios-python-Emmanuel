# Primero: definimos el número secreto
numero_secreto = 10  # puedes cambiarlo

# Segundo: damos 5 intentos
for intento in range(1, 6):
    # pedimos el número
    numero = int(input("Adivina el número (1-20): "))
    
    # Tercero: comparamos
    if numero == numero_secreto:
        # si acierta
        print("¡Correcto!")
        break  # termina el ciclo
    elif numero < numero_secreto:
        # si es menor
        print("Es mayor")
    else:
        # si es mayor
        print("Es menor")

# Cuarto: si no adivinó en los intentos
else:
    print("Se acabaron los intentos")
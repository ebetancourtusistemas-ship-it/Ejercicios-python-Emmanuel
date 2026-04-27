# Primero: pedimos un número
numero = int(input("Escribe un número: "))

# Segundo: verificamos si es positivo
if numero > 0:
    # Tercero: si es mayor que 0
    print("Es positivo")

# Cuarto: verificamos si es negativo
elif numero < 0:
    # Quinto: si es menor que 0
    print("Es negativo")

# Sexto: si no es positivo ni negativo, es cero
else:
    print("Es cero")
# Primero: pedimos una frase
frase = input("Escribe una frase: ")

# Segundo: creamos un contador
contador = 0  # empieza en 0

# Tercero: recorremos cada letra
for letra in frase:
    # pasamos a minúscula para comparar mejor
    if letra.lower() in "aeiou":
        # si es vocal, sumamos 1
        contador = contador + 1

# Cuarto: mostramos el resultado
print("Cantidad de vocales:", contador)
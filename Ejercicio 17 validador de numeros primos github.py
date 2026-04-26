# Primero: pedimos el número
numero = int(input("Escribe un número: "))

# Segundo: asumimos que es primo (bandera)
es_primo = True

# Tercero: verificamos divisores
# probamos desde 2 hasta numero-1
for i in range(2, numero):
    # si se divide exacto, no es primo
    if numero % i == 0:
        es_primo = False  # cambiamos la bandera
        break  # ya no seguimos

# Cuarto: mostramos el resultado
if es_primo and numero > 1:
    print("Es primo")
else:
    print("No es primo")
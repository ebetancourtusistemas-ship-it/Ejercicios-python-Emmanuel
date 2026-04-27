# Primero: pedimos el número
numero = int(input("Escribe un número: "))

# Segundo: usamos for para recorrer del 1 al 10
for i in range(1, 11):
    # mostramos la multiplicación
    print(f"{numero} x {i} = {numero * i}")
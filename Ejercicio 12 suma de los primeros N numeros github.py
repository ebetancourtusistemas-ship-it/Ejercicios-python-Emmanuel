# Primero: pedimos el número
n = int(input("Escribe un número: "))

# Segundo: creamos una variable para guardar la suma
suma = 0  # empieza en 0 porque aún no hemos sumado nada

# Tercero: usamos for para recorrer desde 1 hasta n
for i in range(1, n + 1):  # n+1 para incluir el número final
    suma = suma + i  # acumulamos la suma

# Cuarto: mostramos el resultado
print("La suma es:", suma)
# Primero: pedimos cuántos números quiere
n = int(input("¿Cuántos términos?: "))

# Segundo: empezamos con los dos primeros números
a = 0
b = 1

# Tercero: usamos for para repetir n veces
for i in range(n):
    # mostramos el número actual
    print(a)
    
    # calculamos el siguiente número
    siguiente = a + b
    
    # movemos los valores
    a = b
    b = siguiente
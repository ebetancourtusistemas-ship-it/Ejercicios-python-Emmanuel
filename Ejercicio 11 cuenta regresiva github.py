# Primero: pedimos un número positivo
numero = int(input("Escribe un número: "))

# Segundo: usamos while para repetir mientras sea >= 0
while numero >= 0:
    # mostramos el número actual
    print(numero)
    
    # restamos 1 en cada vuelta (decremento)
    numero = numero - 1

# Tercero: cuando termina el ciclo
print("¡Despegue!")
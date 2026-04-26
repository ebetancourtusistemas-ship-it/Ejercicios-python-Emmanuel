# Primero: iniciamos el total en 0
total = 0

# Segundo: pedimos el primer precio
precio = float(input("Ingresa el precio (0 para terminar): "))

# Tercero: usamos while hasta que el usuario ponga 0
while precio != 0:
    total = total + precio  # acumulamos el total
    
    # volvemos a pedir otro precio
    precio = float(input("Ingresa otro precio (0 para terminar): "))

# Cuarto: aplicamos descuento si supera 100
if total > 100:
    descuento = total * 0.10  # 10%
    total = total - descuento

# Quinto: mostramos el total final
print("Total a pagar:", total)
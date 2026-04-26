# Primero: pedimos el total de la compra
total = float(input("Total de la compra: "))

# Segundo: revisamos cuánto descuento aplica
if total < 50:
    # si es menor a 50, no hay descuento
    descuento = 0

elif total <= 100:
    # si está entre 50 y 100, 5% de descuento
    descuento = total * 0.05

else:
    # si es mayor a 100, 10% de descuento
    descuento = total * 0.10

# Tercero: calculamos el total a pagar
total_pagar = total - descuento

# Cuarto: mostramos el resultado
print("Descuento:", descuento)
print("Total a pagar:", total_pagar)
# Primero: pedimos el año
anio = int(input("Escribe un año: "))

# Segundo: verificamos si es bisiesto
# divisible por 4 y no por 100, o divisible por 400
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    # si cumple la condición
    print("Es bisiesto")
else:
    # si no cumple
    print("No es bisiesto")
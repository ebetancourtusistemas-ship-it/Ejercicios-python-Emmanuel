# Primero: pedimos el salario
salario = float(input("Salario mensual: "))  # float por si tiene decimales

# Segundo: preguntamos si tiene deudas
deuda = input("¿Tienes deudas? (si/no): ").lower()  
# .lower() para evitar problemas con mayúsculas

# Tercero: verificamos las condiciones
# debe ganar más de 1000 y NO tener deudas
if salario > 1000 and deuda == "no":
    print("Crédito Aprobado")
else:
    print("Crédito Denegado")
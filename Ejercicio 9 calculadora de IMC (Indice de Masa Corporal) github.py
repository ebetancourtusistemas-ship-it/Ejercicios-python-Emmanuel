# Primero: pedimos el peso en kg
peso = float(input("Escribe tu peso (kg): "))

# Segundo: pedimos la altura en metros
altura = float(input("Escribe tu altura (m): "))

# Tercero: calculamos el IMC
# fórmula: peso / (altura al cuadrado)
imc = peso / (altura * altura)

# Cuarto: mostramos el IMC
print("Tu IMC es:", imc)

# Quinto: clasificamos según el resultado
if imc < 18.5:
    # si es menor a 18.5
    print("Bajo peso")

elif imc < 25:
    # entre 18.5 y 24.9
    print("Normal")

elif imc < 30:
    # entre 25 y 29.9
    print("Sobrepeso")

else:
    # 30 o más
    print("Obesidad")
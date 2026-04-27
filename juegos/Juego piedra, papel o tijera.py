'''
Reto de programación # 1: Piedra, Papel o Tijera

1. Descripción de problema
Se solicita desarrollar un programa interactivo en Python que permita a un usuario enfrentarse contra la computadora en el 
Clásico juego de Piedra, Papel o Tijera.
El programa debe ser capaz de procesar la entrada del usuario, generar una respuesta aleatoria y determinar un ganador 
basándose en las reglas tradicionales.

2. Requerimientos Técnicos

El algoritmo debe estructurarse de la siguiente manera:

* Interfaz Visual: Mostrar un encabezado decorativo utilizando métodos de cadena como .center() y multiplicación de caracteres.

* Entrada de Datos: Solicitar al usuario su elección. El programa debe ser capaz de reconocer la entrada sin importar si 
se escribe en mayúsculas o minúsculas.

* Inteligencia Aleatoria: La computadora debe elegir una opción de una lista predefinida de opciones (Piedra, Papel, Tijera) 
de forma aleatoria utilizando el módulo random.

* Logica de comparación:

Implementar las condiciones necesarias para evaluar.

1. Empate: Ambas elecciones son iguales.
2. Victoria: El usuario vence a la PC (Priedra vence a Tijera, Tijera vence a Papel, Papel vence a Piedra).
3. Derrota: La PC vence al usuario.

* Control de Flujo: El juego debe repetirse indefinidamente dentro de un blucle hasta que el usuario decida escribir 
la palabra (Salir).

Solución del Ejercicio Propuesto    
'''

import random

print("=" * 50) 
print("Bienvenido al juego de Piedra, Papel o Tijera".center(50)) 
print("=" * 50) 

opciones = ["Piedra", "Papel", "Tijera"] 

input("Empezar el juego (Presiona Enter)") 
print("Opciones:")
print("1= Piedra")
print("2= Papel")
print("3= Tijera")
input("Elige tu opción: Piedra, Papel o Tijera (Escribe tu elección y presiona Enter)")

opciones = random.randint(1, 3)

if opciones == 1:
    print("Escogiste: Piedra")
elif opciones == 2:
    print("Escogiste: Papel")   
elif opciones == 3:
    print("Escogiste: Tijera")
else:
    print("Opción no válida. Por favor, elige Piedra, Papel o Tijera.")



if opciones == 1:
    print("La computadora eligió: Piedra")  
elif opciones == 2:
    print("La computadora eligió: Papel")
elif opciones == 3:
    print("La computadora eligió: Tijera")  
else:
    print("Opción no válida. Por favor, elige Piedra, Papel o Tijera.")

if opciones == 1:
    print("¡Empate! Ambos eligieron Piedra.")       
elif opciones == 2:
    print("¡Derrota! Papel vence a Piedra.")
elif opciones == 3:
    print("¡Victoria! Piedra vence a Tijera.")
elif opciones == 1:
    print("¡Derrota! Piedra vence a Tijera.")
elif opciones == 2:
    print("¡Victoria! Papel vence a Piedra.")
elif opciones == 3:
    print("¡Derrota! Tijera vence a Papel.")
    
 
print("==" * 50)
print("Fin del juego - Gracias por jugar".center(50))       
print("==" * 50)




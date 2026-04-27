"""
Reto de programacion simulador de probabilidades: ruleta rusa

1. Descripción del problema:
Se requiere desarrollar un programa en Python que simule un sistema de azar basado en un revolver de 6 recamaras. El programa debe gestionar eventos aleatorios, pausas de ejecucion para mejorar la experiencia del usuario y control de flujo basado en condiciones de victoria o derrota.

2. Requerimiento tecnicos:

el algoritmo debe cumplir con los siguientes requisitos:

*inicializacion: Definir una recamara ganadora (bala) de forma aleatoria entre 1 y 6. (random)

*bucle de juego: El usuario debe interactuar manualmente para girar  el tambor y disparar (while)  (time)

*Mecanica de azar: En cada turno, la posicion de la recamara que queda al frente al percutor debe ser aleatoria, simulando el giro del tambor.

*Condicion de derrota: Si la recamara seleccionada coincide con la de la bala, el programa termina inmediatamente  (if)

*Condicion de victoria: El jugador gana si logra sobrevivir a 5 intentos (ya que el sexto intento seria el fatal)
"""

import random, time #aqui importamos las librerias necesarias para generar numeros aleatorios y para manejar el tiempo

print("=" * 50) #esto es para imprimir una linea de guiones para separar secciones del programa
print("Bienvenido al simulador de ruleta rusa. Tienes 5 intentos para sobrevivir. ¡Buena suerte!")
print("=" * 50) #otra linea de guiones para separar secciones del programa

input("Poner Bala en el tambor (Presiona enter)") #esto es para que el usuario presione enter para iniciar el juego
bala = random.randint(1, 6) #aqui hacemos que la bala se coloque en una recamara aleatoria entre 1 y 6
time.sleep(0.5) #aqui hacemos una pausa de medio segundo para mejorar la experiencia del usuario

disparos = 0 #es una variable para contar el numero de disparos realizados

while True: 
    input("Girar el tambor (Presiona Enter)") #aqui hacemos que el usuario presione enter para girar el tambor y disparar
    recamara = random.randint(1, 6) #aqui hacemos que la recamara que queda al frente sea aleatoria entre 1 y 6, y el randint es el que genera un numero aleatorio entre el rango especificado

    input("Apuntar y disparar (Presiona Enter)") #aqui hacemos que el usuario presione enter para apuntar y disparar
    time.sleep(1) #otra pausa de medio segundo para mejorar la experiencia del usuario

    if recamara == bala: #aqui hacemos que si la recamara que queda al frente coincide con la recamara donde esta la bala, el jugador pierde
        print("¡Bang! Has perdido. La bala estaba en la recamara", bala) #si la recamara coincide con la bala, el jugador pierde y se muestra un mensaje indicando que ha perdido y en que recamara estaba la bala
        break #aqui se rompe el bucle para terminar el juego
    else: #si la recamara no coincide con la bala, el jugador sobrevive y se muestra un mensaje indicando que ha sobrevivido
        disparos += 1 #aqui se incrementa el contador de disparos realizados
        print("Has sobrevivido a este intento") #aqui se muestra un mensaje indicando que el jugador ha sobrevivido a este intento
        print("Intentos sobrevividos:", disparos) #aqui se muestra el numero de intentos sobrevividos
  
    if disparos == 5: #aqui hacemos que si el jugador ha sobrevivido a 5 intentos, gana el juego
        print("¡Felicidades! Has ganado. Has sobrevivido a 5 intentos") #si el jugador ha sobrevivido a 5 intentos, se muestra un mensaje indicando que ha ganado
        break #aqui se rompe el bucle para terminar el juego

print("==" * 50) #otra linea de guiones para separar secciones del programa
print("fin del juego - Gracias por jugar") #aqui se muestra un mensaje indicando que el juego ha terminado y agradeciendo al jugador por jugar
print("==" * 50) #otra linea de guiones para separar secciones del programa





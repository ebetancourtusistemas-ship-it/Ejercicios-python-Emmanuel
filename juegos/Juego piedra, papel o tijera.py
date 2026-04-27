import random

# Encabezado decorativo
print("=" * 50)
print("JUEGO DE PIEDRA, PAPEL O TIJERA".center(50))
print("=" * 50)

opciones = ['Piedra', 'Papel', 'Tijera']

while True:
    usuario = input("Elige escribiendo Piedra, Papel o Tijera (o escribe 'Salir' para terminar): ").strip().capitalize()
    
    if usuario == 'Salir':
        print("¡Gracias por jugar!")
        break
    
    if usuario not in opciones:
        print("Opción inválida. Inténtalo de nuevo.")
        continue

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    
    if usuario == computadora:
        print("¡Es un empate!")
    elif (usuario == 'Piedra' and computadora == 'Tijera') or \
         (usuario == 'Tijera' and computadora == 'Papel') or \
         (usuario == 'Papel' and computadora == 'Piedra'):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
    
    print("-" * 30)
    print("¿Quieres jugar de nuevo? (Sí/No)")
    respuesta = input().strip().capitalize()
    if respuesta != 'Sí':
        print("¡Gracias por jugar!")
        break   












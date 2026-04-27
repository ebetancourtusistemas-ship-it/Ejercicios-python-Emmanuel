# Primero: definimos el saldo inicial
saldo = 1000

# Segundo: usamos while para repetir el menú
while True:
    # mostramos opciones
    print("\n1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    # Tercero: evaluamos la opción
    if opcion == "1":
        # mostrar saldo
        print("Tu saldo es:", saldo)
    
    elif opcion == "2":
        # pedir cantidad a retirar
        retiro = float(input("¿Cuánto quieres retirar?: "))
        
        # verificar si hay suficiente dinero
        if retiro <= saldo:
            saldo = saldo - retiro  # actualizamos saldo
            print("Retiro exitoso")
        else:
            print("No tienes suficiente saldo")
    
    elif opcion == "3":
        # salir del programa
        print("Gracias por usar el cajero")
        break  # termina el ciclo
    
    else:
        # opción inválida
        print("Opción no válida")
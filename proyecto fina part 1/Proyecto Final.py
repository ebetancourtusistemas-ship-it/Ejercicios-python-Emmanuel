
"""
Enunciado del Ejercicio: Sistema de Control de Notas y Materias


Contexto:
Durante un periodo académico, llevar el control de materias y notas ayuda a conocer el rendimiento en cada asignatura.
El objetivo de este proyecto es desarrollar un programa en Python que permita registrar materias, ingresar notas y calcular promedios de forma sencilla desde la consola.

Instrucciones

Escribe un programa en Python que realice las siguientes acciones:

1. Entrada de datos
• Solicitar al usuario el nombre de una materia.
• Permitir ingresar una o varias notas para cada materia.

2. Gestión de información
• Guardar varias materias dentro del programa.
• Guardar varias notas para cada materia.
• Permitir agregar nuevas materias y nuevas notas en cualquier momento.

3. Procesamiento de datos
• Calcular el promedio de cada materia.
• Calcular el promedio general de todas las materias.
• Mostrar cuáles materias están aprobadas y cuáles están perdidas.

4. Funciones adicionales
• Buscar una materia por nombre.
• Mostrar la materia con mejor promedio.
• Mostrar la materia con peor promedio.
• Permitir eliminar una materia.

5. Interfaz visual (Consola)
• Mostrar un menú con opciones para que el usuario pueda elegir qué desea hacer.
• El programa debe repetirse hasta que el usuario seleccione la opción de salir.

Ejemplo de salida esperada

----- CONTROL DE NOTAS -----

1. Registrar materia
2. Agregar nota
3. Ver materias
4. Calcular promedio
5. Promedio general
6. Materias aprobadas y perdidas
7. Mejor materia
8. Peor materia
9. Buscar materia
10. Eliminar materia
11. Salir

Elige una opción: 1
Ingrese el nombre de la materia: Matemáticas

Elige una opción: 2
Ingrese la materia: Matemáticas
Ingrese la nota: 4.5

Elige una opción: 4
Promedio de Matemáticas: 4.5

• Puedes usar una lista para guardar todas las materias.
• Cada materia puede guardarse como un diccionario con nombre y lista de notas.
• Usa ciclos while para el menú y for para recorrer materias.
• Usa condicionales para verificar si una materia aprueba o pierde.

"""
import os 
import time

materias = []


# ============================================
# ANIMACION DE CARGA
# ============================================
def cargar_sistema():

    for i in range(101):

        barra = "■" * (i // 2)
        espacio = " " * (50 - (i // 2))

        print(f"\rCargando sistema |{barra}{espacio}| {i}%",
              end="")

        time.sleep(0.02)

        # aqui hacemos la animacion de carga

    print("\nSistema iniciado correctamente")
    time.sleep(1)


# ============================================
# LIMPIAR CONSOLA
# ============================================
def limpiar():
    os.system("cls") 


# ============================================
# MENU
# ============================================
def menu():

    limpiar()

    print("=" * 55)
    print("        SISTEMA DE CONTROL DE NOTAS")
    print("=" * 55)

    print("""
        ____________________________
       /                           /|
      /___________________________/ |
      |                           | |
      |   1. Registrar materia    | |
      |   2. Agregar nota         | |
      |   3. Ver materias         | |
      |   4. Promedio materia     | |
      |   5. Promedio general     | |
      |   6. Materias aprobadas   | |
      |   7. Mejor materia        | |
      |   8. Peor materia         | |
      |   9. Buscar materia       | |
      |  10. Eliminar materia     | |
      |  11. Salir                | |
      |___________________________|/
    """)


# ============================================
# BUSCAR MATERIA
# ============================================
def buscar(nombre):

    for materia in materias:

        if materia["nombre"].lower() == nombre.lower(): 
            return materia
        # aqui hacemos la busqueda de la materia por su nombre

    return None


# ============================================
# INICIO
# ============================================
cargar_sistema()

while True:

    menu()

    opcion = input("Seleccione una opcion: ")

    # ============================================
    # REGISTRAR MATERIA
    # ============================================
    if opcion == "1":
        # si se elige la opcion 1, se registra una nueva materia

        nombre = input("Ingrese el nombre de la materia: ")

        if buscar(nombre):

            print("La materia ya existe")

        else:

            materias.append({
                "nombre": nombre,
                "notas": []
            })     #append para agregar la materia a la lista de materias
            print("Materia registrada correctamente")

        input("\nPresione ENTER para continuar...")


    # ============================================
    # AGREGAR NOTA
    # ============================================
    elif opcion == "2":
        # si se elige la opcion 2, se agrega una nota a una materia existente

        nombre = input("Ingrese la materia: ")

        materia = buscar(nombre)

        if materia:

            nota = float(input("Ingrese la nota: "))   

            if 0 <= nota <= 5:

                materia["notas"].append(nota)  #append para agregar la nota a la lista de notas de la materia

                print("Nota agregada correctamente")

            else:

                print("Nota invalida")

        else:

            print("Materia no encontrada")

        input("\nPresione ENTER para continuar...")  


    # ============================================
    # VER MATERIAS
    # ============================================
    elif opcion == "3":
        # si se elige la opcion 3, se muestran todas las materias registradas con sus notas

        if len(materias) == 0:  # el len de materias es 0, significa que no hay materias registradas 

            print("No hay materias registradas")

        else:

            for materia in materias: # aqui recorremos la lista de materias para mostrar cada una con sus notas

                print("\n--------------------------------")

                print("Materia:", materia["nombre"])
                print("Notas:", materia["notas"])

                print("--------------------------------")

        input("\nPresione ENTER para continuar...")


    # ============================================
    # PROMEDIO POR MATERIA
    # ============================================
    elif opcion == "4":
        # si se elige la opcion 4, se calcula y muestra el promedio de una materia especifica

        nombre = input("Ingrese la materia: ")

        materia = buscar(nombre)

        if materia:

            if len(materia["notas"]) > 0: 

                promedio = sum(materia["notas"]) / len(materia["notas"]) # aqui calculamos el promedio de las notas de la materia sumando todas las notas y dividiendo por la cantidad de notas

                print(f"Promedio de {nombre}: {round(promedio,2)}")  # el round para mostrar el promedio con 2 decimales 

            else:

                print("La materia no tiene notas")

        else:

            print("Materia no encontrada")

        input("\nPresione ENTER para continuar...")


    # ============================================
    # PROMEDIO GENERAL
    # ============================================
    elif opcion == "5":
        # si se elige la opcion 5, se calcula y muestra el promedio general de todas las materias

        total = 0
        cantidad = 0

        for materia in materias:

            total += sum(materia["notas"])   # aqui sumamos todas las notas de todas las materias para obtener el total de notas ingresadas
            cantidad += len(materia["notas"]) # += para contar la cantidad total de notas ingresadas en todas las materias

        if cantidad > 0:

            promedio_general = total / cantidad

            print("Promedio general:", round(promedio_general,2)) 

        else:

            print("No hay notas registradas")

        input("\nPresione ENTER para continuar...")


    # ============================================
    # APROBADAS Y PERDIDAS
    # ============================================
    elif opcion == "6":
        # si se elige la opcion 6, se muestra el estado de cada materia (aprobada o perdida) dependiendo del promedio de sus notas

        for materia in materias:

            if len(materia["notas"]) > 0:  # aqui verificamos que la materia tenga notas para poder calcular su promedio y determinar si esta aprobada o perdida

                promedio = sum(materia["notas"]) / len(materia["notas"]) # sacamos el promedio de las notas de la materia

                if promedio >= 3:

                    estado = "APROBADA"

                else:

                    estado = "PERDIDA"

                print("\nMateria:", materia["nombre"])
                print("Estado:", estado)

        input("\nPresione ENTER para continuar...")


    # ============================================
    # MEJOR MATERIA
    # ============================================
    elif opcion == "7":
        # si se elige la opcion 7, se busca y muestra la materia con el mejor promedio entre todas las materias registradas

        mejor = None
        mejor_promedio = 0

        for materia in materias:

            if len(materia["notas"]) > 0: # aqui verificamos que la materia tenga notas para poder calcular su promedio y compararlo con el mejor promedio encontrado hasta ahora

                promedio = sum(materia["notas"]) / len(materia["notas"]) # aqui calculamos el promedio de las notas de la materia para compararlo con el mejor promedio encontrado hasta ahora

                if promedio > mejor_promedio:

                    mejor_promedio = promedio
                    mejor = materia["nombre"] # aqui guardamos el nombre de la materia que tiene el mejor promedio encontrado hasta ahora

        if mejor:

            print("Mejor materia:", mejor)
            print("Promedio:", round(mejor_promedio,2))

        else:

            print("No hay datos")

        input("\nPresione ENTER para continuar...")


    # ============================================
    # PEOR MATERIA
    # ============================================
    elif opcion == "8":
        # si se elige la opcion 8, se busca y muestra la materia con el peor promedio entre todas las materias registradas

        peor = None
        peor_promedio = 5

        for materia in materias:

            if len(materia["notas"]) > 0:

                promedio = sum(materia["notas"]) / len(materia["notas"]) # aqui calculamos el promedio de las notas de la materia para compararlo con el peor promedio encontrado hasta ahora

                if promedio < peor_promedio:

                    peor_promedio = promedio
                    peor = materia["nombre"] # aqui guardamos el nombre de la materia que tiene el peor promedio encontrado hasta ahora

        if peor:

            print("Peor materia:", peor)
            print("Promedio:", round(peor_promedio,2))

        else:

            print("No hay datos")

        input("\nPresione ENTER para continuar...")


    # ============================================
    # BUSCAR MATERIA
    # ============================================
    elif opcion == "9":
        # si se elige la opcion 9, se busca una materia por su nombre y se muestra su informacion (nombre y notas)

        nombre = input("Ingrese la materia a buscar: ")

        materia = buscar(nombre)

        if materia:

            print("\nMateria encontrada")
            print("Nombre:", materia["nombre"])
            print("Notas:", materia["notas"])

        else:

            print("Materia no encontrada")

        input("\nPresione ENTER para continuar...")


    # ============================================
    # ELIMINAR MATERIA
    # ============================================
    elif opcion == "10":
        # si se elige la opcion 10, se busca una materia por su nombre y se elimina de la lista de materias si es encontrada

        nombre = input("Ingrese la materia a eliminar: ")

        materia = buscar(nombre)

        if materia:

            materias.remove(materia) # remove para eliminar la materia encontrada de la lista de materias

            print("Materia eliminada correctamente")

        else:

            print("Materia no encontrada")

        input("\nPresione ENTER para continuar...")


    # ============================================
    # SALIR
    # ============================================
    elif opcion == "11":
        # si se elige la opcion 11, se muestra una animacion de carga y se cierra el programa

        print("\nCerrando sistema...")

        for i in range(5):

            print("■", end="", flush=True)  # aqui hacemos la animacion de carga al cerrar el sistema, el flush para que se muestre cada ■ sin esperar a que termine el ciclo
            time.sleep(0.4)

        print("\nPrograma finalizado")

        break 


    # ============================================
    # ERROR
    # ============================================
    else:

        print("Opcion invalida")

        input("\nPresione ENTER para continuar...")
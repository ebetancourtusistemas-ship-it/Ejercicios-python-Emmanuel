
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

Tips de lógica para el estudiante
• Puedes usar una lista para guardar todas las materias.
• Cada materia puede guardarse como un diccionario con nombre y lista de notas.
• Usa ciclos while para el menú y for para recorrer materias.
• Usa condicionales para verificar si una materia aprueba o pierde.

"""

materias = []

while True:
    print("\n" + "=" * 35)
    print("   SISTEMA DE CONTROL DE NOTAS")
    print("=" * 35)
    print("1. Registrar materia")
    print("2. Agregar nota")
    print("3. Ver materias")
    print("4. Calcular promedio por materia")
    print("5. Ver promedio general")
    print("6. Materias aprobadas y perdidas")
    print("7. Mejor materia")
    print("8. Peor materia")
    print("9. Buscar materia")
    print("10. Eliminar materia")
    print("11. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        print("Registrar materia")

    elif opcion == "2":
        print("Agregar nota")

    elif opcion == "3":
        print("Ver materias")

    elif opcion == "4":
        print("Calcular promedio por materia")

    elif opcion == "5":
        print("Ver promedio general")

    elif opcion == "6":
        print("Materias aprobadas y perdidas")

    elif opcion == "7":
        print("Mejor materia")

    elif opcion == "8":
        print("Peor materia")

    elif opcion == "9":
        print("Buscar materia")

    elif opcion == "10":
        print("Eliminar materia")

    elif opcion == "11":
        print("Programa finalizado")
        break

    else:
        print("Opcion no valida")
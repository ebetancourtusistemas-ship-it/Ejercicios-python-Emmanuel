"""
TALLER AUTÓNOMO: EL ARTE DE LAS FUNCIONES EN PYTHON
Autor   : Emmanuel Betancourt Osorio
Materia : Fundamentos de Programación
Fecha   : Mayo 2026
Propósito: Demostrar los 4 tipos de funciones en Python
           vistos en clase, usando un sistema de estudiantes.
"""

import random

# ================================================================
# --- TIPO 1: SIN PARÁMETROS Y SIN RETURN ---
# ================================================================

# Este tipo de función no necesita datos externos ni devuelve nada.
# Solo ejecuta instrucciones cada vez que la llamamos.
# Útil para mostrar mensajes o realizar acciones repetitivas.

# Para modificarlo, debes de cambiar el contenido de la función, pero no los parámetros (porque no tiene) ni el tipo de resultado (porque no devuelve nada).

def mostrar_menu():
    print("╔══════════════════════════════════════════════╗")
    print("║      TIPO 1: SIN PARÁMETROS / SIN RETURN     ║")
    print("╠══════════════════════════════════════════════╣")
    print("║   SISTEMA DE ESTUDIANTES                     ║")
    print("║   1. Registrar estudiante                    ║")
    print("║   2. Calcular promedio                       ║")
    print("║   3. Salir                                   ║")
    print("╚══════════════════════════════════════════════╝")

mostrar_menu()


# ================================================================
# --- TIPO 2: CON PARÁMETROS Y SIN RETURN ---
# ================================================================

# Recibe datos cuando la llamamos, pero no devuelve ningún resultado.
# Útil cuando solo necesitamos mostrar o procesar información.
# Para modificarla, debes de cambiar los parámetros que recibe y el contenido de la función, pero no el tipo de resultado (porque no devuelve nada).

def registrar_estudiante(nombre, edad, carrera):
    print("╔═══════════════════════════════════════════╗")
    print("║    TIPO 2: CON PARÁMETROS / SIN RETURN    ║")
    print("╚═══════════════════════════════════════════╝")
    print(f"  Nombre  : {nombre}")
    print(f"  Edad    : {edad} años")
    print(f"  Carrera : {carrera}")

# Llamada posicional (el orden de los argumentos importa)
registrar_estudiante("Laura Torres", 19, "Ingeniería de Sistemas")

# Llamada por nombre (el orden no importa)
registrar_estudiante(carrera="Diseño Gráfico", edad=21, nombre="Camilo Ríos")


# ================================================================
# --- TIPO 3: SIN PARÁMETROS Y CON RETURN ---
# ================================================================

# No necesita datos externos, pero sí devuelve un resultado.
# Podemos guardar ese resultado en una variable y usarlo después.
# Para modificarla, debes de cambiar el contenido y el tipo de resultado que devuelve, pero no los parámetros (porque no tiene).

def tirar_dado():
    numero = random.randint(1, 6)
    return numero

print("╔═══════════════════════════════════════════╗")
print("║    TIPO 3: SIN PARÁMETROS / CON RETURN    ║")
print("╚═══════════════════════════════════════════╝")
resultado = tirar_dado()
print(f"  Tiraste el dado y obtuviste: {resultado}")


# ================================================================
# --- TIPO 4: CON PARÁMETROS Y CON RETURN ---
# ================================================================

# Es el tipo más completo: recibe datos Y devuelve un resultado.
# Muy usado cuando necesitamos calcular algo y usar ese valor después.

# Para modificarla, debes de cambiar tanto los parámetros como el contenido y el tipo de resultado que devuelve.

def calcular_promedio(nota1, nota2, nota3):
    """
    Calcula el promedio de tres notas.
    Parámetros: nota1, nota2, nota3 (float)
    Retorna: el promedio redondeado a 2 decimales (float)
    """
    promedio = (nota1 + nota2 + nota3) / 3
    return round(promedio, 2)

print("╔═══════════════════════════════════════════╗")
print("║    TIPO 4: CON PARÁMETROS / CON RETURN    ║")
print("╚═══════════════════════════════════════════╝")
promedio = calcular_promedio(3.5, 4.2, 3.8)
print(f"  Promedio del estudiante: {promedio}")

if calcular_promedio(2.5, 3.0, 2.8) >= 3.0:
    print("  Estado: Aprobado ✓")
else:
    print("  Estado: Reprobado ✗")


# ================================================================
# --- EXTRA: PARÁMETROS POR DEFECTO ---
# ================================================================

# Un parámetro con valor por defecto es opcional al llamar la función.
# Si no lo enviamos, la función usa el valor que ya tiene definido.

# Para modificarla, debes de cambiar el contenido y el tipo de resultado que devuelve, pero no el parámetro con valor por defecto (porque es opcional).

def generar_reporte(nombre, semestre, estado="Activo"):
    """
    Genera un reporte del estudiante.
    Si no se indica el estado, se asume 'Activo' por defecto.
    """
    print(f"  Reporte | {nombre} | Semestre {semestre} | Estado: {estado}")

print("╔═══════════════════════════════════════════╗")
print("║    TIPO 5 : PARÁMETROS POR DEFECTO          ║")
print("╚═══════════════════════════════════════════╝")
generar_reporte("Sofía Mendez", 1)
generar_reporte("Andrés Gil", 3, "Beca")



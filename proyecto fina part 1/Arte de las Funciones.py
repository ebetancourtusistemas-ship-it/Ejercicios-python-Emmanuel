"""
===========================================================
  TALLER AUTÓNOMO: EL ARTE DE LAS FUNCIONES EN PYTHON
===========================================================
  Autor      : Emmanuel Betancourt Osorio
  Materia    : Fundamentos de Programación
  Fecha      : Lunes 18 de Mayo del 2026
  Propósito  : Construir un documento vivo donde cada concepto
               de funciones en Python se explica y se ejecuta
               al mismo tiempo, demostrando los 6 temas.
===========================================================
"""

import random

# ===========================================================
# --- 1. DEFINICIÓN BÁSICA ---
# ===========================================================

# Una función es un bloque de código reutilizable que solo se ejecuta
# cuando la llamamos. Se define con 'def' seguido del nombre y paréntesis.

def mostrar_bienvenida():
    """
    Función básica sin parámetros ni return.
    Demuestra la estructura mínima de una función en Python.
    """
    print("╔══════════════════════════════════════════╗")
    print("║      TIPO 1 — DEFINICIÓN BÁSICA          ║")
    print("╠══════════════════════════════════════════╣")
    print("║   Bienvenido al taller de funciones      ║")
    print("║   Python — Fundamentos de Programación   ║")
    print("╚══════════════════════════════════════════╝")

# Llamamos la función por su nombre seguido de paréntesis
mostrar_bienvenida()


# ===========================================================
# --- 2. PARÁMETROS Y ARGUMENTOS ---
# ===========================================================

# Los parámetros permiten enviarle datos a la función.
# Posicionales: el orden importa. Por nombre: el orden NO importa.

def registrar_estudiante(nombre, edad, carrera):
    # Recibe tres parámetros y los muestra. No devuelve nada (sin return).
    print("╔══════════════════════════════════════════╗")
    print("║      TIPO 2 — PARÁMETROS Y ARGUMENTOS    ║")
    print("╚══════════════════════════════════════════╝")
    print(f"  Nombre  : {nombre}")
    print(f"  Edad    : {edad} años")
    print(f"  Carrera : {carrera}")

# Argumentos POSICIONALES — el orden debe coincidir con los parámetros
registrar_estudiante("Laura Torres", 19, "Ingeniería de Sistemas")

# Argumentos POR NOMBRE — el orden no importa porque indicamos el nombre
registrar_estudiante(carrera="Diseño Gráfico", edad=21, nombre="Camilo Ríos")


# ===========================================================
# --- 3. SENTENCIA RETURN ---
# ===========================================================

# 'return' hace que la función entregue un resultado hacia afuera.
# Sin return, la función solo ejecuta cosas pero no devuelve nada útil.

def calcular_promedio(nota1, nota2, nota3):
    """
    Calcular el promedio de tres notas académicas.

    Parámetros:
        nota1, nota2, nota3 (float): Las tres notas del estudiante.
    Retorna:
        float: El promedio redondeado a 2 decimales.
    """
    promedio = (nota1 + nota2 + nota3) / 3
    return round(promedio, 2)  # El resultado sale de la función con return

print("╔══════════════════════════════════════════╗")
print("║       TIPO 3 — SENTENCIA RETURN          ║")
print("╚══════════════════════════════════════════╝")

# Guardamos el valor retornado en una variable para usarlo después
mi_promedio = calcular_promedio(3.5, 4.2, 3.8)
print(f"  Promedio calculado: {mi_promedio}")

# El return también nos permite usar el resultado en condiciones
if calcular_promedio(2.5, 3.0, 2.8) >= 3.0:
    print("  Estado: Aprobado ✓")
else:
    print("  Estado: Reprobado ✗")


# ===========================================================
# --- 4. PARÁMETROS POR DEFECTO ---
# ===========================================================

# Un parámetro por defecto ya tiene un valor asignado desde la definición.
# Si no lo enviamos al llamar la función, Python usa ese valor automáticamente.
# Regla : los parámetros con defecto siempre van al final de la lista.

def generar_reporte(nombre, semestre, estado="Activo"):
    """
    Genera un reporte del estudiante.
    El parámetro 'estado' es opcional; si no se pasa, usa 'Activo'.
    """
    print(f"  Reporte | {nombre} | Semestre {semestre} | Estado: {estado}")

print("╔══════════════════════════════════════════╗")
print("║     TIPO 4 — PARÁMETROS POR DEFECTO      ║")
print("╚══════════════════════════════════════════╝")

# Solo enviamos los obligatorios; 'estado' usa su valor por defecto
generar_reporte("Sofía Mendez", 1)

# Sobreescribimos el valor por defecto enviando un argumento
generar_reporte("Andrés Gil", 3, "Beca")

# También se puede pasar por nombre
generar_reporte("Valentina Cruz", 2, estado="Suspendido")


# ===========================================================
# --- 5. SCOPE: VARIABLES LOCALES VS GLOBALES ---
# ===========================================================

# Variable GLOBAL: se define fuera de las funciones, toda la app la ve.
# Variable LOCAL: se define dentro de una función, solo vive ahí.
# Esto importa porque evita errores al usar el mismo nombre en dos lugares.

universidad = "Universidad del Quindío"   # Variable GLOBAL

def mostrar_info():
    ciudad = "Armenia"                     # Variable LOCAL — solo existe aquí
    print(f"  Universidad : {universidad}") # Puede leer la global sin problema
    print(f"  Ciudad      : {ciudad}")      # Lee su propia variable local

print("╔══════════════════════════════════════════╗")
print("║     TIPO 5 — SCOPE: LOCAL VS GLOBAL      ║")
print("╚══════════════════════════════════════════╝")

mostrar_info()
print(f"  Global accesible afuera: {universidad}")
# print(ciudad)  ← esto daría ERROR: 'ciudad' no existe fuera de la función


# ===========================================================
# --- 6. ARGUMENTOS VARIABLES (*args) ---
# ===========================================================

# *args permite que una función reciba cualquier cantidad de argumentos.
# Python los agrupa en una tupla que podemos recorrer con un for.
# Es útil cuando no sabemos cuántos valores recibirá la función.

def calcular_mejor_nota(*notas):
    # Recorre todas las notas recibidas y encuentra la más alta
    mejor = 0
    for nota in notas:
        if nota > mejor:
            mejor = nota
    return mejor

print("╔══════════════════════════════════════════╗")
print("║   TIPO 6 — ARGUMENTOS VARIABLES *args    ║")
print("╚══════════════════════════════════════════╝")

# La misma función acepta 3, 5 o cualquier cantidad de notas
print(f"  Mejor nota (3 materias): {calcular_mejor_nota(3.2, 4.5, 3.8)}")
print(f"  Mejor nota (5 materias): {calcular_mejor_nota(2.9, 3.7, 4.1, 3.5, 4.8)}")





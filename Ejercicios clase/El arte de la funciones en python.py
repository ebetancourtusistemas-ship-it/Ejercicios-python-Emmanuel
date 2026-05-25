"""
===========================================================
  TALLER AUTÓNOMO: EL ARTE DE LAS FUNCIONES EN PYTHON
===========================================================
  Autor      : Emmanuel Betancourt Osorio
  Materia    : Fundamentos de Programación
  Fecha      : Lunes 18 de Mayo del 2026
  Propósito  : Construir un documento vivo donde cada concepto
               de funciones en Python se explica con comentarios
               y se demuestra con código ejecutable, basado en
               el Capítulo 4 de ellibrodepython.com
===========================================================
"""

# ===========================================================
# --- 1. DEFINICIÓN BÁSICA ---
# ===========================================================

# Una función es un bloque de código reutilizable.
# Se define usando la palabra clave 'def'.
# Solo se ejecuta cuando la llamamos por su nombre.
# Sin la llamada, el código de adentro nunca corre.

print("╔══════════════════════════════════════════════════╗")
print("║              1. DEFINICION BÁSICA                ║")
print("╚══════════════════════════════════════════════════╝")

def mostrar_bienvenida():
    """
    Función sin parámetros de entrada ni de salida.
    Solo ejecuta instrucciones cuando es llamada.
    Fuente: ellibrodepython.com - Capítulo 4.
    """
    print("  >> Bienvenido al taller de funciones en Python.")

mostrar_bienvenida()


# ===========================================================
# --- 2. PARÁMETROS Y ARGUMENTOS ---
# ===========================================================

# Los parámetros son variables que reciben datos externos.
# Los argumentos son los valores que pasamos al llamar la función.
# En argumentos posicionales, el orden determina qué valor va a qué parámetro.
# En argumentos por nombre, indicamos explícitamente a qué parámetro va cada valor.
# Con argumentos por nombre el orden ya no importa.

print("╔══════════════════════════════════════════════════╗")
print("║           2. PARAMETROS Y ARGUMENTOS             ║")
print("╚══════════════════════════════════════════════════╝")

def mostrar_resta(a, b):
    print(f"     {a} - {b} = {a - b}")

# Llamada por posición: el primer valor va a 'a', el segundo a 'b'.
print("  >> Por posición:")
mostrar_resta(10, 3)

# Llamada por nombre: cada valor lleva la etiqueta de su parámetro.
print("  >> Por nombre (el orden no importa):")
mostrar_resta(b=3, a=10)


# ===========================================================
# --- 3. SENTENCIA RETURN ---
# ===========================================================

# 'return' hace que la función entregue un resultado hacia afuera.
# Sin return, el resultado queda atrapado dentro de la función.
# Gracias a return podemos guardar el resultado en una variable.
# También podemos usar el resultado directamente en condiciones.
# return además detiene la ejecución de la función al instante.

print("╔══════════════════════════════════════════════════╗")
print("║             3. SENTENCIA RETURN                  ║")
print("╚══════════════════════════════════════════════════╝")
def calcular_promedio(nota1, nota2, nota3):
    """
    Calcula el promedio de tres notas y lo devuelve.

    ¿Por qué usamos return aquí?
    Porque el promedio es un dato que necesitamos fuera
    de la función: para guardarlo, compararlo o imprimirlo.

    Parámetros:
        nota1 (float): Primera nota.
        nota2 (float): Segunda nota.
        nota3 (float): Tercera nota.
    Retorna:
        float: El promedio redondeado a 2 decimales.
    """
    promedio = (nota1 + nota2 + nota3) / 3
    return round(promedio, 2)

# El valor retornado se guarda en una variable para usarlo después.
mi_promedio = calcular_promedio(3.5, 4.2, 3.8)
print(f"  >> Promedio obtenido : {mi_promedio}")

# Aquí usamos el return directamente dentro de un if.
if calcular_promedio(2.0, 2.5, 1.8) >= 3.0:
    print("  >> Estado            : Aprobado  ✓")
else:
    print("  >> Estado            : Reprobado ✗")


# ===========================================================
# --- 4. PARÁMETROS POR DEFECTO ---
# ===========================================================

# Un parámetro por defecto ya tiene un valor asignado desde la definición.
# Si no lo enviamos al llamar la función, Python usa ese valor automáticamente.
# Esto hace que el parámetro sea opcional en la llamada.
# Los parámetros con defecto siempre van al FINAL de la lista.
# Solo lo sobreescribimos cuando necesitamos un valor diferente.

print("╔══════════════════════════════════════════════════╗")
print("║             4. PARAMETROS POR DEFECTO            ║")
print("╚══════════════════════════════════════════════════╝")

def registrar_estudiante(nombre, semestre, estado="Activo"):
    """
    Registra un estudiante con su nombre, semestre y estado.

    ¿Por qué 'estado' tiene valor por defecto?
    Porque la mayoría de estudiantes están activos. Solo lo
    pasamos cuando el estado es diferente al habitual.

    Parámetros:
        nombre   (str): Nombre del estudiante.
        semestre (int): Semestre actual.
        estado   (str): Estado académico. Por defecto: 'Activo'.
    """
    print(f"  >> {nombre:<20} | Semestre {semestre} | Estado: {estado}")

# No enviamos 'estado', Python usa "Activo" automáticamente.
registrar_estudiante("Laura Torres", 1)

# Aquí el estado es diferente, así que lo sobreescribimos.
registrar_estudiante("Carlos Pérez", 3, "Beca Completa")

# También podemos pasarlo por nombre para mayor claridad.
registrar_estudiante("Sofía Mendez", 2, estado="Suspendido")


# ===========================================================
# --- 5. SCOPE: VARIABLES LOCALES VS GLOBALES ---
# ===========================================================

# Variable GLOBAL: se define fuera de las funciones.
# Una variable global es visible en todo el programa.
# Variable LOCAL: se define dentro de una función.
# Una variable local solo existe mientras la función se ejecuta.
# Intentar usar una variable local afuera causa un error NameError.

print("╔══════════════════════════════════════════════════╗")
print("║           5. SCOPE: LOCAL VS GLOBAL              ║")
print("╚══════════════════════════════════════════════════╝")

nombre_universidad = "Universidad del Quindío"  # Variable GLOBAL

def mostrar_sede():
    ciudad = "Armenia, Colombia"  # Variable LOCAL: solo vive aquí adentro.
    print(f"  >> Universidad   : {nombre_universidad}")
    print(f"  >> Ciudad (local): {ciudad}")

mostrar_sede()

# La variable global sigue disponible fuera de la función.
print(f"  >> Global afuera : {nombre_universidad}")
# print(ciudad)  <-- esto causaría NameError porque 'ciudad' es local.


# ===========================================================
# --- 6. ARGUMENTOS VARIABLES (*args) ---
# ===========================================================

# *args permite recibir cualquier cantidad de argumentos.
# Python empaqueta todos esos valores en una tupla automáticamente.
# Podemos recorrer esa tupla con un ciclo for.
# Es útil cuando no sabemos cuántos valores recibirá la función.
# La misma función sirve para 2, 5 o cualquier cantidad de argumentos.

print("╔══════════════════════════════════════════════════╗")
print("║             6. ARGUMENTOS VARIABLES              ║")
print("║                      (*ARGS)                     ║")
print("╚══════════════════════════════════════════════════╝")


def sumar_notas(*notas):
    total = 0
    for nota in notas:  # 'notas' es una tupla con todos los valores recibidos.
        total += nota
    return total

# La misma función acepta diferente cantidad de argumentos cada vez.
print(f"  >> Suma de 2 notas : {sumar_notas(4.0, 3.5)}")
print(f"  >> Suma de 4 notas : {sumar_notas(3.2, 4.5, 3.8, 4.1)}")
print(f"  >> Suma de 6 notas : {sumar_notas(2.5, 3.0, 4.0, 3.5, 4.8, 3.2)}")



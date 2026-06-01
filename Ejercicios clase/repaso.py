"""
# ============================================================
# REPASO PYTHON 🧠
# ============================================================


# ── 1. VARIABLES ──────────────────────────────────────────
# Una variable es una cajita con nombre donde guardas un dato.
# Hay 4 tipos básicos:

nombre = "Emmanuel"  # str   → texto, siempre entre comillas
edad   = 20          # int   → número sin decimales
precio = 9.99        # float → número con decimales
activo = True        # bool  → solo puede ser True o False

# ⚠️ IMPORTANTE: input() siempre devuelve texto aunque escribas un número.
# Si vas a hacer matemáticas con lo que el usuario escribe, conviértelo:
edad = int(input("¿Cuántos años? "))    # int() convierte texto a entero
precio = float(input("¿Precio? "))      # float() convierte texto a decimal


# ── 2. PRINT ──────────────────────────────────────────────
# Muestra información en pantalla.
# La forma más útil es el f-string: pones f antes de las comillas
# y las variables las metes entre { }

nombre = "Emmanuel"
edad   = 20
print(f"Me llamo {nombre} y tengo {edad} años")  # → Me llamo Emmanuel y tengo 20 años
print(f"Precio: ${9.99:.2f}")   # :.2f → muestra exactamente 2 decimales → $9.99
print("-" * 30)                 # imprime 30 guiones de golpe


# ── 3. MATEMÁTICAS ────────────────────────────────────────
a, b = 10, 3

print(a + b)   # 13   → suma
print(a - b)   # 7    → resta
print(a * b)   # 30   → multiplicación
print(a / b)   # 3.33 → división con decimales
print(a // b)  # 3    → división sin decimales (se come los decimales)
print(a % b)   # 1    → residuo de dividir. Si da 0 = es divisible
print(a ** b)  # 1000 → potencia (10 elevado al cubo)

# Atajos para modificar una variable:
x = 10
x += 5   # x = x + 5 → ahora x vale 15
x -= 3   # x = x - 3 → ahora x vale 12
x *= 2   # x = x * 2 → ahora x vale 24


# ── 4. COMPARACIONES Y LÓGICA ─────────────────────────────
# Hacen una pregunta y solo responden True o False.
# Siempre los verás dentro de un if o un while.

# ==  ¿son iguales?      !=  ¿son diferentes?
# >   ¿es mayor?         <   ¿es menor?
# >=  ¿es mayor o igual? <=  ¿es menor o igual?

# and → AMBAS condiciones deben ser True para que el resultado sea True
# or  → con que UNA sola sea True, el resultado es True
# not → invierte: convierte True en False y False en True

edad = 20
if edad >= 18 and edad < 65:
    print("Eres adulto en edad laboral")


# ── 5. IF / ELIF / ELSE ───────────────────────────────────
# Sirve para tomar decisiones.
# Python evalúa de arriba hacia abajo y cuando encuentra
# una condición True, ejecuta ese bloque y SALE. No sigue revisando.

nota = int(input("¿Tu nota? "))

if nota >= 90:
    print("Excelente 🏆")
elif nota >= 70:        # solo llega aquí si la de arriba fue False
    print("Aprobado ✅")
else:                   # solo llega aquí si TODAS las de arriba fueron False
    print("Reprobado ❌")

# Versión corta en una sola línea (if ternario):
print("Par" if nota % 2 == 0 else "Impar")


# ── 6. FOR ────────────────────────────────────────────────
# Repite código cuando YA SABES cuántas veces o tienes una lista.
# La variable (i, fruta, etc.) cambia de valor en cada vuelta.

for i in range(5):          # i vale: 0, 1, 2, 3, 4
    print(i)

for i in range(1, 11, 2):   # (inicio, fin, paso) → 1, 3, 5, 7, 9
    print(i)                 # el número final NUNCA entra

frutas = ["manzana", "pera", "uva"]
for fruta in frutas:         # recorre cada elemento de la lista
    print(fruta)

for i, fruta in enumerate(frutas):  # cuando necesitas el índice Y el valor
    print(f"{i}: {fruta}")           # 0: manzana, 1: pera, 2: uva


# ── 7. WHILE ──────────────────────────────────────────────
# Repite código mientras una condición sea True.
# Úsalo cuando NO sabes cuántas veces vas a repetir.
# ⚠️ Siempre cambia la variable dentro, si no se repite para siempre.

contador = 1
while contador <= 5:
    print(contador)
    contador += 1    # sin esto, contador siempre es 1 → bucle infinito

# break    → para el ciclo completamente y sale
# continue → salta lo que queda de esa vuelta y va a la siguiente
for i in range(10):
    if i == 3: continue   # cuando i es 3, salta y va al 4
    if i == 7: break      # cuando i es 7, para todo
    print(i)              # imprime: 0,1,2,4,5,6


# ── 8. LISTAS ─────────────────────────────────────────────
# Guarda varios datos en orden dentro de una sola variable.
# Cada dato tiene una posición (índice) que empieza en 0.

nums = [10, 20, 30, 40, 50]
#        0   1   2   3   4   → positivos: de izquierda a derecha
#       -5  -4  -3  -2  -1   → negativos: de derecha a izquierda

print(nums[0])    # 10  → primero
print(nums[-1])   # 50  → último (truco con negativo)
print(nums[1:3])  # [20, 30] → slice: desde índice 1 hasta el 2 (el 3 no entra)

nums.append(60)   # agrega el 60 al final
nums.remove(10)   # elimina el valor 10
nums.sort()       # ordena de menor a mayor
print(len(nums))  # cuántos elementos tiene
print(max(nums))  # el mayor
print(min(nums))  # el menor
print(sum(nums))  # suma de todos


# ── 9. TUPLAS ─────────────────────────────────────────────
# Exactamente igual a una lista PERO no se puede modificar nunca.
# Úsala cuando los datos son fijos y no deben cambiar.

colores = ("rojo", "verde", "azul")
print(colores[0])    # rojo → se accede igual que una lista
r, g, b = colores    # desempaquetar: r="rojo", g="verde", b="azul"

# El uso más común: devolver varios valores desde una función
def min_max(lista):
    return min(lista), max(lista)   # devuelve dos valores a la vez

menor, mayor = min_max([3, 1, 8, 5])
print(menor, mayor)  # 1  8


# ── 10. DICCIONARIOS ──────────────────────────────────────
# Guarda datos con nombre propio. Formato: "clave": valor
# Piénsalo como una ficha: cada campo tiene su etiqueta.

alumno = {"nombre": "Emmanuel", "edad": 20, "nota": 9.5}

print(alumno["nombre"])              # Emmanuel → accedes con la clave
print(alumno.get("tel", "No tiene")) # .get() no da error si la clave no existe
alumno["ciudad"] = "CDMX"           # agrega una clave nueva
del alumno["edad"]                   # elimina esa clave

for clave, valor in alumno.items():  # recorrer todo el diccionario
    print(f"{clave}: {valor}")


# ── 11. FUNCIONES ─────────────────────────────────────────
# Bloque de código con nombre. Lo escribes una vez y lo reutilizas.
# Pueden recibir datos (parámetros) y devolver un resultado (return).

def saludar(nombre, pais="México"):  # pais="México" es el valor por defecto
    return f"Hola {nombre} de {pais}"  # return devuelve el resultado

print(saludar("Emmanuel"))            # → Hola Emmanuel de México
print(saludar("Ana", "Colombia"))     # → Hola Ana de Colombia

def promedio(notas):
    return sum(notas) / len(notas)

print(promedio([80, 90, 85]))         # → 85.0


# ── 12. TRY / EXCEPT ──────────────────────────────────────
# Cuando algo PUEDE fallar, lo metes en try.
# Si falla, Python no se rompe sino que va al except.
# finally siempre se ejecuta, haya error o no.

try:
    n = int(input("Dame un número: "))
    print(10 / n)
except ValueError:           # si el usuario escribe letras en lugar de número
    print("Eso no es un número")
except ZeroDivisionError:    # si el usuario escribe 0
    print("No se puede dividir entre 0")
finally:
    print("Fin del programa")   # esto corre siempre


# ── 13. MATH Y RANDOM ─────────────────────────────────────
# Módulos = cajas de herramientas que importas cuando las necesitas.

import math
import random

# MATH → matemáticas avanzadas
print(math.sqrt(25))     # 5.0  → raíz cuadrada
print(math.ceil(3.2))    # 4    → redondea HACIA ARRIBA siempre
print(math.floor(3.9))   # 3    → redondea HACIA ABAJO siempre
print(math.pi)           # 3.14159... → el número Pi
print(math.factorial(5)) # 120  → 5 × 4 × 3 × 2 × 1

# RANDOM → genera cosas al azar
print(random.randint(1, 6))                        # número entre 1 y 6
print(random.choice(["piedra","papel","tijera"]))   # elige uno al azar de la lista


# ── 14. STRINGS ───────────────────────────────────────────
# Los textos tienen métodos propios para manipularlos.

t = "  Hola Mundo  "
print(t.strip())               # "Hola Mundo"  → quita espacios de los extremos
print(t.lower())               # "  hola mundo  " → todo minúsculas
print(t.upper())               # "  HOLA MUNDO  " → todo mayúsculas
print(t.replace("Hola","Bye")) # cambia "Hola" por "Bye"
print("a,b,c".split(","))      # ['a','b','c'] → corta el texto y hace una lista
print("-".join(["a","b","c"])) # "a-b-c" → une una lista en un solo texto
print("hola".startswith("ho")) # True → ¿empieza con "ho"?
print("hola".endswith("la"))   # True → ¿termina con "la"?


# ── 15. COMPRENSIÓN DE LISTAS ─────────────────────────────
# Crea una lista en una sola línea.
# Estructura: [qué guardar  for variable in lista  if condición]
# La condición al final es opcional, sirve para filtrar.

cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)    # [1, 4, 9, 16, 25]

aprobados = [n for n in [45, 78, 92, 55] if n >= 60]
print(aprobados)    # [78, 92]  → solo los que pasaron el filtro


# ── 16. SETS ──────────────────────────────────────────────
# Como una lista pero NUNCA tiene duplicados y no tiene orden.
# Su uso más común: eliminar repetidos de una lista.

lista = [1, 2, 2, 3, 3, 3]
sin_rep = list(set(lista))
print(sin_rep)   # [1, 2, 3]

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # {1,2,3,4,5,6} → todos los elementos de ambos
print(a & b)  # {3,4}         → solo los que están en LOS DOS
print(a - b)  # {1,2}         → los de A que NO están en B


# ── 17. CLASES Y OBJETOS ──────────────────────────────────
# Clase = molde para crear objetos con sus propios datos y funciones.
# __init__ es el método que se ejecuta automáticamente al crear el objeto.
# self representa al objeto mismo, siempre va de primer parámetro.

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre   # dato que guarda el objeto
        self.nota   = nota

    def estado(self):          # función propia del objeto
        if self.nota >= 60:
            return f"{self.nombre}: Aprobado ✅"
        else:
            return f"{self.nombre}: Reprobado ❌"

# Crear objetos con el molde:
e1 = Estudiante("Emmanuel", 85)
e2 = Estudiante("Ana", 45)
"""
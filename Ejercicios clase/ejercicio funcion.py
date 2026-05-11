'''
Ejercicio: El Simulador "Python Coffee Shop"

El estudiante debe construir un programa que gestione la venta de un café. Para ello, deberá programar 4 funciones específicas, cada una representando uno de los 4 tipos de funciones que aprendimos.

El Flujo de Trabajo

El programa debe funcionar así:

Se muestra un saludo.

Se le pregunta al usuario qué tamaño de café quiere.

Se calcula el precio sumando impuestos.

Se confirma que el pedido está listo.

1. Sin parámetros y Sin retorno: mostrar_bienvenida()

¿Qué debe hacer el estudiante?
Crear una función que solo imprima texto decorativo.

Instrucción: Debe imprimir el nombre de la cafetería y el menú de tamaños (Pequeño: $2.00, Mediano: $3.00, Grande: $4.00).

Objetivo: Entender que hay funciones que solo sirven para comunicar información fija al usuario.

2. Sin parámetros y Con retorno: elegir_tamano()

¿Qué debe hacer el estudiante?
Crear una función que interactúe con el teclado y "envíe" la respuesta hacia afuera.

Instrucción: Debe preguntar al usuario: "¿Qué tamaño desea? (P/M/G):". La función debe capturar la letra con un input() y devolverla usando return.

Objetivo: Entender que una función puede obtener datos del mundo exterior y entregarlos al programa.

3. Con parámetros y Con retorno: calcular_precio(letra_tamano)

¿Qué debe hacer el estudiante?
Crear la lógica matemática del negocio.

Instrucción: La función recibe la letra (P, M o G).

Si es 'P', el precio es 2.0.

Si es 'M', es 3.0.

Si es 'G', es 4.0.

Al final, debe sumarle un 10% de impuesto y retornar el total final.

Objetivo: Entender el procesamiento: entra un dato crudo (letra) y sale un dato procesado (dinero).

4. Con parámetros y Sin retorno: preparar_pedido(letra_tamano, total)

¿Qué debe hacer el estudiante?
Crear la acción final que cierra el proceso.

Instrucción: La función recibe el tamaño y el precio final. Debe imprimir un mensaje como: "Preparando su café [tamaño]... El total fue $[total]. ¡Disfrute!".

Objetivo: Entender que una función puede usar resultados previos para ejecutar una acción de cierre.
'''

import time
def mostrar_bienvenida():
    time.sleep(1)
    print("╔══════════════════════════════╗")
    print("║      PYTHON COFFEE ☕        ║")
    print("╚══════════════════════════════╝")

    time.sleep(1)
    print("        (  )   (   )  )")
    print("         ) (   )  (  (")
    print("         ( )  (    ) )")
    print("         _____________")
    print("        <_____________> ___")
    print("        |             |/ _ \\")
    print("        |   PYTHON    | | | |")
    print("        |    COFFEE   | |_| |")
    print("     ___|             |\\___/")
    print("    /    \\___________/    \\")
    print("    \\_____________________/")

    time.sleep(1)
    print("┌──────────────────────────────┐")
    print("│  P - Pequeño  : $2.00        │")
    print("│  M - Mediano  : $3.00        │")
    print("│  G - Grande   : $4.00        │")
    print("└──────────────────────────────┘")


def elegir_tamano():
    tamano = input("☞ ¿Qué tamaño desea? (P/M/G): ").upper()
    return tamano


def calcular_precio(letra_tamano):
    if letra_tamano == "P":
        precio = 2.0
    elif letra_tamano == "M":
        precio = 3.0
    elif letra_tamano == "G":
        precio = 4.0
    else:
        precio = 0

    total = precio + (precio * 0.10)
    return total


def preparar_pedido(letra_tamaño, total):
    if letra_tamaño == "P":
        nombre = "Pequeño"
    elif letra_tamaño == "M":
        nombre = "Mediano"
    elif letra_tamaño == "G":
        nombre = "Grande"
    else:
        nombre = "No válido"


    time.sleep(1.5)

    print("\n Preparando su café", nombre)
    print(" El total fue: $", round(total, 2))
    print("¡Disfrute su bebida!")


# Programa principal
mostrar_bienvenida()
tamano = elegir_tamano()
total = calcular_precio(tamano)
preparar_pedido(tamano, total)




    
  

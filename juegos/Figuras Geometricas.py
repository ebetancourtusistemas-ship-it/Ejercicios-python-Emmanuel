'''
Enunciado del Ejercicio: Geometría con Bucles (Arte ASCII)

Objetivo: Desarrollar la lógica de programación y el manejo de bucles anidados (for o while) para representar figuras 
geométricas bidimensionales en la terminal utilizando caracteres (como *, + o #).

Descripción de la Tarea

Debes crear un programa que, al ejecutarse, imprima de forma clara las siguientes cinco figuras. El usuario debería poder 
definir el tamaño (lado, radio o altura) de las figuras antes de imprimirlas.

Figuras Requeridas:
	1.	Triángulo Rectángulo: El programa debe imprimir un triángulo alineado a la izquierda.
	2.	Cuadrado: Una representación con la misma cantidad de filas y columnas.
	3.	Rectángulo: Donde la base sea visiblemente mayor a la altura (ejemplo: proporción 2:1).
	4.	Círculo: (Reto de lógica) Utiliza la ecuación del círculo o una aproximación de distancia de puntos para dibujar 
        una forma redondeada.
	5.	Pentágono: Una figura de 5 lados (puedes combinar un triángulo sobre un trapecio o rectángulo).

Requerimientos Técnicos
•	Visualización: Crear un menú que permita elegir la figura a imprimir.
•	Interactividad: El programa debe preguntar al usuario: "Ingrese el tamaño para sus figuras:".
•	Estructura: Utiliza bucles anidados. El bucle externo controlará las filas (eje Y y el interno las columnas (eje X).
•	Presentación: Cada figura debe estar separada por un título y un espacio en blanco para que sea legible.

Ejemplo de Salida Esperada (Tamaño 5)

--- CUADRADO ---
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #

--- RECTÁNGULO (5x10) ---
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #

--- TRIÁNGULO ---
# 
# # 
# # # 
# # # # 
# # # # #

--- CÍRCULO (Radio 5) ---
      # # # #      
    # # # # # #    
  # # # # # # # #  
  # # # # # # # #  
    # # # # # #    
      # # # #      

--- PENTÁGONO ---
      #      
    # # #    
  # # # # #  
  # # # # #  
  # # # # #  

  Solución del Ejercicio Propuesto 
'''


def print_square(size): 
    # Imprime un cuadrado de tamaño x tamaño
    print("--- CUADRADO ---")
    for i in range(size):
        # Cada fila contiene 'size' símbolos #
        print("# " * size)

def print_rectangle(size):
    # Crea un rectángulo con altura = size y ancho = 2 * size
    height = size
    width = 2 * size
    print(f"--- RECTÁNGULO ({height}x{width}) ---")
    for i in range(height):
        # Imprime cada fila con el ancho especificado
        print("# " * width)

def print_triangle(size):
    # Imprime un triángulo rectángulo aumentando # en cada fila
    print("--- TRIÁNGULO ---")
    for i in range(1, size + 1):
        # La fila i contiene i símbolos #
        print("# " * i)

def print_circle(radius):
    # Dibuja un círculo usando la ecuación x² + y² = r²
    print(f"--- CÍRCULO (Radio {radius}) ---")
    for y in range(-radius, radius + 1):
        line = ""
        for x in range(-radius, radius + 1):
            # Si el punto está dentro del círculo, dibuja #
            if x**2 + y**2 <= radius**2:
                line += "# "
            else:
                # Si no, dibuja espacios
                line += "  "
        print(line)

def print_pentagon(size):
    # Imprime un pentágono aproximado con un triángulo y base rectangular
    print("--- PENTÁGONO ---")
    for i in range(size):
        if i == 0:
            # Primera fila: solo un # centrado
            print(" " * (size - 1) + "#")
        elif i < size // 2:
            # Filas superiores: van aumentando de ancho
            spaces = size - i - 1
            hashes = 2 * i + 1
            print(" " * spaces + "# " * hashes)
        else:
            # Filas inferiores: base rectangular del pentágono
            print("# " * (2 * size - 1))

def main():
    # Menú principal interactivo
    while True:
        print("\nFiguras disponibles:")
        print("1. Triángulo Rectángulo")
        print("2. Cuadrado")
        print("3. Rectángulo")
        print("4. Círculo")
        print("5. Pentágono")
        print("6. Salir")
        
        choice = input("Elige una figura (1-6): ")
        if choice == "6":
            print("Escogiste salir del programa. ¡Hasta luego!")
            # Salir del programa
            break
        if choice not in ["1", "2", "3", "4", "5"]:
            # Validar opción ingresada
            print("Opción inválida.")
            continue
        
        # Solicitar tamaño al usuario con ejemplo
        size = int(input("Ingrese el tamaño para sus figuras (ejemplo: 5): "))
        
        # Dibujar la figura seleccionada
        if choice == "1":
            print_triangle(size)
        elif choice == "2": 
            print_square(size)
        elif choice == "3":
            print_rectangle(size)
        elif choice == "4":   
            print_circle(size)
        elif choice == "5":
            print_pentagon(size)

if __name__ == "__main__":
    main()
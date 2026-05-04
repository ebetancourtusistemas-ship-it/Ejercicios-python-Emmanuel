import random

#  1.>/ Funciones que no reciben parametros y no devuelven resultados.

def mostrar_bienvenida():
    # no hay parametros de entrada y no se deviuelve nigun resultado

    print("¡Bienvenido a la funcion de bienvenida!")
    print("Por favor, selecciona una opcion del menu.")
    print("1. Opcion 1")
    print("2. Opcion 2")        
    print("3. Opcion 3")
    print("4. Salir")

#Para usar la funcion, simplemente la llamamos por su nombre seguida de parentesis  
mostrar_bienvenida()       


#   2.>/ Funciones que reciben parametros y no devuelven resultados.

def saludar_persona(nombre,edad):
    #recibe "nombre" y "edad" como parametros de entrada, pero no devuelve ningun resultado 
 print(f"¡Hola {nombre}, veo que tienes {edad} años!")  
 #no tiene return, solo imprime en pantalla el mensaje 

saludar_persona("Emmanuel", 25)  #llamamos a la funcion pasando un nombre y una edad como argumentos

#    3.>/ Funciones que no reciben parametros y devuelven resultados.

def tirar_dado():
    #no recibe parametros de entrada, pero devuelve un resultado (un numero aleatorio entre 1 y 6)
    numero_obtenido = random.randint(1,6)  #genera un numero aleatorio entre 1 y 6
    return numero_obtenido

resultado = tirar_dado()  #llamamos a la funcion y guardamos el resultado en una variable
print(f"Has tirado el dado y obtuviste: {resultado}")  #imprime el resultado obtenido al tirar el dado




#    4.>/ Funciones que reciben parametros y devuelven resultados.

def calcular_area_rectangulo(base, altura):
    #recibe "base" y "altura" como parametros de entrada, y devuelve el area del rectangulo
    area = base * altura  #calcula el area multiplicando base por altura
    return area  #devuelve el resultado del area calculada

#para usarla
mi_area = calcular_area_rectangulo(5, 10)  
print(f"El area del rectangulo es: {mi_area}")  
# esto es un comentario de una sola linea

"""" esto es un comentario
de multiples lineas
en Python
"""

#condicionales


"""
simples: Si ()                 |    if():
Dobles: si() si() sino()       |    if():  elif()
multiples switch               |    No existe

"""

#Phyton Trabje Con IF Simple

"""
Palabrareservada (Condicion):
       SentenciaUno
       SentenciaDos

"""

if (True):
    print("Hola")
    print("Como estas")


if (False):
    print("Bien")
    print("Y Usted")
# Comparacion de numeros enteros en Phyton
a=5;b=3
if(a>b):
    print("A es mayor que B")
# Comparacion de datos booleanos en Phyton
C = False
if (C==True):
    print("C es VERDADERO")
# Comparacion de caracteres en Python

caracter = 'a'
if(caracter == 'b'):
    print("El caracter es:", caracter)

palabra = "Hola"
if(palabra == "Chao"):
    print("La palabra es:", caracter)

#Python Trabaje con si Doble
"""
Palabra reservada (condicion)
     SentenciaUno
     SentenciaDos
SINO(Condicion)
     SentenciaUno
     SentenciaDos
"""
nota=5

if (nota >= 4):   #Condicion de inicion
    print("Excelente")
elif (nota >= 2 and nota <= 3):    #Condicion Anidada
    print("Necesita recuperar")
elif (nota < 2):
    print("Reprobo")
else: # Condicion Cierre
    print("Su nota fue 0")
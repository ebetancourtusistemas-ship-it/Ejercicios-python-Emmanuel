# calculadora_promedios.py

def ingresar_calificaciones():
    materias = []
    calificaciones = []
    
    while True:
        nombre = input("Ingrese la materia: ")
        
        # validar nota
        while True:
            try:
                nota = float(input("Ingrese la calificación (0 a 10): "))
                if 0 <= nota <= 10:
                    break
                else:
                    print("Debe estar entre 0 y 10")
            except:
                print("Ingrese un número válido")
        
        materias.append(nombre)
        calificaciones.append(nota)
        
        seguir = input("¿Desea agregar otra? (s/n): ").lower()
        if seguir != "s":
            break
    
    return materias, calificaciones


def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []
    
    for i in range(len(calificaciones)):
        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    
    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    if len(calificaciones) == 0:
        return None, None
    
    mayor = calificaciones.index(max(calificaciones))
    menor = calificaciones.index(min(calificaciones))
    
    return mayor, menor


def main():
    materias, calificaciones = ingresar_calificaciones()
    
    if len(materias) == 0:
        print("No ingresó materias")
        return
    
    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    mayor, menor = encontrar_extremos(calificaciones)
    
    print("\n--- RESUMEN ---")
    
    # mostrar materias
    for i in range(len(materias)):
        print(materias[i], ":", calificaciones[i])
    
    print("Promedio:", round(promedio, 2))
    
    print("\nAprobadas:")
    for i in aprobadas:
        print(materias[i])
    
    print("\nReprobadas:")
    for i in reprobadas:
        print(materias[i])
    
    print("\nMejor materia:", materias[mayor], "-", calificaciones[mayor])
    print("Peor materia:", materias[menor], "-", calificaciones[menor])
    
    print("\nPrograma finalizado")


if __name__ == "__main__":
    main()
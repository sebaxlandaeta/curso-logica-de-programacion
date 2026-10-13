# Función que recorre y muestra en pantalla todos los signos del arreglo
def imprimir_arreglo(arreglo):
    print("""                    Signos Zodiacales:                   """)
    for value in arreglo:
        print(value)


# Captura por teclado el día y el mes de nacimiento transformándolos a enteros
def captura_datos():
    print("""         Indique el dia de su nacimiento:       """)
    dia = int(input("-"))
    print("""         Indique el mes de su nacimiento:     """)
    mes = int(input("-"))
    return dia, mes


# Utiliza condiciones compuestas para determinar el índice del signo y la estación
def procesar(dia, mes):
    # Condicionales anidadas/compuestas para asociar el rango de fechas al signo
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        posicion = 0
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        posicion = 1
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        posicion = 2
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        posicion = 3
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        posicion = 4
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        posicion = 5
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        posicion = 6
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        posicion = 7
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        posicion = 8
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        posicion = 9
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        posicion = 10
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        posicion = 11
    else:
        posicion = 12  # Bandera de error para fechas inválidas

    # Evalúa el mes para asignar la estación del año correspondiente
    if mes == 11 or mes == 12 or mes == 1:
        estacion = estaciones[0]
    elif mes == 8 or mes == 9 or mes == 10:
        estacion = estaciones[1]
    elif mes == 5 or mes == 6 or mes == 7:
        estacion = estaciones[2]
    elif mes == 2 or mes == 3 or mes == 4:
        estacion = estaciones[3]
    else:
        estacion = "Desconocida"
    return posicion, estacion


# Valida la posición obtenida para imprimir el signo correcto o un error
def imprimir_resultado(posicion, estacion):
    if posicion < 12:
        print("-" * 50)
        print(f"Tu signo zodiacal es: -> {signos[posicion]}")
    else:
        print("La fecha que ingresaste no es valida.")
    print(f"Usted nacio en la estacion: -> {estacion}")
    print("-" * 50)


# Arreglos globales con los 12 signos y las 4 estaciones
signos = [
    "Aries",
    "Tauro",
    "Geminis",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Escorpio",
    "Sagitario",
    "Capricornio",
    "Acuario",
    "Piscis",
]
estaciones = [
    "Invierno",
    "Otoño",
    "Verano",
    "Primavera",
]  # Nota: corregido "Inviervo" a "Invierno"

# Ejecución principal del programa
imprimir_arreglo(signos)
dia, mes = captura_datos()
posicion, estacion = procesar(dia, mes)
imprimir_resultado(posicion, estacion)
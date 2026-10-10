while True:
    print("          ¡Bienvenido a cines unidos!          ")
    print("-" * 46)
    print("               Introduzca su edad:               ")
    edad = int(input("---> "))
    print("Introduzca el dia que desea ver la pelicula:")
    dia = input("---> ").lower()
    print("          Horarios de la pelicula:        ")
    print("        1pm - 3pm - 5pm - 7pm - 9pm       \n")
    print("Introduzca la hora que desea ver la pelicula:")
    hora = int(input("---> "))
    print("-" * 46)
    
    # Validación de números negativos
    if edad < 1 or hora < 1:
        print("Ingresaste algun numero negativo. Intentanlo de nuevo.\n")
        continue
        
    dia_valido = dia in ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

    # Estructura match-case para asignar precios según la hora
    match hora:
        case 1:
            precio = 1
        case 3:
            precio = 2
        case 5:
            precio = 3
        case _:
            precio = 4

    # Reglas de descuento por edad o día especial
    if edad < 3 or edad > 70:
        porc = 100
    elif dia == "lunes":
        porc = 50
    else:
        porc = 0

    descuento = precio * porc / 100
    total = precio - descuento

    # Validación de día válido de la semana
    if not dia_valido:
        print("        Debes seleccionar un dia valido.\n        ")
        continue
    else:
        print(f"- Edad del cliente: -> {edad}")
        print(f"- Hora de la pelicula: -> {hora}pm")
        print(f"- Dia de la pelicula: {dia}")
        print(f"- Precio de la pelicula: -> {precio}bs")
        print(f"- % Descuento: -> {porc}%")
        print(f"- Monto de descuento: -> {descuento}bs")
        print(f"- Total a pagar: -> {total}bs \n")

    # Control para repetir o finalizar el ciclo principal del programa
    resp = input("    Desea realizar otra compra? (si/no)     \n").lower()
    if resp != "si":
        break

print("          ¡Gracias por la compra!          ")
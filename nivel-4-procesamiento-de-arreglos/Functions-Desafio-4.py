# Valida que el número de camiseta esté dentro de un rango permitido (min y max)
def validar_camisa(min, max):
    while True:
        valor = int(input("- Ingrese el numero de camiseta del jugador: -> "))
        if valor >= min and valor <= max:
            return valor
        else:
            print("-" * 61)
            print(f"        El valor ingresado debe estar entre {min} y {max}.        ")
            print("-" * 61)


# Valida que el nombre tenga al menos 8 caracteres y esté compuesto solo por letras y espacios (para incluir apellido)
def validar_nombre():
    while True:
        name = input("- Ingrese el nombre completo del jugador: -> ")
        # Se remueven los espacios temporalmente con replace para comprobar que el resto sean letras
        if len(name) >= 8 and name.replace(" ", "").isalpha():
            return name
        else:
            print("-" * 61)
            print("      Necesitas un minimo de 8 caracteres (Solo letras y espacios)      ")
            print("-" * 61)


# Valida que la posición ingresada sea una de las permitidas en el béisbol
def validar_posicion(posiciones_validas):
    while True:
        encontrado = False
        valor = input(
            "- Ingrese la posicion en la que juega (Ejemplo: 1B, 2B, P) -> "
        ).upper()
        for opcion in posiciones_validas:
            if valor == opcion:
                encontrado = True
                break
        if encontrado:
            return valor
        else:
            print("-" * 61)
            print(
                "Posición inválida. Las opciones son: 1B, 2B, 3B, SS, LF, CF, RF, P, C."
            )
            print("-" * 61)


# Valida que la cantidad de hits se encuentre dentro de un rango permitido
def validar_hits(min, max):
    while True:
        valor = int(input("- Ingrese los hits del jugador: -> "))
        if valor >= min and valor <= max:
            return valor
        else:
            print("-" * 61)
            print(f"         El valor ingresado debe estar entre {min} y {max}.         ")
            print("-" * 61)


# Valida que el average de bateo sea un número real dentro de un rango permitido
def validar_avarage(min, max):
    while True:
        valor = float(input("- Ingrese el avarage de bateo del jugador: -> "))
        if valor >= min and valor <= max:
            return valor
        else:
            print("-" * 61)
            print(f"        El valor ingresado debe estar entre {min} y {max}.")
            print("-" * 61)
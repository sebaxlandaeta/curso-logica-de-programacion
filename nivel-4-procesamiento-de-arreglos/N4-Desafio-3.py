# Permite registrar empleados de forma dinámica validando que la cédula no se repita
def leer_datos():
    while True:
        print("-" * 61)
        ci = int(input("- Ingrese la cedula del empleado: -> "))
        existe = buscar_unico(ci, cedulas)
        if existe:
            print('"Ya se encuentra registrado. Intente con otra cédula."')
            continue
        cedulas.append(ci)
        name = input("- Ingrese el nombre del empleado: -> ")
        nombres.append(name)
        total = float(input("- Ingrese el total facturado: -> "))
        montos.append(total)
        cant_fact = int(input("- Ingrese la cantidad de facturas: -> "))
        facturas.append(cant_fact)
        localidad = input("- Ingrese la ciudad del empleado: -> ")
        print("-" * 61)
        ciudad.append(localidad)
        print("-" * 61)
        resp = input(
            """        Presione x para detener el registro        """
        ).lower()
        print("-" * 61)
        if resp == "x":
            break


# Recorre las listas paralelas para mostrar la ficha completa de todos los empleados
def mostrar_datos(arreglo_n, arreglo_t, arreglo_f, arreglo_ci, arreglo_c):
    for i in range(len(arreglo_n)):
        print(f"""                     Empleado N°{i+1}:                     """)
        print("-" * 61)
        print(f"-Nombre: -> {arreglo_n[i]}")
        print(f"-Total Facturado: -> {arreglo_t[i]}$")
        print(f"-Cantidad de facturas: -> {arreglo_f[i]}")
        print(f"-CI: -> V{arreglo_ci[i]}")
        print(f"-Localidad: -> {arreglo_c[i]}")
        print("-" * 61)


# Suma todos los montos totales y calcula su promedio aritmético global
def promediar(arreglot):
    acumulador = 0
    for valor in arreglot:
        acumulador = acumulador + valor
    prom = acumulador / len(arreglot)
    print("-" * 61)
    print(f"El total sumado de todas las facturas es: -> {acumulador}$")
    print(f"Y su promedio es: -> {prom}$")
    print("-" * 61)
    return acumulador, prom


# Muestra los nombres de los empleados cuyo monto facturado supera el promedio
def mayor_a_promediar(arreglo_n, arreglo_t, prom):
    for i in range(len(arreglo_n)):
        if arreglo_t[i] > prom:
            print("-" * 61)
            print(
                f"El empleado: {arreglo_n[i]} tiene un monto total de las facturas mayor al promedio."
            )
            print("-" * 61)


# Muestra los vendedores que superan las 5 facturas procesadas
def mayor_facturas(arreglo_c, arreglo_n, arreglo_f):
    for i in range(len(arreglo_c)):
        if arreglo_f[i] > 5:
            print("-" * 61)
            print(
                f"- El empleado {arreglo_n[i]} de la ciudad de {arreglo_c[i]} ha vendido un total de {arreglo_f[i]} facturas."
            )
            print("-" * 61)


# Búsqueda secuencial booleana para verificar si un valor ya existe en la lista
def buscar_unico(dato, lista):
    encontro = False
    i = 0
    while i < len(lista) and not encontro:
        if lista[i] == dato:
            encontro = True
        i = i + 1
    return encontro


# Búsqueda secuencial que retorna el índice exacto de una cédula o -1 si no existe
def buscar_ci(dato, lista):
    i = 0
    pos = -1
    while i < len(lista):
        if lista[i] == dato:
            pos = i
            break
        i = i + 1
    return pos


# Muestra las opciones del menú principal y captura la elección del usuario
def menu():
    print("-" * 61)
    print("""                        Menu de opciones:                        """)
    print("-" * 61)
    print("1) Leer datos")
    print("2) Mostrar promedios de montos y montos mayores al promedio")
    print("3) Consultar usuario por cedula")
    print("4) Mostrar listado de vendedores")
    print("5) Mostrar vendedores con mas de 5 facturas vendidas")
    print("6) Salir")
    print("-" * 61)
    opcion = int(input("- Ingrese una opcion del menu: -> "))
    print("-" * 61)
    return opcion


# Controla el flujo general de la aplicación mediante un ciclo y match-case
def main():
    while True:
        opcion = menu()
        match opcion:
            case 1:
                leer_datos()
            case 2:
                if not len(montos) == 0:
                    sumatoria, promedio = promediar(montos)
                    mayor_a_promediar(nombres, montos, promedio)
                else:
                    print("-" * 61)
                    print("""                 ¡No hay montos registrados!                """)
                    print("-" * 61)
            case 3:
                print("-" * 61)
                ci_empleado = int(
                    input("- Ingrese la cedula del vendedor que desea buscar: -> ")
                )
                print("-" * 61)
                pos = buscar_ci(ci_empleado, cedulas)
                if pos != -1:
                    print(f"""                   Empleado encontrado:                    """)
                    print("-" * 61)
                    print(f"-Nombre: -> {nombres[pos]}")
                    print(f"-Total Facturado: -> {montos[pos]}$")
                    print(f"-Cantidad de facturas: -> {facturas[pos]}")
                    print(f"-CI: -> V{cedulas[pos]}")
                    print(f"-Localidad: -> {ciudad[pos]}")
                    print("-" * 61)
                else:
                    print("-" * 61)
                    print("""           ¡El empleado no se encuentra registrado!            """)
                    print("-" * 61)
            case 4:
                if not nombres:
                    print("-" * 61)
                    print("""                ¡No hay empleados registrados!                """)
                    print("-" * 61)
                    continue
                mostrar_datos(nombres, montos, facturas, cedulas, ciudad)
            case 5:
                if not nombres:
                    print("-" * 61)
                    print("""     ¡No hay empleados registrados para calcular facturas!     """)
                    print("-" * 61)
                    continue
                mayor_facturas(ciudad, nombres, facturas)
            case 6:
                print("-" * 61)
                print("""                    ¡Hasta luego estimado!                    """)
                print("-" * 61)
                break
            case _:
                print("-" * 61)
                print("""   ¡La opcion que elegiste es invalida, intenta de nuevo.!    """)
                print("-" * 61)


# Listas paralelas globales vacías para el almacenamiento dinámico
cedulas = []
nombres = []
ciudad = []
montos = []
facturas = []

main()
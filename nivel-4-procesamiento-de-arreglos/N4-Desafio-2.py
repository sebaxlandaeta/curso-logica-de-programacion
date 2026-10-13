# Recorre los arreglos vacíos preinicializados para llenar los datos de cada empleado
def leer_datos(arreglo1, arreglo2, arreglo3):
    for i in range(len(arreglo1)):
        print(f"""                   Empleado Nº{i+1}                    """)
        print("-" * 52)
        arreglo1[i] = input("- Ingrese el nombre del empleado: -> ")
        arreglo2[i] = float(input("- Ingrese el monto total que facturo: -> "))
        arreglo3[i] = int(
            input("- Ingrese la cantidad de facturas que proceso: -> ")
        )
        print("-" * 52)


# Recorre las listas paralelas para mostrar un resumen en pantalla de cada empleado
def mostrar_datos(arreglo1, arreglo2, arreglo3):
    for i in range(len(arreglo1)):
        print(
            f"\nEmpleado {i+1} -> Nombre:{arreglo1[i] } /Total Facturado:{arreglo2[i]}$ /Cantidad de facturas:{arreglo3[i]}"
        )


# Suma todos los valores del arreglo de totales y calcula su promedio aritmético
def promediar(arreglot):
    acumulador = 0
    for valor in arreglot:
        acumulador = acumulador + valor
    prom = acumulador / len(arreglot)
    print("-" * 52)
    print(f"El total sumado de todas las facturas es: -> {acumulador}$")
    print(f"Y su promedio es: -> {prom}$")
    print("-" * 52)
    return acumulador, prom


# Compara el monto facturado de cada empleado frente al promedio general
def mayor_a_promediar(arreglo_n, arreglo_t, prom):
    for i in range(len(arreglo_n)):
        if arreglo_t[i] > prom:
            print("-" * 52)
            print(
                f"El empleado: {arreglo_n[i]} tiene un monto total de las facturas mayor al promedio."
            )
            print("-" * 52)


# Pide por teclado y asigna la ciudad correspondiente a cada empleado en su arreglo
def cosultar_ciudad(arreglo_c):
    for i in range(len(arreglo_c)):
        arreglo_c[i] = input(f"-Ingrese la ciudad del empleado Nº{i+1}: -> ")


# Filtra y muestra los empleados cuya cantidad de facturas procesadas supera 5
def mayor_facturas(arreglo_c, arreglo_n, arreglo_f):
    for i in range(len(arreglo_c)):
        if arreglo_f[i] > 5:
            print("-" * 52)
            print(
                f"- El empleado {arreglo_n[i]} de la ciudad de {arreglo_c[i]} ha vendido un total de {arreglo_f[i]} facturas."
            )
            print("-" * 52)


# Arreglos paralelos globales predefinidos con un tamaño fijo de 5 elementos
nombres = [""] * 5
ciudad = [""] * 5
total = [0, 0, 0, 0, 0]
facturas = [0, 0, 0, 0, 0]

# Cuerpo principal: Ejecución secuencial de todas las funciones definidas
leer_datos(nombres, total, facturas)
mostrar_datos(nombres, total, facturas)
sumatoria_facturas, prom_facturas = promediar(total)
mayor_a_promediar(nombres, total, prom_facturas)
cosultar_ciudad(ciudad)
mayor_facturas(ciudad, nombres, facturas)
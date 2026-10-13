import funciones  # Importa las funciones de validacion del archivo externo


# Registra los datos de los jugadores en listas paralelas
def registrar_jug():
    while True:
        num = funciones.validar_camisa(1, 99)
        existe = buscar_unico(num, camisetas_jugador)
        if existe:
            print("-" * 61)
            print("          ¡El jugador ya se encuentra registrado!          ")
            print("-" * 61)
            continue
        
        camisetas_jugador.append(num)

        nombre = funciones.validar_nombre()
        nombres_jugador.append(nombre)

        posicion = funciones.validar_posicion(pos_validas)
        posiciones_jugador.append(posicion)

        hits = funciones.validar_hits(0, 200)
        hits_jugador.append(hits)

        average = funciones.validar_avarage(0, 1000)
        average_jugador.append(average)

        print("-" * 61)
        resp = input("          Presione x para detener el registro: -> ").strip().upper()
        print("-" * 61)
        if resp == "X":
            break


# Verifica si un numero ya existe en la lista (True o False)
def buscar_unico(dato, lista):
    encontro = False
    i = 0
    while i < len(lista) and not encontro:
        if lista[i] == dato:
            encontro = True
        i = i + 1
    return encontro


# Busca un numero de camiseta y devuelve su posicion en la lista o -1 si no esta
def buscar_camiseta(dato, lista):
    i = 0
    pos = -1
    while i < len(lista):
        if lista[i] == dato:
            pos = i
            break
        i = i + 1
    return pos


# Pide la camiseta asegurandose de que solo se ingresen numeros
def consultar_jugador():
    while True:
        print("-" * 61)
        busqueda = input("- Ingrese el numero de camiseta: -> ")
        print("-" * 61)
        if busqueda.isdigit():
            return int(busqueda)
        else:
            print("-" * 61)
            print("          ERROR: Solo se pueden ingresar numeros.          ")
            print("-" * 61)


# Muestra en pantalla el listado completo de todos los jugadores
def imprimir_datos(arreglo_c, arreglo_n, arreglo_p, arreglo_h, arreglo_a):
    for i in range(len(arreglo_n)):
        print(f"                    Jugador N°{i+1}:                    ")
        print("-" * 61)
        print(f"- Numero de camiseta: -> {arreglo_c[i]}")
        print(f"- Nombre del jugador: -> {arreglo_n[i]}")
        print(f"- Posicion del jugador: -> {arreglo_p[i]}")
        print(f"- Hits del jugador: -> {arreglo_h[i]}")
        print(f"- Average de bateo: -> {arreglo_a[i]}")
        print("-" * 61)


# Busca un jugador por su camiseta y muestra sus datos
def mostrar_datos_jugador(arreglo_c, arreglo_n, arreglo_p, arreglo_h, arreglo_a):
    while True:
        opcion = consultar_jugador()
        indice = buscar_camiseta(opcion, camisetas_jugador)
        if indice != -1:
            print("-" * 61)
            print(f"- Numero de camiseta: -> {arreglo_c[indice]}")
            print(f"- Nombre del jugador: -> {arreglo_n[indice]}")
            print(f"- Posicion del jugador: -> {arreglo_p[indice]}")
            print(f"- Hits del jugador: -> {arreglo_h[indice]}")
            print(f"- Average de bateo: -> {arreglo_a[indice]}")
            print("-" * 61)
        else:
            print("-" * 61)
            print("   ¡El numero introducido no le pertenece a ningun jugador!   ")
            print("-" * 61)
        
        resp = input("          Presione x para detener la busqueda: -> ").strip().upper()
        print("-" * 61)
        if resp == "X":
            break


# Estadística: Encuentra al jugador que tiene mas hits conectados
def jug_mayor_hits(arreglo_h, arreglo_n):
    mayor_hits = -1
    nombre_mayor = ""
    for i in range(len(arreglo_h)):
        if arreglo_h[i] > mayor_hits:
            mayor_hits = arreglo_h[i]
            nombre_mayor = arreglo_n[i]
    return mayor_hits, nombre_mayor


# Estadística: Calcula el promedio general del average de bateo
def promediar_avarage(arreglo_a):
    acumulador = 0
    for i in range(len(arreglo_a)):
        acumulador = acumulador + arreglo_a[i]
    prom = acumulador / len(arreglo_a)
    return prom


# Estadística: Muestra los jugadores cuyo average es menor al promedio general
def menor_a_promediar(arreglo_n, arreglo_a):
    promedio = promediar_avarage(average_jugador)
    print(f"Average Promedio del Equipo: {promedio:.2f}")
    print("-" * 61)
    for i in range(len(arreglo_n)):
        if arreglo_a[i] < promedio:
            print(f"- El jugador {arreglo_n[i]} tiene un average de bateo ({arreglo_a[i]}) menor al promedio")
    print("-" * 61)


# Estadística: Cuenta cuantos jugadores juegan en la posicion de Pitcher (P)
def contar_pitchers(dato, lista):
    contador = 0
    for valor in lista:
        if valor == dato:
            contador = contador + 1
    return contador


# Muestra el menú de opciones y valida que la entrada sea un entero entre 1 y 4
def menu():
    while True:
        print("-" * 61)
        print("                        Menu de opciones:                        ")
        print("-" * 61)
        print("1) Registrar jugador")
        print("2) Consultar datos de jugador")
        print("3) Mostrar estadisticas")
        print("4) Salir")
        print("-" * 61)
        opcion = input("- Ingrese una opcion del menu: -> ").strip()
        print("-" * 61)
        if opcion.isdigit():
            op = int(opcion)
            if 1 <= op <= 4:
                return op
        print("-" * 61)
        print("       ERROR: Debe ingresar un numero entero entre 1 y 4.       ")


# Función principal que controla el flujo del programa
def main():
    while True:
        opcion = menu()
        match opcion:
            case 1:
                registrar_jug()
            case 2:
                if len(nombres_jugador) > 0:
                    mostrar_datos_jugador(
                        camisetas_jugador,
                        nombres_jugador,
                        posiciones_jugador,
                        hits_jugador,
                        average_jugador,
                    )
                else:
                    print("          ¡No hay jugadores registrados para consultar!          ")
            case 3:
                if len(nombres_jugador) > 0:
                    imprimir_datos(
                        camisetas_jugador,
                        nombres_jugador,
                        posiciones_jugador,
                        hits_jugador,
                        average_jugador,
                    )
                    mayor_hits, nombre_mayor = jug_mayor_hits(hits_jugador, nombres_jugador)
                    print(f"- El jugador con mas hits es: -> {nombre_mayor} ({mayor_hits} hits)")
                    print("-" * 61)
                    menor_a_promediar(nombres_jugador, average_jugador)
                    total_pitchers = contar_pitchers("P", posiciones_jugador)
                    print(f"- Hay un total de {total_pitchers} pitchers (P) registrados")
                    print("-" * 61)
                else:
                    print("                    ¡No hay datos registrados!                    ")
            case 4:
                print("                        ¡Hasta luego!                        ")
                print("-" * 61)
                break


# Variables globales: arreglos paralelos inicializados vacíos
camisetas_jugador = []
nombres_jugador = []
posiciones_jugador = []
hits_jugador = []
average_jugador = []
pos_validas = ["1B", "2B", "3B", "SS", "LF", "CF", "RF", "P", "C"]

# Ejecución del programa
if __name__ == "__main__":
    main()
# Módulo 1: Captura de datos de entrada del usuario
def capturar_datos():
    print("""                    N3-Desafio 2                    \n""")
    print("""        ¿Cual es el codigo del producto?       """)
    codigo=int(input("-"))
    print("""        ¿Cual es el precio del procucto?       """)
    precio_u=float(input("-"))
    print("""            ¿Cuantos deseas llevar?              """)
    cantidad=int(input("-"))
    print("-"*48)
    return codigo, precio_u, cantidad # Retorna múltiples valores

# Módulo 2: Calcula el subtotal multiplicando precio por cantidad
def calcular_subtotal(precio_u, cantidad):
    subtotal=precio_u*cantidad
    return subtotal # Devuelve el resultado

# Módulo 3: Aplica descuento según el subtotal (>1000 = 10%, sino 2%) y calcula el total
def calcular_total(subtotal):
    if subtotal>1000:
        porc=0.10
    else:
        porc=0.02
    monto_descuento=subtotal*porc
    total=subtotal-monto_descuento
    return monto_descuento, total # Retorna descuento y total final

# Módulo 4: Imprime la factura formateada con todos los datos calculados
def imprimir_factura(codigo, cantidad, precio_u, subtotal, monto_descuento, total):
    print(f"-El codigo del producto es: -> {codigo}")
    print("-"*48)
    print(f"-Cantidad de productos: -> {cantidad}")
    print("-"*48)
    print(f"-Precio del producto: -> {precio_u}bs c/u")
    print("-"*48)
    print(f"-Subtotal a pagar: -> {subtotal}bs")
    print("-"*48)
    print(f"-Monto de descuento: -> {monto_descuento}bs")
    print("-"*48)
    print(f"-Total a pagar: -> {total}bs")
    print("-"*48)

# Módulo principal: Coordina la ejecución secuencial de todas las funciones
def procesar():
    codigo,precio_u,cantidad=capturar_datos()
    subtotal=calcular_subtotal(precio_u, cantidad)
    monto_descuento, total=calcular_total(subtotal)
    imprimir_factura(codigo, cantidad, precio_u, subtotal, monto_descuento, total)

# Cuerpo principal: Ejecuta la función controladora del programa
procesar()
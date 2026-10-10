import random

print("    ¡Bienvenido a nuestra empresa!    ")
print("-" * 40)

# Solicitamos los datos al usuario
modelo = input("Indique el modelo del vehiculo que desea alquilar: -> ")
print("-" * 40)
dias = int(input("Indique la cantidad de dias que desea alquilar el vehiculo: -> "))

# Generamos costo aleatorio y calculamos totales
costo_diario = random.randint(25, 50)
monto_total = dias * costo_diario
monto_inicial = monto_total * 0.35

# Estructura condicional para evaluar los días de alquiler
if dias <= 10:
    print("-" * 40)
    print("    El total de la compra seria:     ")
    print(
        f"""
    Modelo: {modelo}
    Cantidad de dias: -> {dias}
    Costo diario: -> {costo_diario}$
    Monto total: -> {monto_total}$
    Monto inicial: -> {monto_inicial}$"""
    )
else:
    print("-" * 40)
    print(
        "Si deseas alquilar un vehiculo una cantidad mayor a 10 dias, "
        "debes cancelar un monto adicional de 100$ al monto inicial. "
        "El total de la compra seria:"
    )
    # Sumamos el recargo de 100$ al monto inicial correspondiente
    monto_inicial_con_recargo = monto_inicial + 100

    print(
        f"""
    Modelo: {modelo}
    Cantidad de dias: -> {dias} 
    Costo diario: -> {costo_diario}$
    Monto total: -> {monto_total}$
    Monto inicial: -> {monto_inicial_con_recargo}$"""
    )
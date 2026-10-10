import random

print("¡Bienvenido a nuestra empresa!")

# Entradas: Solicitud de datos al usuario
modelo = input("Indique el modelo del vehiculo que desea alquilar:\n")
dias = int(input("Indique la cantidad de dias que desea alquilar el vehiculo:\n"))

# Proceso: Generación de costos aleatorios y cálculos aritméticos básicos
costo_diario = random.randint(25, 50)
monto_total = dias * costo_diario
monto_inicial = monto_total * 0.35

# Salidas: Impresión organizada de los datos usando f-strings
print(
    f"""
Modelo:{modelo}
Cantidad de dias: -> {dias}
Costo diario: -> {costo_diario}$
Monto total: -> {monto_total}$
Monto inicial: -> {monto_inicial}$"""
)
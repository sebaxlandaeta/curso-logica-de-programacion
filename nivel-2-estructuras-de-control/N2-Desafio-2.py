import random

# Bucle para simular 4 ventas consecutivas
for i in range(1, 5):
    print("\n    ¡Bienvenido a nuestra empresa!    ")
    print(f"               VENTA #{i}               ")
    print("-" * 40)
    
    modelo = input("Indique el modelo del vehiculo que desea alquilar: -> ")
    print("-" * 40)
    dias = int(input("Indique la cantidad de dias que desea alquilar el vehiculo: -> "))
    
    costo_diario = random.randint(25, 50)
    monto_total = dias * costo_diario
    monto_inicial = monto_total * 0.35

    # Validación de límite máximo de alquiler (más de 30 días)
    if dias > 30:
        print("-" * 40)
        print("Lo sentimos, no se puede alquilar un vehiculo una cantidad mayor a 30 dias.")
    
    # Rango entre 11 y 30 días (aplica recargo)
    elif dias > 10:
        print("-" * 40)
        print("Si deseas alquilar un vehiculo una cantidad mayor a 10 dias, debes cancelar un monto adicional de 100$ al monto inicial. El total de la compra seria:")
        
        # Corrección en el salto de línea que rompía el f-string
        print(f"\nModelo: {modelo}")
        print(f"- Cantidad de dias: -> {dias}") 
        print(f"- Costo diario: -> {costo_diario}$")
        print(f"- Monto total: -> {monto_total}$")
        print(f"- Monto inicial: -> {monto_inicial + 100}$")
    
    # Menor o igual a 10 días
    else:
        # Validación de promoción exacta para 5 días
        if dias == 5:
            print("\nY por el alquiler de 5 dias te daremos un descuento del 10%, tu total seria:")
            print(f"\n      Total con Descuento -> {monto_total * 0.90}$      ")
        else:
            print("-" * 40)
            print("    El total del compra seria:     ")
            print(f"\nModelo: {modelo}")
            print(f"- Cantidad de dias: -> {dias}")
            print(f"- Costo diario: -> {costo_diario}$")
            print(f"- Monto total: -> {monto_total}$")
            print(f"- Monto inicial: -> {monto_inicial}$")
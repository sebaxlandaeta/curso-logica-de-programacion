# Módulo auxiliar: Calcula un porcentaje dado un monto y una tasa
def calcular_porcentaje(monto, porcentaje):
    return monto*porcentaje/100

# Módulo de sucursal: Procesa facturas individuales, acumula totales y cuenta condiciones
def procesar_facturas_sucursal(nombre):
    total_sucursal=0
    cant_facturas=0
    facturas_menor_200=0
    
    while True: # Bucle para registrar múltiples facturas por sucursal
        print("""              ¿Cual es el monto?                """)
        monto_base=float(input("-"))
        print("""              Ingrese la cantidad:               """)
        cantidad_art=int(input("-"))
        print("-"*53)

        monto_iva=calcular_porcentaje(monto_base, 16) # Calcula el IVA (16%)
        monto_total=monto_iva+monto_base              # Suma base + IVA

        if cantidad_art>0: # Evita división entre cero
            prom_articulo=monto_total/cantidad_art
        else:
            prom_articulo=0
            
        print(f"Monto del IVA: -> {monto_iva} bs")
        print(f"Monto total: -> {monto_total} bs")
        print(f"Promedio por articulo: -> {prom_articulo}")

        cant_facturas=cant_facturas+1              # Cuenta facturas de la sucursal
        total_sucursal=total_sucursal+monto_total   # Acumula dinero de la sucursal

        if monto_total<200: # Cuenta facturas menores a 200
            facturas_menor_200=facturas_menor_200+1

        print("""\n       ¿Desea procesar otra factura? S/N       """)
        resp=input("-") .upper()
        if resp=="N": # Sale del ciclo si la respuesta es No
            break
            
    if cant_facturas>0: # Calcula promedios y porcentajes finales de la sucursal
        prom_sucursal=total_sucursal/cant_facturas
        porc_menor_200=calcular_porcentaje(facturas_menor_200, 100)/cant_facturas
    else:
        prom_sucursal=0
        porc_menor_200=0

    # Imprime reporte de la sucursal
    print("-"*53)
    print("""            Factura de la sucursal:             """)
    print("-"*53)
    print(f"-Nombre de la sucursal: -> {nombre}")
    print(f"-Total facturado en la sucursal: -> {total_sucursal} bs")
    print(f"-Monto promedio de facturas: -> {prom_sucursal} bs")
    print(f"-Cantidad de facturas procesadas: -> {cant_facturas}")
    print(f"-Porcentaje de facturas < 200: -> {porc_menor_200} %")
    return total_sucursal, cant_facturas

# Módulo principal: Controla el ciclo de las sucursales (rango de 1 a 4) y el resumen general
def principal():
    total_general=0
    total_facturas_general=0
    
    for i in range(1,5): # Repite para 4 sucursales
        print("-"*53)
        print(F"""                    FACTURA Nº{i}                    """)
        print("-"*53)
        print("""        ¿Cual es el nombre de la sucursal?       """)
        nombre=input("-")

        total_sucursal, cant_facturas=procesar_facturas_sucursal(nombre)
        total_general=total_general+total_sucursal              # Acumula total general
        total_facturas_general=total_facturas_general+cant_facturas # Acumula facturas totales

        if total_facturas_general>0:
            prom_general=total_general/total_facturas_general
        else:
            prom_general=0
            
        # Imprime resumen parcial/general por iteración
        print("-"*53)
        print("""                Resumen general:                 """)
        print("-"*53)
        print(f"-Total general facturado: -> {total_general} bs")
        print(f"-Monto promedio de todas las facturas: -> {prom_general} bs\n")

# Ejecución del programa principal
principal()
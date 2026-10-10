for i in range(1, 6):
    print(f"                VENTA #{i}                ")
    print("           ¡Elige tu boleto!         ")
    print("-" * 42)
    print("           Tipo de boletos:            \n")
    print("- Tipo V: 50$")
    print("- Tipo P: 30$")
    print("- Tipo G: 15$\n")
    print("          ¿Cual deseas llevar?           ")
    
    # .upper() convierte la letra ingresada a mayúscula para evitar errores de validación
    tipo = input("- ").upper()
    print("         ¿Cuantos deseas llevar?         ")
    cantidad = int(input("- "))
    print("-" * 42)

    # Asignación de precio según el tipo de boleto seleccionado
    if tipo == "V":
        precio = 50
    elif tipo == "P":
        precio = 30
    elif tipo == "G":
        precio = 15
    else:
        precio = 0

    subtotal = precio * cantidad
    
    # Cálculo de porcentaje de descuento según el rango del subtotal
    if subtotal > 0 and subtotal < 200:
        porc = 0
    elif subtotal >= 200 and subtotal <= 400:
        porc = 0.05
    elif subtotal > 400 and subtotal <= 1000:
        porc = 0.07
    else:
        porc = 0.1

    descuento = subtotal * porc
    total = subtotal - descuento

    # Validaciones de seguridad para la impresión de resultados
    if cantidad > 0:
        if precio > 0:
            print(f"- Tipo de boleto seleccionado: -> {tipo}")
            print(f"- Precio del boleto: -> {precio}$")
            print(f"- Cantidad de boletos: -> {cantidad}")
            print(f"- Subtotal: -> {subtotal}$")
            print(f"- % Descuento: -> {int(porc * 100)}%")
            print(f"- Monto de descuento: -> {descuento}$")
            print(f"- Total: -> {total}$\n")
        else:
            print("    ¡Elegiste un tipo de boleto invalido!    \n")
    else:
        print("    ¡La cantidad debe ser mayor a 0!    \n")   
        print("""     ¡Debes ingresar un numero positivo!       \n""")
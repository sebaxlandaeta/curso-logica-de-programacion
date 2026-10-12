# Módulo 1: Captura los datos de entrada del estudiante
def captura_datos():
    print("""             Academia de Sofware CADIF1             """)
    print("-"*56)
    print("""          Ingrese el nombre del estudiante:         """)
    nombre=input("-")
    print("""                  ¿Cual fue su nota?                  """)
    nota=float(input("-"))
    print("""              Indique su modalidad P/O            """)
    modalidad=input("-"). lower()
    print("""             ¿Cuanto fue el monto a pagar?            """)
    monto=float(input("-"))
    return nombre, nota, modalidad, monto 

# Módulo 2: Controla el ciclo, acumula montos, cuenta condiciones y halla mayores/menores
def procesar():
    cant_aprobados=0
    cant_reprobados=0
    cant_presencial =0
    cant_online=0
    acum_alumnos=0
    acum_online=0
    nota_mayor=0
    nota_menor=101
    nom_mayor=""
    nom_menor=""
    
    while True: # Bucle infinito para registro múltiple
        nombre, nota, modalidad, monto=captura_datos()
        acum_alumnos=acum_alumnos+monto # Acumula total general
        
        if nota>=80: # Cuenta aprobados
            cant_aprobados=cant_aprobados+1

        if nota<80: # Cuenta reprobados
            cant_reprobados=cant_reprobados+1

        if modalidad=="p": # Cuenta presenciales
            cant_presencial=cant_presencial+1

        if modalidad=="o": # Cuenta y acumula online
            cant_online=cant_online+1
            acum_online=acum_online+monto

        if nota>nota_mayor: # Evalúa nota máxima
            nota_mayor=nota
            nom_mayor=nombre

        if nota<nota_menor: # Evalúa nota mínima
            nota_menor=nota
            nom_menor=nombre

        resp=input("""         ¿Quieres volver a leer otra nota? S/N          \n"""). upper()
        if resp=="N": # Rompe el ciclo si la respuesta es No
            break
            
    return cant_aprobados, cant_reprobados, cant_presencial, cant_online, acum_alumnos, acum_online, nota_mayor, nota_menor, nom_mayor, nom_menor
    
# Módulo 3: Imprime el reporte final con los resultados procesados
def imprimir(cant_aprobados, cant_reprobados,cant_presencial, cant_online, acum_alumnos, acum_online, nota_mayor, nota_menor, nom_mayor, nom_menor):
    print("-"*56)
    print(f"Alumnos aprobados: {cant_aprobados}")
    print("-"*56)
    print(f"Alumnos reprobados: {cant_reprobados}")
    print("-"*56)
    print(f"Alumnos presenciales: {cant_presencial}")
    print("-"*56)
    print(f"Alumnos online: {cant_online}")
    print("-"*56)
    print(f"La nota mayor fue {nota_mayor} y la obtuvo {nom_mayor}")
    print("-"*56)
    print(f"La nota menor fue {nota_menor} y la obtuvo {nom_menor}")
    print("-"*56)
    print(f"Total a pagar por todos los alumnos: {acum_alumnos} bs")
    print("-"*56)
    print(f"Total a pagar por la modalidad online: {acum_online} bs")
    print("-"*56)
  
# Cuerpo principal: Ejecuta el procesamiento y muestra la salida en pantalla
cant_aprobados, cant_reprobados, cant_presencial, cant_online, acum_alumnos, acum_online, nota_mayor, nota_menor, nom_mayor, nom_menor=procesar()

imprimir(cant_aprobados, cant_reprobados, cant_presencial, cant_online, acum_alumnos, acum_online, nota_mayor, nota_menor, nom_mayor, nom_menor)
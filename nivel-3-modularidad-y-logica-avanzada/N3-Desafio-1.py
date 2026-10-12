import random

# Módulo 1: Lectura de entradas del usuario
def leer_entradas():
    global nombre, modelo, dias
    nombre = input('Como se llama?  ')
    modelo = input('Cual modelo desea alquilar?  ')
    dias = int(input('Cuantos dias desea alquilar el vehiculo? '))

# Módulo 2: Procesamiento y cálculos lógicos
def calcular_montos():
    global costo_diario, subtotal, inicial, cuotas
    costo_diario = random.randint(10, 50)  # Genera costo aleatorio
    subtotal = dias * costo_diario           # Calcula el total bruto
    inicial = subtotal * 0.35                # Calcula la inicial (35%)
    cuotas = (subtotal - inicial) / dias     # Calcula el valor de las cuotas

# Módulo 3: Presentación de resultados en pantalla
def mostrar_salidas():
    print(f'''Sr {nombre}, el costo diario de alquiler
del {modelo.upper()} es {costo_diario}
El total a pagar es {subtotal}
Debe cancelar una inicial de {inicial} 
y el resto debe pagarlo en {dias} cuotas diarias 
con un monto de {cuotas}''')

# Cuerpo principal: Declaración de variables globales iniciales
nombre = ""
modelo = ""
dias = 0

# Llamada secuencial a los módulos creados
leer_entradas()
calcular_montos()
mostrar_salidas()
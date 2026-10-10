import random

# Definición de variables iniciales (nombre y salario base fijo)
nombre = "Argenis Romero"
salario_b = 25

# Generación de valores aleatorios para las horas trabajadas y la tarifa por hora
horas_t = random.randint(5, 40)
tarifa = random.randint(20, 50)

# Cálculos aritméticos para el monto por horas y el salario total combinado
total_monto = horas_t * tarifa
salario_t = salario_b + total_monto

# Impresión formateada de los resultados en consola con separadores visuales
print("-" * 50)
print("Nombre del vendedor:", nombre)
print("-" * 50)
print("Su salario base es de:", salario_b, "$")
print("-" * 50)
print("Trabaja un total de", horas_t, "horas al mes.")
print("-" * 50)
print("Su tarifa por horas de trabajo es de:", tarifa, "$")
print("-" * 50)
print("Y gana un total de", total_monto, "$ por horas de trabajo")
print("-" * 50)
print("Por lo tanto, su salario total al mes es de:", salario_t, "$")
print("-" * 50)
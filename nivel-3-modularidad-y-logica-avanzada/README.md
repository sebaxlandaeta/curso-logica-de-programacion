# Nivel 3: Modularidad, Funciones y Lógica Avanzada

Nivel 3 del curso de lógica de programación en Python, enfocado en el diseño modular, creación de funciones con retorno de valores, paso de parámetros por valor, contadores, acumuladores, cálculo de máximos y mínimos, y gestión de bucles anidados con control de flujo interactivo.

---

## 📋 Resumen de Desafíos

### Desafío 1: Sistema de Alquiler de Vehículos (Modular)
**Objetivo:** Introducir la modularidad básica y el uso de variables globales para dividir la lógica de un programa en funciones independientes.

**Requerimientos principales:**
1. **Captura de datos modular:** Utilizar el módulo `leer_entradas()` con variables globales para pedir el nombre del cliente, el modelo del vehículo y la cantidad de días.
2. **Generación de costo aleatorio:** Emplear la función `random.randint(10, 50)` dentro de `calcular_montos()` para definir de forma dinámica el costo diario del alquiler.
3. **Cálculos automáticos:** Procesar el subtotal, el pago inicial equivalente al 35% y el valor de las cuotas diarias a partir de los datos ingresados.
4. **Salida formateada:** Mostrar los resultados en pantalla utilizando el módulo `mostrar_salidas()`, asegurando que el modelo del vehículo se imprima en mayúsculas mediante `.upper()`.
5. **Flujo secuencial:** Coordinar y llamar en orden a los tres módulos (`leer_entradas`, `calcular_montos`, `mostrar_salidas`) desde el cuerpo principal del programa.

---

### Desafío 2: Sistema de Facturación de Artículos
**Objetivo:** Dominar el retorno múltiple de valores y evitar el uso de variables globales mediante la estructuración de funciones puras e independientes.

**Requerimientos principales:**
1. **Captura modular de entradas:** Solicitar por teclado el código, el precio unitario y la cantidad de un artículo mediante una función independiente que retorne estos tres valores sin usar variables globales.
2. **Cálculo del subtotal:** Procesar el monto bruto multiplicando el precio unitario por la cantidad comprada dentro de una función exclusiva que devuelva dicho resultado.
3. **Aplicación de reglas de descuento:** Calcular un descuento dinámico (por ejemplo, del 10% si el subtotal supera los 1000, o del 2% en caso contrario) y determinar el monto total a pagar mediante una función específica.
4. **Formato de factura y salida:** Mostrar en pantalla de forma ordenada y estructurada el código del producto, la cantidad, el precio unitario, el subtotal, el descuento aplicado y el total final a pagar.
5. **Estructura limpia:** Mantener la separación de responsabilidades entre la captura, el cálculo y la presentación de resultados.

---

### Desafío 3: Control de Notas Estudiantiles (CADIF1)
**Objetivo:** Aplicar contadores, acumuladores y algoritmos de búsqueda de máximos y mínimos combinados con ciclos repetitivos interactivos.

**Requerimientos principales:**
1. **Captura modular de datos:** Solicitar por teclado el nombre, la nota, la modalidad (`P`/`O`) y el monto a pagar de cada estudiante mediante una función independiente que retorne dichos valores.
2. **Procesamiento y conteo:** Utilizar un bucle con ciclo repetitivo para contar alumnos aprobados, reprobados, presenciales y online, aplicando contadores incrementales (`+ 1`).
3. **Acumulación de montos:** Sumar y acumular el dinero total a pagar de todos los alumnos y el subtotal específico de la modalidad online.
4. **Cálculo de máximos y mínimos:** Evaluar e identificar la nota mayor y la nota menor ingresadas, guardando junto con ellas el nombre del estudiante correspondiente.
5. **Módulos de coordinación y salida:** Implementar una función principal (`procesar`) que controle el flujo con opción de salida interactiva (`S/N`) y una función final para imprimir el reporte detallado.

---

### Desafío 4: Sistema de Sucursales y Facturación Múltiple
**Objetivo:** Integrar ciclos anidados complejos, funciones de porcentaje obligatorias y reportes estadísticos consolidados por sucursal y a nivel general.

**Requerimientos principales:**
1. **Ciclo anidado de sucursales y facturas:** Recorrer exactamente 4 sucursales usando un ciclo externo, y procesar una cantidad indeterminada de facturas por cada una mediante un bucle interno con control de continuación (`S/N`).
2. **Lectura de entradas:** Solicitar en el lugar y orden correctos el nombre de la sucursal, así como el monto base y la cantidad de artículos de cada factura.
3. **Cálculos por factura:** Calcular y mostrar obligatoriamente el IVA (16% mediante una función de porcentaje), el monto total (`base + IVA`) y el promedio por artículo de cada transacción.
4. **Reportes por sucursal:** Calcular y mostrar al cierre de cada sucursal el total facturado, el monto promedio de sus facturas, la cantidad de facturas procesadas y el porcentaje de aquellas cuyo monto fue menor a 200.
5. **Reporte general y diseño modular:** Calcular los ingresos promedio generales de las sucursales aplicando una estructura estrictamente modular basada en funciones y temas fundamentales del curso.

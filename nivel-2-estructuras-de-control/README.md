# Nivel 2: Estructuras de Control y Lógica Condicional

Nivel 2 del curso de lógica de programación en Python, enfocado en el uso de estructuras condicionales simples y anidadas, rangos contiguos, operadores lógicos avanzados, control de flujo con bucles (`for` y `while`) y lógica de negocio aplicada.

---

## 📋 Resumen de Desafíos

### Desafío 1: Sistema Básico de Alquiler de Vehículos
**Objetivo:** Introducir la captura de datos, manipulación de tipos de datos, generación de valores aleatorios y condiciones simples para la aplicación de recargos.

**Requerimientos principales:**
1. **Captura del modelo del vehículo:** Solicitar al usuario mediante una entrada de texto (`input`) el modelo específico del vehículo que desea alquilar.
2. **Captura y conversión de la duración:** Solicitar la cantidad de días de alquiler transformando la entrada en un número entero (`int`).
3. **Generación de costo diario aleatorio:** Utilizar la librería `random` (`randint`) para asignar un costo por día de forma dinámica entre 25 y 50 unidades.
4. **Cálculo de montos financieros:** Automatizar el cálculo del costo total (días por costo diario) y determinar el monto inicial base equivalente al 35% del total.
5. **Aplicación de regla condicional por plazo:** Evaluar si la duración supera los 10 días, aplicando un recargo fijo de 100$ al monto inicial en caso afirmativo.

---

### Desafío 2: Alquiler de Vehículos (Iterativo y con Validaciones)
**Objetivo:** Expandir el control de flujo incorporando la repetición de procesos por lotes y reglas estrictas de negocio (límites máximos y promociones).

**Requerimientos principales:**
1. **Simulación iterativa de transacciones:** Implementar un bucle `for` para procesar exactamente 4 ventas consecutivas, indicando el número de venta en cada ciclo.
2. **Captura y conversión de datos:** Solicitar de manera interactiva dentro de cada iteración el modelo del vehículo y la cantidad de días de alquiler convertidos a enteros.
3. **Cálculo automático financiero y aleatorio:** Generar un costo diario dinámico (entre 25$y 50$), calcular el monto total y el 35% correspondiente al pago inicial base.
4. **Control de límites y recargos por plazos largos:** Bloquear transacciones si el alquiler supera los 30 días, y aplicar el recargo de 100$ para alquileres entre 11 y 30 días.
5. **Gestión de descuentos promocionales específicos:** Evaluar si la cantidad de días solicitada es exactamente igual a 5 para aplicar un descuento del 10% sobre el monto total.

---

### Desafío 3: Sistema de Boletos para Teatro
**Objetivo:** Dominar el uso de estructuras condicionales anidadas, rangos contiguos e intervalos con expresiones lógicas compuestas para calcular tarifas y descuentos escalonados.

**Requerimientos principales:**
1. **Asignación de precios por tipo de boleto:** Utilizar condiciones anidadas para determinar el precio según la letra ingresada (Tipo V: 50$, Tipo P: 30$, Tipo G: 15$), normalizando el texto a mayúsculas.
2. **Cálculo del subtotal de compra:** Multiplicar el precio unitario del boleto por la cantidad de entradas ingresadas por el cliente.
3. **Determinación del porcentaje de descuento por rangos:** Evaluar intervalos contiguos mediante expresiones lógicas para otorgar porcentajes de rebaja: 0% (<200$), 5\% (200$ - 400$), 7\% (>400$ a 1000$) y 10\% (>1000$).
4. **Cálculo del total y desglose completo:** Calcular el monto monetario del descuento y el total final, imprimiendo un reporte detallado con todos los parámetros de la transacción.
5. **Validación de seguridad y ciclo repetitivo:** Condicionar la impresión de resultados a que el tipo de boleto sea válido y la cantidad positiva, estructurando todo bajo un ciclo `for` de 5 iteraciones.

---

### Desafío 4: Sistema de Cine (Cines Unidos)
**Objetivo:** Integrar instrucciones avanzadas de selección múltiple (`match-case`), condiciones compuestas complejas para excepciones y control interactivo mediante bucles `while`.

**Requerimientos principales:**
1. **Determinación de precio mediante `match`:** Utilizar la instrucción `match` de Python para asignar tarifas basadas estrictamente en la hora de la función (1pm=1$, 3pm=2$, 5pm=3$, otras=4$).
2. **Exención de pago por edad (Condiciones anidadas):** Aplicar un descuento del 100% (gratis) mediante condiciones compuestas anidadas para niños menores de 3 años y adultos mayores de 70 años, independientemente de la hora.
3. **Descuento especial por día de la semana:** Incorporar la regla de que los días lunes todas las personas obtienen un 50% de descuento, respetando la excepción prioritaria de la gratuidad por edad.
4. **Cálculo del descuento y monto final:** Calcular con precisión matemática el monto en dinero descontado y el total definitivo que el cliente debe cancelar.
5. **Control interactivo con ciclo `while` y `break`:** Implementar un bucle infinito controlado (`while True`) para repetir el sistema tantas veces como el usuario desee, utilizando validaciones y la salida basada en la respuesta del usuario.

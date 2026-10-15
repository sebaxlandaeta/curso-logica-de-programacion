# Nivel 4: Listas Paralelas, Búsquedas Secuenciales, Menús Interactivos y Módulos Externos

Nivel 4 del curso de lógica de programación en Python, enfocado en el manejo avanzado de arreglos estáticos y dinámicos (listas paralelas), algoritmos de búsqueda secuencial pura, validaciones de datos con módulos externos, menús interactivos robustos y estructuración modular avanzada.

---

## 📋 Resumen de Desafíos

### Desafío 1: Signos Zodiacales y Estaciones del Año
**Objetivo:** Implementar condiciones compuestas y anidadas para mapear entradas del usuario hacia arreglos paralelos de datos fijos.

**Requerimientos principales:**
1. **Arreglo y visualización de signos:** Definir una lista con los 12 signos del zodiaco y mostrárselos al usuario por pantalla usando una función dedicada.
2. **Captura de fecha y cálculo de posición:** Solicitar el día y mes de nacimiento como enteros y determinar mediante condiciones compuestas el índice exacto en el arreglo.
3. **Mostrar signo zodiacal:** Utilizar el índice calculado para acceder y mostrar el signo correspondiente, o manejar errores ante fechas inválidas.
4. **Arreglo de estaciones del año:** Crear un segundo arreglo con las 4 estaciones (Invierno, Otoño, Verano, Primavera).
5. **Indicar estación de nacimiento:** Evaluar el mes ingresado para relacionarlo con el arreglo y mostrar la estación correspondiente.

---

### Desafío 2: Gestión de Empleados con Listas Paralelas (Estático)
**Objetivo:** Consolidar el uso de arreglos paralelos de tamaño fijo para la lectura, almacenamiento y análisis estadístico básico.

**Requerimientos principales:**
1. **Cuatro arreglos paralelos:** Declarar listas para el nombre, la ciudad de residencia, el monto total facturado y la cantidad de facturas, cada una con un tamaño fijo de 5 elementos.
2. **Lectura unificada:** Diseñar un módulo que permita ingresar por teclado los datos de cada vendedor en un ciclo secuencial.
3. **Visualización en paralelo:** Mostrar la información organizada de forma que los datos de cada empleado se aprecien lado a lado.
4. **Cálculo de promedio y filtro:** Calcular la media de los montos facturados y mostrar los nombres de quienes superen dicho promedio.
5. **Consulta por ciudad y facturas:** Filtrar el listado para mostrar únicamente a los vendedores de una ciudad específica que superen las 5 facturas procesadas.

---

### Desafío 3: Registro Dinámico, Cédulas Únicas y Menú Modular
**Objetivo:** Desarrollar sistemas interactivos utilizando arreglos dinámicos (`.append()`), validación de duplicados y algoritmos de búsqueda secuencial sin métodos mágicos.

**Requerimientos principales:**
1. **Registro dinámico y cédulas únicas:** Usar listas vacías e insertar datos mediante `.append()`, validando al inicio que la cédula no se repita.
2. **Búsqueda secuencial algorítmica:** Crear funciones de búsqueda puras para verificar duplicados y retornar el índice exacto de una cédula o `-1` si no existe.
3. **Consulta por cédula:** Permitir buscar un vendedor por su cédula para desplegar su ficha completa o un aviso de error si no se encuentra.
4. **Menú de opciones modular:** Diseñar un menú interactivo con las 6 opciones obligatorias (Lectura, Estadísticas, Consulta, Listado, Filtro de facturas y Salir).
5. **Estructura principal (`main`):** Centralizar la ejecución y controlar el flujo continuo del programa mediante un ciclo interactivo.

---

### Desafío 4: Sistema de Béisbol y Módulo Externo de Validaciones
**Objetivo:** Integrar la separación de responsabilidades importando un módulo externo de validación y procesando estadísticas complejas sobre listas paralelas.

**Requerimientos principales:**
1. **Registro validado:** Almacenar datos en listas vacías (camisetas del 1 al 99, nombres completos de mínimo 8 caracteres, posiciones válidas de béisbol, hits de 0 a 200 y average de 0 a 1000) evitando duplicados.
2. **Módulo de validación externo:** Mantener estrictamente las funciones de validación en un archivo independiente (`funciones.py`).
3. **Consulta de jugadores:** Buscar un jugador por su número de camiseta con validación numérica y manejo de errores.
4. **Reportes estadísticos:** Mostrar el listado completo, el jugador con más hits, los bateadores con average menor al promedio general y el conteo de Pitchers (`P`).
5. **Menú interactivo robusto:** Controlar el flujo principal mediante un menú del 1 al 4 con validación estricta de entradas.

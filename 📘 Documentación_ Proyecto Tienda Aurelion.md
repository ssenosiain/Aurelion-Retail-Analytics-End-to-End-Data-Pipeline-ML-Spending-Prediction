# 📘 Documentación: Proyecto **Tienda Aurelion**

---

## 1. Tema, problema y solución

**Tema**  
Inteligencia Artificial aplicada a la validación, gestión y documentación de datos de una tienda minorista.

**Problema**  
- **Problema principal: Bajas ventas**
- Problema secundario a considerar: Los datos operativos crudos de la *Tienda Aurelion* (catálogos de productos, registros de clientes y transacciones de ventas) proceden de fuentes con inconsistencias relevantes. Se han detectado:  

  - **Errores estructurales**: columnas malformadas, campos vacíos, formatos heterogéneos.  
  - **Errores lógicos**: categorizaciones incorrectas (por ejemplo, *bebidas* clasificadas como *Limpieza*).

  Esto impide realizar análisis de negocio confiables o entrenar modelos de IA. El objetivo es transformar datos crudos y poco fiables en un **activo de información coherente, validado y documentado**.

## Solución
**Estrategias de fidelización**
  Se definirán  **estrategias de fidelización** basadas en el análisis de los datos.  Se realizará a partir de una herramienta en **Python** que, tras limpiar y estandarizar los datos, consolide la información, genere métricas por cliente y producto, y exporte los resultados en formatos **CSV** o **Markdown**.  



---

## 2. Dataset de referencia — Fuente, definición, estructura y escalas

**Fuente**  
Datos sintéticos con fines educativos generados a partir de los archivos: `clientes.xlsx`, `productos.xlsx`, `ventas.xlsx` y `detalle_ventas.xlsx`. Todos los archivos fueron preprocesados para corregir errores estructurales y lógicos.

**Definición**  
Conjunto de tablas que representan las operaciones de la tienda: catálogo de productos, registro de clientes, ventas y detalle de ventas. Compuesto por cuatro tablas principales.

---

### Clientes (`clientes.csv`) — ~100 filas

| Campo            | Tipo | Escala    | Justificación                            |
| :--------------- | :--- | :-------- | :--------------------------------------- |
| `id_cliente`     | int  | Nominal   | Identificador único.                     |
| `nombre_cliente` | str  | Nominal   | Nombre del cliente.                      |
| `email`          | str  | Nominal   | Identificador de contacto.               |
| `ciudad`         | str  | Nominal   | Ubicación geográfica.                    |
| `fecha_alta`     | date | Intervalo | Fecha de alta (differences medibles).    |


---

### Productos (`productos_limpio.csv`) — ~100 filas

| Campo             | Tipo | Escala  | Justificación                              |
| :---------------- | :--- | :------ | :----------------------------------------- |
| `id_producto`     | int  | Nominal | Identificador único.                       |
| `nombre_producto` | str  | Nominal | Nombre textual del producto.               |
| `categoria`       | str  | Nominal | Clasificación (ej. Bebidas, Limpieza).     |
| `precio_unitario` | int  | Razón   | Medida cuantitativa con cero absoluto.     |


---

### Ventas (`ventas_limpio.csv`) — ~120 filas

| Campo            | Tipo | Escala    | Justificación                             |
| :--------------- | :--- | :-------- | :---------------------------------------- |
| `id_venta`       | int  | Nominal   | Identificador de la transacción.          |
| `fecha`          | date | Intervalo | Fecha de la venta.                        |
| `id_cliente`     | int  | Nominal   | Clave foránea a `clientes.csv`.           |
| `nombre_cliente` | str  | Nominal   | Nombre (redundante).                      |
| `email`          | str  | Nominal   | Email (redundante).                       |
| `medio_pago`     | str  | Nominal   | Método de pago (tarjeta, qr, efectivo).   |


---

### Detalle de Ventas (`detalle_ventas.csv`) — ~300 filas

| Campo             | Tipo | Escala  | Justificación                                              |
| :---------------- | :--- | :------ | :--------------------------------------------------------- |
| `id_venta`        | int  | Nominal | Clave foránea a `ventas_limpio.csv`.                       |
| `id_producto`     | int  | Nominal | Clave foránea a `productos_limpio.csv`.                    |
| `nombre_producto` | str  | Nominal | Nombre del producto (redundante).                          |
| `cantidad`        | int  | Razón   | Número de unidades vendidas (conteo con cero absoluto).    |
| `precio_unitario` | int  | Razón   | Precio en el momento de la venta.                          |
| `importe`         | int  | Razón   | `cantidad * precio_unitario` — valor total del ítem.       |

---

### Ejemplo de estructura relacional (Python)

```python
ventas = [
  {
    "id_venta": 101,
    "fecha": "2024-05-15",
    "id_cliente": 12,
    "medio_pago": "tarjeta",
    "detalle": [
      {"id_producto": 39, "producto": "Helado Vainilla 1L", "cantidad": 2, "precio_unitario": 469.0, "importe": 938.0},
      {"id_producto": 70, "producto": "Fernet 750ml", "cantidad": 1, "precio_unitario": 4061.0, "importe": 4061.0}
    ]
  },
  {
    "id_venta": 102,
    "fecha": "2024-06-01",
    "id_cliente": 45,
    "medio_pago": "qr",
    "detalle": [
      {"id_producto": 82, "producto": "Aceitunas Negras 200g", "cantidad": 4, "precio_unitario": 2394.0, "importe": 9576.0}
    ]
  }
]
```

---

## 3. Programa: contenidos, pasos y pseudocódigo
### 3.1 Contenidos accesibles desde el menú (Sprint 1)

1. Tema, problema y solución  
2. Dataset de referencia (fuente, definición y estructura)  
3. Estrategias de fidelización y KPIs (métricas y segmentos exportables)  
4. Sugerencias y mejoras con Copilot  
5. Salir

---

### 3.2 Pasos del Programa (Lógica para Sprint 1)

1. **Inicio**: ejecutar el programa.  
2. **Carga de contenidos**: importar textos desde `textos.py`.  
3. **Bucle principal**: mantener el programa activo hasta salir.  
4. **Mostrar menú**: desplegar opciones numeradas.  
5. **Validar entrada**: comprobar que la selección sea válida.  
6. **Procesar entrada**: mostrar sección, o salir.  
7. **Regresar al menú**: esperar *Enter* para continuar.


---

### 3.3 Pseudocódigo detallado

```text
INICIO
  Definir función para mostrar el tema, problema y solución:
    - Imprimir el contenido correspondiente

  Definir función para mostrar la base de datos:
    - Imprimir la descripción de las tablas y su estructura

  Definir función para mostrar los pasos del programa:
    - Imprimir los pasos y el flujo del programa

  Definir función para mostrar el menú principal:
    - Imprimir las opciones disponibles:
      1. Mostrar Tema, Problema y Solución
      2. Mostrar Base de Datos
      3. Mostrar Pasos del Programa
      4. Pseudocódigo
      5. Salir

  Mientras el programa esté activo:
    - Llamar a la función para mostrar el menú principal
    - Leer la opción ingresada por el usuario

    Si la opción es "1":
      - Llamar a la función para mostrar el tema, problema y solución

    Si la opción es "2":
      - Llamar a la función para mostrar la base de datos

    Si la opción es "3":
      - Llamar a la función para mostrar los pasos del programa

    Si la opción es "4":
      - Mostrar Pseudocódigo

    Si la opción es "5":
      - Imprimir mensaje de despedida
      - Terminar el programa

    Si la opción no es válida:
      - Imprimir mensaje de error indicando que la opción no es válida

FIN
```

---


### 3.4 Diagrama de Flujo - Sistema de Menú

```
                    ( Inicio )
                        |
                        v
            +-------------------------+
            |  Mostrar menu principal |
            +-------------------------+
                        |
                        v
                /-----------------/
               /  Menu principal / <-------------------------------------------------+
              /-----------------/                                                    |
                        |                                                            |
                        v                                                            |
                  /-----------\                                                      |
                 |  Opción 1   | --(Si)-->  /-------------------------------------/  |
                  \-----------/            /   Mostrar Tema, Problema y Solución / --+
                        | (No)            /-------------------------------------/    |
                        v                                                            |
                  /-----------\                                                      |
                 |  Opción 2   | --(Si)--> /-------------------------/               |
                  \-----------/           /   Mostrar Base de Datos / ---------------+
                        | (No)           /-------------------------/                 |           
                        v                                                            |          
                  /-----------\                                                      |          
                 |  Opción 3   | --(Si)--> /------------------------------/          | 
                  \-----------/           /   Mostrar Pasos del Programa / ----------+ 
                        | (No)           /------------------------------/            | 
                        v                                                            | 
                  /-----------\                                                      | 
                 |  Opción 4   | --(Si)--> /------------------------/                | 
                  \-----------/           /   Mostrar Pseudocódigo / ----------------+
                        | (No)           /------------------------/                  | 
                        v                                                            | 
                  /-----------\                                                      | 
                 |  Opción 5   | --(No)----------------------------------------------+
                  \-----------/                                   
                        | (Si)
                        v                                   
                 /-------------------/
                / Mostrar Despedida / -----------> ( Fin )  
               /-------------------/                             

```


### 3.5 Funcionalidades avanzadas (sprints futuros)

- Cálculo automático de KPIs (ingresos mensuales, ventas por categoría, ticket promedio).  
- Exportación de secciones y KPIs a `.txt` / `.csv`.  
- Búsqueda de términos dentro de la documentación.  
- Conexión con herramientas de visualización (Power BI, Tableau).

---

## 4. Sugerencias y mejoras aplicadas con Copilot

| Estado     | Sugerencia                              | Justificación                          |
|:----------:|:---------------------------------------:|:--------------------------------------:|
| Aceptada   | Separar la documentación en `textos.py` | Mejora la mantenibilidad y claridad.   |
| Aceptada   | Usar un diccionario para el menú        | Código más limpio y escalable.         |
| Descartada | Implementar búsqueda por palabra clave  | Fuera de alcance para la primera demo. |
| Descartada | Exportar secciones a `.txt`/`.csv`      | No prioritaria para Sprint 1.          |

---

## 5. Análisis exploratorio de datos (EDA)

### 5.1 Objetivos del EDA

El notebook de análisis exploratorio se diseñó para cumplir con los siguientes objetivos:

1. Dejar la base de datos *limpia y lista para análisis*.  
2. Calcular *estadísticas descriptivas básicas*.  
3. Identificar el tipo de *distribución* de las variables numéricas principales.  
4. Analizar *correlaciones* entre variables clave (cantidad, precio unitario, importe).  
5. Detectar *outliers* mediante el método de cuartiles (IQR).  
6. Generar una *interpretación de resultados orientada al problema de negocio* (bajas ventas).  
7. Producir al menos *3 gráficos representativos* (histograma/KDE, boxplot, mapa de calor de correlaciones, pairplot).  
8. Documentar el análisis de forma *paso a paso* dentro del notebook.

---

### 5.2 Preparación y limpieza de datos

Las siguientes transformaciones se aplicaron antes de hacer el análisis estadístico:

- *Carga de las cuatro tablas base* desde los archivos Excel: clientes.xlsx, productos.xlsx, ventas.xlsx y detalle_ventas.xlsx.  
- *Eliminación de columnas auxiliares* como las que comienzan con Unnamed en la tabla de productos.  
- *Tipificación de columnas* para asegurar coherencia:

  - id_cliente, id_producto, id_venta, cantidad → enteros.  
  - nombre_cliente, nombre_producto, email, ciudad, categoria, medio_pago → cadenas de texto.  
  - fecha, fecha_alta → fechas (datetime64[ns]).  

- *Conversión numérica robusta* (pd.to_numeric(..., errors='coerce') en columnas como precio_unitario, precio_unitario_x, precio_unitario_y, importe y cantidad, garantizando que cualquier valor no válido se convierta en NaN y no contamine los cálculos posteriores.

- **Construcción de un dataset maestro _df** mediante joins:

  - detalle_ventas ⟶ ventas (clave id_venta).  
  - Resultado ⟶ clientes (clave id_cliente).  
  - Resultado ⟶ productos (clave id_producto).  

- *Variables derivadas de fecha*:

  - Año: año de la venta.  
  - Mes: mes de la venta.  
  - dia_semana: nombre del día de la semana (en español cuando está disponible).

- *Normalización de nombres de columnas*:  
  Tras los merges surgieron columnas duplicadas con sufijos _x y _y (por ejemplo, nombre_producto_x y nombre_producto_y, precio_unitario_x y precio_unitario_y). Se inspeccionaron sus valores y se confirmó que eran equivalentes fila a fila, por lo que se renombraron a una versión única (nombre_producto, precio_unitario, nombre_cliente, email) y luego se eliminaron las duplicadas.

- *Eliminación de columnas duplicadas por nombre*:  
  Se utilizó _df = _df.loc[:, ~_df.columns.duplicated()] para dejar *una sola columna por nombre lógico*.

---

### 5.3 Estructura final del dataset maestro

Las columnas más relevantes del dataset final _df son:

- Identificadores y claves:
  - id_venta: identificador de la transacción.  
  - id_producto: identificador del producto.  
  - id_cliente: identificador del cliente.

- Variables del ítem de venta:
  - nombre_producto, categoria.  
  - cantidad: unidades vendidas en la línea de detalle.  
  - precio_unitario: precio de venta por unidad.  
  - importe: valor total de la línea (cantidad * precio_unitario).

- Contexto de la venta:
  - fecha: fecha de la venta.  
  - medio_pago: tarjeta, QR, efectivo, etc.  
  - Año, Mes, dia_semana: variables temporales derivadas.  
  - nombre_cliente, email, ciudad, fecha_alta.

---

### 5.4 Distribuciones y correlaciones

Se generaron:

- Un *histograma + KDE* del precio_unitario.  
- Un *boxplot* del importe.  
- Un *mapa de calor de correlaciones* entre las variables numéricas.  
- Un *pairplot* (diagrama de pares) entre precio_unitario, cantidad e importe.

Principales hallazgos cualitativos:

- La distribución de precio_unitario está concentrada en un rango de precios relativamente acotado, con una cola hacia productos más caros.  
- El boxplot de importe evidencia la presencia de tickets altos (que luego aparecen como outliers según IQR).  
- El análisis de correlaciones y el pairplot muestran una *correlación positiva clara* entre:

  - importe y cantidad.  
  - importe y precio_unitario.

- Visualmente, la nube de puntos indica que:

  - A medida que aumentan precio unitario y cantidad, el *importe total también aumenta*.  
  - Los puntos se vuelven más dispersos en la zona de importes altos, pero la mayoría de ventas se concentra en *precios bajos a medios* y tickets moderados.
---

## 6. Modelo de Machine Learning: Estimación de Gasto por Cliente

Para abordar el problema principal de **Bajas Ventas**, se implementó un modelo de **Regresión Lineal** simple. El objetivo es predecir el **Gasto Total** que un cliente realizará, permitiendo a la tienda identificar clientes de alto valor potencial para aplicar estrategias de fidelización.

### 6.1. Ingeniería de Características (Feature Engineering)

Se transformó el dataset maestro de transacciones (_df) en un dataset a nivel de cliente (df_features) con las siguientes variables:

| Variable | Tipo | Descripción |
| :--- | :--- | :--- |
| `gasto_total` (Y) | Numérica | **Variable Objetivo:** Suma total de `importe` gastado por el cliente. |
| `total_compras` (X) | Numérica | Número de transacciones únicas realizadas por el cliente. |
| `total_productos` (X) | Numérica | Suma total de `cantidad` de productos comprados. |
| `antiguedad_dias` (X) | Numérica | Días transcurridos desde la fecha de alta del cliente. |
| `ciudad` (X) | Categórica | Se aplicó One-Hot Encoding para incluir la ciudad de residencia como variable predictora. |

### 6.2. Implementación del Modelo (Regresión Lineal)

Se utilizó el algoritmo de Regresión Lineal de `scikit-learn` para modelar la relación entre las características (X) y el gasto total (Y).

- **División de Datos:** 80% para entrenamiento, 20% para prueba (`random_state=42`).
- **Modelo:** `sklearn.linear_model.LinearRegression`.

### 6.3. Resultados y Evaluación

El modelo fue evaluado con las siguientes métricas:

| Métrica | Valor | Interpretación |
| :--- | :--- | :--- |
| **Error Cuadrático Medio (MSE)** | 177,542,970.59 | Mide el promedio de los errores al cuadrado. Un valor más bajo es mejor. |
| **Coeficiente de Determinación (R²)** | 0.4761 | Indica que el 47.61% de la varianza en el gasto total del cliente es explicada por las variables predictoras. |

El valor de **R² de 0.4761** sugiere que el modelo tiene una capacidad predictiva moderada. Esto es un buen punto de partida para un modelo básico, y puede mejorarse con más ingeniería de características o modelos más complejos.

---

### 6.4. Visualización de Resultados

Para evaluar visualmente el rendimiento del modelo, se generó un gráfico de dispersión que compara el **Gasto Total Real** (eje X) con el **Gasto Total Predicho** (eje Y) para el conjunto de prueba.

La línea diagonal roja representa la predicción perfecta (donde el valor real es igual al predicho). Cuanto más cerca estén los puntos de esta línea, mejor es el rendimiento del modelo.

![Gráfico de dispersión: Gasto Total Real vs. Predicho](https://private-us-east-1.manuscdn.com/sessionFile/dGr5NQKVX3sYCwuHF0SReK/sandbox/DmbAE7dMQIbF8qsWoOY4uz-images_1765147275296_na1fn_L2hvbWUvdWJ1bnR1L2dhc3RvX3ByZWRpY2hvX3ZzX3JlYWw.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUvZEdyNU5RS1ZYM3NZQ3d1SEYwU1JlSy9zYW5kYm94L0RtYkFFN2RNUUliRjhxc1dvT1k0dXotaW1hZ2VzXzE3NjUxNDcyNzUyOTZfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwyZGhjM1J2WDNCeVpXUnBZMmh2WDNaelgzSmxZV3cucG5nIiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNzk4NzYxNjAwfX19XX0_&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=SVHbJJvO9vU1bKm4HP6ZUjihHzEW4SrYfW90doF2Eb3Vc-rXk~gkC4gLlf3P5xyolKHXYuvsIVtq3-5IwS80AQTgUBuLfgTMUMC93m7xOjoEVArOs-ocbpPhkYsL1DZi23ncg~HDLs-JCPHXG6oFCVbL-99Ga6mukjtq7Y-IKQsnNQ6iMTJKGNKaQRG8M1eGJM1Q-HZFTxwJ6veRrgR8BenC5qN6tYjDv5uTts4dm7k590ITquyxz82J9Af-ZBC-cSdtlGCwU7WotmhqoDUYNB6kiDeGbhz6lV762bbiDThRkpXBV5JfE6ZCv5cC3Zy07VjoLokefIJBT5EunAKxwQ__)

---

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. Configuración y Carga de Datos ---
print("--- 1. Configuración y Carga de Datos ---")
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")
sns.set(context="notebook")

PROJECT_PATH = "/home/ubuntu/projects/machine-learning-2350df0a/"
OUTPUT_PATH = "/home/ubuntu/"
GRAPH_FILE = "gasto_predicho_vs_real.png"

# Carga de datos (ajustado a archivos CSV)
try:
    df_detalle_ventas = pd.read_csv(os.path.join(PROJECT_PATH, "detalle_ventas.csv"))
    df_clientes = pd.read_csv(os.path.join(PROJECT_PATH, "clientes.csv"))
    df_productos = pd.read_csv(os.path.join(PROJECT_PATH, "productos.csv"))
    df_ventas = pd.read_csv(os.path.join(PROJECT_PATH, "ventas.csv"))
except FileNotFoundError as e:
    print(f"Error al cargar archivos: {e}")
    exit()

# --- 2. Limpieza y Preparación de Datos ---
print("--- 2. Limpieza y Preparación de Datos ---")

# Eliminar columnas "Unnamed" (si existen)
for df in [df_clientes, df_productos, df_ventas, df_detalle_ventas]:
    df.columns = df.columns.str.replace(r"^Unnamed: \d+", "", regex=True)
    df.columns = df.columns.str.strip()
    df.dropna(axis=1, how='all', inplace=True)

# Función para eliminar duplicados
def drop_dupes(df, subset_cols):
    if not set(subset_cols).issubset(df.columns):
        return df
    return df.sort_values(by=subset_cols).drop_duplicates(subset=subset_cols, keep='last')

# Aplicar limpieza de duplicados
df_clientes = drop_dupes(df_clientes, ['id_cliente'])
df_productos = drop_dupes(df_productos, ['id_producto'])
df_ventas = drop_dupes(df_ventas, ['id_venta'])
df_detalle_ventas = drop_dupes(df_detalle_ventas, ['id_venta','id_producto'])

# Conversión de fechas
if 'fecha' in df_ventas.columns:
    df_ventas['fecha'] = pd.to_datetime(df_ventas['fecha'], errors='coerce')
if 'fecha_alta' in df_clientes.columns:
    df_clientes['fecha_alta'] = pd.to_datetime(df_clientes['fecha_alta'], errors='coerce')

# Merge maestro
_df = df_detalle_ventas.merge(df_ventas, on='id_venta', how='left')
_df = _df.merge(df_clientes, on='id_cliente', how='left')
_df = _df.merge(df_productos, on='id_producto', how='left')

# Imputaciones numéricas robustas
for col in [c for c in ['precio_unitario_x','precio_unitario_y','importe','cantidad'] if c in _df.columns]:
    _df[col] = pd.to_numeric(_df[col], errors='coerce')

# Renombrar y consolidar columnas duplicadas (asumiendo que _x es el valor correcto de detalle_ventas)
_df.rename(columns={'precio_unitario_x': 'precio_unitario_venta', 'nombre_producto_x': 'nombre_producto_venta'}, inplace=True)
_df.drop(columns=['precio_unitario_y', 'nombre_producto_y', 'nombre_cliente_y', 'email_y'], inplace=True, errors='ignore')
_df.rename(columns={'nombre_cliente_x': 'nombre_cliente', 'email_x': 'email'}, inplace=True)

# Eliminar filas con valores nulos en columnas clave para el modelo
_df.dropna(subset=['id_cliente', 'importe', 'cantidad', 'fecha'], inplace=True)

# --- 3. Feature Engineering para Modelo de Regresión (Gasto Total por Cliente) ---
print("--- 3. Feature Engineering ---")

# 3.1. Variable Objetivo (Y): Gasto Total por Cliente
df_gasto_total = _df.groupby('id_cliente').agg(
    gasto_total=('importe', 'sum'),
    total_compras=('id_venta', 'nunique'),
    total_productos=('cantidad', 'sum'),
    # Usar la fecha de la primera compra para calcular la antigüedad
    fecha_primera_compra=('fecha', 'min') 
).reset_index()

# 3.2. Features Adicionales (X)
# Unir con la tabla de clientes para obtener 'ciudad' y 'fecha_alta'
df_gasto_total = df_gasto_total.merge(df_clientes[['id_cliente', 'ciudad', 'fecha_alta']], on='id_cliente', how='left')

# Calcular antigüedad del cliente (en días)
# Usamos la fecha de la primera compra para calcular la antigüedad de la relación de compra
df_gasto_total['antiguedad_dias'] = (pd.to_datetime('today') - df_gasto_total['fecha_primera_compra']).dt.days
df_gasto_total.drop(columns=['fecha_alta', 'fecha_primera_compra'], inplace=True)

# One-Hot Encoding para 'ciudad'
df_features = pd.get_dummies(df_gasto_total, columns=['ciudad'], drop_first=True)

# Definir X e Y
# Excluir columnas no numéricas o no relevantes para el modelo
X = df_features.select_dtypes(include=np.number).drop(columns=['id_cliente', 'gasto_total'])
y = df_features['gasto_total']

# --- 4. Entrenamiento del Modelo de Regresión Lineal ---
print("--- 4. Entrenamiento del Modelo de Regresión Lineal ---")

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# --- 5. Evaluación del Modelo ---
print("--- 5. Evaluación del Modelo ---")
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Métricas del Modelo de Regresión Lineal (Estimación de Gasto Total por Cliente):")
print(f"  Error Cuadrático Medio (MSE): {mse:,.2f}")
print(f"  Coeficiente de Determinación (R²): {r2:,.4f}")

# --- 6. Visualización de Resultados ---
print("--- 6. Visualización de Resultados ---")

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2) # Línea de predicción perfecta
plt.xlabel("Gasto Total Real (Y_test)")
plt.ylabel("Gasto Total Predicho (Y_pred)")
plt.title(f"Modelo de Regresión Lineal: Real vs. Predicho (R²: {r2:,.4f})")
plt.grid(True)

# Guardar el gráfico
full_graph_path = os.path.join(OUTPUT_PATH, GRAPH_FILE)
plt.savefig(full_graph_path)
print(f"Gráfico guardado en: {full_graph_path}")

# --- 7. Guardar Resultados y Modelo (Opcional: para demostración) ---
print("--- 7. Resultados de Predicción ---")
# Mostrar las 5 primeras predicciones
df_resultados = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
print("\nPrimeras 5 Predicciones vs. Real:")
print(df_resultados.head().applymap(lambda x: f"{x:,.2f}"))

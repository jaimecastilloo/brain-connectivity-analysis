import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os
import scipy.stats as stats

# --- Configuración ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ruta_srs = os.path.join(BASE_DIR, "Metodologia_srs", "resumen.csv")
ruta_lhs = os.path.join(BASE_DIR, "Metodologia_lhs", "resumen.csv")
salida_dir = os.path.join(os.path.dirname(__file__), "relacion_regresiones")
os.makedirs(salida_dir, exist_ok=True)

# Cargar datos
srs = pd.read_csv(ruta_srs)
lhs = pd.read_csv(ruta_lhs)

# Variables a modelar
pares = [
    ("fa_threshold", "media_conectividad"),
    ("fa_threshold", "n_tractos_reales"),
    ("track_voxel_ratio", "n_tractos_reales")
]

# Para guardar resultados
regresiones = []

# Función para ajustar y guardar resultados
def ajustar_regresion(df, xvar, yvar, metodo):
    X = df[[xvar]].values
    Y = df[yvar].values
    modelo = LinearRegression().fit(X, Y)
    pred = modelo.predict(X)
    r2 = r2_score(Y, pred)

    # Cálculo p-value para la pendiente (test t)
    slope, intercept, r, p_value, _ = stats.linregress(df[xvar], df[yvar])

    regresiones.append({
        "Método": metodo,
        "Input": xvar,
        "Output": yvar,
        "Intercepto": intercept,
        "Pendiente": slope,
        "R2": r2,
        "p-value": p_value
    })

    # Figura
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=xvar, y=yvar, data=df, color="gray", alpha=0.6)
    plt.plot(X, pred, color="red", label=f"Regresión (R² = {r2:.2f})")
    plt.title(f"{yvar} vs {xvar} ({metodo})")
    plt.legend()
    plt.tight_layout()
    fname = f"reg_{metodo.lower()}_{xvar}_vs_{yvar}.png"
    plt.savefig(os.path.join(salida_dir, fname), dpi=300)
    plt.close()

# Aplicar a cada método y par de variables
for metodo, datos in [("SRS", srs), ("LHS", lhs)]:
    for xvar, yvar in pares:
        ajustar_regresion(datos, xvar, yvar, metodo)

# Exportar tabla de regresiones
pd.DataFrame(regresiones).to_csv(os.path.join(salida_dir, "tabla_regresiones.csv"), index=False)

print("Regresiones calculadas y guardadas.")
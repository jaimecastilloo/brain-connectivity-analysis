import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

# --- Configuración ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ruta_srs = os.path.join(BASE_DIR, "Metodologia_srs", "resumen.csv")
ruta_lhs = os.path.join(BASE_DIR, "Metodologia_lhs", "resumen.csv")
salida = os.path.join(os.path.dirname(__file__), "relacion_regresiones.png")

# Cargar datos
srs = pd.read_csv(ruta_srs)
lhs = pd.read_csv(ruta_lhs)

# Parámetros
pares = [
    ("fa_threshold", "n_tractos_reales", "A. n_tractos vs fa_threshold"),
    ("fa_threshold", "media_conectividad", "B. conectividad media vs fa_threshold"),
    ("track_voxel_ratio", "n_tractos_reales", "C. n_tractos vs track_voxel_ratio")
]

# Crear figura
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

for ax, (xvar, yvar, titulo) in zip(axs, pares):
    for datos, nombre, color in [(srs, "SRS", "#4C72B0"), (lhs, "LHS", "#55A868")]:
        X = datos[[xvar]].values
        Y = datos[yvar].values
        modelo = LinearRegression().fit(X, Y)
        pred = modelo.predict(X)

        ax.scatter(X, Y, alpha=0.4, label=f"{nombre}", color=color)
        ax.plot(X, pred, color=color, linestyle="-", linewidth=2)

    ax.set_xlabel(xvar)
    ax.set_ylabel(yvar)
    ax.set_title(titulo)
    ax.legend()

plt.tight_layout()
plt.savefig(salida, dpi=300)
print("Figura 'regresiones_comparadas.png' guardada.")
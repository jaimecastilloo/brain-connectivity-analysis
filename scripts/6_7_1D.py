import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carpeta de salida
OUT = "figs_1d"
os.makedirs(OUT, exist_ok=True)
print("Guardando en:", os.path.abspath(OUT))

# Límites conocidos de cada parámetro (solo para fijar ejes)
param_bounds = {
    "fa_threshold": (0.116, 0.238),
    "turning_angle": (42, 66),
    "track_voxel_ratio": (1.21, 2.12)
}

# Carga de datos
df_srs = pd.read_csv("srs.csv")
df_lhs = pd.read_csv("lhs.csv")
parametros = list(param_bounds.keys())

def graficar_comparativa(param, point_size=36, alpha=0.55):
    """
    Representa los 50 valores en una línea horizontal para SRS (rojo) y LHS (azul),
    sin estratos, sin etiquetas de conteo y sin jitter. Se usa alpha para que
    los solapes se aprecien por densidad.
    """
    # Figura más ancha para apreciar solapes
    fig, axs = plt.subplots(2, 1, figsize=(12, 3.2), sharex=True)

    x_min, x_max = param_bounds[param]

    # -------- SRS --------
    x_srs = df_srs[param].to_numpy()
    y_srs = np.zeros_like(x_srs, dtype=float)

    axs[0].scatter(
        x_srs, y_srs,
        c="red", alpha=alpha, s=point_size,
        edgecolors="black", linewidths=0.3, zorder=2
    )
    axs[0].set_xlim(x_min, x_max)
    axs[0].set_yticks([])
    axs[0].set_ylim(-0.12, 0.12)
    axs[0].set_ylabel("SRS")
    axs[0].set_title(f"Distribución 1D de {param} (valores exactos)")

    # -------- LHS --------
    x_lhs = df_lhs[param].to_numpy()
    y_lhs = np.zeros_like(x_lhs, dtype=float)

    axs[1].scatter(
        x_lhs, y_lhs,
        c="blue", alpha=alpha, s=point_size,
        edgecolors="black", linewidths=0.3, zorder=2
    )
    axs[1].set_xlim(x_min, x_max)
    axs[1].set_yticks([])
    axs[1].set_ylim(-0.12, 0.12)
    axs[1].set_ylabel("LHS")
    axs[1].set_xlabel(param)

    # Diseño final y guardado
    fig.tight_layout()
    out_path = os.path.join(OUT, f"{param}.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print("Creado:", out_path)

# --- Genera las figuras ---
for param in parametros:
    graficar_comparativa(param, point_size=36, alpha=0.55)
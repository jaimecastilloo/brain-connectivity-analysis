import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Colores consistentes
COLORS = {"SRS": "#1f77b4", "LHS": "#2ca02c"}

# Rango real de parámetros
param_bounds = {
    "fa_threshold": (0.116, 0.238),
    "turning_angle": (42, 66),
    "track_voxel_ratio": (1.21, 2.12),
}

# Carpeta de salida
OUT = "figs_1d_compacto"
os.makedirs(OUT, exist_ok=True)

# Datos
df_srs = pd.read_csv("srs.csv")
df_lhs = pd.read_csv("lhs.csv")

def strip1d_compacto(df_srs, df_lhs, column, jitter=0.15):
    fig, axs = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)

    # Rango
    low, high = param_bounds[column]

    # --- SRS ---
    y_srs = np.random.uniform(-jitter, jitter, len(df_srs))
    axs[0].scatter(df_srs[column], y_srs, c=COLORS["SRS"], s=28, alpha=0.8)
    axs[0].axhline(0, color="black", linewidth=0.5)
    axs[0].set_xlim(low, high)
    axs[0].set_yticks([])
    axs[0].set_title("SRS", fontsize=10)

    # --- LHS ---
    y_lhs = np.random.uniform(-jitter, jitter, len(df_lhs))
    axs[1].scatter(df_lhs[column], y_lhs, c=COLORS["LHS"], s=28, alpha=0.8)
    axs[1].axhline(0, color="black", linewidth=0.5)
    axs[1].set_xlim(low, high)
    axs[1].set_yticks([])
    axs[1].set_title("LHS", fontsize=10)

    # Ejes
    axs[1].set_xlabel(column.replace("_", " "))

    fig.tight_layout()
    out_path = os.path.join(OUT, f"{column}_1d.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print("Creado:", out_path)

for col in param_bounds:
    strip1d_compacto(df_srs, df_lhs, col)
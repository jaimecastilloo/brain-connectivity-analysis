import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carpeta salida
OUT = "figs_2d_horizontal"
os.makedirs(OUT, exist_ok=True)
print("Guardando en:", os.path.abspath(OUT))

# Rangos previos al muestreo
param_bounds = {
    "fa_threshold": (0.116, 0.238),
    "turning_angle": (42, 66),
    "track_voxel_ratio": (1.21, 2.12)
}

# Datos
df_srs = pd.read_csv("srs.csv")
df_lhs = pd.read_csv("lhs.csv")

# Pares de parámetros a graficar
pairs = [
    ("fa_threshold", "turning_angle"),
    ("fa_threshold", "track_voxel_ratio"),
    ("turning_angle", "track_voxel_ratio"),
]

# Colores consistentes
COLORS = {
    "SRS": "#1f77b4",   # azul oscuro
    "LHS": "#2ca02c"    # verde oscuro
}

def scatter_2d_horizontal(xn, yn, jitter_frac_x=0.002, jitter_frac_y=0.0025):
    fig, axs = plt.subplots(1, 2, figsize=(11, 5), sharex=False, sharey=False)

    # Rangos y escalas para jitter
    x_min, x_max = param_bounds[xn]
    y_min, y_max = param_bounds[yn]
    rx = x_max - x_min
    ry = y_max - y_min

    # --- SRS ---
    N_srs = len(df_srs)
    jx_srs = np.random.uniform(-jitter_frac_x, jitter_frac_x, N_srs) * rx
    jy_srs = np.random.uniform(-jitter_frac_y, jitter_frac_y, N_srs) * ry
    xs_srs = df_srs[xn].to_numpy() + jx_srs
    ys_srs = df_srs[yn].to_numpy() + jy_srs

    axs[0].scatter(xs_srs, ys_srs, c=COLORS["SRS"], alpha=0.6, s=36,
                   edgecolors="black", linewidths=0.3, zorder=2)
    axs[0].set_xlim(x_min, x_max)
    axs[0].set_ylim(y_min, y_max)
    axs[0].set_title("SRS")
    axs[0].set_xlabel(xn)
    axs[0].set_ylabel(yn)
    axs[0].grid(True, linestyle="--", linewidth=0.5, alpha=0.5)

    # --- LHS ---
    N_lhs = len(df_lhs)
    jx_lhs = np.random.uniform(-jitter_frac_x, jitter_frac_x, N_lhs) * rx
    jy_lhs = np.random.uniform(-jitter_frac_y, jitter_frac_y, N_lhs) * ry
    xs_lhs = df_lhs[xn].to_numpy() + jx_lhs
    ys_lhs = df_lhs[yn].to_numpy() + jy_lhs

    axs[1].scatter(xs_lhs, ys_lhs, c=COLORS["LHS"], alpha=0.6, s=36,
                   edgecolors="black", linewidths=0.3, zorder=2)
    axs[1].set_xlim(x_min, x_max)
    axs[1].set_ylim(y_min, y_max)
    axs[1].set_title("LHS")
    axs[1].set_xlabel(xn)
    axs[1].set_ylabel(yn)
    axs[1].grid(True, linestyle="--", linewidth=0.5, alpha=0.5)

    fig.suptitle(f"{yn} vs {xn}")
    fig.tight_layout()
    out_path = os.path.join(OUT, f"{yn}_vs_{xn}.png")
    fig.savefig(out_path, dpi=300)
    plt.close(fig)
    print("Creado:", out_path)

for x, y in pairs:
    scatter_2d_horizontal(x, y)
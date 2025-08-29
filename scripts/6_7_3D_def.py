import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Definir colores consistentes
COLORS = {
    "SRS": "#1f77b4",   # azul oscuro
    "LHS": "#2ca02c"    # verde oscuro
}

# Rango real usado antes del muestreo
param_bounds = {
    "fa_threshold": (0.116, 0.238),
    "turning_angle": (42, 66),
    "track_voxel_ratio": (1.21, 2.12),
}

# Rutas
base = Path(".")
df_srs = pd.read_csv(base / "srs.csv")
df_lhs = pd.read_csv(base / "lhs.csv")

def plot_3d(df, title, outfile, color):
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(projection="3d")
    ax.scatter(df["fa_threshold"], df["turning_angle"], df["track_voxel_ratio"],
               c=color, alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel("FA threshold")
    ax.set_ylabel("Turning angle (°)")
    ax.set_zlabel("Track voxel ratio")
    ax.set_xlim(*param_bounds["fa_threshold"])
    ax.set_ylim(*param_bounds["turning_angle"])
    ax.set_zlim(*param_bounds["track_voxel_ratio"])
    ax.view_init(elev=18, azim=35)
    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close(fig)

plot_3d(df_srs, "Cobertura del espacio tridimensional: SRS", "srs_3d.png", COLORS["SRS"])
plot_3d(df_lhs, "Cobertura del espacio tridimensional: LHS", "lhs_3d.png", COLORS["LHS"])
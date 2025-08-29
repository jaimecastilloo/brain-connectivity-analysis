import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Rango real usado antes del muestreo
param_bounds = {
    "fa_threshold": (0.116, 0.238),
    "turning_angle": (42, 66),
    "track_voxel_ratio": (1.21, 2.12)
}

# Cargar los datos
df_srs = pd.read_csv("srs.csv")
df_lhs = pd.read_csv("lhs.csv")

# --- Figura SRS ---
fig_srs = plt.figure(figsize=(7, 6))
ax1 = fig_srs.add_subplot(111, projection='3d')
ax1.scatter(df_srs['fa_threshold'], df_srs['turning_angle'], df_srs['track_voxel_ratio'],
            c='red', alpha=0.6)
ax1.set_title('Cobertura del espacio tridimensional: SRS')
ax1.set_xlabel('FA threshold')
ax1.set_ylabel('Turning angle (°)')
ax1.set_zlabel('Track voxel ratio')
ax1.set_xlim(*param_bounds["fa_threshold"])
ax1.set_ylim(*param_bounds["turning_angle"])
ax1.set_zlim(*param_bounds["track_voxel_ratio"])
plt.tight_layout()
plt.savefig("srs_3d.png", dpi=300)
plt.close(fig_srs)

# --- Figura LHS ---
fig_lhs = plt.figure(figsize=(7, 6))
ax2 = fig_lhs.add_subplot(111, projection='3d')
ax2.scatter(df_lhs['fa_threshold'], df_lhs['turning_angle'], df_lhs['track_voxel_ratio'],
            c='blue', alpha=0.6)
ax2.set_title('Cobertura del espacio tridimensional: LHS')
ax2.set_xlabel('FA threshold')
ax2.set_ylabel('Turning angle (°)')
ax2.set_zlabel('Track voxel ratio')
ax2.set_xlim(*param_bounds["fa_threshold"])
ax2.set_ylim(*param_bounds["turning_angle"])
ax2.set_zlim(*param_bounds["track_voxel_ratio"])
plt.tight_layout()
plt.savefig("lhs_3d.png", dpi=300)
plt.close(fig_lhs)
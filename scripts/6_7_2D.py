import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
df_srs = pd.read_csv("srs.csv")
df_lhs = pd.read_csv("lhs.csv")

# Número de muestras (estratos)
N = len(df_srs)

# Rangos reales definidos antes del muestreo
param_bounds = {
    "fa_threshold": (0.05, 0.30),
    "turning_angle": (30, 80),
    "track_voxel_ratio": (0.8, 2.5)
}

# Pares de parámetros para graficar
pairs = [
    ("fa_threshold", "turning_angle"),
    ("fa_threshold", "track_voxel_ratio"),
    ("turning_angle", "track_voxel_ratio")
]

# Función para graficar con rejilla de estratos
def graficar_con_rejilla(df, tipo, color):
    for x, y in pairs:
        fig, ax = plt.subplots(figsize=(6, 5))

        # Dibujar puntos
        ax.scatter(df[x], df[y], c=color, alpha=0.6, s=40)

        # Rango original de ambos ejes
        x_min, x_max = param_bounds[x]
        y_min, y_max = param_bounds[y]

        # Estratos uniformes
        x_lines = np.linspace(x_min, x_max, N + 1)
        y_lines = np.linspace(y_min, y_max, N + 1)

        # Dibujar rejilla
        for xl in x_lines:
            ax.axvline(x=xl, color='gray', linestyle='--', linewidth=0.5)
        for yl in y_lines:
            ax.axhline(y=yl, color='gray', linestyle='--', linewidth=0.5)

        # Etiquetas
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"{tipo}: {x} vs {y}")
        plt.tight_layout()
        filename = f"{tipo.lower()}_{x}_vs_{y}_grid.png"
        plt.savefig(filename, dpi=300)
        plt.close()

# Generar gráficos para cada combinación
graficar_con_rejilla(df_srs, "SRS", "red")
graficar_con_rejilla(df_lhs, "LHS", "blue")
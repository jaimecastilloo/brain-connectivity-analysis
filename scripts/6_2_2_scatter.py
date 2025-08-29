import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- CARGA DE DATOS ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ruta_srs = os.path.join(BASE_DIR, "Metodologia_srs", "resumen.csv")
ruta_lhs = os.path.join(BASE_DIR, "Metodologia_lhs", "resumen.csv")
carpeta_salida = os.path.join(os.path.dirname(__file__), "relacion_scatter")
os.makedirs(carpeta_salida, exist_ok=True)

# Cargar datasets
srs = pd.read_csv(ruta_srs)
srs["Método"] = "SRS"
lhs = pd.read_csv(ruta_lhs)
lhs["Método"] = "LHS"
df = pd.concat([srs, lhs], ignore_index=True)

# --- Variables a representar ---
pares = [
    ("fa_threshold", "n_tractos_reales"),
    ("fa_threshold", "media_conectividad"),
    ("track_voxel_ratio", "n_tractos_reales"),
    ("turning_angle", "n_conexiones"),
]

# --- Generar scatter plots ---
for xvar, yvar in pares:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=xvar, y=yvar, hue="Método", alpha=0.6)
    plt.title(f"{yvar} vs {xvar}")
    plt.xlabel(xvar)
    plt.ylabel(yvar)
    plt.legend(title="Muestreo")
    plt.tight_layout()
    nombre = f"scatter_{xvar}_vs_{yvar}.png"
    plt.savefig(os.path.join(carpeta_salida, nombre), dpi=300)
    plt.close()

print("Scatter plots generados correctamente.")

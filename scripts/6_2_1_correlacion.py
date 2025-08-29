import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- CONFIGURACIÓN ---
tipo = "lhs"  # Cambiar a "lhs" para usar LHS
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ruta_csv = os.path.join(BASE_DIR, f"Metodologia_{tipo}", "resumen.csv")
carpeta_salida = os.path.join(os.path.dirname(__file__), f"relacion_{tipo}")
os.makedirs(carpeta_salida, exist_ok=True)

# Leer datos
df = pd.read_csv(ruta_csv)

# Seleccionar columnas
inputs = ["fa_threshold", "turning_angle", "track_voxel_ratio"]
outputs = [
    "n_tractos_reales", "media_conectividad", "desviacion_tipica",
    "n_conexiones", "coef_variacion", "densidad_relativa"
]
variables = inputs + outputs
df = df[variables]

# Calcular correlaciones
corr_pearson = df.corr(method="pearson")
corr_spearman = df.corr(method="spearman")

# Exportar matrices
corr_pearson.to_csv(os.path.join(carpeta_salida, "correlacion_pearson.csv"))
corr_spearman.to_csv(os.path.join(carpeta_salida, "correlacion_spearman.csv"))

# Visualización
def heatmap_correlacion(matriz, metodo):
    plt.figure(figsize=(10, 8))
    sns.heatmap(matriz, annot=True, cmap="vlag", center=0, fmt=".2f",
                annot_kws={"size": 8}, square=True)
    plt.title(f"Matriz de correlación ({metodo}) - {tipo.upper()}")
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta_salida, f"correlacion_{metodo}_{tipo}.png"))
    plt.close()

heatmap_correlacion(corr_pearson, "pearson")
heatmap_correlacion(corr_spearman, "spearman")

print(f"Matrices de correlación ({tipo.upper()}) generadas y guardadas.")
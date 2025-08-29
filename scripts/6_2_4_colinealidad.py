import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
import os

# --- Configuración ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ruta_srs = os.path.join(BASE_DIR, "Metodologia_srs", "resumen.csv")
ruta_lhs = os.path.join(BASE_DIR, "Metodologia_lhs", "resumen.csv")
salida = os.path.join(os.path.dirname(__file__), "relacion_colinealidad")

os.makedirs(salida, exist_ok=True)

# Inputs
inputs = ["fa_threshold", "turning_angle", "track_voxel_ratio"]

def analizar_colinealidad(df, metodo):
    df_inputs = df[inputs]

    # --- Matriz de correlación Pearson ---
    corr_pearson = df_inputs.corr(method="pearson")
    sns.heatmap(corr_pearson, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title(f"Matriz de correlación (Pearson) - {metodo}")
    plt.tight_layout()
    plt.savefig(os.path.join(salida, f"correlacion_pearson_{metodo.lower()}.png"))
    plt.close()

    # --- Matriz de correlación Spearman ---
    corr_spearman = df_inputs.corr(method="spearman")
    sns.heatmap(corr_spearman, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title(f"Matriz de correlación (Spearman) - {metodo}")
    plt.tight_layout()
    plt.savefig(os.path.join(salida, f"correlacion_spearman_{metodo.lower()}.png"))
    plt.close()

    # --- Cálculo VIF ---
    vif_data = pd.DataFrame()
    vif_data["Variable"] = inputs
    vif_data["VIF"] = [variance_inflation_factor(df_inputs.values, i) for i in range(len(inputs))]
    vif_data["Método"] = metodo

    return vif_data

# Cargar y analizar
df_srs = pd.read_csv(ruta_srs)
df_lhs = pd.read_csv(ruta_lhs)

vif_srs = analizar_colinealidad(df_srs, "SRS")
vif_lhs = analizar_colinealidad(df_lhs, "LHS")

# Combinar y exportar
vif_total = pd.concat([vif_srs, vif_lhs])
vif_total.to_csv(os.path.join(salida, "tabla_vif.csv"), index=False)

print("Análisis de colinealidad completado.")
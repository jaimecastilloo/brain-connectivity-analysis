import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

# === CONFIGURACIÓN DE RUTAS ===
ruta_matrices = r"C:\Users\jaime\Documents\UNIVERSIDAD\TFG\Metodologia_srs\matrices"
ruta_output = r"C:\Users\jaime\Documents\UNIVERSIDAD\TFG\Resultados\scripts\matrices_extremos"
ruta_parametros = r"C:\Users\jaime\Documents\UNIVERSIDAD\TFG\Metodologia_srs\parametros.csv"

# === CARGA PARÁMETROS PARA LOCALIZAR RUNS EXTREMOS DE TRACK_VOXEL_RATIO ===
param_df = pd.read_csv(ruta_parametros)
min_idx = param_df['track_voxel_ratio'].idxmin()
max_idx = param_df['track_voxel_ratio'].idxmax()
run_min = int(param_df.loc[min_idx, 'run'])
run_max = int(param_df.loc[max_idx, 'run'])

# === CARGAR MATRICES ===
def cargar_matriz(run):
    nombre = f"matrix_{run:02d}.txt.HCP-MMP.count.pass.connectivity.mat"
    ruta = os.path.join(ruta_matrices, nombre)
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"Archivo no encontrado: {ruta}")
    mat = loadmat(ruta)
    return mat["connectivity"]

mat_min = cargar_matriz(run_min)
mat_max = cargar_matriz(run_max)

# === CÁLCULO DE DIFERENCIAS ===
epsilon = 1e-5  # para evitar división por cero
diff_abs = mat_max - mat_min
diff_rel = (mat_max - mat_min) / (mat_min + epsilon) * 100

# === GUARDAR HEATMAPS ===
def guardar_heatmap(matriz, titulo, nombre_archivo):
    plt.figure(figsize=(10, 8))
    plt.imshow(matriz, cmap='bwr', interpolation='nearest')
    plt.title(titulo)
    plt.colorbar(label='Valor')
    plt.xlabel("Región destino")
    plt.ylabel("Región origen")
    plt.tight_layout()
    plt.savefig(os.path.join(ruta_output, nombre_archivo), dpi=300)
    plt.close()
    print(f"Guardado heatmap: {nombre_archivo}")

guardar_heatmap(diff_abs, f"Diferencia absoluta - track_voxel_ratio", "diff_abs_track_voxel.png")
guardar_heatmap(diff_rel, f"Diferencia relativa (%) - track_voxel_ratio", "diff_rel_track_voxel.png")

# === ESTADÍSTICAS RESUMEN ===
estadisticas = {
    "Tipo": ["Absoluta", "Relativa (%)"],
    "Máximo": [np.max(diff_abs), np.max(diff_rel)],
    "Media": [np.mean(diff_abs), np.mean(diff_rel)],
    "Desviación típica": [np.std(diff_abs), np.std(diff_rel)],
    "Celdas > 10 (abs)": [np.sum(diff_abs > 10), np.nan],
    "Celdas > 50% (rel)": [np.nan, np.sum(diff_rel > 50)]
}
df_estadisticas = pd.DataFrame(estadisticas)

# Guardar CSV
csv_path = os.path.join(ruta_output, "resumen_diferencias_track_voxel.csv")
df_estadisticas.to_csv(csv_path, index=False)
print(f"Estadísticas guardadas en: {csv_path}")

print("Comparación completada.")
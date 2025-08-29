import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# === CONFIGURACIÓN DE RUTAS ===
ruta_parametros = r"C:\Users\jaime\Documents\UNIVERSIDAD\TFG\Metodologia_srs\parametros.csv"
ruta_matrices = r"C:\Users\jaime\Documents\UNIVERSIDAD\TFG\Metodologia_srs\matrices"
ruta_output = r"C:\Users\jaime\Documents\UNIVERSIDAD\TFG\Resultados\scripts\matrices_extremos"

# Crear carpeta de salida si no existe
os.makedirs(ruta_output, exist_ok=True)

# === CARGA DE PARÁMETROS ===
param_df = pd.read_csv(ruta_parametros)

# Buscar el mínimo y máximo turning_angle
min_idx = param_df['turning_angle'].idxmin()
max_idx = param_df['turning_angle'].idxmax()

runs_extremos = {
    'min_angle': (int(param_df.loc[min_idx, 'run']), param_df.loc[min_idx, 'turning_angle']),
    'max_angle': (int(param_df.loc[max_idx, 'run']), param_df.loc[max_idx, 'turning_angle'])
}

# === CARGA DE MATRICES Y CÁLCULO DE RANGO GLOBAL ===
matrices = {}
valores_totales = []

for etiqueta, (run, valor_angle) in runs_extremos.items():
    file_name = f"matrix_{run:02d}.txt.HCP-MMP.count.pass.connectivity.mat"
    file_path = os.path.join(ruta_matrices, file_name)

    if not os.path.exists(file_path):
        print(f"Archivo no encontrado: {file_path}")
        continue

    mat_data = loadmat(file_path)
    if "connectivity" not in mat_data:
        print(f"'connectivity' no encontrado en {file_name}")
        continue

    matriz = mat_data["connectivity"]
    matrices[etiqueta] = (matriz, run, valor_angle)
    valores_totales.append(matriz)

# Determinar el valor mínimo y máximo global
valores_concat = np.concatenate([m.flatten() for m in valores_totales])
vmin = valores_concat.min()
vmax = valores_concat.max()

# === GRAFICAR HEATMAPS CON ESCALA COMÚN ===
for etiqueta, (matriz, run, valor_angle) in matrices.items():
    plt.figure(figsize=(10, 8))  # usa el mismo en histogramas y heatmaps
    plt.imshow(matriz, cmap='hot', interpolation='nearest', vmin=vmin, vmax=vmax)

    etiqueta_formateada = "Máx" if "max" in etiqueta else "Mín"
    titulo = f"{etiqueta_formateada} turning_angle ({valor_angle:.0f}°)"
    plt.title(titulo)

    plt.colorbar(label='Número de conexiones')
    plt.xlabel("Región destino")
    plt.ylabel("Región origen")

    nombre_salida = f"heatmap_{etiqueta}_angle_run{run:02d}.png"
    plt.tight_layout()
    plt.savefig(os.path.join(ruta_output, nombre_salida), dpi=300)
    plt.close()
    print(f"Heatmap con escala común guardado: {nombre_salida}")

print("Proceso completado.")
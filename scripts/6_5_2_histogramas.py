import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

# CONFIGURACIÓN
carpeta_scripts = os.path.dirname(__file__)
carpeta_srs = os.path.abspath(os.path.join(carpeta_scripts, "..", "..", "Metodologia_srs", "matrices"))
carpeta_lhs = os.path.abspath(os.path.join(carpeta_scripts, "..", "..", "Metodologia_lhs", "matrices"))
archivo_indices = "indices_regiones_clave.csv"
carpeta_salida = os.path.join(carpeta_scripts, "histogramas_conexiones")
os.makedirs(carpeta_salida, exist_ok=True)

# Cargar índices
df_indices = pd.read_csv(archivo_indices)
regiones = df_indices["Region"].tolist()
indices = df_indices["Indice"].tolist()

# Generar combinaciones únicas (sin repeticiones)
parejas = []
for i in range(len(indices)):
    for j in range(i + 1, len(indices)):
        if "NOT FOUND" not in [indices[i], indices[j]]:
            parejas.append((regiones[i], regiones[j], int(indices[i]), int(indices[j])))

# Función auxiliar

def cargar_matriz_sujeto(carpeta, i):
    base_name = f"matrix_{i:02d}.txt.HCP-MMP.count.pass.connectivity.mat"
    ruta = os.path.join(carpeta, base_name)
    mat = loadmat(ruta)
    return mat["connectivity"]

# Graficar histogramas
def generar_histogramas(metodo, carpeta):
    for (reg1, reg2, i, j) in parejas:
        valores = []
        for n in range(1, 51):
            matriz = cargar_matriz_sujeto(carpeta, n)
            valores.append(matriz[i, j])

        plt.figure(figsize=(6, 4))
        plt.hist(valores, bins=20, color="#4C72B0", alpha=0.75)
        plt.title(f"Histograma de conexión {reg1} - {reg2} ({metodo})")
        plt.xlabel("Valor de conectividad")
        plt.ylabel("Frecuencia")
        plt.tight_layout()
        nombre_archivo = f"hist_{metodo}_{reg1}_{reg2}.png".replace("/", "_")
        plt.savefig(os.path.join(carpeta_salida, nombre_archivo), dpi=300)
        plt.close()

# Ejecutar para ambos métodos
generar_histogramas("SRS", carpeta_srs)
generar_histogramas("LHS", carpeta_lhs)

print("Histogramas generados y guardados correctamente.")
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression
import os

# --- Configuración ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ruta_srs = os.path.join(BASE_DIR, "Metodologia_srs", "resumen.csv")
ruta_lhs = os.path.join(BASE_DIR, "Metodologia_lhs", "resumen.csv")
salida = os.path.join(os.path.dirname(__file__), "sensibilidad_prcc.csv")

# Variables
inputs = ["fa_threshold", "turning_angle", "track_voxel_ratio"]
outputs = [
    "n_tractos_reales", "media_conectividad", "desviacion_tipica",
    "n_conexiones", "coef_variacion", "densidad_relativa"
]

def calcular_prcc(df, metodo):
    df_rank = df[inputs + outputs].rank()
    prcc_resultados = []

    for y in outputs:
        for x in inputs:
            otros_inputs = [var for var in inputs if var != x]

            # Regresión de X respecto a los otros inputs
            modelo_x = LinearRegression().fit(df_rank[otros_inputs], df_rank[x])
            resid_x = df_rank[x] - modelo_x.predict(df_rank[otros_inputs])

            # Regresión de Y respecto a los otros inputs
            modelo_y = LinearRegression().fit(df_rank[otros_inputs], df_rank[y])
            resid_y = df_rank[y] - modelo_y.predict(df_rank[otros_inputs])

            # Correlación entre residuos
            rho, _ = spearmanr(resid_x, resid_y)

            prcc_resultados.append({
                "Método": metodo,
                "Input": x,
                "Output": y,
                "PRCC": rho
            })

    return pd.DataFrame(prcc_resultados)

# Ejecutar para ambos métodos
df_srs = pd.read_csv(ruta_srs)
df_lhs = pd.read_csv(ruta_lhs)

tabla_srs = calcular_prcc(df_srs, "SRS")
tabla_lhs = calcular_prcc(df_lhs, "LHS")
tabla_total = pd.concat([tabla_srs, tabla_lhs])

# Exportar
tabla_total.to_csv(salida, index=False)
print("Tabla PRCC guardada como 'sensibilidad_prcc.csv'")
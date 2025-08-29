import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
import os

# Rutas
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
srs_path = os.path.join(BASE_DIR, "Metodologia_srs", "resumen.csv")
lhs_path = os.path.join(BASE_DIR, "Metodologia_lhs", "resumen.csv")
output_dir = os.path.dirname(__file__)
os.makedirs(output_dir, exist_ok=True)

# Variables a analizar (ampliadas)
variables = [
    "n_tractos_reales",
    "media_conectividad",
    "n_conexiones",
    "desviacion_tipica",
    "coef_variacion"
]

# Cargar datos
datos = {
    "SRS": pd.read_csv(srs_path),
    "LHS": pd.read_csv(lhs_path)
}

# Inicializar resultados
resultados = []

# Función para contar outliers (IQR de Tukey)
def contar_outliers(serie):
    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    iqr = q3 - q1
    outliers = ((serie < q1 - 1.5 * iqr) | (serie > q3 + 1.5 * iqr)).sum()
    return outliers, outliers / len(serie)

# Calcular estadísticas
for metodo, df in datos.items():
    for var in variables:
        x = df[var].dropna()
        outliers_abs, outliers_pct = contar_outliers(x)
        resultados.append({
            "Método": metodo,
            "Variable": var,
            "Asimetría": round(skew(x), 3),
            "Curtosis": round(kurtosis(x), 3),  # Fisher=True por defecto → curtosis normal = 0
            "Outliers absolutos": outliers_abs,
            "% outliers": round(100 * outliers_pct, 1)
        })

# Exportar
df_resultados = pd.DataFrame(resultados)
df_resultados.to_csv(os.path.join(output_dir, "curtosis_asimetria_outliers.csv"), index=False)

print("Estadísticas de asimetría, curtosis y outliers generadas.")
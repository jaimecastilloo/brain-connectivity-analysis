import pandas as pd
import numpy as np
import os

# CONFIGURACIÓN
tipo = "lhs"  # Cambia a "srs" para trabajar con SRS
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ruta_csv = os.path.join(BASE_DIR, f"Metodologia_{tipo}", "resumen.csv")
carpeta_salida = os.path.join(os.path.dirname(__file__), f"incertidumbre_{tipo}")
os.makedirs(carpeta_salida, exist_ok=True)

# Leer datos
df = pd.read_csv(ruta_csv)

# Variables de salida a analizar
variables = [
    "n_tractos_reales",
    "media_conectividad",
    "desviacion_tipica",
    "n_conexiones",
    "coef_variacion",
    "densidad_relativa"
]

# Calcular estadísticas
resumen = []

for var in variables:
    serie = df[var]
    media = serie.mean()
    std = serie.std()
    p5 = np.percentile(serie, 5)
    p95 = np.percentile(serie, 95)
    resumen.append({
        "Variable": var,
        "Media": round(media, 3),
        "Desviación típica": round(std, 3),
        "CV": round(std / media, 3),
        "P5": round(p5, 3),
        "P95": round(p95, 3),
        "Rango 90%": round(p95 - p5, 3)
    })

# Guardar resultados
df_resumen = pd.DataFrame(resumen)
df_resumen.to_csv(os.path.join(carpeta_salida, "propagacion_incertidumbre.csv"), index=False)
print(f"Resultados de propagación de incertidumbre ({tipo.upper()}) guardados correctamente.")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# CONFIGURACIÓN
tipo = "lhs"  # Cambia a "lhs" si quieres trabajar con los datos de LHS
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ruta_csv = os.path.join(BASE_DIR, f"Metodologia_{tipo}", "resumen.csv")
carpeta_salida = os.path.join(os.path.dirname(__file__), f"output_{tipo}")
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

# Tabla estadística resumen
resumen = []

for var in variables:
    serie = df[var]
    resumen.append({
        "Variable": var,
        "Media": round(serie.mean(), 3),
        "Desviación típica": round(serie.std(), 3),
        "Mínimo": round(serie.min(), 3),
        "Máximo": round(serie.max(), 3),
        "Rango": round(serie.max() - serie.min(), 3),
        "Coef. de variación": round(serie.std() / serie.mean(), 3)
    })

# Guardar tabla resumen
df_resumen = pd.DataFrame(resumen)
df_resumen.to_csv(os.path.join(carpeta_salida, "estadisticas_outputs_globales.csv"), index=False)

# Histogramas y boxplots
for var in variables:
    sns.histplot(df[var], kde=True, bins=20, color="steelblue")
    plt.title(f"Histograma de {var} ({tipo.upper()})")
    plt.xlabel(var)
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta_salida, f"hist_{var}.png"))
    plt.close()

    sns.boxplot(data=df, x=var, color="tomato")
    plt.title(f"Boxplot de {var} ({tipo.upper()})")
    plt.tight_layout()
    plt.savefig(os.path.join(carpeta_salida, f"box_{var}.png"))
    plt.close()

print(f"Estadísticas y gráficas descriptivas ({tipo.upper()}) generadas correctamente.")
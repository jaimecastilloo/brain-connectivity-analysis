import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Crear DataFrame con los valores PRCC principales
data = {
    "Output": [
        "n_tractos_reales", "n_tractos_reales",
        "media_conectividad", "media_conectividad",
        "desviacion_tipica", "desviacion_tipica",
        "n_conexiones", "n_conexiones",
        "coef_variacion", "coef_variacion",
        "densidad_relativa", "densidad_relativa"
    ],
    "Método": ["SRS", "LHS"] * 6,
    "PRCC": [
        -0.991, -0.995,
        -0.990, -0.994,
        -0.986, -0.990,
        -0.994, -0.996,
        0.993, 0.996,
        -0.994, -0.996
    ]
}

df = pd.DataFrame(data)

# Crear gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Output", y="PRCC", hue="Método", palette=["#4C72B0", "#55A868"])
plt.axhline(0, color='black', linewidth=0.8)
plt.xticks(rotation=30)
plt.ylim(-1.1, 1.1)
plt.title("Coeficientes PRCC por output y método")
plt.tight_layout()

# Guardar figura
carpeta_salida = os.path.dirname(__file__)
ruta_figura = os.path.join(carpeta_salida, "prcc_barplot_output_vs_metodo.png")
plt.savefig(ruta_figura, dpi=300)
print(f"Figura guardada como: {ruta_figura}")
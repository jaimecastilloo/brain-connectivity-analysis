import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Rutas base
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
srs_path = os.path.join(BASE_DIR, "Metodologia_srs", "resumen.csv")
lhs_path = os.path.join(BASE_DIR, "Metodologia_lhs", "resumen.csv")
output_dir = os.path.dirname(__file__)
os.makedirs(output_dir, exist_ok=True)

# Cargar datos
df_srs = pd.read_csv(srs_path)
df_lhs = pd.read_csv(lhs_path)

# Añadir columna identificadora
df_srs["Método"] = "SRS"
df_lhs["Método"] = "LHS"

# Unir dataframes
df = pd.concat([df_srs, df_lhs], ignore_index=True)

# Variables a graficar
variables = ["n_tractos_reales", "media_conectividad", "n_conexiones"]
titulos = [
    "A) Número total de tractos",
    "B) Conectividad media",
    "C) Número de conexiones no nulas"
]

# Crear figura
plt.figure(figsize=(15, 5))

for i, (var, titulo) in enumerate(zip(variables, titulos), 1):
    plt.subplot(1, 3, i)
    sns.boxplot(data=df, x="Método", y=var, palette=["#4C72B0", "#55A868"])
    plt.title(titulo)
    plt.xlabel("")
    plt.ylabel("")
    plt.grid(True)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "boxplots_comparativos_srs_lhs.png"))
plt.close()

print("Figura comparativa guardada como 'boxplots_comparativos_srs_lhs.png'")
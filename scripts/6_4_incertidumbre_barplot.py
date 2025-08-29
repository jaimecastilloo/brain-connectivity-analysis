import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Leer los CSVs
BASE_DIR = os.path.dirname(__file__)
srs = pd.read_csv(os.path.join(BASE_DIR, "incertidumbre_srs", "propagacion_incertidumbre.csv"))
lhs = pd.read_csv(os.path.join(BASE_DIR, "incertidumbre_lhs", "propagacion_incertidumbre.csv"))

# Añadir columna para identificar el método
srs["Método"] = "SRS"
lhs["Método"] = "LHS"
df = pd.concat([srs, lhs], ignore_index=True)

# Calcular rango relativo: (Rango 90%) / P95
df["Rango relativo"] = df["Rango 90%"] / df["P95"]

# Crear gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Variable", y="Rango relativo", hue="Método", palette=["#4C72B0", "#55A868"])
plt.title("Rango 90 % relativo (normalizado por P95) por variable y método")
plt.ylabel("Rango 90 % / P95")
plt.xlabel("Variable")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()

# Guardar figura
ruta_salida = os.path.join(BASE_DIR, "rango_90_relativo_normalizado.png")
plt.savefig(ruta_salida, dpi=300)
plt.close()

print(f"Figura guardada como: {ruta_salida}")
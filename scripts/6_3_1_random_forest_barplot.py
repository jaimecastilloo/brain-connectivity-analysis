import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Cargar CSV
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
csv_path = os.path.join(BASE_DIR, "scripts", "importancia_random_forest.csv")
df = pd.read_csv(csv_path)

# Ajustar orden y colores si se desea
orden_inputs = ["fa_threshold", "track_voxel_ratio", "turning_angle"]
colores = {
    "fa_threshold": "#4C72B0",
    "track_voxel_ratio": "#55A868",
    "turning_angle": "#C44E52"
}

# Crear gráfico
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Output", y="Importancia", hue="Input", hue_order=orden_inputs, palette=colores)

# Estética
plt.title("Importancia relativa de cada input por Random Forest")
plt.ylabel("Importancia")
plt.xlabel("Output")
plt.legend(title="Input")
plt.tight_layout()

# Guardar figura
fig_path = os.path.join(BASE_DIR, "scripts", "barplot_importancia_random_forest.png")
plt.savefig(fig_path, dpi=300)
plt.close()
print(f"Figura guardada como {fig_path}")
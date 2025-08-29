import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestRegressor

# Rutas
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
csv_path = os.path.join(BASE_DIR, "Metodologia_lhs", "resumen.csv")  # ← usar LHS

# Cargar datos
df = pd.read_csv(csv_path)

# Variables de entrada y salidas
X = df[["fa_threshold", "turning_angle", "track_voxel_ratio"]]
outputs = ["n_tractos_reales", "media_conectividad", "desviacion_tipica", "n_conexiones"]

# Ajustar un modelo por output y guardar importancias
importancias = []
for output in outputs:
    y = df[output]
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X, y)
    for i, param in enumerate(X.columns):
        importancias.append({
            "Output": output,
            "Input": param,
            "Importancia": model.feature_importances_[i]
        })

# Guardar como CSV
df_import = pd.DataFrame(importancias)
output_path = os.path.join(os.path.dirname(__file__), "importancia_random_forest.csv")
df_import.to_csv(output_path, index=False)
print(f"Importancias guardadas en: {output_path}")
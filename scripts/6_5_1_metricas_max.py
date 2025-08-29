import numpy as np
import os
import csv

# Archivo de salida en la misma carpeta del script
output_file = os.path.join(os.getcwd(), "min_max.csv")

# Abrimos el CSV para escritura
with open(output_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    # Cabecera
    writer.writerow(["Tipo", "Métrica", "Min", "Max"])
    
    # Recorremos tipos y métricas
    for tipo in ["srs", "lhs"]:
        path = f"output_por_celda_{tipo}"
        
        for nombre in ["media", "std", "cv"]:
            matriz = np.load(f"{path}/{nombre}.npy")
            writer.writerow([tipo.upper(), nombre.upper(), f"{matriz.min():.3f}", f"{matriz.max():.3f}"])

print(f"Resultados guardados en {output_file}")
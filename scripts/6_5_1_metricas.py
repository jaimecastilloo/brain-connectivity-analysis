import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# === CONFIGURACIÓN ===
tipo = "lhs"  # Cambia a "lhs" si deseas trabajar con los datos LHS
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
matrices_dir = os.path.join(BASE_DIR, f"Metodologia_{tipo}", "matrices")
output_dir = os.path.join(BASE_DIR, "Resultados", "Scripts", f"output_por_celda_{tipo}")
os.makedirs(output_dir, exist_ok=True)

# === LÍMITES DE COLOR FIJOS ===
VMIN_VMAX = {
    "media": (0, 3250),
    "std":   (0, 1550),
    "cv":    (0, 7),
}

# === CARGA DE MATRICES ===
matrices = []
for i in range(1, 51):
    nombre_archivo = f"matrix_{i:02d}.txt.HCP-MMP.count.pass.connectivity.mat"
    ruta = os.path.join(matrices_dir, nombre_archivo)
    if os.path.exists(ruta):
        mat = loadmat(ruta)
        matrices.append(mat["connectivity"])
    else:
        print(f"❌ No encontrado: {ruta}")

if len(matrices) == 0:
    raise FileNotFoundError(f"No se encontraron matrices en {matrices_dir}")

# Convertir a array 3D: (R, N, N)
data = np.array(matrices)

# Calcular estadísticas por celda
media = np.mean(data, axis=0)
std = np.std(data, axis=0)
cv = np.divide(std, media, out=np.zeros_like(std), where=media != 0)

# Guardar como .npy
np.save(os.path.join(output_dir, "media.npy"), media)
np.save(os.path.join(output_dir, "std.npy"), std)
np.save(os.path.join(output_dir, "cv.npy"), cv)

# Guardar heatmaps (con escalas fijas)
def save_heatmap(matrix, title, filename, vmin=None, vmax=None):
    plt.figure(figsize=(10, 8))
    plt.imshow(matrix, cmap="hot", interpolation="nearest", vmin=vmin, vmax=vmax)
    plt.colorbar()
    plt.title(title)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, filename), dpi=200)
    plt.close()

save_heatmap(media, f"Media de conectividad ({tipo.upper()})", "media_heatmap.png",
             *VMIN_VMAX["media"])
save_heatmap(std, f"Desviación típica ({tipo.upper()})", "std_heatmap.png",
             *VMIN_VMAX["std"])
save_heatmap(cv, f"Coeficiente de variación ({tipo.upper()})", "cv_heatmap.png",
             *VMIN_VMAX["cv"])

print(f"Estadísticas por celda y heatmaps guardados en: {output_dir}")
print("Límites usados:")
print(f"  Media: vmin={VMIN_VMAX['media'][0]}, vmax={VMIN_VMAX['media'][1]}")
print(f"  STD: vmin={VMIN_VMAX['std'][0]},   vmax={VMIN_VMAX['std'][1]}")
print(f"  CV: vmin={VMIN_VMAX['cv'][0]},    vmax={VMIN_VMAX['cv'][1]}")
# Brain Connectivity Analysis – Statistical Exploration

Este repositorio contiene los **scripts en Python** y los **resultados** asociados al análisis estadístico y la visualización de tractografía cerebral, en el contexto de un estudio de conectividad estructural.

## 📂 Estructura del repositorio

resultados/ # Resultados organizados por apartados del análisis (capítulo 6)

scripts/ # Scripts en Python para generar los resultados

- **6_1_descriptiva**: estadísticas descriptivas globales (boxplots, histogramas, curtosis, asimetría, outliers).  
- **6_2_entrada_salida**: relación entre parámetros de entrada y outputs globales (correlaciones, scatter plots, regresiones, colinealidad).  
- **6_3_sensibilidad**: análisis de sensibilidad mediante PRCC y Random Forest.  
- **6_4_incertidumbre**: propagación de incertidumbres y visualización de rangos.  
- **6_5_por_celda**: análisis por conexión individual (matrices de medias, desviaciones, CV; histogramas por conexión).  
- **6_6_extremos**: estudio de casos extremos (máximos y mínimos de parámetros) y comparación de matrices.  
- **6_7_espacio**: exploración del espacio de muestreo (representaciones 1D, 2D y 3D).  

Los **scripts** reproducen cada apartado del análisis y generan automáticamente tablas (`.csv`) y figuras (`.png`) dentro de las carpetas correspondientes.

---

## ▶️ Ejecución

1. Clonar el repositorio o descargar el contenido:  
   ```bash
   git clone https://github.com/tu_usuario/brain-connectivity-analysis.git
   cd brain-connectivity-analysis

2. Instalar las dependencias principales (Python 3.8+):
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn

4. Ejecutar los scripts desde la carpeta scripts/.
   ```bash
   python scripts/6_1_descriptiva.py

Cada script genera automáticamente los gráficos y tablas en su subcarpeta de resultados/.

## 📊 Contenido destacado
- Boxplots e histogramas comparativos (SRS vs LHS).
- Correlaciones de Pearson y Spearman entre parámetros y outputs.
- Regresiones lineales y análisis de colinealidad.
- Análisis de sensibilidad mediante PRCC y Random Forest.
- Propagación de incertidumbres.
- Mapas de calor y métricas por conexión.
- Exploración del espacio de parámetros en 1D, 2D y 3D.

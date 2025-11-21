import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Configuración Visual ---
# Establece un tema gráfico consistente y agradable para todas las visualizaciones.
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams['font.family'] = 'sans-serif'

# --- 1. Cargar Datos ---
# Nombre del archivo CSV que subiste.
file_name = 'E:\DIPLOMANDO - ANALÍTICA DE DATOS EN LA GESTIÓN EMPRESARIAL\Actividad 2 - Planteamiento de Proyecto (Parte 1)\SECTORES_CRITICOS_DE_SINIESTRALIDAD_VIAL_20251022.csv'

try:
    df = pd.read_csv(file_name)
    print(f"Archivo '{file_name}' cargado exitosamente.")
except Exception as e:
    print(f"Error fatal al leer el archivo {file_name}: {e}")
    # Si no se puede leer el archivo, se detiene la ejecución.
    exit()

# --- 2. Inspección (Opcional, pero buena práctica) ---
print("\n--- Información del DataFrame ---")
df.info()


# --- 3. Generación de Gráficos (Plan Ajustado) ---

# --- Gráfico 1: Top 10 Municipios por Total de Fallecidos ---
# Verifica que las columnas necesarias existan
if 'Municipio' in df.columns and 'Fallecidos' in df.columns:
    try:
        # 1. Agrupa por 'Municipio'
        # 2. Suma los 'Fallecidos' para cada municipio
        # 3. Selecciona los 10 más altos (nlargest)
        municipios_fallecidos = df.groupby('Municipio')['Fallecidos'].sum().nlargest(10)
        
        plt.figure(figsize=(12, 7))
        # Crea un gráfico de barras horizontal (barh)
        ax = municipios_fallecidos.plot(kind='barh', color=sns.color_palette('rocket_r', 10))
        
        # --- Títulos y Etiquetas ---
        ax.set_title('Top 10 Municipios por Total de Fallecidos en Sectores Críticos', fontsize=16, weight='bold')
        ax.set_xlabel('Total de Fallecidos', fontsize=12)
        ax.set_ylabel('Municipio', fontsize=12)
        
        # Invierte el eje Y para que el municipio con más fallecidos quede arriba
        ax.invert_yaxis() 
        
        # --- Añadir Etiquetas de Valor ---
        # Itera sobre cada barra (patch) para poner su valor al lado
        for i in ax.patches:
            ax.text(i.get_width() + 0.2, # Posición X (ancho de la barra + un margen)
                    i.get_y() + i.get_height() / 2, # Posición Y (centro vertical de la barra)
                    f'{int(i.get_width())}', # El texto a mostrar (el valor numérico)
                    va='center', ha='left', fontsize=10)
            
        plt.tight_layout() # Ajusta el gráfico para que no se corten las etiquetas
        plt.savefig('top_10_municipios_fallecidos.png') # Guarda el gráfico como imagen
        print("Gráfico 'top_10_municipios_fallecidos.png' generado.")
        
    except Exception as e:
        print(f"Error al generar 'top_10_municipios_fallecidos.png': {e}")
else:
    print("Faltan las columnas 'Municipio' o 'Fallecidos' para el Gráfico 1.")

# --- Gráfico 2: Total de Fallecidos por Entidad ---
if 'ENTIDAD' in df.columns and 'Fallecidos' in df.columns:
    try:
        # 1. Agrupa por 'ENTIDAD'
        # 2. Suma los 'Fallecidos'
        # 3. Ordena los valores de mayor a menor
        entidad_fallecidos = df.groupby('ENTIDAD')['Fallecidos'].sum().sort_values(ascending=False)
        
        plt.figure(figsize=(10, 6))
        # Crea un gráfico de barras vertical (barplot)
        ax = sns.barplot(x=entidad_fallecidos.index, y=entidad_fallecidos.values, palette='viridis')
        
        # --- Títulos y Etiquetas ---
        ax.set_title('Total de Fallecidos por Entidad Administradora', fontsize=16, weight='bold')
        ax.set_xlabel('Entidad', fontsize=12)
        ax.set_ylabel('Total de Fallecidos', fontsize=12)
        plt.xticks(rotation=45) # Rota las etiquetas del eje X para mejor lectura
        
        # --- Añadir Etiquetas de Valor ---
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}', # El texto a mostrar (altura de la barra)
                        (p.get_x() + p.get_width() / 2., p.get_height()), # Posición (centro X, altura Y)
                        ha='center', va='center', 
                        xytext=(0, 9), # Desplazamiento vertical de 9 puntos
                        textcoords='offset points',
                        fontsize=10)
            
        plt.tight_layout()
        plt.savefig('fallecidos_por_entidad.png')
        print("Gráfico 'fallecidos_por_entidad.png' generado.")
        
    except Exception as e:
        print(f"Error al generar 'fallecidos_por_entidad.png': {e}")
else:
    print("Faltan las columnas 'ENTIDAD' o 'Fallecidos' para el Gráfico 2.")

# --- Gráfico 3: Distribución de "Intensidad" (GiZScore) ---
if 'GiZScore' in df.columns:
    try:
        plt.figure(figsize=(10, 6))
        # Crea un histograma (distribución) de la columna 'GiZScore'
        # kde=True añade una línea de estimación de densidad
        ax = sns.histplot(df['GiZScore'], kde=True, bins=20, color='blue')
        
        # --- Títulos y Etiquetas ---
        ax.set_title('Distribución del Nivel de Intensidad (GiZScore)', fontsize=16, weight='bold')
        ax.set_xlabel('GiZScore (Intensidad del Hotspot)', fontsize=12)
        ax.set_ylabel('Frecuencia (Nº de Sectores)', fontsize=12)
        
        # --- Línea de Referencia ---
        # Añade una línea vertical en Z=1.96, que es el umbral estándar
        # para una significancia estadística del 95%.
        plt.axvline(x=1.96, color='red', linestyle='--', label='Significancia 95% (Z=1.96)')
        plt.legend() # Muestra la leyenda de la línea roja
        
        plt.tight_layout()
        plt.savefig('distribucion_gizscore.png')
        print("Gráfico 'distribucion_gizscore.png' generado.")
        
    except Exception as e:
        print(f"Error al generar 'distribucion_gizscore.png': {e}")
else:
    print("Falta la columna 'GiZScore' para el Gráfico 3.")

# --- Gráfico 4: Mapa de Puntos Calientes (Hotspots) ---
if 'Longitud' in df.columns and 'Latitud' in df.columns and 'Fallecidos' in df.columns and 'GiZScore' in df.columns:
    try:
        plt.figure(figsize=(10, 10))
        
        # Crea un gráfico de dispersión (scatter plot)
        ax = sns.scatterplot(
            data=df,
            x='Longitud',        # Eje X
            y='Latitud',         # Eje Y
            hue='GiZScore',      # El color del punto se basa en el 'GiZScore'
            size='Fallecidos',   # El tamaño del punto se basa en 'Fallecidos'
            sizes=(50, 1000),    # Rango de tamaños (mínimo, máximo)
            palette='coolwarm',  # Paleta de color: Azul (frío) a Rojo (caliente)
            alpha=0.7,           # Transparencia de los puntos
            edgecolor='black'    # Borde de los puntos
        )
        
        # --- Títulos y Etiquetas ---
        ax.set_title('Mapa de Sectores Críticos de Siniestralidad', fontsize=16, weight='bold')
        ax.set_xlabel('Longitud', fontsize=12)
        ax.set_ylabel('Latitud', fontsize=12)
        
        # --- Ajuste de Leyenda ---
        # Mueve la leyenda fuera del área del gráfico para no tapar puntos
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
        
        # Ajusta el layout para dejar espacio a la leyenda (rect=[left, bottom, right, top])
        plt.tight_layout(rect=[0, 0, 0.85, 1]) 
        
        plt.savefig('mapa_hotspots.png')
        print("Gráfico 'mapa_hotspots.png' generado.")
        
    except Exception as e:
        print(f"Error al generar 'mapa_hotspots.png': {e}")
else:
    print("Faltan 'Longitud', 'Latitud', 'Fallecidos' o 'GiZScore' para el Gráfico 4.")

print("\nProceso de generación de gráficos completado.")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings

# --- Configuración Inicial ---
warnings.filterwarnings('ignore') # Suprimir advertencias
sns.set_theme(style="whitegrid") # Estilo bonito para los gráficos
file_name = "E:\DIPLOMANDO - ANALÍTICA DE DATOS EN LA GESTIÓN EMPRESARIAL\Actividad 3 - Creando un Storytelling con Datos\Resultados_únicos_Saber_11_20251020.csv" # El archivo de 3GB

# --- 1. PROCESAMIENTO POR TROZOS (CHUNKS) ---
# Esto es necesario para el archivo de 3GB

print(f"Iniciando procesamiento del archivo grande: {file_name}")
print("Esto puede tardar varios minutos. Por favor, espera...")

chunk_size = 200000  # Leer de 200,000 en 200,000 filas
filtered_chunks = [] # Aquí guardaremos los pedazos que nos sirven

# Definimos los filtros que planeamos en la Actividad 1
# ¡IMPORTANTE! Asegúrate que los nombres coincidan con los datos.
# Los nombres en mayúsculas son los estándar del ICFES.
ciudades_principales = ['BOGOTÁ D.C.', 'MEDELLÍN', 'CALI', 'BARRANQUILLA', 'CARTAGENA']
naturaleza_tipos = ['OFICIAL', 'NO OFICIAL']

# Definimos las columnas que SÍ necesitamos para reducir el uso de memoria
columnas_necesarias = [
    'PUNT_GLOBAL', 
    'COLE_NATURALEZA', 
    'FAMI_ESTRATOVIVIENDA',
    'COLE_MCPIO_UBICACION',
    'PERIODO' # Usaremos esta para filtrar el año más reciente
]

# Iniciamos el iterador para leer el archivo por trozos
try:
    iterator = pd.read_csv(
        file_name, 
        sep=',',  # Los CSV de datos.gov.co suelen usar ','
        chunksize=chunk_size, 
        low_memory=False,
        usecols=columnas_necesarias # Solo carga las columnas que necesitamos
    )
except ValueError:
    # Si 'usecols' falla (quizás un nombre cambió), lo reintentamos cargando todo
    print("Advertencia: No se pudieron pre-filtrar columnas. Reintentando carga completa de chunks.")
    iterator = pd.read_csv(
        file_name, 
        sep=',',
        chunksize=chunk_size, 
        low_memory=False
    )
except Exception as e:
    print(f"Error fatal al leer el CSV. ¿Estás seguro que el separador es ','?")
    print(f"Error: {e}")
    iterator = None


if iterator:
    for chunk in iterator:
        # --- Aplicamos los filtros a cada trozo ---
        
        # 1. Normalizar texto para la limpieza
        chunk['COLE_MCPIO_UBICACION'] = chunk['COLE_MCPIO_UBICACION'].str.upper().str.strip()
        chunk['COLE_NATURALEZA'] = chunk['COLE_NATURALEZA'].str.upper().str.strip()
        
        # 2. Filtrar
        chunk_filtrado = chunk[
            (chunk['COLE_MCPIO_UBICACION'].isin(ciudades_principales)) &
            (chunk['COLE_NATURALEZA'].isin(naturaleza_tipos))
        ]
        
        # 3. Guardar el trozo filtrado
        filtered_chunks.append(chunk_filtrado)

    print("Procesamiento de chunks terminado.")

    # --- 2. CONSOLIDACIÓN Y LIMPIEZA FINAL ---
    print("Consolidando datos filtrados...")
    
    # Unimos todos los trozos pequeños en un solo DataFrame
    df_ciudades = pd.concat(filtered_chunks, ignore_index=True)

    # Liberamos memoria
    del filtered_chunks
    del iterator
    
    # Filtramos el año más reciente disponible en los datos
    # (El plan decía "la publicación más reciente")
    if 'PERIODO' in df_ciudades.columns:
        año_mas_reciente = df_ciudades['PERIODO'].max()
        print(f"Datos consolidados. Filtrando por el año más reciente: {año_mas_reciente}")
        df_ciudades = df_ciudades[df_ciudades['PERIODO'] == año_mas_reciente].copy()
    else:
        print("No se encontró columna 'PERIODO'. Se usarán todos los años filtrados.")

    # Limpieza final de datos
    df_ciudades.dropna(subset=['PUNT_GLOBAL'], inplace=True)
    df_ciudades['PUNT_GLOBAL'] = pd.to_numeric(df_ciudades['PUNT_GLOBAL'])
    df_ciudades['FAMI_ESTRATOVIVIENDA'] = df_ciudades['FAMI_ESTRATOVIVIENDA'].fillna('SIN INFORMACION')

    print("\n--- ANÁLISIS LISTO ---")
    print(f"Total de registros para el análisis (año {año_mas_reciente}): {len(df_ciudades)}")
    print(df_ciudades['COLE_NATURALEZA'].value_counts())

    # --- 3. GENERACIÓN DE GRÁFICOS ---

    # --- Gráfica 1: Promedio Global (Barras) ---
    plt.figure(figsize=(8, 6))
    sns.barplot(
        x='COLE_NATURALEZA', y='PUNT_GLOBAL', data=df_ciudades,
        palette=['#0072B2', '#D55E00'], order=['OFICIAL', 'NO OFICIAL']
    )
    plt.title('Gráfica 1: Brecha de Rendimiento (Puntaje Promedio)', fontsize=16, fontweight='bold')
    plt.xlabel('Naturaleza del Colegio', fontsize=12)
    plt.ylabel('Puntaje Global Promedio', fontsize=12)
    plt.xticks(ticks=[0, 1], labels=['Colegios Públicos (Oficial)', 'Colegios Privados (No Oficial)'])
    plt.savefig("grafica_1_barras_promedio.png", dpi=300)
    print("Gráfica 1 (Barras) guardada como 'grafica_1_barras_promedio.png'")

    # --- Gráfica 2: Distribución (Box Plot) ---
    plt.figure(figsize=(10, 7))
    sns.boxplot(
        x='COLE_NATURALEZA', y='PUNT_GLOBAL', data=df_ciudades,
        palette=['#0072B2', '#D55E00'], order=['OFICIAL', 'NO OFICIAL']
    )
    plt.title('Gráfica 2: Distribución de Puntajes (Box Plot)', fontsize=16, fontweight='bold')
    plt.xlabel('Naturaleza del Colegio', fontsize=12)
    plt.ylabel('Puntaje Global', fontsize=12)
    plt.xticks(ticks=[0, 1], labels=['Colegios Públicos (Oficial)', 'Colegios Privados (No Oficial)'])
    plt.savefig("grafica_2_boxplot_distribucion.png", dpi=300)
    print("Gráfica 2 (Boxplot) guardada como 'grafica_2_boxplot_distribucion.png'")

    # --- Gráfica 3: Análisis por Estrato (Barras Agrupadas) ---
    
    # Ordenar los estratos para que salgan bien en la gráfica
    estrato_orden = sorted(df_ciudades['FAMI_ESTRATOVIVIENDA'].unique())
    # Mover 'SIN INFORMACION' al final si existe
    if 'SIN INFORMACION' in estrato_orden:
        estrato_orden.remove('SIN INFORMACION')
        estrato_orden.append('SIN INFORMACION')

    plt.figure(figsize=(12, 7))
    sns.barplot(
        x='FAMI_ESTRATOVIVIENDA', y='PUNT_GLOBAL', hue='COLE_NATURALEZA',
        data=df_ciudades, order=estrato_orden,
        palette=['#0072B2', '#D55E00'], hue_order=['OFICIAL', 'NO OFICIAL']
    )
    plt.title('Gráfica 3: Puntaje Promedio por Estrato y Tipo de Colegio', fontsize=16, fontweight='bold')
    plt.xlabel('Estrato Socioeconómico de la Familia', fontsize=12)
    plt.ylabel('Puntaje Global Promedio', fontsize=12)
    plt.legend(title='Tipo de Colegio', labels=['Público (Oficial)', 'Privado (No Oficial)'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafica_3_barras_estrato.png", dpi=300)
    print("Gráfica 3 (Estratos) guardada como 'grafica_3_barras_estrato.png'")
    
    # --- 4. CÁLCULO PRUEBA T-STUDENT (Para Hallazgo 3) ---
    
    puntajes_publicos = df_ciudades[df_ciudades['COLE_NATURALEZA'] == 'OFICIAL']['PUNT_GLOBAL']
    puntajes_privados = df_ciudades[df_ciudades['COLE_NATURALEZA'] == 'NO OFICIAL']['PUNT_GLOBAL']
    
    # Calcular promedios para la narrativa
    promedio_publico = puntajes_publicos.mean()
    promedio_privado = puntajes_privados.mean()

    t_statistic, p_value = stats.ttest_ind(
        puntajes_publicos, puntajes_privados, 
        equal_var=False, nan_policy='omit'
    )

    print("\n--- Resultados de la Prueba T-Student ---")
    print(f"Promedio Público (Oficial): {promedio_publico:.2f}")
    print(f"Promedio Privado (No Oficial): {promedio_privado:.2f}")
    print(f"Diferencia: {promedio_privado - promedio_publico:.2f} puntos")
    print(f"Valor P (p-value): {p_value}")

    if p_value < 0.05:
        print("Conclusión Estadística: La diferencia ES estadísticamente significativa.")
    else:
        print("Conclusión Estadística: La diferencia NO es estadísticamente significativa.")

    print("\n--- ¡Éxito! ---")
    print("Todas las gráficas han sido guardadas como archivos .png en la misma carpeta.")
    print("Usa los números y las gráficas para construir tu narrativa.")

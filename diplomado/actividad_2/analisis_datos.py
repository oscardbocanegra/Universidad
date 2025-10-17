# -*- coding: utf-8 -*-
"""
Análisis de Siniestralidad Vial en Cali (2022-2024)

Este script realiza la descarga, preparación y visualización de los datos
de siniestros viales de la ciudad de Cali, obtenidos del portal de
Datos Abiertos de Colombia.
"""

# 1. Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- Configuración de Estilo para los Gráficos ---
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Calibri'
print("Librerías importadas y estilo configurado.")

# 2. Carga y Preparación de los Datos
try:
    print("Iniciando la descarga de datos...")
    # URL del recurso en el portal de Datos Abiertos de Colombia
    url = 'https://www.datos.gov.co/resource/y34d-e4sx.json'
    
    # Se construye una URL para filtrar los datos desde el año 2022 y aumentar el límite de registros
    socrata_url = f"{url}?$limit=50000&$where=fecha_accidente between '2022-01-01T00:00:00' and '2024-12-31T23:59:59'"
    
    df = pd.read_json(socrata_url)
    print(f"Descarga completada. Se cargaron {len(df)} registros.")

    # --- Limpieza y Transformación de Datos ---
    # Convertir la columna de fecha a formato datetime
    df['fecha_accidente'] = pd.to_datetime(df['fecha_accidente'])

    # Crear nuevas columnas para el análisis temporal
    dias_semana = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}
    df['dia_semana'] = df['fecha_accidente'].dt.dayofweek.map(dias_semana)
    df['hora'] = df['fecha_accidente'].dt.hour

    # Estandarizar valores en la columna 'gravedad' para agruparlos correctamente
    df['gravedad'] = df['gravedad'].str.replace('HERIDO', 'HERIDOS', regex=False)
    df['gravedad'] = df['gravedad'].str.replace('MUERTO', 'MUERTOS', regex=False)
    
    print("Preparación de datos finalizada.")

    # 3. Generación de Gráficos

    # --- Gráfico 1: Siniestros por Día de la Semana ---
    plt.figure(figsize=(12, 7))
    order_days = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    ax = sns.countplot(y='dia_semana', data=df, order=order_days, palette='viridis', hue='dia_semana', dodge=False)
    plt.title('Número de Siniestros Viales por Día de la Semana en Cali (2022-2024)', fontsize=16, weight='bold')
    plt.xlabel('Cantidad de Accidentes', fontsize=12)
    plt.ylabel('Día de la Semana', fontsize=12)
    ax.get_legend().remove()
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', padding=5, weight='bold')
    plt.tight_layout()
    plt.savefig('siniestros_por_dia.png')
    plt.close()
    print("Gráfico 'siniestros_por_dia.png' generado.")

    # --- Gráfico 2: Siniestros por Clase de Accidente ---
    plt.figure(figsize=(12, 7))
    class_order = df['clase_accidente'].value_counts().index
    ax = sns.countplot(y='clase_accidente', data=df, order=class_order, palette='plasma', hue='clase_accidente', dodge=False)
    plt.title('Número de Siniestros por Clase de Accidente en Cali (2022-2024)', fontsize=16, weight='bold')
    plt.xlabel('Cantidad de Accidentes', fontsize=12)
    plt.ylabel('Clase de Accidente', fontsize=12)
    ax.get_legend().remove()
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', padding=5, weight='bold')
    plt.tight_layout()
    plt.savefig('siniestros_por_clase.png')
    plt.close()
    print("Gráfico 'siniestros_por_clase.png' generado.")

    # --- Gráfico 3: Top 15 Barrios con Mayor Siniestralidad ---
    df_barrio = df[df['barrio'].str.upper() != 'SIN INFORMACION'].copy()
    plt.figure(figsize=(12, 9))
    barrio_order = df_barrio['barrio'].value_counts().nlargest(15).index
    ax = sns.countplot(y='barrio', data=df_barrio, order=barrio_order, palette='magma', hue='barrio', dodge=False)
    plt.title('Top 15 Barrios con Mayor Siniestralidad Vial en Cali (2022-2024)', fontsize=16, weight='bold')
    plt.xlabel('Cantidad de Accidentes', fontsize=12)
    plt.ylabel('Barrio', fontsize=12)
    ax.get_legend().remove()
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', padding=5, weight='bold')
    plt.tight_layout()
    plt.savefig('siniestros_por_barrio.png')
    plt.close()
    print("Gráfico 'siniestros_por_barrio.png' generado.")

    # --- Gráfico 4: Siniestros por Hora del Día ---
    plt.figure(figsize=(12, 7))
    sns.countplot(x='hora', data=df, palette='viridis', hue='hora', dodge=False)
    plt.title('Número de Siniestros Viales por Hora del Día en Cali (2022-2024)', fontsize=16, weight='bold')
    plt.xlabel('Hora del Día (Formato 24h)', fontsize=12)
    plt.ylabel('Cantidad de Accidentes', fontsize=12)
    plt.xticks(np.arange(0, 24, 1))
    plt.legend([],[], frameon=False)
    plt.tight_layout()
    plt.savefig('siniestros_por_hora.png')
    plt.close()
    print("Gráfico 'siniestros_por_hora.png' generado.")

    # --- Gráfico 5: Top 10 Vehículos Más Involucrados ---
    plt.figure(figsize=(12, 8))
    df_vehiculo = df[df['clase_vehiculo'] != 'NO APLICA'].copy()
    vehicle_order = df_vehiculo['clase_vehiculo'].value_counts().nlargest(10).index
    ax = sns.countplot(y='clase_vehiculo', data=df_vehiculo, order=vehicle_order, palette='plasma', hue='clase_vehiculo', dodge=False)
    plt.title('Top 10 Vehículos Más Involucrados en Siniestros (2022-2024)', fontsize=16, weight='bold')
    plt.xlabel('Cantidad de Accidentes', fontsize=12)
    plt.ylabel('Clase de Vehículo', fontsize=12)
    ax.get_legend().remove()
    for container in ax.containers:
        ax.bar_label(container, fmt='%d', label_type='edge', padding=5, weight='bold')
    plt.tight_layout()
    plt.savefig('siniestros_por_vehiculo.png')
    plt.close()
    print("Gráfico 'siniestros_por_vehiculo.png' generado.")

    # --- Gráfico 6: Proporción de Gravedad por Tipo de Vehículo ---
    top_vehicles = df['clase_vehiculo'].value_counts().nlargest(5).index
    df_filtered = df[(df['clase_vehiculo'].isin(top_vehicles)) & (df['gravedad'] != 'SOLO DAÑOS')].copy()
    ct = pd.crosstab(df_filtered['clase_vehiculo'], df_filtered['gravedad'])
    ct_normalized = ct.div(ct.sum(axis=1), axis=0)
    ax = ct_normalized.plot(kind='barh', stacked=True, figsize=(12, 8), colormap='Oranges_r')
    plt.title('Proporción de Gravedad (Heridos/Muertos) por Tipo de Vehículo', fontsize=16, weight='bold')
    plt.xlabel('Proporción del Total de Siniestros con Víctimas', fontsize=12)
    plt.ylabel('Clase de Vehículo', fontsize=12)
    plt.legend(title='Gravedad', bbox_to_anchor=(1.02, 1), loc='upper left')
    for n, x in enumerate([*ct_normalized.index.values]):
        for (proportion, y_loc) in zip(ct_normalized.loc[x], ct_normalized.loc[x].cumsum()):
            if proportion > 0.05:
                plt.text(y=n, x=(y_loc - proportion) + (proportion / 2), s=f'{proportion:.1%}', 
                         va='center', ha='center', color="black", fontsize=10, fontweight='bold')
    plt.gca().invert_yaxis()
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.savefig('severidad_por_vehiculo.png')
    plt.close()
    print("Gráfico 'severidad_por_vehiculo.png' generado.")
    print("\n¡Todos los gráficos han sido generados y guardados como archivos PNG!")

except Exception as e:
    print(f"Ocurrió un error: {e}")
    print("No se pudo descargar o procesar los datos. Verifica la URL y el formato de los datos.")

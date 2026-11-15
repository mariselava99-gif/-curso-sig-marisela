# ==========================================
# RUTA B - B1
# Procesamiento de datos con Pandas y GeoPandas
# ==========================================

import requests
import geopandas as gpd

# URL del servicio geográfico del IDE Boyacá
url = "https://services6.arcgis.com/Ex2fmFOuTOHRZtML/ArcGIS/rest/services/Veredas_Boyaca_2024/FeatureServer/0/query"

# Parámetros de consulta
params = {
    "where": "NOMB_MPIO = 'TUNJA'",
    "outFields": "NOMB_MPIO,NOMBRE_VER,CODIGO_VER",
    "outSR": "4326",
    "f": "geojson",
}

# Consultar el servicio
r = requests.get(url, params=params, timeout=30)
r.raise_for_status()

# Convertir respuesta a GeoDataFrame
tunja = gpd.GeoDataFrame.from_features(
    r.json()["features"],
    crs=4326
)

# Mostrar resultados
print("VEREDAS DE TUNJA")
print("Total de veredas:", len(tunja))
print(tunja[["NOMB_MPIO", "NOMBRE_VER", "CODIGO_VER"]])


# ==========================================
# EJERCICIO 2. VEREDAS POR MUNICIPIO
# ==========================================

# Leer el archivo completo de veredas
gdf = gpd.read_file("datos/veredas_boyaca.geojson")

# Consultar dimensiones de la información
print("\nINFORMACIÓN GENERAL")
print("Número de registros y columnas:", gdf.shape)

# Contar las veredas por municipio
por_municipio = (
    gdf.groupby("NOMB_MPIO")
    .size()
    .sort_values(ascending=False)
)

# Mostrar los 10 municipios con más veredas
print("\nTOP 10 MUNICIPIOS CON MÁS VEREDAS")
print(por_municipio.head(10))
# ==========================================
# EJERCICIO 3. AREA DE LAS VEREDAS
# ==========================================

# Reproyectar a EPSG:9377 (MAGNA-SIRGAS)
gdf_m = gdf.to_crs(9377)

# Calcular area en hectareas
gdf_m["area_ha"] = gdf_m.geometry.area / 10000

# Identificar las 5 veredas mas grandes
top_5 = gdf_m.nlargest(5, "area_ha")

print("\nTOP 5 VEREDAS CON MAYOR AREA")
print(top_5[["NOMB_MPIO", "NOMBRE_VER", "area_ha"]])

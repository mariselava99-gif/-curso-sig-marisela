import requests

# ============================================================
# EJERCICIO B2 - PAGINACION DE VEREDAS DE BOYACA
# ============================================================


# 1. DIRECCION DEL SERVICIO ARCGIS

url = "https://services6.arcgis.com/Ex2fmFOuTOHRZtML/ArcGIS/rest/services/Veredas_Boyaca_2024/FeatureServer/0/query"


# 2. CONFIGURACION DE LA CONSULTA
base = {
    "where": "1=1",
    "outFields": "*",
    "returnGeometry": "false",
    "f": "json"
}


# 3. CONFIGURACION DE PAGINACION

features = []

offset = 0
bloque = 500


print("=" * 55)
print("DESCARGA DE VEREDAS DE BOYACA")
print("=" * 55)


# 4. CONSULTAR INFORMACION DEL SERVICIO

try:

    url_capa = url.replace("/query", "")

    metadata_respuesta = requests.get(
        url_capa,
        params={"f": "json"},
        timeout=60
    )

    metadata_respuesta.raise_for_status()

    metadata = metadata_respuesta.json()

    if "error" in metadata:
        print("ERROR EN EL SERVICIO:")
        print(metadata["error"])
        raise SystemExit

    print("\nSERVICIO ARCGIS CONECTADO")

    nombre_id = metadata.get("objectIdField")

    if nombre_id:
        print("Campo identificador:", nombre_id)


    # 5. RECUPERAR REGISTROS POR BLOQUES

    while True:

        parametros = {
            **base,
            "resultOffset": offset,
            "resultRecordCount": bloque
        }

        # Ordenar los registros para mantener
        # una paginacion estable.

        if nombre_id:
            parametros["orderByFields"] = nombre_id

        try:

            respuesta = requests.get(
                url,
                params=parametros,
                timeout=60
            )

            print(
                "\nCodigo de respuesta:",
                respuesta.status_code
            )

            respuesta.raise_for_status()

            datos = respuesta.json()

            # Verificar errores del servidor

            if "error" in datos:
                print("\nERROR DEL SERVIDOR ARCGIS:")
                print(datos["error"])
                break

            # Recuperar los registros

            nuevos = datos.get("features", [])

            # Verificar si existen registros

            if not nuevos:
                print("\nNo existen mas registros.")
                break

            # Agregar registros a la lista general

            features.extend(nuevos)

            print(
                f"Offset {offset}: "
                f"{len(nuevos)} registros recuperados"
            )

            # Detener cuando llegue al ultimo bloque

            if len(nuevos) < bloque:
                break

            # Avanzar al siguiente bloque

            offset += len(nuevos)

        except requests.exceptions.RequestException as error:

            print("\nERROR EN LA SOLICITUD:")
            print(error)
            break

        except ValueError:

            print("\nERROR: El servidor no devolvio un JSON valido.")
            print(respuesta.text[:1000])
            break


except requests.exceptions.RequestException as error:

    print("\nERROR DE CONEXION:")
    print(error)


# ============================================================
# 6. RESULTADOS
# ============================================================

print("\n" + "=" * 55)
print("RESULTADOS DEL EJERCICIO B2")
print("=" * 55)

# Total de veredas recuperadas

print("\nTOTAL DE VEREDAS:", len(features))


# 7. CONTAR MUNICIPIOS DISTINTOS

municipios = set()

for feature in features:

    atributos = feature.get("attributes", {})

    nombre = atributos.get("NOMB_MPIO")

    if nombre:
        municipios.add(nombre)


print("MUNICIPIOS DISTINTOS:", len(municipios))


# 8. FINALIZACION

print("\nPROCESO FINALIZADO")
print("=" * 55)
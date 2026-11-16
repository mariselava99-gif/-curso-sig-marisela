# Ruta C – C1. Repaso de estándares con servicios reales



## 1. Servicio WMS – DANE



### Información general



- **Entidad:** Departamento Administrativo Nacional de Estadística (DANE).

- **Servicio:** Serv_CapasMGN_2024.

- **Estándar:** Web Map Service (WMS).

- **Versión:** 1.3.0.

- **Operación consultada:** GetCapabilities.



### Capas publicadas



El servicio publica 10 capas geográficas:



| ID | Nombre de la capa |

|---|---|

| 0 | Manzana |

| 1 | Sección Urbana |

| 2 | Sector Urbano |

| 3 | Sección Rural |

| 4 | Sector Rural |

| 5 | Clase |

| 6 | Zona Urbana |

| 7 | Municipio |

| 8 | Departamento |

| 9 | País |



### Sistemas de referencia de coordenadas



| Sistema | Descripción |

|---|---|

| CRS:84 | Sistema de coordenadas geográficas |

| EPSG:4326 | WGS 84 |

| EPSG:3857 | WGS 84 / Pseudo-Mercator |

| EPSG:102100 | Web Mercator Auxiliary Sphere (alias de EPSG:3857) |



### Extensión geográfica



| Parámetro | Valor |
|---|---:|
| Longitud mínima | -81.735621 |
| Longitud máxima | -66.847215 |
| Latitud mínima | -4.229406 |
| Latitud máxima | 13.394728 |



### Análisis del servicio



La consulta GetCapabilities permite conocer las características del servicio WMS, identificar las capas publicadas, los sistemas de referencia compatibles y la extensión geográfica de la información.



El servicio está orientado a la visualización de información geográfica mediante mapas renderizados. La respuesta obtenida corresponde a un documento XML que describe las capacidades del servicio.



### Conclusión



El servicio WMS del DANE permite consultar y visualizar información cartográfica del Marco Geoestadístico Nacional 2024. Su principal característica es la entrega de representaciones cartográficas, sin que la respuesta WMS corresponda directamente a la descarga de las geometrías y atributos vectoriales.


---

## 2. Servicio REST – Veredas Boyacá 2024

### Información general
- **Entidad:** Servicio de información geográfica de Veredas de Boyacá.
- **Servicio:** Veredas_Boyaca_2024.
- **Plataforma:** ArcGIS REST API.
- **Tipo de servicio:** FeatureServer.
- **Capa consultada:** Veredas_Boyaca_2024 (ID: 0).
- **Estándar:** Servicio REST de ArcGIS.
- **Geometría:** Polígono.
- **Formato de respuesta:** JSON.

### Parámetros de consulta

| Parámetro | Valor |
|---|---|
| where | 1=1 |
| outFields | * |
| returnGeometry | true |
| f | json |
| resultRecordCount | 500 |
| resultOffset | 0, 500, 1000, 1500, 2000 |

### Campos de información

Entre los atributos identificados se encuentran:

- FID
- OBJECTID
- CODIGO_VER
- NOM_DEP
- NOMB_MPIO
- NOMBRE_VER
- VIGENCIA
- FUENTE
- AREA_HA
- OBSERVACIO
- SHAPE_Area
- SHAPE_Leng

### Sistema de referencia espacial

- **WKID:** 102100.
- **Último WKID:** 3857.
- **Sistema:** Web Mercator Auxiliary Sphere.

### Consulta y paginación

Se realizaron consultas mediante el parámetro resultOffset, utilizando bloques de 500 registros por solicitud.

| Desplazamiento | Resultado |
|---|---|
| 0 | Registros encontrados |
| 500 | Registros encontrados |
| 1000 | Registros encontrados |
| 1500 | Registros encontrados |
| 2000 | Sin registros |

La consulta permitió identificar un total de 1.713 registros disponibles, según el recuento mostrado por el servicio.

### Análisis del servicio

El servicio REST permite consultar los atributos y las geometrías de las entidades geográficas mediante solicitudes al servidor. A través de la operación Query fue posible recuperar información de las veredas de Boyacá, aplicando filtros y parámetros de paginación para controlar la cantidad de registros devueltos.

### Conclusión

El servicio REST de ArcGIS permite acceder a información geográfica estructurada, consultar sus atributos y recuperar entidades mediante solicitudes parametrizadas. A diferencia del servicio WMS, orientado principalmente a la visualización cartográfica, el servicio REST facilita el acceso directo a los registros y sus características.

---

## 3. Comparación entre servicios

| Característica | WMS – DANE | REST – Veredas Boyacá |
|---|---|---|
| Tipo de servicio | WMS | FeatureServer |
| Operación consultada | GetCapabilities | Query |
| Respuesta | XML | JSON |
| Información | Capacidades y capas | Atributos y geometrías |
| Uso principal | Visualización cartográfica | Consulta de entidades geográficas |
| Acceso a registros | No directamente | Sí |

---

## 3. Comparación entre servicios

| Característica | WMS – DANE | REST – Veredas Boyacá |
|---|---|---|
| Tipo de servicio | WMS | FeatureServer |
| Operación consultada | GetCapabilities | Query |
| Respuesta | XML | JSON |
| Información | Capacidades y capas | Atributos y geometrías |
| Uso principal | Visualización cartográfica | Consulta de entidades geográficas |
| Acceso a registros | No directamente | Sí |

### Conclusión general

Los servicios WMS y REST permiten acceder a información geográfica mediante diferentes estándares. WMS facilita la visualización cartográfica, mientras que REST permite consultar directamente los atributos y geometrías de las entidades geográficas.
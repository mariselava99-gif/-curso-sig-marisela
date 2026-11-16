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




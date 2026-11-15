import json
from collections import Counter
import pandas as pd

with open("datos/provincias_boyaca.geojson", encoding="utf-8") as f:
    datos = json.load(f)

conteo = Counter(
    feat["properties"]["provincia"]
    for feat in datos["features"]
)

for provincia, n in conteo.most_common():
    print(f"{provincia:20} {n}")
    

props = [f["properties"] for f in datos["features"]]
df = pd.DataFrame(props)
print(df.groupby("provincia").size().sort_values(ascending=False))
print("Número de provincias distintas:", df["provincia"].nunique())
print("Total de municipios:", len(df))
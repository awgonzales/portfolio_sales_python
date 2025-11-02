import geopandas  
from geodatasets import get_path

path_to_dasta = get_path("nybb")
gdf = geopandas.read_file(path_to_dasta)

print(gdf)

# Write a .geojson file -> make a map
gdf.to_file("NYC.geojson", driver = "GeoJSON")

import osmnx as ox

# 1. Define location and query POIs (e.g., cafes in "City, Country")
place_name = "Banff, Canada"
# Fetch POIs (amenity=bar)
pois = ox.features_from_place(place_name, tags={"amenity": "bar"})

print("Full POIS\n")
print(pois)
print("#"*50)

# get columsn names
print(pois.columns)
print("#"*50)

# get coordinates
print(pois['geometry'])
print("#"*50)

print(pois['geometry'].iloc[0])
print("#"*50)

print("lat: ", pois['geometry'].iloc[0].x)
print("lon: ", pois['geometry'].iloc[0].y)
print("name: ", pois['name'].iloc[0])

html = pois.to_html()
with open("pois_dataframe_table.html", "w") as f:
    f.write(html)
import folium
import osmnx as ox

# 1. Define location and query POIs (e.g., cafes in "City, Country")
place_name = "Banff, Canada"
# Fetch POIs (amenity=cafe)
pois = ox.features_from_place(place_name, tags={"amenity": "cafe"})

# 2. Get location center for the map
center = ox.geocode(place_name)

# 3. Create Map object
m = folium.Map(location=center, zoom_start=14)

# 4. Add POIs to the map
for _, row in pois.iterrows():
    if row.geometry.type == 'Point':
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=row.get('name', 'unknown'),
            icon=folium.Icon(color='brown', icon='coffee', prefix='fa'),
        ).add_to(m)
        

# 5. Save/Display Map
m.save("map_with_pois.html")

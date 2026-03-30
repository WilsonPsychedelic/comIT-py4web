import folium

# Define the coordinates for the start and end points
# Format is [latitude, longitude]
point1 = [40.7128, -74.0060] # New York City
point2 = [51.5074, -0.1278]  # London

# Create a map centered around an average location or a specific start point
m = folium.Map(location=[(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2], zoom_start=2)

# Add markers for clarity (optional)
folium.Marker(point1, popup="New York City", tooltip="Point 1").add_to(m)
folium.Marker(point2, popup="London", tooltip="Point 2").add_to(m)

# Define the path as a list of coordinate tuples
route_coordinates = [point1, point2]

# Add the PolyLine to the map
folium.PolyLine(
    locations=route_coordinates,
    color="blue",
    weight=5,
    opacity=0.7,
    tooltip="Route between NYC and London"
).add_to(m)

# Save the map as an HTML file
m.save("map_with_line.html")


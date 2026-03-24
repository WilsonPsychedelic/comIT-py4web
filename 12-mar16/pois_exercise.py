import math
import folium
import osmnx as ox
from folium import plugins
import webbrowser
import random
import pandas as pd

class PointOfInterest:
    """Base class demonstrating ENCAPSULATION"""

    def __init__(self, name, latitude, longitude):
        self._name = name
        self._latitude = latitude
        self._longitude = longitude

    def get_name(self):
        return self._name
    
    def get_coordinates(self):
        return (self._latitude, self._longitude)
    
    def distance_to(self, other_poi):
        """Calculate distance to another POI"""
        lat_diff = abs(self._latitude - other_poi._latitude)
        lon_diff = abs(self._longitude - other_poi._longitude)

        if lat_diff < 0.1 and lon_diff < 0.1:
            return self._euclidean_distance(other_poi)
        else:
            return self._haversine_distance(other_poi)
        
    def _euclidean_distance(self, other_poi):
        """Private method for short distances"""
        lat_km = (self._latitude - other_poi._latitude) * 111
        lon_km = (self._longitude - other_poi._longitude) * 111 * math.cos(math.radians(self._latitude))
        return math.sqrt(lat_km**2 + lon_km**2)
        
    def _haversine_distance(self, other_poi):
        """Private method for long distances"""
        R = 6371
        lat1 = math.radians(self._latitude)
        lon1 = math.radians(self._longitude)
        lat2 = math.radians(other_poi._latitude)
        lon2 = math.radians(other_poi._longitude)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))

        return R * c

    def get_marker_color(self):
        return "blue"
    
    def get_popup_text(self):
        """Returns text for map popup"""
        return (f"<b>{self.get_name()}</b><br>"
                f"Lat: {self._latitude:.4f}<br>"
                f"Lon: {self._longitude:.4f}")
    
class Restaurant(PointOfInterest):

    def __init__(self, name, latitude, longitude, cuisine_type, price_range):
       super().__init__(name, latitude, longitude)
       self.cuisine_type = cuisine_type
       self.price_range = price_range

    def get_marker_color(self):
        if self.cuisine_type.lower() == "italian":
            return "red"
        elif self.cuisine_type.lower() == "french":
            return "green"
        elif self.cuisine_type.lower() == "asian":
            return "orange"
        return "blue"

    def get_popup_text(self):
        lat, lon = self.get_coordinates()
        price = "$" * self.price_range
        return (f"🍽️ <b>{self.get_name()}</b><br>"
                f"Cuisine: {self.cuisine_type}<br>"
                f"Price: {price}<br>"
                f"Location: ({lat:.4f}, {lon:.4f})")

class Museum(PointOfInterest):

    def __init__(self, name, latitude, longitude, artifact_count, entry_fee):
        # Call parent constructor
        super().__init__(name, latitude, longitude)

        # Add museum-specific attributes
        self.artifact_count = artifact_count
        self.entry_fee = entry_fee
        
    def get_marker_color(self):
        return "purple" if self.artifact_count > 10000 else "pink"
    
    def get_popup_text(self):
        lat, lon = self.get_coordinates()
        fee_text = "Free" if self.entry_fee == 0 else f"${self.entry_fee}"
        return (f"🏛️ <b>{self.get_name()}</b><br>"
                f"Artifacts: {self.artifact_count}<br>"
                f"Entry Fee: {fee_text}<br>"
                f"Location: ({lat:.4f}, {lon:.4f})")
        
class Park(PointOfInterest):
    """Park class (INHERITANCE)"""

    def __init__(self, name, latitude, longitude, area_hectares, has_playground):
        # Call parent constructor
        super().__init__(name, latitude, longitude)

        #Park-specific attributes
        self.area_hectares = area_hectares
        self.has_playground = has_playground

    def get_marker_color(self):
        return "green"
    
    def get_popup_text(self):
        lat, lon = self.get_coordinates()
        playground = "Yes 🎠" if self.has_playground else "No"

        return (f"🌳 <b>{self.get_name()}</b><br>"
                f"Area: {self.area_hectares} hectares<br>"
                f"Playground: {playground}<br>"
                f"Location: ({lat:.4f}, {lon:.4f})")

class POIMap:
    """Encapsulates map creation and POI management"""

    def __init__(self, center_latitude, center_longitude, zoom_start=13):
        # Create folium map
        self.map = folium.Map(location=[center_latitude, center_longitude], zoom_start=zoom_start)

        # Store POIs
        self.pois = []

        print(f"🗺️ Map created with center at ({center_latitude}, {center_longitude})")

    def add_poi(self, poi):
        # Add to list
        self.pois.append(poi)

        # Create marker
        marker = folium.Marker(
            location=poi.get_coordinates(),
            popup=poi.get_popup_text(),
            icon=folium.Icon(color=poi.get_marker_color())
        )

        # Add to map
        marker.add_to(self.map)

        print(f" ✅ Added: {poi.get_name()}")

    def add_multiple_pois(self, pois):
        for poi in pois:
            self.add_poi(poi)

    def draw_distance_line(self, poi1, poi2):
        # Calculate distance
        distance = poi1.distance_to(poi2)

        coords1 = poi1.get_coordinates()
        coords2 = poi2.get_coordinates()

        # Draw line
        folium.PolyLine(
            locations=[coords1, coords2],
            tooltip=f"{distance:.2f} km",
            popup=f"Distance: {distance:.2f} km"
        ).add_to(self.map)

        print(f" 📏 Distance between {poi1.get_name()} and {poi2.get_name()}: {distance:.2f} km")

    def add_map_controls(self):
        folium.LayerControl().add_to(self.map)
        plugins.Fullscreen().add_to(self.map)
        plugins.MeasureControl().add_to(self.map)

    def save_map(self, filename="map.html"):
        self.map.save(filename)
        print(f"💾 Map saved as {filename}")
        return filename

class ParisPOIFetcher:
    """
    Fetches real POI data from OpenStreetMap using OSMnx
    Demonstrates ABSTRACTION - hides complex OSMnx queries
    """

    def __init__(self):
        self.paris_center = (48.8566, 2.3522)
        print("🌍 Initialized Paris POI Fetcher")

    def fetch_restaurants(self, limit=5):
        """
        Fetch restaurants from OpenStreetMap
        """
        restaurants = []

        try:
            print("Fetching restaurants from OpenStreetMap...")
            features = ox.features_from_place(
                "Paris, France",
                tags={'amenity': 'restaurant'}
            )

            count = 0
            for idx, feature in features.iterrows():
                if count >= limit:
                    break

                if pd.isna(feature.get('name')):
                    continue

                name = feature['name']

                if feature.geometry.geom_type == 'Point':
                    lon, lat = feature.geometry.x, feature.geometry.y
                else:
                    centroid = feature.geometry.centroid
                    lon, lat = centroid.x, centroid.y

                cuisine = feature.get('cuisine', 'French')
                if isinstance(cuisine, list):
                    cuisine = cuisine[0] if cuisine else 'French'
                if pd.isna(cuisine):
                    cuisine = 'French'
                        
                price_range = random.randint(1, 4)

                restaurant = Restaurant(name, lat, lon, cuisine.capitalize(), price_range)
                restaurants.append(restaurant)
                count += 1

        except Exception as e:
            print(f"Error fetching restaurants: {e}")
            restaurants = self._get_sample_restaurants()

        return restaurants[:limit]
    
    def fetch_museums(self, limit=3):
        """
        Fetch museums from OpenStreetMap
        """
        museums = []

        try:
            print("Fetching museums from OpenStreetMap...")
            features = ox.features_from_place(
                "Paris, France",
                tags={'tourism': 'museum'}
            )

            count = 0
            for idx, feature in features.iterrows():
                if count >= limit:
                    break

                if pd.isna(feature.get('name')):
                    continue

                name = feature['name']

                if feature.geometry.geom_type == 'Point':
                    lon, lat = feature.geometry.x, feature.geometry.y
                else:
                    centroid = feature.geometry.centroid
                    lon, lat = centroid.x, centroid.y

                artifact_count = random.randint(1000, 50000)

                fee = feature.get('fee', 'no')
                entry_fee = 15 if fee == 'yes' else 0

                museum = Museum(name, lat, lon, artifact_count, entry_fee)
                museums.append(museum)
                count += 1
        except Exception as e:
            print(f" Error fetching museums: {e}")
            print(" Using sample data instead...")
            museums = self._get_sample_museums()

        return museums[:limit]
    
    def fetch_parks(self, limit=3):
        """
        Fetch parks from OpenStreetMap
        """
        parks = []

        try:
            print("Fetching parks from OpenStreetMap...")
            features = ox.features_from_place(
                "Paris, France",
                tags={'leisure': 'park'}
            )

            count = 0
            for idx, feature in features.iterrows():
                if count >= limit:
                    break

                if pd.isna(feature.get('name')):
                    continue

                name = feature['name']

                if feature.geometry.geom_type == 'Point':
                    lon, lat = feature.geometry.x, feature.geometry.y
                else:
                    centroid = feature.geometry.centroid
                    lon, lat = centroid.x, centroid.y

                if feature.geometry.geom_type != 'Point':
                    area = feature.geometry.area * 111 * 111 * 100
                else:
                    area = random.uniform(1, 30)

                has_playground = not pd.isna(feature.get('playground', None))

                park = Park(name, lat, lon, round(area, 1), has_playground)
                parks.append(park)
                count += 1

        except Exception as e:
            print(f" Error fetching parks: {e}")
            print(" Using sample data instead...")
            parks = self._get_sample_parks()

        return parks[:limit]
    
    # Sample data methods (fallback if OSMnx fails)
    def _get_sample_restaurants(self):
        """Provide sample restaurant data"""
        return [
            Restaurant("Le Meurice", 48.8655, 2.3278, "French", 4),
            Restaurant("Cafe de Flore", 48.8540, 2.3325, "French", 3),
            Restaurant("Pizza Roma", 48.8570, 2.3450, "Italian", 2),
            Restaurant("Sushi Shop", 48.8620, 2.3150, "Asian", 2),
            Restaurant("Le Procope", 48.8525, 2.3385, "French", 3)
        ]
    
    def _get_sample_museums(self):
        """Provide sample museum data"""
        return [
            Museum("Louvre Museum", 48.8606, 2.3376, 35000, 17),
            Museum("Musée d'Orsay", 48.8600, 2.3265, 4000, 14),
            Museum("Centre Pompidou", 48.8606, 2.3522, 5000, 15)
    ]

    def _get_sample_parks(self):
        """Provide sample park data"""
        return [
            Park("Jardin du Luxembourg", 48.8462, 2.3372, 23, True),
            Park("Tuileries Garden", 48.8639, 2.3272, 25.5, True),
            Park("Parc des Buttes-Chaumont", 48.8800, 2.3825, 24.7, True)
    ]

def main():

    print("=" * 60)
    print("🗺️ PARIS POINTS OF INTEREST MAPPER")
    print("=" * 60)

    fetcher = ParisPOIFetcher()

    print("\n📥 Fetching POIs from OpenStreetMap...")

    restaurants = fetcher.fetch_restaurants(limit=5)
    print(f"Found {len(restaurants)} restaurants")

    museums = fetcher.fetch_museums(limit=3)
    print(f"Found {len(museums)} museums")
    
    parks = fetcher.fetch_parks(limit=3)
    print(f"Found {len(parks)} parks")

    print("\n🗺️ Creating map...")
    poi_map = POIMap(48.8566, 2.3522, zoom_start=13)

    print("\n📍Adding POIs to map...")
    poi_map.add_multiple_pois(restaurants)
    poi_map.add_multiple_pois(museums)
    poi_map.add_multiple_pois(parks)

    print("\n📏 Drawing distance line...")
    if len(restaurants) > 0 and len(museums) > 0:
        # Draw line between first restaurant and first museum
        poi_map.draw_distance_line(restaurants[0], museums[0])

    print("\n🎮 Adding map controls...")
    poi_map.add_map_controls()

    print("\n💾 Saving map...")
    filename = poi_map.save_map("my_paris_map.html")

    # Automatically open the map in your browser
    print("\n🌐 Opening map in browser...")
    webbrowser.open(filename)

if __name__ == "__main__":
    main()

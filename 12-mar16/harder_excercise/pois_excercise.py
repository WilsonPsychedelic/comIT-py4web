"""
EXERCISE: Mapping Points of Interest with OOP, Folium, and OSMnx

OBJECTIVES:
1. Practice using the 4 pillars of OOP with real-world mapping
2. Learn to use Folium for interactive maps
3. Use OSMnx to fetch real POI data from OpenStreetMap
4. Create a visual representation of different POI types

BEFORE YOU BEGIN:
Install required packages:
    pip install folium osmnx

COMPLETE THE TODOs in this file to create an interactive map of Paris attractions!
"""

import math
import folium
import osmnx as ox
from folium import plugins
import webbrowser
import random

# ============================================================================
# PART 1: Review the OOP Classes (Already Provided)
# Study how these classes use the 4 pillars of OOP
# ============================================================================

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
        """TODO: Override this in child classes to return different colors"""
        return "blue"
    
    def get_popup_text(self):
        """Returns text for map popup"""
        return f"<b>{self._name}</b><br>Lat: {self._latitude:.4f}<br>Lon: {self._longitude:.4f}"


class Restaurant(PointOfInterest):
    """TODO: Implement Restaurant class (INHERITANCE)"""
    
    def __init__(self, name, latitude, longitude, cuisine_type, price_range):
        # TODO: Call parent constructor
        # TODO: Add restaurant-specific attributes
        # TODO: Set cuisine_type and price_range (1-4)
        pass
    
    def get_marker_color(self):
        """TODO: Return a color based on cuisine type (POLYMORPHISM)
        HINT: Return "red" for Italian, "green" for French, "orange" for Asian, "blue" for others
        """
        pass
    
    def get_popup_text(self):
        """TODO: Create detailed popup text for restaurant
        HINT: Include name, cuisine, price range ($ signs), and coordinates
        """
        pass


class Museum(PointOfInterest):
    """TODO: Implement Museum class (INHERITANCE)"""
    
    def __init__(self, name, latitude, longitude, artifact_count, entry_fee):
        # TODO: Call parent constructor
        # TODO: Add museum-specific attributes
        pass
    
    def get_marker_color(self):
        """TODO: Return "purple" for museums with >10000 artifacts, "pink" for smaller ones"""
        pass
    
    def get_popup_text(self):
        """TODO: Create detailed popup text for museum
        HINT: Include name, artifact count, entry fee, and coordinates
        """
        pass


class Park(PointOfInterest):
    """TODO: Implement Park class (INHERITANCE)"""
    
    def __init__(self, name, latitude, longitude, area_hectares, has_playground):
        # TODO: Call parent constructor
        # TODO: Add park-specific attributes
        pass
    
    def get_marker_color(self):
        """TODO: Return "green" for parks"""
        pass
    
    def get_popup_text(self):
        """TODO: Create detailed popup text for park
        HINT: Include name, area, playground info, and coordinates
        """
        pass


# ============================================================================
# PART 2: Map Creation Class (Demonstrates ENCAPSULATION)
# ============================================================================

class POIMap:
    """Encapsulates map creation and POI management"""
    
    def __init__(self, center_latitude, center_longitude, zoom_start=13):
        """
        Initialize map with center coordinates
        """
        # TODO: Create a folium Map object
        # HINT: folium.Map(location=[lat, lon], zoom_start=zoom_start)
        self.map = None  # Replace with actual map creation
        
        # TODO: Initialize an empty list to store POIs
        self.pois = []
        
        print(f"🗺️  Map created with center at ({center_latitude}, {center_longitude})")
    
    def add_poi(self, poi):
        """
        Add a POI to the map
        """
        # TODO: Add the POI to the self.pois list
        
        # TODO: Create a folium.Marker for this POI
        # HINT: Use poi.get_coordinates() for location
        # HINT: Use poi.get_popup_text() for popup
        # HINT: Use poi.get_marker_color() for marker color
        
        # TODO: Add the marker to self.map
        
        print(f"  ✅ Added: {poi.get_name()}")
    
    def add_multiple_pois(self, pois):
        """
        Add multiple POIs at once
        """
        for poi in pois:
            self.add_poi(poi)
    
    def draw_distance_line(self, poi1, poi2):
        """
        Draw a line between two POIs and show distance
        """
        # TODO: Calculate distance between poi1 and poi2 using distance_to()
        distance = 0  # Replace with actual calculation
        
        # TODO: Create a line between the two POIs
        # HINT: Use folium.PolyLine with locations=[poi1_coords, poi2_coords]
        # HINT: Add popup with distance information
        
        print(f"  📏 Distance between {poi1.get_name()} and {poi2.get_name()}: {distance:.2f} km")
    
    def add_map_controls(self):
        """
        Add useful controls to the map
        """
        # TODO: Add layer control
        # HINT: folium.LayerControl().add_to(self.map)
        
        # TODO: Add fullscreen button
        # HINT: plugins.Fullscreen().add_to(self.map)
        
        # TODO: Add measure control (to measure distances manually)
        # HINT: plugins.MeasureControl().add_to(self.map)
        
        pass
    
    def save_map(self, filename="paris_pois.html"):
        """
        Save the map to an HTML file
        """
        # TODO: Save the map to file
        # HINT: self.map.save(filename)
        
        print(f"\n💾 Map saved as '{filename}'")
        return filename


# ============================================================================
# PART 3: Fetch Real Data with OSMnx (ABSTRACTION)
# ============================================================================

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
        TODO: Fetch restaurants from OpenStreetMap
        HINT: Use ox.features_from_place() with tags={'amenity': 'restaurant'}
        """
        restaurants = []
        
        try:
            print("  Fetching restaurants from OpenStreetMap...")
            # TODO: Get restaurant features from Paris
            # features = ox.features_from_place("Paris, France", tags={'amenity': 'restaurant'})
            
            # Loop through features and create Restaurant objects
            count = 0
            for idx, feature in features.iterrows():
                if count >= limit:
                    break
                    
                # Check if name exists
                if pd.isna(feature.get('name')):
                    continue
                
                # Get name
                name = feature['name']
                
                # Get coordinates (centroid of the polygon/point)
                if feature.geometry.geom_type == 'Point':
                    lon, lat = feature.geometry.x, feature.geometry.y
                else:
                    # For polygons, use centroid
                    centroid = feature.geometry.centroid
                    lon, lat = centroid.x, centroid.y
                
                # Determine cuisine type (simplified for demo)
                cuisine = feature.get('cuisine', 'French')
                if isinstance(cuisine, list):
                    cuisine = cuisine[0] if cuisine else 'French'
                if pd.isna(cuisine):
                    cuisine = 'French'
                
                # Random price range for demo (in real app, you'd parse this)
                price_range = random.randint(1, 4)
                
                # Create Restaurant object
                restaurant = Restaurant(name, lat, lon, cuisine.capitalize(), price_range)
                restaurants.append(restaurant)
                count += 1

        except Exception as e:
            print(f"Error fetching restaurants: {e}")
            # Return sample data if API fails
            restaurants = self._get_sample_restaurants()
        
        return restaurants[:limit]
    
    def fetch_museums(self, limit=3):
        """
        TODO: Fetch museums from OpenStreetMap
        HINT: Use tags={'tourism': 'museum'}
        """
        museums = []
        
        try:
            # TODO: Implement similar to fetch_restaurants
            # Loop through features
            count = 0
            for idx, feature in features.iterrows():
                if count >= limit:
                    break
                    
                # Check if name exists
                if pd.isna(feature.get('name')):
                    continue
                
                # Get name
                name = feature['name']
                
                # Get coordinates
                if feature.geometry.geom_type == 'Point':
                    lon, lat = feature.geometry.x, feature.geometry.y
                else:
                    centroid = feature.geometry.centroid
                    lon, lat = centroid.x, centroid.y
                
                # Estimate artifact count (simplified for demo)
                artifact_count = random.randint(1000, 50000)
                
                # Get or estimate entry fee
                fee = feature.get('fee', 'no')
                entry_fee = 15 if fee == 'yes' else 0
                
                # Create Museum object
                museum = Museum(name, lat, lon, artifact_count, entry_fee)
                museums.append(museum)
                count += 1
        except Exception as e:
            print(f"  Error fetching museums: {e}")
            print("  Using sample data instead...")
            museums = self._get_sample_museums()
        
        return museums[:limit]
    
    def fetch_parks(self, limit=3):
        """
        TODO: Fetch parks from OpenStreetMap
        HINT: Use tags={'leisure': 'park'}
        """
        parks = []
        
        try:
            # TODO: Implement similar to fetch_restaurants
            
            #Loop through features
            count = 0
            for idx, feature in features.iterrows():
                if count >= limit:
                    break
                    
                # Check if name exists
                if pd.isna(feature.get('name')):
                    continue
                
                # Get name
                name = feature['name']
                
                # Get coordinates
                if feature.geometry.geom_type == 'Point':
                    lon, lat = feature.geometry.x, feature.geometry.y
                else:
                    centroid = feature.geometry.centroid
                    lon, lat = centroid.x, centroid.y
                
                # Estimate area (simplified for demo)
                if feature.geometry.geom_type != 'Point':
                    area = feature.geometry.area * 111 * 111 * 100  # Rough conversion to hectares
                else:
                    area = random.uniform(1, 30)
                
                # Check for playground
                has_playground = not pd.isna(feature.get('playground', None))
                
                # Create Park object
                park = Park(name, lat, lon, round(area, 1), has_playground)
                parks.append(park)
                count += 1
                
        except Exception as e:
            print(f"  Error fetching parks: {e}")
            print("  Using sample data instead...")
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


# ============================================================================
# PART 4: Main Function - Your Code Starts Here!
# ============================================================================

def main():
    """
    Main function to demonstrate all concepts
    COMPLETE THE TODOs to create your interactive map!
    """
    print("=" * 60)
    print("🗺️  PARIS POINTS OF INTEREST MAPPER")
    print("=" * 60)
    
    # Import pandas for data handling (needed for OSMnx)
    global pd
    import pandas as pd
    
    # TODO 1: Create a POIFetcher object
    fetcher = ParisPOIFetcher()
    
    # TODO 2: Fetch different types of POIs
    print("\n📥 Fetching POIs from OpenStreetMap...")
    
    # HINT: Use fetcher.fetch_restaurants(limit=5)
    restaurants = []  # Replace with actual fetch: fetcher.fetch_restaurants(limit=5)
    print(f"Found {len(restaurants)} restaurants")
    
    # TODO: Fetch museums, limit=3
    museums = []
    print(f"Found {len(museums)} museums")
    
    # TODO: Fetch parks, limit=3
    parks = []
    print(f"Found {len(parks)} parks")
    
    
    # TODO 3: Create a map centered on Paris
    print("\n🗺️  Creating map...")
    poi_map = POIMap(48.8566, 2.3522, zoom_start=13)
    
    # TODO 4: Add all POIs to the map
    print("\n📍 Adding POIs to map...")
    poi_map.add_multiple_pois(restaurants)
    poi_map.add_multiple_pois(museums)
    poi_map.add_multiple_pois(parks)
    
    # TODO 5: Add a distance line between two famous locations
    print("\n📏 Drawing distance line...")
    if len(restaurants) > 0 and len(museums) > 0:
        # Draw line between first restaurant and first museum
        poi_map.draw_distance_line(restaurants[0], museums[0])
    
    # TODO 6: Add map controls
    print("\n🎮 Adding map controls...")
    poi_map.add_map_controls()
    
    # TODO 7: Save and open the map
    print("\n💾 Saving map...")
    filename = poi_map.save_map("my_paris_map.html")
    
    # Automatically open the map in your browser
    print("\n🌐 Opening map in browser...")
    webbrowser.open(filename)
    
    
if __name__ == "__main__":
    main()
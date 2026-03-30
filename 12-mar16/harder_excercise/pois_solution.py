"""
SOLUTION: Mapping Points of Interest with OOP, Folium, and OSMnx

This is the complete solution with all TODOs implemented.
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
        """Default marker color"""
        return "blue"
    
    def get_popup_text(self):
        """Returns text for map popup"""
        return f"<b>{self._name}</b><br>Lat: {self._latitude:.4f}<br>Lon: {self._longitude:.4f}"


class Restaurant(PointOfInterest):
    """Restaurant class demonstrating INHERITANCE and POLYMORPHISM"""
    
    def __init__(self, name, latitude, longitude, cuisine_type, price_range):
        # Call parent constructor
        super().__init__(name, latitude, longitude)
        
        # Add restaurant-specific attributes
        self._cuisine_type = cuisine_type
        self._price_range = max(1, min(4, price_range))  # Ensure between 1-4
        self._rating = 0
        self._reviews = []
    
    def get_marker_color(self):
        """Return color based on cuisine type (POLYMORPHISM)"""
        cuisine_colors = {
            "French": "red",
            "Italian": "green", 
            "Asian": "orange",
            "Japanese": "orange",
            "Chinese": "orange",
            "Thai": "orange",
            "Indian": "purple",
            "Mexican": "brown",
            "American": "darkblue"
        }
        return cuisine_colors.get(self._cuisine_type, "blue")
    
    def get_popup_text(self):
        """Create detailed popup text for restaurant"""
        price_symbols = "$" * self._price_range
        rating_text = f"Rating: {self._rating:.1f}/5" if self._rating > 0 else "No ratings yet"
        
        return (f"<b>🍽️ {self._name}</b><br>"
                f"Cuisine: {self._cuisine_type}<br>"
                f"Price: {price_symbols}<br>"
                f"{rating_text}<br>"
                f"<i>{self._latitude:.4f}, {self._longitude:.4f}</i>")
    
    def add_review(self, rating, comment):
        """Add a review and update rating"""
        self._reviews.append({'rating': rating, 'comment': comment})
        total = sum(r['rating'] for r in self._reviews)
        self._rating = total / len(self._reviews)


class Museum(PointOfInterest):
    """Museum class demonstrating INHERITANCE and POLYMORPHISM"""
    
    def __init__(self, name, latitude, longitude, artifact_count, entry_fee):
        # Call parent constructor
        super().__init__(name, latitude, longitude)
        
        # Add museum-specific attributes
        self._artifact_count = artifact_count
        self._entry_fee = entry_fee
        self._current_exhibition = "Permanent Collection"
    
    def get_marker_color(self):
        """Purple for large museums, pink for smaller ones"""
        return "purple" if self._artifact_count > 10000 else "pink"
    
    def get_popup_text(self):
        """Create detailed popup text for museum"""
        fee_text = f"€{self._entry_fee}" if self._entry_fee > 0 else "Free"
        
        return (f"<b>🏛️ {self._name}</b><br>"
                f"Artifacts: {self._artifact_count:,}<br>"
                f"Entry: {fee_text}<br>"
                f"Current: {self._current_exhibition}<br>"
                f"<i>{self._latitude:.4f}, {self._longitude:.4f}</i>")
    
    def set_exhibition(self, exhibition_name):
        """Change current exhibition"""
        self._current_exhibition = exhibition_name


class Park(PointOfInterest):
    """Park class demonstrating INHERITANCE and POLYMORPHISM"""
    
    def __init__(self, name, latitude, longitude, area_hectares, has_playground):
        # Call parent constructor
        super().__init__(name, latitude, longitude)
        
        # Add park-specific attributes
        self._area_hectares = area_hectares
        self._has_playground = has_playground
        self._has_dog_park = random.choice([True, False])  # Random for demo
    
    def get_marker_color(self):
        """All parks are green"""
        return "green"
    
    def get_popup_text(self):
        """Create detailed popup text for park"""
        playground_text = "✅ Playground" if self._has_playground else "❌ No playground"
        dogpark_text = "✅ Dog park" if self._has_dog_park else "❌ No dog park"
        
        return (f"<b>🌳 {self._name}</b><br>"
                f"Area: {self._area_hectares} hectares<br>"
                f"{playground_text}<br>"
                f"{dogpark_text}<br>"
                f"<i>{self._latitude:.4f}, {self._longitude:.4f}</i>")


# ============================================================================
# PART 2: Map Creation Class (Demonstrates ENCAPSULATION)
# ============================================================================

class POIMap:
    """Encapsulates map creation and POI management"""
    
    def __init__(self, center_latitude, center_longitude, zoom_start=13):
        """
        Initialize map with center coordinates
        """
        # Create a folium Map object
        self.map = folium.Map(
            location=[center_latitude, center_longitude], 
            zoom_start=zoom_start,
            tiles='OpenStreetMap'
        )
        
        # Initialize empty list to store POIs
        self.pois = []
        
        print(f"🗺️  Map created with center at ({center_latitude}, {center_longitude})")
    
    def add_poi(self, poi):
        """
        Add a POI to the map
        """
        # Add POI to the list
        self.pois.append(poi)
        
        # Get coordinates
        lat, lon = poi.get_coordinates()
        
        # Create a folium Marker with custom popup
        marker = folium.Marker(
            location=[lat, lon],
            popup=folium.Popup(poi.get_popup_text(), max_width=300),
            tooltip=poi.get_name(),
            icon=folium.Icon(color=poi.get_marker_color(), icon='info-sign')
        )
        
        # Add marker to map
        marker.add_to(self.map)
        
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
        # Calculate distance between POIs
        distance = poi1.distance_to(poi2)
        
        # Get coordinates
        coords1 = poi1.get_coordinates()
        coords2 = poi2.get_coordinates()
        
        # Create a line between the two POIs
        line = folium.PolyLine(
            locations=[coords1, coords2],
            color='red',
            weight=3,
            opacity=0.7,
            popup=f"Distance: {distance:.2f} km"
        )
        
        # Add line to map
        line.add_to(self.map)
        
        # Add midpoint marker with distance
        mid_lat = (coords1[0] + coords2[0]) / 2
        mid_lon = (coords1[1] + coords2[1]) / 2
        
        folium.Marker(
            location=[mid_lat, mid_lon],
            popup=f"📏 {distance:.2f} km",
            icon=folium.DivIcon(html=f'<div style="font-size: 12pt; background-color: white; padding: 3px; border-radius: 5px;">{distance:.1f}km</div>')
        ).add_to(self.map)
        
        print(f"  📏 Distance between {poi1.get_name()} and {poi2.get_name()}: {distance:.2f} km")
    
    def add_map_controls(self):
        """
        Add useful controls to the map
        """
        # Add layer control
        folium.LayerControl().add_to(self.map)
        
        # Add fullscreen button
        plugins.Fullscreen().add_to(self.map)
        
        # Add measure control (to measure distances manually)
        plugins.MeasureControl(position='topleft').add_to(self.map)
        
        # Add minimap
        plugins.MiniMap().add_to(self.map)
        
        # Add mouse position display
        plugins.MousePosition().add_to(self.map)
        
        print("  🎮 Added map controls: layers, fullscreen, measure, minimap")
    
    def save_map(self, filename="paris_pois.html"):
        """
        Save the map to an HTML file
        """
        # Save the map to file
        self.map.save(filename)
        
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
        Fetch restaurants from OpenStreetMap
        """
        restaurants = []
        
        try:
            print("  Fetching restaurants from OpenStreetMap...")
            # Get restaurant features from Paris
            features = ox.features_from_place("Paris, France", tags={'amenity': 'restaurant'})
            
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
            print(f"  Error fetching restaurants: {e}")
            print("  Using sample data instead...")
            restaurants = self._get_sample_restaurants()
        
        return restaurants[:limit]
    
    def fetch_museums(self, limit=3):
        """
        Fetch museums from OpenStreetMap
        """
        museums = []
        
        try:
            print("  Fetching museums from OpenStreetMap...")
            # Get museum features from Paris
            features = ox.features_from_place("Paris, France", tags={'tourism': 'museum'})
            
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
        Fetch parks from OpenStreetMap
        """
        parks = []
        
        try:
            print("  Fetching parks from OpenStreetMap...")
            # Get park features from Paris
            features = ox.features_from_place("Paris, France", tags={'leisure': 'park'})
            
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
            Restaurant("Sushi Shop", 48.8620, 2.3150, "Japanese", 2),
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
# PART 4: Main Function - Complete Solution
# ============================================================================

def main():
    """
    Main function to demonstrate all concepts
    """
    print("=" * 60)
    print("🗺️  PARIS POINTS OF INTEREST MAPPER - SOLUTION")
    print("=" * 60)
    
    # Import pandas for data handling (needed for OSMnx)
    global pd
    import pandas as pd
    
    # TODO 1: Create a POIFetcher object
    fetcher = ParisPOIFetcher()
    
    # TODO 2: Fetch different types of POIs
    print("\n📥 Fetching POIs from OpenStreetMap...")
    
    # Fetch restaurants
    restaurants = fetcher.fetch_restaurants(limit=5)
    print(f"Found {len(restaurants)} restaurants")
    
    # Fetch museums
    museums = fetcher.fetch_museums(limit=3)
    print(f"Found {len(museums)} museums")
    
    # Fetch parks
    parks = fetcher.fetch_parks(limit=3)
    print(f"Found {len(parks)} parks")
    
    # Combine all POIs
    all_pois = restaurants + museums + parks
    
    # TODO 3: Create a map centered on Paris
    print("\n🗺️  Creating map...")
    poi_map = POIMap(48.8566, 2.3522, zoom_start=13)
    
    # TODO 4: Add all POIs to the map
    print("\n📍 Adding POIs to map...")
    poi_map.add_multiple_pois(all_pois)
    
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
    filename = poi_map.save_map("paris_pois_solution.html")
    
    # Automatically open the map in your browser
    print("\n🌐 Opening map in browser...")
    webbrowser.open(filename)
    
    
if __name__ == "__main__":
    main()
"""
SOLUTION: My Favorite Places Map

Complete solution for the beginner OOP mapping exercise
"""

import folium
import webbrowser
import math

# ============================================================================
# PART 1: BASE CLASS - Encapsulation
# ============================================================================

class Place:
    """A simple place with a name and coordinates."""
    
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
    def get_info(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"
    
    def distance_to(self, other_place):
        """Calculate distance to another place in kilometers"""
        lat_diff = self.latitude - other_place.latitude
        lon_diff = self.longitude - other_place.longitude
        distance_km = math.sqrt(lat_diff**2 + lon_diff**2) * 111
        return round(distance_km, 2)
    
    def get_marker_color(self):
        return "blue"
    
    def get_popup_text(self):
        return f"<b>{self.name}</b><br>Just a regular place"


# ============================================================================
# PART 2: INHERITANCE and POLYMORPHISM - Child Classes
# ============================================================================

class Restaurant(Place):
    """Restaurant class - inherits from Place"""
    
    def __init__(self, name, latitude, longitude, food_type):
        # Call parent constructor
        super().__init__(name, latitude, longitude)
        # Add new attribute
        self.food_type = food_type
    
    def get_popup_text(self):
        # Polymorphism: different text for restaurants
        return (f"<b>🍽️ RESTAURANT: {self.name}</b><br>"
                f"Food: {self.food_type}<br>"
                f"📍 {self.latitude}, {self.longitude}")
    
    def get_marker_color(self):
        # Polymorphism: different color for restaurants
        return "red"


class Park(Place):
    """Park class - inherits from Place"""
    
    def __init__(self, name, latitude, longitude, has_playground):
        super().__init__(name, latitude, longitude)
        self.has_playground = has_playground
    
    def get_popup_text(self):
        playground_text = "Yes" if self.has_playground else "No"
        return (f"<b>🌳 PARK: {self.name}</b><br>"
                f"Playground: {playground_text}<br>"
                f"📍 {self.latitude}, {self.longitude}")
    
    def get_marker_color(self):
        return "green"


class Museum(Place):
    """Museum class - inherits from Place"""
    
    def __init__(self, name, latitude, longitude, entry_fee):
        super().__init__(name, latitude, longitude)
        self.entry_fee = entry_fee
    
    def get_popup_text(self):
        fee_text = f"€{self.entry_fee}" if self.entry_fee > 0 else "Free"
        return (f"<b>🏛️ MUSEUM: {self.name}</b><br>"
                f"Entry: {fee_text}<br>"
                f"📍 {self.latitude}, {self.longitude}")
    
    def get_marker_color(self):
        return "purple"


# ============================================================================
# PART 3: MAP CLASS - Encapsulation
# ============================================================================

class MyMap:
    """Encapsulates all map-related functionality"""
    
    def __init__(self, city, zoom=12):
        self.city = city
        self.places = []
        
        # Map centers for some cities
        centers = {
            "Paris": [48.8566, 2.3522],
            "London": [51.5074, -0.1278],
            "New York": [40.7128, -74.0060],
            "Tokyo": [35.6762, 139.6503],
            "Rome": [41.9028, 12.4964],
            "Sydney": [-33.8688, 151.2093]
        }
        
        if city in centers:
            center = centers[city]
        else:
            center = [0, 0]
            print(f"Warning: {city} not in our list, using (0,0)")
        
        self.map = folium.Map(location=center, zoom_start=zoom)
        print(f"🗺️  Created map of {city}")
    
    def add_place(self, place):
        """Add a place to the map - demonstrates POLYMORPHISM"""
        self.places.append(place)
        
        # Different icons for different place types
        icon_type = "info-sign"
        if isinstance(place, Restaurant):
            icon_type = "cutlery"
        elif isinstance(place, Park):
            icon_type = "leaf"
        elif isinstance(place, Museum):
            icon_type = "bank"
        
        folium.Marker(
            location=[place.latitude, place.longitude],
            popup=folium.Popup(place.get_popup_text(), max_width=300),
            tooltip=place.name,
            icon=folium.Icon(color=place.get_marker_color(), 
                            icon=icon_type,
                            prefix='fa')
        ).add_to(self.map)
        
        print(f"  ✅ Added: {place.name}")
    
    def show_distances(self):
        """Show distances between all places"""
        if len(self.places) < 2:
            print("Add at least 2 places to see distances")
            return
        
        print(f"\n📏 Distances in {self.city}:")
        for i in range(len(self.places)):
            for j in range(i+1, len(self.places)):
                place1 = self.places[i]
                place2 = self.places[j]
                dist = place1.distance_to(place2)
                print(f"  {place1.name} → {place2.name}: {dist} km")
    
    def find_closest_places(self):
        """Find the two closest places on the map"""
        if len(self.places) < 2:
            return None
        
        min_distance = float('inf')
        closest_pair = None
        
        for i in range(len(self.places)):
            for j in range(i+1, len(self.places)):
                dist = self.places[i].distance_to(self.places[j])
                if dist < min_distance:
                    min_distance = dist
                    closest_pair = (self.places[i], self.places[j])
        
        return closest_pair, min_distance
    
    def save(self, filename="my_map.html"):
        """Save the map to an HTML file"""
        self.map.save(filename)
        print(f"\n💾 Map saved as '{filename}'")
        return filename


# ============================================================================
# PART 4: CREATE YOUR MAP!
# ============================================================================

def create_my_places():
    """Create a list of your favorite places"""
    places = []
    
    # Add restaurants
    places.append(Restaurant("Le Meurice", 48.8655, 2.3278, "French"))
    places.append(Restaurant("Cafe de Flore", 48.8540, 2.3325, "French"))
    places.append(Restaurant("Pizza Roma", 48.8570, 2.3450, "Italian"))
    
    # Add parks
    places.append(Park("Jardin du Luxembourg", 48.8462, 2.3372, True))
    places.append(Park("Tuileries Garden", 48.8639, 2.3272, True))
    places.append(Park("Parc Monceau", 48.8795, 2.3087, True))
    
    # Add museums
    places.append(Museum("Louvre Museum", 48.8606, 2.3376, 17))
    places.append(Museum("Musée d'Orsay", 48.8600, 2.3265, 14))
    
    return places


def main():
    """Main function"""
    print("=" * 50)
    print("🗺️  MY FAVORITE PLACES MAP")
    print("=" * 50)
    
    # Choose a city
    my_city = "Paris"
    
    # Create map
    mymap = MyMap(my_city)
    
    # Get places
    print("\n📝 Creating my favorite places...")
    my_places = create_my_places()
    
    # Add all places to the map
    print("\n📍 Adding places to map...")
    for place in my_places:
        mymap.add_place(place)
    
    # Show distances
    mymap.show_distances()
    
    # Find closest places
    closest, distance = mymap.find_closest_places()
    if closest:
        print(f"\n🎯 Closest places: {closest[0].name} and {closest[1].name}")
        print(f"   Distance: {distance} km")
    
    # Save map
    filename = mymap.save("my_paris_map.html")
    
    # Open in browser
    print("\n🌐 Opening map in browser...")
    webbrowser.open(filename)
    
    print("\n" + "=" * 50)
    print("✅ EXERCISE COMPLETE!")
    print("=" * 50)
    print("\n📚 OOP Concepts Demonstrated:")
    print("1. ENCAPSULATION: Place class bundles data + methods")
    print("2. INHERITANCE: Restaurant, Park, Museum inherit from Place")
    print("3. POLYMORPHISM: get_popup_text() works differently for each")
    print("4. ABSTRACTION: MyMap hides all the map complexity")
    
    # Bonus: Add a line between the two closest places
    if closest:
        line = folium.PolyLine(
            locations=[[closest[0].latitude, closest[0].longitude],
                      [closest[1].latitude, closest[1].longitude]],
            color='red',
            weight=2,
            popup=f"Closest pair: {distance} km"
        ).add_to(mymap.map)
        
        # Save updated map
        mymap.save("my_paris_map_with_line.html")
        print("\n🎁 Bonus: Added red line between closest places!")


# ============================================================================
# BONUS CHALLENGES - Solutions
# ============================================================================

class Cafe(Restaurant):
    """Bonus: Cafe class inherits from Restaurant"""
    
    def __init__(self, name, latitude, longitude, food_type, has_wifi):
        super().__init__(name, latitude, longitude, food_type)
        self.has_wifi = has_wifi
    
    def get_popup_text(self):
        wifi_text = "✅ WiFi" if self.has_wifi else "❌ No WiFi"
        return (f"<b>☕ CAFE: {self.name}</b><br>"
                f"Food: {self.food_type}<br>"
                f"{wifi_text}<br>"
                f"📍 {self.latitude}, {self.longitude}")


if __name__ == "__main__":
    main()
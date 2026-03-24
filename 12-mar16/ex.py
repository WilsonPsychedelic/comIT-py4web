import folium
import webbrowser
import math

class Place:
    """
    A simple place with a name and coordinates.

    ENCAPSULATION: This class bundles together:
   - Data: name, latitude, longitude
   - Methods: get_info(), distance_to()
    """

    def __init__(self, name, latitude, longitude):
        # Attributes (data)
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_info(self):
        """Return basic information about this place"""
        return f"{self.name} ({self.latitude}, {self.longitude})"

    def distance_to(self, other_place):
        """
        Calculate distance to another place in kilometers
        This is a simplified formula for beginners
        """
        # Difference in latitude and longitude
        lat_diff = self.latitude - other_place.latitude
        lon_diff = self.longitude - other_place.longitude

        # Simple Euclidean distance (good enough for learning)
        # 1 degree = 111 km
        distance_km = math.sqrt(lat_diff**2 + lon_diff**2) * 111

        return round(distance_km, 2)
    
    def get_marker_color(self):
        """Default marker color - will be overridden by child classes"""
        return "blue"
    
    def get_popup_text(self):
        """Text to show when clicking on marker"""
        return f"<b>{self.name}</b><br>Click for more info!"
    
    
class Restaurant(Place):
    def __init__(self, name, latitude, longitude, food_type):
        # Call the parent constructor
        super().__init__(name, latitude, longitude)

        #Store food_type
        self.food_type = food_type

    def get_popup_text(self):
        return f"<b>RESTAURANT: {self.name}</b><br>Food: {self.food_type}"
        
    def get_marker_color(self):
        return "red"
        
class Park(Place):
    def __init__(self, name, latitude, longitude, has_playground):
        # Call the parent constructor
        super().__init__(name, latitude, longitude)
    
        #Store has_playground
        self.has_playground = has_playground
    
    def get_popup_text(self):
        playground_text = "Yes" if self.has_playground else "No"
        return f"<b>PARK: {self.name}</b><br>Playground: {playground_text}"
        
    def get_marker_color(self):
        return "green"
    
    
class Museum(Place):
    def __init__(self, name, latitude, longitude, entry_fee):
        # Call the parent constructor
        super().__init__(name, latitude, longitude)

        # Store entry_fee
        self.entry_fee = entry_fee

    def get_popup_text(self):
        return f"<b>MUSEUM: {self.name}</b><br>Entry: €{self.entry_fee}"
            
    def get_marker_color(self):
        return "purple"
            
class MyMap:
    """
    This class ENCAPSULATES all map-related functionality
    """

    def __init__(self, city, zoom=12):
        """Create a new map centered on a city"""
        self.city = city
        self.places = []  # List to store all our places
        
        # Map centers for some cities
        centers = {
            "Paris": [48.8566, 2.3522],
            "London": [51.5074, -0.1278],
            "New York": [40.7128, -74.0060],
            "Tokyo": [35.6762, 139.6503]
            }
        
        # Get center coordinates or use default
        if city in centers:
            center = centers[city]
        else:
            center = [0, 0] # Default to (0,0)
            print(f"Warning: {city} not in our list, using (0,0)")
        
        # Create the map
        self.map = folium.Map(location=center, zoom_start=zoom)
        print(f"🗺️ Created map of {city}")
        
    def add_place(self, place):
        """
        Add a place to the map

        This demonstrates POLYMORPHISM - the same method works
        for any type of Place (Restaurant, Park, Museum)!
        """
        # Add to our list
        self.places.append(place)

        # Create a marker on the map
        folium.Marker(
            location=[place.latitude, place.longitude],
            popup=place.get_popup_text(), # Different for each place type!
            tooltip=place.name,
            icon=folium.Icon(color=place.get_marker_color()) # Different colors!
        ).add_to(self.map)

        print(f" ✅ Added: {place.name}")

    def show_distances(self):
        """
        Show distances between all places
        """
        if len(self.places) < 2:
            print("Add at least 2 places to see distances")
            return
                
        print(f"\n📏 Distances in {self.city}:")
        for i in range(len(self.places)):
            for j in range(i+1, len(self.places)):
                place1 = self.places[i]
                place2 = self.places[j]
                dist = place1.distance_to(place2)
                print(f" {place1.name} -> {place2.name}: {dist} km")
        
    def save(self, filename="my_map.html"):
        """Save the map to an HTML file"""
        self.map.save(filename)
        print(f"\n💾 Map saved as '{filename}'")
        return filename

def create_my_places():
    """
    Create a list of your favorite places
    """
    places = []
            
    # Add at least 2 restaurants
    restaurants = [
        Restaurant("Le Comptoir", 48.8528, 2.3332, "French"),
        Restaurant("Pizza Rossi", 48.8707, 2.3494, "Italian")
]
            
    # Add at least 2 parks
    parks = [
        Park("Luxembourg Garden", 48.8462, 2.3372, True),
        Park("Tuileries Garden", 48.8635, 2.3270, False)
        ]
            
    # Add at least 1 museum
    museums = [
        Museum("Louvre Museum", 48.8606, 2.3376, 17)
        ]
            
    # Combine all places
    places.extend(restaurants)
    places.extend(parks)
    places.extend(museums)
            
    return places
            
            
def main():
    """
    Main function - this is where your program starts!
    """
    print("=" * 50)
    print("🗺️ MY FAVORITE PLACES MAP")
    print("=" * 50)
    print("\nThis program demonstrates the 4 pillars of OOP:")
    print("1. ENCAPSULATION: Place class bundles data + methods")
    print("2. INHERITANCE: Restaurant, Park, Museum inherit from Place")
    print("3. POLYMORPHISM: get_popup_text() works differently for each")
    print("4. ABSTRACTION: MyMap hides map complexity")
    print("\n" + "-" * 50)

    # Choose a city
    my_city = "Paris"

    # Create a map
    mymap = MyMap(my_city)

    # Get your places
    my_places = create_my_places()

    print("\n📝 Adding your favorite places to the map...")

    # Add all places to the map
    for place in my_places:
        mymap.add_place(place)

    # Show distances between places
    mymap.show_distances()

    # Save the map
    filename = mymap.save("my_favorite_places.html")

    # Open in browser
    print("\n🌐 Opening map in browser...")
    webbrowser.open(filename)

    print("\n" + "=" * 50)
    print("✅ EXERCISE COMPLETE!")
    print("=" * 50)
    print("\nREFLECTION QUESTIONS:")
    print("1. How did Restaurant, Park, and Museum INHERIT from Place?")
    print("2. How is POLYMORPHISM shown when adding places to the map?")
    print("3. What data and methods are ENCAPSULATED in the Place class?")
    print("4. What complexity does the MyMap class ABSTRACT away?")
    print("\n🎯 BONUS: Try adding your own real favorite places!")

if __name__ == "__main__":
    main()
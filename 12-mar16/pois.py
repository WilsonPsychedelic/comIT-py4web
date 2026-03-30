"""
OOP Demonstration using Points of Interest (POI)
This file demonstrates the 4 pillars of Object-Oriented Programming:
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism
"""

import math

# ============================================================================
# 1. ENCAPSULATION - Bundling data and methods within a class, controlling access
# ============================================================================

class PointOfInterest:
    """
    Base class demonstrating ENCAPSULATION:
    - Data (attributes) are bundled with methods that operate on them
    - Name and coordinates are kept together
    - Distance calculation logic is contained within the class
    """
    
    def __init__(self, name, latitude, longitude):
        # Private attributes (by convention, _ indicates "protected" in Python)
        self._name = name
        self._latitude = latitude
        self._longitude = longitude
    
    # Getter methods - controlled access to private attributes
    def get_name(self):
        return self._name
    
    def get_latitude(self):
        return self._latitude
    
    def get_longitude(self):
        return self._longitude
    
    # Setter methods - controlled modification with validation
    def set_name(self, name):
        if name and isinstance(name, str):
            self._name = name
        else:
            print("Error: Name must be a non-empty string")
    
    def set_coordinates(self, latitude, longitude):
        # Simple validation for demo purposes
        if -90 <= latitude <= 90 and -180 <= longitude <= 180:
            self._latitude = latitude
            self._longitude = longitude
        else:
            print("Error: Invalid coordinates")
    
    # Method to calculate distance to another POI - demonstrates ENCAPSULATION
    def distance_to(self, other_poi):
        """
        Calculate distance to another POI
        Uses Euclidean for short distances, Haversine for long distances
        """
        # Check if points are relatively close (within ~10km)
        lat_diff = abs(self._latitude - other_poi.get_latitude())
        lon_diff = abs(self._longitude - other_poi.get_longitude())
        
        # If differences are small (less than 0.1 degrees ~ 11km), use Euclidean
        if lat_diff < 0.1 and lon_diff < 0.1:
            return self._euclidean_distance(other_poi)
        else:
            return self._haversine_distance(other_poi)
    
    # Private methods (by convention, __ indicates "private" in Python)
    def _euclidean_distance(self, other_poi):
        """Calculate Euclidean distance (for short distances)"""
        # Approximate conversion: 1 degree latitude ≈ 111 km
        lat_km = (self._latitude - other_poi.get_latitude()) * 111
        lon_km = (self._longitude - other_poi.get_longitude()) * 111 * math.cos(math.radians(self._latitude))
        return math.sqrt(lat_km**2 + lon_km**2)
    
    def _haversine_distance(self, other_poi):
        """Calculate Haversine distance (for long distances)"""
        R = 6371  # Earth's radius in kilometers
        
        lat1 = math.radians(self._latitude)
        lon1 = math.radians(self._longitude)
        lat2 = math.radians(other_poi.get_latitude())
        lon2 = math.radians(other_poi.get_longitude())
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        return R * c
    
    def __str__(self):
        """String representation of the POI"""
        return f"{self._name} ({self._latitude:.4f}°, {self._longitude:.4f}°)"


# ============================================================================
# 2. ABSTRACTION - Hiding complex implementation details, showing only essential features
# ============================================================================

class TouristAttraction(PointOfInterest):
    """
    Demonstrates ABSTRACTION:
    - Hides the complexity of entry fee calculation
    - Provides simple interface for visitors
    """
    
    def __init__(self, name, latitude, longitude, entry_fee=0):
        super().__init__(name, latitude, longitude)
        self._entry_fee = entry_fee
        self._visitors_today = 0
    
    # Abstracted method - user doesn't need to know how revenue is calculated
    def visit(self, number_of_visitors=1):
        """Simple interface for visiting the attraction"""
        self._visitors_today += number_of_visitors
        revenue = self._calculate_revenue(number_of_visitors)
        print(f"Welcome to {self.get_name()}! {number_of_visitors} visitor(s) added.")
        print(f"Today's revenue: ${revenue:.2f}")
        return revenue
    
    # Complex calculation hidden from the user
    def _calculate_revenue(self, visitors):
        """Hidden implementation detail"""
        base_revenue = visitors * self._entry_fee
        
        # Special discounts (hidden complexity)
        if visitors >= 10:
            base_revenue *= 0.9  # 10% group discount
        
        return base_revenue
    
    def get_stats(self):
        """Simple interface to get attraction statistics"""
        return {
            'name': self.get_name(),
            'visitors': self._visitors_today,
            'revenue': self._visitors_today * self._entry_fee
        }


# ============================================================================
# 3. INHERITANCE - Creating new classes based on existing ones
# ============================================================================

class Restaurant(PointOfInterest):
    """
    Demonstrates INHERITANCE:
    - Inherits all attributes and methods from PointOfInterest
    - Adds restaurant-specific features
    """
    
    def __init__(self, name, latitude, longitude, cuisine_type, price_range):
        # Call parent constructor to initialize inherited attributes
        super().__init__(name, latitude, longitude)
        
        # Add new attributes specific to Restaurant
        self._cuisine_type = cuisine_type
        self._price_range = price_range  # 1-4 ($ to $$$$)
        self._rating = 0
        self._reviews = []
    
    # New method specific to Restaurant
    def add_review(self, rating, comment):
        self._reviews.append({'rating': rating, 'comment': comment})
        # Update average rating
        total = sum(r['rating'] for r in self._reviews)
        self._rating = total / len(self._reviews)
        print(f"Review added for {self.get_name()}. New rating: {self._rating:.1f}/5")
    
    # Override the __str__ method (polymorphism)
    def __str__(self):
        price_symbols = "$" * self._price_range
        return f"{super().__str__()} - {self._cuisine_type} cuisine {price_symbols}"


class Museum(PointOfInterest):
    """
    Another class demonstrating INHERITANCE
    """
    
    def __init__(self, name, latitude, longitude, artifact_count, has_cafe=True):
        super().__init__(name, latitude, longitude)
        self._artifact_count = artifact_count
        self._has_cafe = has_cafe
        self._current_exhibition = "Permanent Collection"
    
    def set_exhibition(self, exhibition_name):
        self._current_exhibition = exhibition_name
        print(f"{self.get_name()} now showing: {exhibition_name}")
    
    # Override the __str__ method (polymorphism)
    def __str__(self):
        cafe_status = "with cafe" if self._has_cafe else "no cafe"
        return f"{super().__str__()} - Museum: {self._artifact_count} artifacts, {cafe_status}"


# ============================================================================
# 4. POLYMORPHISM - Same interface, different implementations
# ============================================================================

def display_poi_info(poi):
    """
    Demonstrates POLYMORPHISM:
    - Same function works with different types of POI
    - Each object's __str__ method is called appropriately
    """
    print(f"\n📍 POI Information:")
    print(f"   {poi}")
    
    # Check if it's a TouristAttraction (has visit method)
    if hasattr(poi, 'visit'):
        print(f"   This is a tourist attraction")
    
    # Check if it's a Restaurant (has cuisine_type)
    if hasattr(poi, '_cuisine_type'):
        print(f"   Cuisine: {poi._cuisine_type}")
    
    # Check if it's a Museum (has artifact_count)
    if hasattr(poi, '_artifact_count'):
        print(f"   Artifacts: {poi._artifact_count}")


# ============================================================================
# Demonstration of all 4 pillars
# ============================================================================

def main():
    print("=" * 60)
    print("DEMONSTRATING THE 4 PILLARS OF OOP")
    print("=" * 60)
    
    # 1. ENCAPSULATION Demo
    print("\n📦 1. ENCAPSULATION - Data and methods bundled together")
    print("-" * 50)
    
    eiffel = PointOfInterest("Eiffel Tower", 48.8584, 2.2945)
    louvre = PointOfInterest("Louvre Museum", 48.8606, 2.3376)
    
    print(f"Created: {eiffel}")
    print(f"Created: {louvre}")
    
    # Using getters
    print(f"\nControlled access via getters:")
    print(f"Name: {eiffel.get_name()}")
    print(f"Coordinates: {eiffel.get_latitude()}°, {eiffel.get_longitude()}°")
    
    # Using setters with validation
    print(f"\nControlled modification via setters:")
    eiffel.set_name("Eiffel Tower (Paris)")
    eiffel.set_coordinates(48.8584, 2.2945)  # Valid coordinates
    eiffel.set_coordinates(100, 200)  # Invalid coordinates (will show error)
    print(f"Updated: {eiffel}")
    
    # Distance calculation (internal logic encapsulated)
    distance = eiffel.distance_to(louvre)
    print(f"\nDistance calculation (encapsulated logic):")
    print(f"Distance from Eiffel Tower to Louvre: {distance:.2f} km")
    
    # 2. ABSTRACTION Demo
    print("\n\n🎯 2. ABSTRACTION - Hiding complex implementation")
    print("-" * 50)
    
    disney = TouristAttraction("Disneyland Paris", 48.8675, 2.7825, entry_fee=60)
    print(f"Created: {disney}")
    
    # Simple interface hides complex revenue calculation
    print(f"\nVisiting the attraction (simple interface):")
    disney.visit(5)
    disney.visit(12)  # Group discount applied automatically (hidden)
    
    # Get simple statistics (complex calculations hidden)
    stats = disney.get_stats()
    print(f"\nAttraction stats (simple output):")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # 3. INHERITANCE Demo
    print("\n\n🌳 3. INHERITANCE - Creating specialized classes")
    print("-" * 50)
    
    # Restaurant inherits from PointOfInterest
    restaurant = Restaurant("Le Meurice", 48.8655, 2.3278, "French", 4)
    print(f"Created Restaurant (inherits from POI):")
    print(f"  {restaurant}")
    
    # Using inherited method
    dist = restaurant.distance_to(eiffel)
    print(f"  Distance to Eiffel Tower: {dist:.2f} km (inherited method)")
    
    # Using new method
    restaurant.add_review(5, "Excellent!")
    restaurant.add_review(4, "Very good but expensive")
    
    # Museum inherits from PointOfInterest
    museum = Museum("Louvre Museum", 48.8606, 2.3376, 35000, True)
    print(f"\nCreated Museum (also inherits from POI):")
    print(f"  {museum}")
    museum.set_exhibition("Egyptian Treasures")
    
    # 4. POLYMORPHISM Demo
    print("\n\n🔄 4. POLYMORPHISM - Same interface, different behaviors")
    print("-" * 50)
    
    # Create a list of different POI types
    places = [
        PointOfInterest("Generic POI", 0, 0),
        TouristAttraction("Arc de Triomphe", 48.8738, 2.2950, 13),
        Restaurant("Cafe de Flore", 48.8540, 2.3325, "French", 3),
        Museum("Orsay Museum", 48.8600, 2.3265, 4000, True)
    ]
    
    print("All objects respond to the same interface differently:")
    for place in places:
        display_poi_info(place)  # Same function, different behaviors
    
    # Distance calculation works with any POI type (polymorphism)
    print("\n\nDistance calculations work with any POI type:")
    for i in range(len(places)-1):
        dist = places[i].distance_to(places[i+1])
        print(f"  Distance between place {i+1} and {i+2}: {dist:.2f} km")
    
    print("\n" + "=" * 60)
    print("✅ All 4 pillars of OOP demonstrated!")
    print("=" * 60)


if __name__ == "__main__":
    main()
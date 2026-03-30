
# Exercise Instructions for Students:

### Learning Objectives:

1.Practice implementing inheritance by creating specialized POI classes

2.Use polymorphism to customize marker colors and popups

3.Apply encapsulation by working with the POIMap class

4.Understand abstraction through the ParisPOIFetcher class

5.Learn to use external libraries (folium, osmnx) with OOP

### Step-by-Step Tasks:

#### Part 1: Implement the Classes (20-30 minutes)

1.Complete the Restaurant class constructor and methods

2.Complete the Museum class constructor and methods

3.Complete the Park class constructor and methods

#### Part 2: Complete the Map Class (15-20 minutes)

1.Implement the POIMap.__init__ method to create a folium map

2.Complete add_poi to create markers

3.Implement draw_distance_line to show distances

4.Add map controls in add_map_controls

#### Part 3: Fetch Real Data (20-30 minutes)

1.Implement fetch_restaurants using OSMnx

2.Implement fetch_museums using OSMnx

3.Implement fetch_parks using OSMnx

#### Part 4: Main Function (15 minutes)

1.Complete all TODOs in the main function

2.Test your code and view the map

### Expected Output:

* An interactive HTML map of Paris with colored markers for different POI types

* Popup windows with detailed information when clicking markers

* Distance lines between selected POIs

* Working map controls (zoom, fullscreen, measure tool)

### Hints:

* Marker colors help identify POI types at a glance

* OSMnx might sometimes fail - that's why we have sample data

* Use the browser's developer tools (F12) to debug JavaScript issues

* The distance calculation should work between any two POI objects

### Reflection Questions:

1.How does inheritance help you reuse code across different POI types?

2.Where do you see polymorphism in action when adding markers to the map?

3.How does the POIMap class encapsulate map-related functionality?

4.What complex details does the ParisPOIFetcher abstract away?

This exercise provides hands-on practice with OOP concepts while creating something visual and interactive that you can immediately see results from!

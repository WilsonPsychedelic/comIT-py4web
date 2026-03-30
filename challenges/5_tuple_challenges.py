# ============================================================
# Python Tuple Methods & Operations — 10 Beginner Challenges
# Practice each one before reading the hint!
# Hints are at the bottom of the file.
# ============================================================


# --------------------------------------------------------------
# Challenge 1 — Spot the Real Tuple
# Three variables are defined below. Print the type of each
# and identify which ones are actually tuples.
# Method: type()
# --------------------------------------------------------------

a = (42)
b = (42,)
c = (1, 2, 3)
# your code here


# --------------------------------------------------------------
# Challenge 2 — Index & Count
# Using the tuple below:
# 1. Find the index of the FIRST occurrence of "python".
# 2. Count how many times "python" appears in total.
# Methods: index(), count()
# --------------------------------------------------------------

langs = ("java", "python", "go", "python", "rust", "python")
# your code here


# --------------------------------------------------------------
# Challenge 3 — Unpack a Coordinate
# Unpack the tuple into three separate variables
# lat, lon, altitude and print each one on its own line.
# Method: tuple unpacking
# --------------------------------------------------------------

location = (43.65, -79.38, 76)
# your code here


# --------------------------------------------------------------
# Challenge 4 — Extended Unpacking
# Unpack the scores tuple so that:
# - first  = the first score
# - last   = the last score
# - rest   = all scores in between
# Then print all three.
# Method: * (star) unpacking
# --------------------------------------------------------------

scores = (88, 72, 95, 60, 83, 91)
# your code here


# --------------------------------------------------------------
# Challenge 5 — Swap Without a Temp Variable
# Swap the values of x and y using tuple unpacking
# in a single line, then print both variables.
# Method: tuple unpacking swap
# --------------------------------------------------------------

x = "hello"
y = "world"
# your code here


# --------------------------------------------------------------
# Challenge 6 — Concatenate & Repeat
# 1. Combine t1 and t2 into a new tuple called combined.
# 2. Create a tuple called repeated where t1 is repeated 4 times.
# Print both results.
# Operators: +, *
# --------------------------------------------------------------

t1 = (1, 2, 3)
t2 = (4, 5, 6)
# your code here


# --------------------------------------------------------------
# Challenge 7 — Tuple from a Function
# Write a function called stats() that receives a list of
# numbers and returns a tuple of (min, max, sum, count).
# Call it with the list below and unpack the result directly.
# Method: returning multiple values as a tuple
# --------------------------------------------------------------

data = [4, 8, 15, 16, 23, 42]
# your code here


# --------------------------------------------------------------
# Challenge 8 — Named Tuple Profile
# Create a named tuple called Student with fields:
# name, grade, subject.
# Instantiate one student, print their info by field name,
# then create a copy with an updated grade using _replace().
# Method: namedtuple, _replace()
# --------------------------------------------------------------

from collections import namedtuple
# your code here


# --------------------------------------------------------------
# Challenge 9 — Tuple as a Dictionary Key
# You have a list of (city, country) tuples paired with
# populations. Build a dictionary using the tuples as keys
# and populations as values, then look up Toronto's population.
# Method: tuple as dict key
# --------------------------------------------------------------

city_data = [
    (("Toronto",  "Canada"),   2_930_000),
    (("Paris",    "France"),   2_161_000),
    (("Tokyo",    "Japan"),   13_960_000),
]
# your code here


# --------------------------------------------------------------
# Challenge 10 — Sort a List of Tuples
# Sort the leaderboard by score (second element) from highest
# to lowest and print the ranked result.
# Method: sorted() with key=
# --------------------------------------------------------------

leaderboard = [("Alice", 88), ("Bob", 95), ("Charlie", 72), ("Diana", 90)]
# your code here


# ============================================================
# BONUS TIPS
# - A single-element tuple MUST have a trailing comma: (42,)
#   Without it, (42) is just an integer.
# - Tuples are immutable — you cannot append, remove, or sort
#   them in place. Use sorted() which returns a new list.
# - Prefer namedtuple over plain tuples when fields have meaning
#   — it makes code far easier to read and maintain.
# - Tuples are hashable (if their contents are), so they can
#   be used as dictionary keys or stored in sets.
# ============================================================


# ============================================================
# HINTS — try to solve each challenge before reading these!
# ============================================================

# Challenge 1:  (42) is just parentheses around an int; the comma in (42,) makes it a tuple.

# Challenge 2:  index() returns the position of the first match; count() tallies all occurrences.

# Challenge 3:  List the variable names on the left separated by commas: lat, lon, altitude = ...

# Challenge 4:  Place * before the middle variable to capture everything between first and last.

# Challenge 5:  Write x, y = y, x — Python evaluates the right side first as a tuple, then unpacks.

# Challenge 6:  Use + to join tuples and * to repeat; both always produce a NEW tuple.

# Challenge 7:  Return multiple values separated by commas — Python automatically packs them into a tuple.

# Challenge 8:  namedtuple("Student", ["name","grade","subject"]); _replace() returns a NEW tuple.

# Challenge 9:  Use the (city, country) tuple directly as the dictionary key inside {}.

# Challenge 10: sorted(leaderboard, key=lambda item: item[1], reverse=True) sorts by the second element.

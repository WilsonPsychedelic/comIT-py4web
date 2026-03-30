# ============================================================
# Python Set Methods — 10 Beginner Challenges
# Practice each one before reading the hint!
# Hints are at the bottom of the file.
# ============================================================


# --------------------------------------------------------------
# Challenge 1 — No Duplicates Allowed
# Convert the list below into a set to remove duplicates,
# then print how many unique numbers there are.
# Method: set(), len()
# --------------------------------------------------------------

numbers = [4, 2, 7, 2, 9, 4, 1, 7, 7]
# your code here


# --------------------------------------------------------------
# Challenge 2 — Build a Tag Set
# Start with an empty set and add "python", "code", and
# "beginner" one at a time, then print the set.
# Method: add()
# --------------------------------------------------------------

tags = set()
# your code here


# --------------------------------------------------------------
# Challenge 3 — Bulk Import
# You already have some skills. Add all items from new_skills
# into existing_skills in a single call, then print the result.
# Method: update()
# --------------------------------------------------------------

existing_skills = {"python", "sql"}
new_skills = ["git", "linux", "docker"]
# your code here


# --------------------------------------------------------------
# Challenge 4 — Safe Removal
# Try to remove "javascript" from the set below. It may or may
# not be present — make sure no error is raised either way.
# Method: discard()
# --------------------------------------------------------------

languages = {"python", "ruby", "go"}
# your code here


# --------------------------------------------------------------
# Challenge 5 — Common Interests
# Find the movies that BOTH Alice and Bob have watched.
# Print the shared titles.
# Method: intersection() or &
# --------------------------------------------------------------

alice_watched = {"Inception", "Dune", "Matrix", "Interstellar"}
bob_watched   = {"Dune", "Matrix", "Tenet", "Arrival"}
# your code here


# --------------------------------------------------------------
# Challenge 6 — Full Catalogue
# Combine both music libraries into one complete set of songs
# without modifying the originals. Print the result.
# Method: union() or |
# --------------------------------------------------------------

library_a = {"Song A", "Song B", "Song C"}
library_b = {"Song C", "Song D", "Song E"}
# your code here


# --------------------------------------------------------------
# Challenge 7 — Exclusive Items
# Find items that are in cart_a OR cart_b, but NOT in both.
# Method: symmetric_difference() or ^
# --------------------------------------------------------------

cart_a = {"apple", "milk", "bread", "eggs"}
cart_b = {"milk", "eggs", "butter", "cheese"}
# your code here


# --------------------------------------------------------------
# Challenge 8 — Who Didn't RSVP?
# Find attendees who were invited but did NOT confirm.
# Method: difference() or -
# --------------------------------------------------------------

invited   = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
confirmed = {"Alice", "Diana", "Eve"}
# your code here


# --------------------------------------------------------------
# Challenge 9 — Subset Check
# Check if required_fields is a subset of submitted_fields,
# then print a message saying if the form is complete or not.
# Method: issubset() or <=
# --------------------------------------------------------------

required_fields  = {"name", "email", "age"}
submitted_fields = {"name", "email", "age", "phone", "city"}
# your code here


# --------------------------------------------------------------
# Challenge 10 — No Overlap?
# Check whether the day_shift and night_shift workers share
# no employees (i.e. no one is working both shifts).
# Method: isdisjoint()
# --------------------------------------------------------------

day_shift   = {"Alice", "Bob", "Charlie"}
night_shift = {"Diana", "Eve", "Frank"}
# your code here


# ============================================================
# BONUS TIPS
# - Sets are UNORDERED — you cannot index or slice them.
# - Use discard() instead of remove() when unsure if an element exists.
# - set() on a string splits it into individual characters.
# - Operators (|, &, -, ^) only work between sets; methods
#   (.union(), .intersection(), etc.) accept any iterable.
# ============================================================


# ============================================================
# HINTS — try to solve each challenge before reading these!
# ============================================================

# Challenge 1:  Pass the list directly to set() — duplicates disappear automatically.

# Challenge 2:  add() takes a single element; calling it multiple times builds the set.

# Challenge 3:  update() accepts any iterable and adds all its elements in one call.

# Challenge 4:  discard() silently ignores missing elements; remove() raises KeyError.

# Challenge 5:  a & b (or a.intersection(b)) returns only elements present in both sets.

# Challenge 6:  a | b (or a.union(b)) returns a NEW set; neither original is changed.

# Challenge 7:  a ^ b gives elements that are in one set or the other, but not both.

# Challenge 8:  a - b (or a.difference(b)) gives elements in a that are not in b.

# Challenge 9:  issubset() returns True if every element of the set is in the argument.

# Challenge 10: isdisjoint() returns True if the two sets share zero elements.

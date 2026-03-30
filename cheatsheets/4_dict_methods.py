# ============================================================
# Python Dictionary Methods - Overview & Common Variations
# ============================================================

person = {"name": "Alice", "age": 30, "city": "Toronto"}

# ------ Accessing Elements ------

name = person["name"]               # Direct access (raises KeyError if missing)
age = person.get("age")             # Safe access, returns None if missing
country = person.get("country", "Unknown")  # Safe access with default value

# ------ Adding & Updating Elements ------

person["email"] = "alice@example.com"   # Add new key or overwrite existing
person.update({"age": 31, "job": "Dev"})# Update multiple keys at once
person.update(age=32, city="Montreal")  # update() also accepts keyword arguments

# setdefault() — sets a key only if it doesn't already exist
person.setdefault("nickname", "Ali")    # Adds "nickname": "Ali"
person.setdefault("name", "Bob")        # Does nothing — "name" already exists

# ------ Removing Elements ------

removed = person.pop("email")           # Remove key & return its value (raises KeyError if missing)
removed_safe = person.pop("phone", None)# Remove with default — avoids KeyError
last = person.popitem()                 # Remove & return the last inserted (key, value) pair
del person["nickname"]                  # Delete key directly (raises KeyError if missing)
person.clear()                          # Remove all key-value pairs

# ------ Views — Dynamic, Reflect Changes ------

person = {"name": "Alice", "age": 30, "city": "Toronto"}

keys   = person.keys()      # dict_keys view of all keys
values = person.values()    # dict_values view of all values
items  = person.items()     # dict_items view of all (key, value) tuples

# Convert views to static lists when you need to iterate and modify simultaneously
keys_list   = list(person.keys())
values_list = list(person.values())
items_list  = list(person.items())

# ------ Iterating ------

for key in person:                      # Iterate over keys (default)
    print(key)

for value in person.values():           # Iterate over values
    print(value)

for key, value in person.items():       # Iterate over key-value pairs (most common)
    print(f"{key}: {value}")

# ------ Copying ------

shallow = person.copy()                 # Shallow copy — nested objects still shared

import copy
nested = {"user": {"name": "Alice", "scores": [10, 20]}}
deep = copy.deepcopy(nested)            # Deep copy — fully independent clone

# ------ Merging Dictionaries ------

defaults = {"theme": "light", "lang": "en", "debug": False}
user_prefs = {"theme": "dark", "lang": "fr"}

# Python 3.9+ merge operator — returns a new dict, right side wins on conflict
merged = defaults | user_prefs          # {"theme": "dark", "lang": "fr", "debug": False}

# Python 3.9+ in-place merge
defaults |= user_prefs                  # Updates defaults in place

# Works in all versions — unpack into a new dict, right side wins
merged_compat = {**defaults, **user_prefs}

# ------ Building Dictionaries ------

# dict.fromkeys() — create a dict from a list of keys with a shared default value
keys = ["a", "b", "c"]
zeroed = dict.fromkeys(keys, 0)         # {"a": 0, "b": 0, "c": 0}
empty_vals = dict.fromkeys(keys)        # {"a": None, "b": None, "c": None}

# Dict comprehension — concise way to build or transform dicts
squares = {x: x**2 for x in range(1, 6)}                    # {1:1, 2:4, 3:9, 4:16, 5:25}
filtered = {k: v for k, v in squares.items() if v > 5}      # Keep only values > 5
inverted = {v: k for k, v in person.items()}                 # Swap keys and values

# ------ Sorting ------

scores = {"Bob": 88, "Alice": 95, "Charlie": 72}

# sorted() on a dict iterates over keys by default
sorted_keys = sorted(scores)                                  # Sort keys alphabetically
sorted_by_val = sorted(scores, key=lambda k: scores[k])      # Sort keys by their value
sorted_desc  = sorted(scores, key=lambda k: scores[k], reverse=True)  # Descending

# Rebuild a sorted dict (preserves insertion order in Python 3.7+)
sorted_dict = dict(sorted(scores.items(), key=lambda item: item[1]))

# ------ Checking Membership ------

print("name" in person)                 # True — checks keys
print("Alice" in person.values())       # True — checks values
print(("name", "Alice") in person.items())  # True — checks key-value pair

# ------ Other Useful Patterns ------

# Counting occurrences with a dict
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1    # {"apple": 3, "banana": 2, "cherry": 1}

# Same thing using collections.Counter (recommended for counting)
from collections import Counter
count = Counter(words)                       # Counter({"apple": 3, "banana": 2, "cherry": 1})
most_common = count.most_common(2)           # [("apple", 3), ("banana", 2)]

# Grouping items with setdefault
animals = [("mammal", "dog"), ("bird", "eagle"), ("mammal", "cat"), ("bird", "parrot")]
grouped = {}
for category, animal in animals:
    grouped.setdefault(category, []).append(animal)
# {"mammal": ["dog", "cat"], "bird": ["eagle", "parrot"]}

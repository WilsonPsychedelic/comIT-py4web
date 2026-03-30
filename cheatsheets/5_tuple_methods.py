# ============================================================
# Python Tuple Methods & Operations - Overview
# Tuples are IMMUTABLE — they cannot be changed after creation.
# ============================================================

coords  = (10, 20, 30)
mixed   = (1, "hello", 3.14, True)
single  = (42,)             # Trailing comma is REQUIRED for a single-element tuple
not_tuple = (42)            # This is just an int — parentheses alone don't make a tuple

# ------ Creating Tuples ------

empty      = ()                     # Empty tuple
from_list  = tuple([1, 2, 3])       # Convert list to tuple
from_str   = tuple("abc")           # ('a', 'b', 'c')
from_range = tuple(range(5))        # (0, 1, 2, 3, 4)

# ------ The Only Two Tuple Methods ------

t = (3, 1, 4, 1, 5, 9, 2, 6, 1)

idx   = t.index(1)          # Index of the FIRST occurrence of 1 → 1
idx2  = t.index(1, 2)       # Search starting from index 2 → 5
idx3  = t.index(1, 2, 7)    # Search between index 2 and 7 (exclusive) → 5
count = t.count(1)          # Number of times 1 appears → 3

# ------ Accessing Elements ------

point = (10, 20, 30, 40, 50)

first  = point[0]           # Indexing — same as lists
last   = point[-1]          # Negative index from the end
sliced = point[1:4]         # Slicing returns a new tuple: (20, 30, 40)
every2 = point[::2]         # Step slicing: (10, 30, 50)

# ------ Unpacking — Tuples Shine Here ------

x, y, z = (1, 2, 3)                        # Basic unpacking — must match exactly
first, *rest = (1, 2, 3, 4, 5)             # Extended: first=1, rest=[2,3,4,5]
*start, last = (1, 2, 3, 4, 5)             # start=[1,2,3,4], last=5
a, *middle, b = (1, 2, 3, 4, 5)            # a=1, middle=[2,3,4], b=5

# Swap variables without a temp variable
a, b = 10, 20
a, b = b, a                                # a=20, b=10 — classic Pythonic swap

# Unpack from a function returning multiple values
def min_max(values):
    return min(values), max(values)        # Returns a tuple implicitly

low, high = min_max([3, 1, 4, 1, 5, 9])   # low=1, high=9

# Unpack nested tuples
(name, (lat, lon)) = ("Toronto", (43.65, -79.38))

# ------ Iteration & Membership ------

rgb = (255, 128, 0)

for channel in rgb:             # Iterate like a list
    print(channel)

print(128 in rgb)               # True  — membership check
print(999 not in rgb)           # True
print(len(rgb))                 # 3

# enumerate() gives index + value pairs
for i, val in enumerate(rgb):
    print(f"Channel {i}: {val}")

# ------ Tuple Operations ------

t1 = (1, 2, 3)
t2 = (4, 5, 6)

combined   = t1 + t2            # Concatenation → (1, 2, 3, 4, 5, 6)
repeated   = t1 * 3             # Repetition    → (1, 2, 3, 1, 2, 3, 1, 2, 3)
length     = len(t1)            # 3
minimum    = min(t1)            # 1
maximum    = max(t1)            # 3
total      = sum(t1)            # 6
sorted_new = sorted(t1)         # Returns a LIST [1, 2, 3], not a tuple

# ------ Named Tuples — Self-Documenting Tuples ------

from collections import namedtuple

Point  = namedtuple("Point",  ["x", "y"])
Person = namedtuple("Person", ["name", "age", "city"])

p = Point(3, 7)
print(p.x, p.y)                 # Access by name (readable) or index
print(p[0], p[1])               # Same values via index

alice = Person("Alice", 30, "Toronto")
print(alice.name, alice.age)    # Much clearer than alice[0], alice[1]

# _asdict() — convert to an OrderedDict
print(alice._asdict())          # {"name": "Alice", "age": 30, "city": "Toronto"}

# _replace() — create a new tuple with some fields changed (immutability preserved)
older_alice = alice._replace(age=31)

# ------ Tuples as Dict Keys ------

# Lists cannot be dict keys (mutable), but tuples can (immutable/hashable)
locations = {
    (43.65, -79.38): "Toronto",
    (48.85,   2.35): "Paris",
    (35.68, 139.69): "Tokyo",
}
print(locations[(43.65, -79.38)])   # "Toronto"

# ------ Tuple vs List — When to Use Each ------

# Use TUPLES for:
# - Fixed collections that should not change (coordinates, RGB, DB records)
# - Returning multiple values from a function
# - Dictionary keys
# - Slight memory/speed advantage over lists

# Use LISTS for:
# - Collections that need to grow, shrink, or be sorted in place
# - Any situation requiring mutation

# Memory comparison
import sys
lst = [1, 2, 3, 4, 5]
tpl = (1, 2, 3, 4, 5)
print(sys.getsizeof(lst))       # Typically larger
print(sys.getsizeof(tpl))       # Typically smaller

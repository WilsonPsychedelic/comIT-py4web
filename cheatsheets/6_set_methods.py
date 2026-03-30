# ============================================================
# Python Set Methods - Overview & Common Variations
# ============================================================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# ------ Creating Sets ------

empty = set()                   # Empty set — NOT {} (that creates an empty dict!)
from_list = set([1, 2, 2, 3])   # Duplicates are removed automatically: {1, 2, 3}
from_str  = set("hello")        # Each character becomes an element: {'h','e','l','o'}

# ------ Adding & Removing Elements ------

a.add(6)                        # Add a single element (no-op if already present)
a.update([7, 8, 9])             # Add multiple elements from any iterable
a.update([10], {11}, (12,))     # update() accepts multiple iterables at once

a.remove(12)                    # Remove element (raises KeyError if missing)
a.discard(99)                   # Remove element — silently does nothing if missing
popped = a.pop()                # Remove & return an ARBITRARY element (sets are unordered)
a.clear()                       # Remove all elements

# ------ Set Operations — return NEW sets ------

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

union        = a | b            # All elements from both sets
intersection = a & b            # Only elements present in BOTH
difference   = a - b            # Elements in a but NOT in b
sym_diff     = a ^ b            # Elements in either, but NOT in both

# Method equivalents (also accept any iterable, not just sets)
union        = a.union(b)
intersection = a.intersection(b)
difference   = a.difference(b)
sym_diff     = a.symmetric_difference(b)

# Multiple sets at once (methods only)
c = {3, 4, 9, 10}
multi_union = a.union(b, c)             # Union of three sets
multi_inter = a.intersection(b, c)      # Intersection of three sets

# ------ In-Place Set Operations — modify the original ------

a |= b                          # Add all elements of b into a
a &= b                          # Keep only elements also in b
a -= b                          # Remove all elements found in b
a ^= b                          # Keep only elements not shared with b

# Method equivalents
a = {1, 2, 3, 4, 5}
a.update(b)                             # Same as a |= b
a.intersection_update(b)                # Same as a &= b
a.difference_update(b)                  # Same as a -= b
a.symmetric_difference_update(b)        # Same as a ^= b

# ------ Comparison & Relationships ------

x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
z = {6, 7}

print(x.issubset(y))        # True  — all of x's elements are in y
print(y.issuperset(x))      # True  — y contains all of x's elements
print(x.isdisjoint(z))      # True  — x and z share no elements
print(x == y)               # False — sets are equal only if identical

# Subset/superset shorthand operators
print(x <= y)               # issubset:   x <= y
print(x < y)                # proper subset: x < y (x <= y AND x != y)
print(y >= x)               # issuperset: y >= x
print(y > x)                # proper superset

# ------ Copying ------

original = {1, 2, 3}
shallow  = original.copy()      # Independent shallow copy
also_ref = original             # NOT a copy — same object in memory!

# ------ Membership & Info ------

nums = {10, 20, 30}

print(20 in nums)               # True  — O(1) average, much faster than list search
print(99 not in nums)           # True
print(len(nums))                # 3 — number of elements

# ------ Frozenset — Immutable Set ------

fs = frozenset([1, 2, 3, 2])   # Like a set but cannot be modified after creation
# fs.add(4)                    # AttributeError — frozensets have no add/remove
print(fs & {2, 3, 4})          # Set operations still work on frozensets
nested = {frozenset([1, 2]), frozenset([3, 4])}  # Can be used as dict keys or inside sets

# ------ Common Patterns ------

# Remove duplicates from a list while preserving nothing about order
items  = [3, 1, 2, 1, 3, 4]
unique = list(set(items))       # [1, 2, 3, 4] — order not guaranteed

# Find items in one list but not another
all_users   = {"Alice", "Bob", "Charlie", "Diana"}
active      = {"Alice", "Diana"}
inactive    = all_users - active        # {"Bob", "Charlie"}

# Check if two lists share any element
likes_python = {"Alice", "Bob", "Eve"}
likes_java   = {"Bob", "Charlie", "Eve"}
both         = likes_python & likes_java        # {"Bob", "Eve"}
neither      = likes_python.isdisjoint({"Dave", "Frank"})  # True

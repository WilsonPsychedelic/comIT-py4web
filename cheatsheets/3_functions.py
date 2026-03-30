# ============================================================
# Python Functions — Complete Overview
# ============================================================


# ============================================================
# 1. FUNCTION WITH NO ARGUMENTS
# ============================================================

def greet():
    print("Hello, World!")

greet()                         # Call with no arguments


# ============================================================
# 2. FUNCTION WITH ARGUMENTS (POSITIONAL)
# ============================================================

def greet_user(name, message):
    print(f"{message}, {name}!")

greet_user("Alice", "Hello")    # Arguments matched by position


# ============================================================
# 3. DEFAULT ARGUMENT VALUES
# ============================================================

def greet_default(name, message="Hello"):
    print(f"{message}, {name}!")

greet_default("Bob")            # Uses default: "Hello, Bob!"
greet_default("Bob", "Hi")      # Overrides default: "Hi, Bob!"

# Note: default arguments must come AFTER non-default ones
# def wrong(name="Alice", age):  ← SyntaxError


# ============================================================
# 4. KEYWORD ARGUMENTS
# ============================================================

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

create_profile(age=30, city="Toronto", name="Alice")  # Order doesn't matter
create_profile("Bob", city="Paris", age=25)           # Mix positional + keyword


# ============================================================
# 5. POSITIONAL-ONLY ARGUMENTS (Python 3.8+)
# Use / to mark everything before it as positional-only
# ============================================================

def circle_area(radius, /):
    import math
    return math.pi * radius ** 2

circle_area(5)                  # OK
# circle_area(radius=5)         # TypeError — radius is positional-only


# ============================================================
# 6. KEYWORD-ONLY ARGUMENTS
# Use * to mark everything after it as keyword-only
# ============================================================

def send_email(to, *, subject, body):
    print(f"To: {to} | Subject: {subject}")

send_email("alice@x.com", subject="Hi", body="Hello!")
# send_email("alice@x.com", "Hi", "Hello!")  # TypeError — subject must be named


# ============================================================
# 7. COMBINED ARGUMENT TYPES
# Order: positional-only / regular / *args / keyword-only / **kwargs
# ============================================================

def full_signature(pos_only, /, regular, *args, kw_only, **kwargs):
    print(f"pos_only={pos_only}, regular={regular}")
    print(f"args={args}, kw_only={kw_only}, kwargs={kwargs}")

full_signature(1, 2, 3, 4, kw_only="must_name", extra="yes")


# ============================================================
# 8. *ARGS — VARIABLE POSITIONAL ARGUMENTS
# Collects extra positional arguments into a tuple
# ============================================================

def add(*args):
    return sum(args)

add(1, 2)                       # 3
add(1, 2, 3, 4, 5)             # 15
add()                           # 0 — works with zero args too

def log(level, *messages):      # First arg captured normally, rest go to *messages
    for msg in messages:
        print(f"[{level}] {msg}")

log("INFO", "Server started", "Listening on port 8080")

# Unpacking a list/tuple into positional args with *
nums = [1, 2, 3]
print(add(*nums))               # Same as add(1, 2, 3)


# ============================================================
# 9. **KWARGS — VARIABLE KEYWORD ARGUMENTS
# Collects extra keyword arguments into a dict
# ============================================================

def build_tag(tag, **attributes):
    attrs = " ".join(f'{k}="{v}"' for k, v in attributes.items())
    return f"<{tag} {attrs}>"

build_tag("a", href="https://python.org", target="_blank")
build_tag("img", src="logo.png", alt="Logo", width="200")

def create_user(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

create_user(name="Alice", age=30, city="Toronto", admin=True)

# Unpacking a dict into keyword args with **
settings = {"href": "https://python.org", "target": "_blank"}
print(build_tag("a", **settings))   # Same as passing each key=value


# ============================================================
# 10. RETURN VALUES
# ============================================================

def square(n):
    return n ** 2               # Returns a single value

result = square(5)              # 25

# Return multiple values — Python packs them into a tuple
def min_max(values):
    return min(values), max(values)

low, high = min_max([3, 1, 4, 1, 5, 9])    # Unpack directly

# Return early to exit a function before the end
def find_first(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i            # Exits immediately
    return -1                   # Default if not found

# Functions with NO explicit return statement return None
def do_nothing():
    pass

print(do_nothing())             # None


# ============================================================
# 11. TYPE HINTS (Annotations)
# Not enforced at runtime, but great for readability & tooling
# ============================================================

def add_numbers(a: int, b: int) -> int:
    return a + b

def greet_typed(name: str, times: int = 1) -> None:
    for _ in range(times):
        print(f"Hello, {name}!")

from typing import Optional, Union, List, Dict, Tuple

def find_user(user_id: int) -> Optional[str]:   # May return str or None
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

def process(value: Union[int, float]) -> float: # Accepts int or float
    return float(value) * 2

def summarize(data: List[int]) -> Dict[str, int]:
    return {"min": min(data), "max": max(data), "sum": sum(data)}


# ============================================================
# 12. DOCSTRINGS
# ============================================================

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Returns:
        BMI as a float rounded to 2 decimal places.

    Raises:
        ValueError: If height is zero or negative.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return round(weight_kg / height_m ** 2, 2)

help(calculate_bmi)             # Displays the docstring
print(calculate_bmi.__doc__)    # Raw docstring string


# ============================================================
# 13. LAMBDA FUNCTIONS — anonymous one-liners
# ============================================================

square   = lambda x: x ** 2
add      = lambda x, y: x + y
clamp    = lambda x, lo, hi: max(lo, min(x, hi))

print(square(5))                # 25
print(add(3, 4))                # 7
print(clamp(150, 0, 100))       # 100

# Most useful as inline callbacks
nums   = [3, -1, 4, -1, 5, -9]
pos    = list(filter(lambda x: x > 0, nums))        # [3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))          # [6,-2,8,-2,10,-18]
people = [("Bob", 30), ("Alice", 25), ("Eve", 35)]
people.sort(key=lambda p: p[1])                     # Sort by age


# ============================================================
# 14. HIGHER-ORDER FUNCTIONS
# Functions that accept or return other functions
# ============================================================

# Passing a function as an argument
def apply(func, value):
    return func(value)

apply(square, 6)                # 36
apply(str.upper, "hello")       # "HELLO"

# Returning a function (closure)
def make_multiplier(factor):
    def multiplier(x):          # Inner function captures `factor`
        return x * factor
    return multiplier           # Returns the function itself

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))                # 10
print(triple(5))                # 15

# Built-in higher-order functions
nums   = [1, 2, 3, 4, 5, 6]
evens  = list(filter(lambda x: x % 2 == 0, nums))          # [2,4,6]
squares = list(map(lambda x: x**2, nums))                   # [1,4,9,16,25,36]

from functools import reduce
product = reduce(lambda acc, x: acc * x, nums)              # 720


# ============================================================
# 15. DECORATORS
# Wrap a function to add behaviour without changing its code
# ============================================================

import time
from functools import wraps

# Simple decorator
def timer(func):
    @wraps(func)                # Preserves original function's name & docstring
    def wrapper(*args, **kwargs):
        start  = time.perf_counter()
        result = func(*args, **kwargs)
        end    = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer                          # Sugar for: slow_sum = timer(slow_sum)
def slow_sum(n):
    return sum(range(n))

slow_sum(1_000_000)

# Decorator with arguments
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")              # Prints 3 times

# Stacking decorators (applied bottom-up)
@timer
@repeat(times=2)
def process(n):
    return n * 2

process(5)


# ============================================================
# 16. GENERATORS — functions that yield values lazily
# ============================================================

def count_up(limit):
    n = 0
    while n < limit:
        yield n                 # Pauses here and returns value to caller
        n += 1

gen = count_up(5)
print(next(gen))                # 0
print(next(gen))                # 1
for val in count_up(5):         # Works in for loops too
    print(val)

# Generator expression (no function needed for simple cases)
squares_gen = (x**2 for x in range(10))  # Lazy — no list built in memory

# yield from — delegate to another iterable
def chain(*iterables):
    for it in iterables:
        yield from it           # Flattens one level

list(chain([1, 2], [3, 4], [5]))    # [1, 2, 3, 4, 5]


# ============================================================
# 17. RECURSIVE FUNCTIONS
# ============================================================

def factorial(n: int) -> int:
    if n <= 1:                  # Base case — must always exist
        return 1
    return n * factorial(n - 1) # Recursive case

factorial(5)                    # 120

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Recursion with memoization (cache) to avoid re-computation
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n: int) -> int:
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

fib_cached(50)                  # Fast — results are cached


# ============================================================
# 18. FUNCTION INTROSPECTION
# ============================================================

import inspect

def example(a: int, b: str = "hi", *args, kw: bool = False, **kwargs):
    """Example function for introspection."""
    pass

print(example.__name__)         # "example"
print(example.__doc__)          # Docstring
print(example.__annotations__)  # Type hints dict
print(inspect.signature(example))           # Full signature string
print(inspect.getfullargspec(example))      # Detailed arg info

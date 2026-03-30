# ============================================================
# Python Functions — 10 Beginner Challenges
# Practice each one before reading the hint!
# Hints are at the bottom of the file.
# ============================================================


# --------------------------------------------------------------
# Challenge 1 — Temperature Converter
# Write a function called celsius_to_fahrenheit(celsius) that
# converts a Celsius value to Fahrenheit and RETURNS the result.
# Formula: F = (C * 9/5) + 32
# Then write a second function fahrenheit_to_celsius(fahrenheit)
# for the reverse. Call both and print the results.
# Concept: function with argument, return value
# --------------------------------------------------------------

# your code here


# --------------------------------------------------------------
# Challenge 2 — Greeting with Default
# Write a function called greet(name, greeting="Hello") that
# prints "<greeting>, <name>!".
# Call it three ways:
#   1. With only a name
#   2. With a name and custom greeting
#   3. Using keyword arguments in reverse order
# Concept: default argument, keyword arguments
# --------------------------------------------------------------

# your code here


# --------------------------------------------------------------
# Challenge 3 — Flexible Sum
# Write a function called total(*args) that accepts ANY number
# of numeric arguments and returns their sum.
# Test it with 0, 3, and 6 arguments.
# Then write running_total(*args) that returns a list of
# cumulative sums: e.g. (1,2,3,4) -> [1, 3, 6, 10]
# Concept: *args
# --------------------------------------------------------------

# your code here


# --------------------------------------------------------------
# Challenge 4 — HTML Tag Builder
# Write a function called tag(name, content, **attrs) that
# builds and returns an HTML string like:
#   <a href="https://python.org" target="_blank">Python</a>
# The name and content are required; all other attributes
# are passed as keyword arguments.
# Concept: **kwargs
# --------------------------------------------------------------

# your code here


# --------------------------------------------------------------
# Challenge 5 — Return Multiple Values
# Write a function called analyze(numbers) that receives a list
# and returns a tuple of (minimum, maximum, mean, count).
# Unpack the return value directly when calling the function
# and print each value with a label.
# Concept: returning multiple values, tuple unpacking
# --------------------------------------------------------------

data = [12, 45, 7, 23, 56, 3, 89, 34]
# your code here


# --------------------------------------------------------------
# Challenge 6 — Type-Hinted Calculator
# Write four functions: add, subtract, multiply, divide.
# Each accepts two floats and returns a float.
# Add full type hints and a one-line docstring to each.
# divide() should handle ZeroDivisionError and return None.
# Concept: type hints, docstrings, None return
# --------------------------------------------------------------

# your code here


# --------------------------------------------------------------
# Challenge 7 — Decorator: Logger
# Write a decorator called log_call that prints:
#   "Calling <function_name> with args=... kwargs=..."
# before the function runs, and:
#   "<function_name> returned <result>"
# after it returns.
# Apply it to a function multiply(a, b) that returns a * b.
# Concept: decorator, *args/**kwargs forwarding, @wraps
# --------------------------------------------------------------

from functools import wraps
# your code here


# --------------------------------------------------------------
# Challenge 8 — Generator: Fibonacci Sequence
# Write a generator function called fibonacci(limit) that
# yields Fibonacci numbers up to (but not exceeding) limit.
# Collect the results into a list and print it.
# Concept: generator, yield
# --------------------------------------------------------------

# your code here


# --------------------------------------------------------------
# Challenge 9 — Closure: Make Counter
# Write a function called make_counter(start=0, step=1) that
# returns an inner function. Each time the inner function is
# called it should return the next value in the sequence.
# Create two independent counters and show they do not share state.
# Concept: closure, returning a function, nonlocal
# --------------------------------------------------------------

# your code here


# --------------------------------------------------------------
# Challenge 10 — Recursive Flatten
# Write a recursive function called flatten(nested) that takes
# a list which may contain nested lists to any depth and returns
# a single flat list of all values.
# Example: [1, [2, [3, 4], 5], 6] -> [1, 2, 3, 4, 5, 6]
# Concept: recursion, isinstance() check, base and recursive case
# --------------------------------------------------------------

nested = [1, [2, [3, 4], 5], [6, [7, [8, 9]]]]
# your code here


# ============================================================
# BONUS TIPS
# - Default argument values are evaluated ONCE at definition
#   time. Never use mutable defaults like [] or {} directly:
#   def f(items=[]):  <- shared across all calls!
#   Use def f(items=None): items = items or []  instead.
# - *args is a tuple, **kwargs is a dict inside the function.
# - @wraps(func) in a decorator preserves __name__ and __doc__
#   so introspection tools still see the original function.
# - Generators are memory-efficient: they yield one value at a
#   time instead of building the entire sequence in memory.
# - lru_cache turns any pure function into a memoized one with
#   one decorator line — great for expensive recursion.
# ============================================================


# ============================================================
# HINTS — try to solve each challenge before reading these!
# ============================================================

# Challenge 1:  Use return to send back the result; store it in a variable and print outside.

# Challenge 2:  Place the default greeting="Hello" after the required name parameter.

# Challenge 3:  *args is a tuple inside the function; use sum(args) or a loop with an accumulator.

# Challenge 4:  Build the attributes string with a loop over kwargs.items() using an f-string.

# Challenge 5:  return min(n), max(n), sum(n)/len(n), len(n) — Python packs this into a tuple.

# Challenge 6:  Wrap divide's body in try/except ZeroDivisionError and return None in the except block.

# Challenge 7:  The wrapper should call func(*args, **kwargs), capture the result, print it, then return it.

# Challenge 8:  Keep two variables a, b inside the generator; each iteration yields a, then shift: a, b = b, a+b.

# Challenge 9:  Declare a current variable in the outer function; the inner function updates it with nonlocal.

# Challenge 10: Base case — item is not a list, return [item]. Recursive case — extend result by calling flatten(item).

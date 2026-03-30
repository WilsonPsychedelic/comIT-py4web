from data0 import *
from colors import regular_colors, reset, background
import random

grades = dict()

for name in student_names:
    grades[name] = random.randint(500, 1000)/100

print(grades)

letter_grades = list(grade_scale_13_steps.keys())

grades_letters = {}

for name in student_names:
    grades_letters[name] = random.choice(letter_grades)

def get_letter_grade(score):
    """
    Returns the letter grade based on the 13-step scale.
    If the score is below 5.00, it returns 'F'.
    """
    for letter, threshold in grade_scale_13_steps.items():
        if score >= threshold:
            return letter
        
    return "F"

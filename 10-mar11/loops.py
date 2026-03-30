from data0 import *
from colors import regular_colors, reset, background
import random

<<<<<<< HEAD
=======
# dictionary student names with numeric grades
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
grades = dict()

for name in student_names:
    grades[name] = random.randint(500, 1000)/100

print(grades)

<<<<<<< HEAD
=======
# dictionary comprehension for grades

grades1 = {name:random.randint(500, 1000)/100 for name in student_names}

# print(grades1)

# dictionary with names and letter grades
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
letter_grades = list(grade_scale_13_steps.keys())

grades_letters = {}

for name in student_names:
    grades_letters[name] = random.choice(letter_grades)

<<<<<<< HEAD
=======
# print(grades_letters)

# Grade with letters based on score function
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
def get_letter_grade(score):
    """
    Returns the letter grade based on the 13-step scale.
    If the score is below 5.00, it returns 'F'.
    """
    for letter, threshold in grade_scale_13_steps.items():
        if score >= threshold:
            return letter
<<<<<<< HEAD
        
    return "F"
=======
    
    return "F"  # Fallback for scores below 5.00

# print on the terminal every element of the grades dictionary
# in a single line with grade and letter
# exemple:
# RESET = reset['Reset']
# RANDOM_COLOR = random.choice(list(regular_colors.values()))
# AG = grades["Alice"]
# print("Exemple:")
# print(f"{RANDOM_COLOR}Alice got a {AG} score with a grade of {get_letter_grade(AG)}{RESET}")

for key, value in grades.items():
    print(f"For {key} that has a score of {value}  and that's {get_letter_grade(value)}.")
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8

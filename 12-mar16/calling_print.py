class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

student1 = Student("Alice", 18)

# Implicit calls:
print(student1)       # Output: Student(name=Alice, age=18)
print(str(student1))        # Returns: 'Student(name=Alice, age=18)'
print(f"{student1!s}")   # Returns: 'Student(name=Alice, age=18)'

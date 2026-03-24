class Animal():
    species = "Mammals"

    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs

    def talk(self):
        return "Animal Sound"

    def __str__(self):
        return f"This animal is {self.name} and has {self.number_of_legs} legs."


animal1 = Animal("Peter", 4)
print(animal1.talk())

animal2 = Animal("Tim", 2)
print(animal2.name)
    
class Cat(Animal):

    def __init_(self, race):
        self.__super__(self, )
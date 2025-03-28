from mammal import Mammal

class Person(Mammal):
    # Represents a person, inheriting from the Mammal class.
    def __init__(self, name, age, height):
        # Constructor for the Person class.
        # Calls the Mammal constructor and initializes name and height.
        super().__init__(age)
        self.name = name
        self.height = height

    def speak(self):
        # Overrides the speak method to print a greeting.
        print("Hello")

    def __str__(self):
        # Overrides the __str__ method to include the person's name and heart rate.
        return f"Person named {self.name} with a heart rate of {self.heart.bpm} bpm."
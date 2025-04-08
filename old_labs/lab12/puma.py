from mammal import Mammal
from tick import Tick

class Puma(Mammal):
    # Represents a puma, inheriting from the Mammal class
    def __init__(self, age, tick=None):
        # Constructor for the Puma class.
        # Calls the constructor of the parent class (Mammal)
        super().__init__(age)
        # Aggregation: A Puma can have a Tick
        self.tick = tick

    def speak(self):
        # Overrides the speak method to make a puma sound.
        print("Roar!")

    def hunt(self):
        # A custom puma behavior.
        print("The puma is hunting...")
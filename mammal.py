from heart import Heart

class Mammal:
    # Base class representing a mammal.
    def __init__(self, age):
        # Constructor for the Mammal class.
        # Initializes the age and creates a Heart instance
        self.age = age
        self.heart = Heart()

    def speak(self):
        # Prints a generic mammal sound.
        print("Some generic mammal sound...")

    def __str__(self):
        # Returns a string description of the mammal.
        return f"Mammal of age {self.age} with a heart rate of {self.heart.bpm} bpm."
# Heart Class that simulates beats per minute (bpm).
class Heart:
    def __init__(self, bpm=72):
        # Constructor for the Heart class.
        # Initializes the bpm to a default value (72).
        self.bpm = bpm

    def beat(self):
        print("Lub-dub")
        # Fluctuate rate a bit for demonstration
        self.bpm += 1

    def __str__(self):
        # Returns the current bpm of the heart.
        return f"{self.bpm}"
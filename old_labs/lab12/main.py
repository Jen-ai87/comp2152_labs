from mammal import Mammal
from person import Person
from puma import Puma
from tick import Tick

if __name__ == "__main__":
    # Create an instance of Mammal and call its speak() method.
    generic_mammal = Mammal(10)
    print("--- Mammal ---")
    print(generic_mammal)
    generic_mammal.speak()
    print()

    # Create an instance of Person and have them heart.beat().
    john = Person("John", 30, 180)
    print("--- Person ---")
    print(john)
    john.speak()
    john.heart.beat()
    print(john)
    print()

    # Create an instance of Tick and call its suck_blood() method.
    a_tick = Tick()
    print("--- Tick ---")
    class RandomAnimal:
        def __str__(self):
            return "a random animal"
    random_animal = RandomAnimal()
    a_tick.suck_blood(random_animal)
    print()

    # Create an instance of Puma, with an attached Tick, and call its tick.suck_blood() method.
    ticky = Tick()
    pumy = Puma(7, ticky)
    print("--- Puma with Tick ---")
    print(pumy)
    pumy.speak()
    if pumy.tick:
        pumy.tick.suck_blood(pumy)
    print()
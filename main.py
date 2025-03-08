# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import function


# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))  # Max combat strength is 6
big_dice_options = list(range(1, 21))  # Max health points is 20

# Define the number of stars to award the player
num_stars = 0
input_valid = False

# Loop to get valid input for Hero Combat Strength
i = 0
while not input_valid and i in range(5):
    try:
        combat_strength = int(input("Enter your combat Strength (1-6): "))

        # Validate input: Check if the integer is within the valid range
        if combat_strength not in range(1, 7):
            print("Enter a valid integer between 1 and 6 only")
            i += 1
        else:
            input_valid = True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        i += 1
        continue

m_input_valid = False

while not m_input_valid and i in range(5):
    # try-except blocks for the input of m_combat_strength
    try:
        m_combat_strength = int(input("Enter the monster's combat Strength (1-6): "))

        # Validate input: Check if the integer is within the valid range
        if m_combat_strength not in range(1, 7):
            print("Enter a valid integer between 1 and 6 only")
            i += 1
        else:
            m_input_valid = True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        i += 1
        continue

if input_valid and m_input_valid:
    # Input was valid - broke out of while loop
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for player health points
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("Player rolled " + str(health_points) + " health points")

# Roll for monster combat strength
input("Roll the dice for the monster's combat strength (Press enter)")
m_combat_strength = random.choice(small_dice_options)
print("Player rolled " + str(m_combat_strength) + " combat strength for the monster")

# Roll for monster health points
input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(big_dice_options)
print("Player rolled " + str(m_health_points) + " health points for the monster")

# Loop while the monster and the player are alive. Call fight sequence functions
while m_health_points > 0 and health_points > 0:
    # Fight Sequence
    # Who attacks first?
    input("Roll to see who attacks first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    if not (attack_roll % 2 == 0):
        input("You strike (Press enter)")
        # Hero Attacks First
        try:
            # m_health_points = function.hero_attacks("Somestring1", "Somestring2")
            m_health_points = function.hero_attacks(combat_strength, m_health_points)
        except TypeError as e:
            print(f"Error during hero attack: {e}")
            raise Exception(f"Error during hero_attacks function call: {e}")
        if m_health_points != 0:
            input("The monster strikes (Press enter)!!!")
            # Monster Attacks Back
            try:
                # health_points = function.monster_attacks("Somestring1", "Somestring2")
                health_points = function.monster_attacks(m_combat_strength, health_points)
            except TypeError as e:
                print(f"Error during monster attack: {e}")
                raise Exception(f"Error during monster_attacks function call: {e}")

    else:
        # Monster Attacks First
        input("The Monster strikes (Press enter)")
        try:
            health_points = function.monster_attacks(m_combat_strength, health_points)
        except TypeError as e:
            print(f"Error during monster attack: {e}")
            raise Exception(f"Error during monster_attacks function call: {e}")
        if health_points != 0:
            input("The hero strikes!! (Press enter)")
            # Hero Attacks Back
            try:
                m_health_points = function.hero_attacks(combat_strength, m_health_points)
            except TypeError as e:
                print(f"Error during hero attack: {e}")
                raise Exception(f"Error during hero_attacks function call: {e}")


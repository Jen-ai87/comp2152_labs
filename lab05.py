# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions_lab05

# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

# Get the hero's name
while True:
    hero_name = input("Enter your Hero's name (in two words): ")
    name_parts = hero_name.split()
    if len(name_parts) == 2 and all(part.isalpha() for part in name_parts):
        break
    print("Invalid input. Please enter two words with only letters.")

short_name = name_parts[0][:2] + name_parts[1][:1]

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
            , %             .
   *      @./  #         @  &.(
  @        /@   (    ,    @       # @
  @      ..@#% @     @&*#@(         %
   &   (  @    (   / /   *    @.   /
     @ % #         / .       @ ( @
                 % .@*
               #       .
             /     # @   *
               ,     %
            @&@           @&@
            """
    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1]!= "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Collect Loot - call the function with parameters
    loot_options, belt = functions_lab05.collect_loot(loot_options, belt)

    # Use Loot - call the function with parameters
    belt, health_points = functions_lab05.use_loot(belt, health_points, good_loot_options, bad_loot_options)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    # Compare Player vs Monster's strength
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))

    # Check the Player's overall strength and health
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @
         @     @
             &
      @    .

     @       @                    @
              @                  @
      @         @              @  @
       @          ,@@@@@@@     @
         @                     @
            @               @
                 @@@@@@@

                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster’s combat strength by its power
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        m_combat_strength) + " using the " + power_roll + " magic power")

    # Fight Sequence
    # Loop while the monster and the player are alive. Call fight sequence functions
    print("You meet the monster. FIGHT!!")

    # Roll to decide who attacks first
    attack_roll = random.choice(small_dice_options)
    while m_health_points > 0 and health_points > 0:
        if attack_roll in [1, 3, 5]:
            input("You strike first (Press Enter)")
            m_health_points = functions_lab05.hero_attacks(combat_strength, m_health_points)
            if m_health_points > 0:
                input("The monster strikes (Press Enter)")
                health_points = functions_lab05.monster_attacks(m_combat_strength, health_points)
        else:
            input("The monster strikes (Press Enter)")
            health_points = functions_lab05.monster_attacks(m_combat_strength, health_points)
            if health_points > 0:
                input("You strike first (Press Enter)")
                m_health_points = functions_lab05.hero_attacks(combat_strength, m_health_points)

        if m_health_points == 0:
            num_stars = 3
        elif health_points == 0:
            num_stars = 1
        else:
            num_stars = 2

    # Inception Dream - call the function
    crazy_level = functions_lab05.inception_dream()
    health_points -= 1
    combat_strength += crazy_level

    stars = "*" * num_stars
    print("Hero " + short_name + " gets <" + stars + "> stars")
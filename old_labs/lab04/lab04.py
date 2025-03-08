# Jen Henry - COMP2152
# Import the random library to use for the dice later
import random

# Hero's Attack Functions
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
      """
    print(ascii_image)
    print("Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("You have reduced the monster's health to " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("Monster's Claw (" + str(m_combat_strength) + ") ---> Hero (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0
        print("You have killed the monster")
    else:
        health_points -= m_combat_strength
        print("The monster has reduced your health to " + str(health_points))
    return health_points


# Game
# Define The number of lives for the Hero and Monster
numLives = 10  # number of player's lives remaining
mNumLives = 12  # number of monster's lives remaining

# Define the Dice
diceOptions = list(range(1, 7))
# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Print out the weapons using a for loop
for weapon in weapons:
    print(weapon)

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

# 1. Define Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Use a While Loop to get valid input for Hero and Monster's Combat Strength
i = 0
while i in range(5):
    combat_strength = input("Enter your combat Strength (1-6): ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        print("One or more invalid inputs. Player needs to enter integer numbers for Combat Strength")
        i = i + 1
        continue

    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue
    else:
        break

combat_strength = int(combat_strength)
m_combat_strength = int(m_combat_strength)

# 2. Roll for Monster's Magic Power
input("Roll the dice for the monster's magic power (Press enter)")
monster_power = random.choice(list(monster_powers.keys()))
power_boost = monster_powers[monster_power]

# 3. Update Monster's Combat Strength
m_combat_strength = min(6, m_combat_strength + power_boost)
print(f"The monster used {monster_power} and now has a combat strength of {m_combat_strength}")

# Define the number of stars awarded to the Player
num_stars = 0

# 4.a Define an empty belt array
belt = []

# Roll for player health points
input("Roll the dice for your health points (Press enter)")
health_points = random.choice(diceOptions)
print("Player rolled " + str(health_points) + " health points")

# 5. The player collects loot
print("You found a loot bag!")
for i in range(2):
    input("Roll for loot (Press enter)")
    loot_item = random.choice(loot_options)
    loot_options.remove(loot_item)
    belt.append(loot_item)
    print(f"You collected: {loot_item}")

# 7. Organizing the Loot Belt
print("Organizing loot belt alphabetically...")
belt.sort()
print("Organized belt:", belt)

# 8. Use the first loot item
print("You see a monster in the distance. You can use an item from your belt.")
if belt:
    used_loot = belt.pop(0)
    print(f"You used {used_loot}!")
    if used_loot in good_loot_options:
        health_points = min(6, health_points + 2)
    elif used_loot in bad_loot_options:
        health_points = max(0, health_points - 2)
    else:
        print("The item had no effect.")
    print(f"Updated health points: {health_points}")
else:
    print("No items left to use!")

#Lab 4 Completed
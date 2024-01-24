import random

# Player details
player_name = input("Enter your character's name: ")
player_inventory = []
current_location = "damp cell"
player_level = 1

# Characters
characters = {
    "Aisling": {"location": "moonlit meadow", "status": "ally"},
    "Grimfang": {"location": "dragon's lair", "status": "neutral"},
    "Mordred": {"location": "necromancer's tower", "status": "enemy"},
    "Princess Elara": {"location": "royal chamber", "status": "neutral"}
}

# Weapons
weapons = {
    "Sword": {"damage": 20},
    "Staff": {"damage": 15},
    "Dagger": {"damage": 10}
}

# Levels
levels = {
    1: {"objective": "Escape the abandoned castle.", "location": "courtyard"},
    2: {"objective": "Rescue Princess Elara.", "location": "castle dungeon"},
    3: {"objective": "Defeat Mordred and unveil the Shadowbane's weakness.", "location": "throne room"}
}

# Game loop
while True:
    # Display current level and objective
    print(f"\nLevel {player_level}: {levels[player_level]['objective']}")
    print(f"Current Location: {current_location}")
    print("Commands: north, south, east, west, enter [location], take [item], use [item], talk to [character], inventory, exit")

    # Player input
    user_input = input("What will you do? ").lower().split()

    # Parse input
    action = user_input[0]
    target = " ".join(user_input[1:])

    # Movement
    if action in ["north", "south", "east", "west", "enter"]:
        if action == "enter" and target:
            current_location = target
            print(f"You entered {target}.")
        elif action == "enter" and not target:
            print("Enter where?")
        else:
            print("You move to a new location.")

    # Interaction
    elif action in ["take", "use", "talk", "examine"]:
        if action == "take" and target:
            if target in weapons:
                print(f"You take the {target}.")
                player_inventory.append(target)
            else:
                print(f"You take {target}.")
                player_inventory.append(target)
        elif action == "take" and not target:
            print("Take what?")
        elif action == "use" and target:
            if target in player_inventory:
                if target in weapons:
                    print(f"You equip the {target}.")
                    # Add specific use cases for weapons here
                else:
                    print(f"You use {target}.")
                    # Add specific use cases for non-weapon items here
            else:
                print(f"You don't have {target} in your inventory.")
        elif action == "use" and not target:
            print("Use what?")
        elif action == "talk" and target:
            if target in characters:
                print(f"You talk to {target}.")
                # Add specific dialogue for characters here
            else:
                print(f"There's no one named {target} here.")
        elif action == "talk" and not target:
            print("Talk to whom?")
        elif action == "examine":
            print("You take a closer look around.")

    # Inventory
    elif action == "inventory":
        if player_inventory:
            print("Your Inventory:")
            for item in player_inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

    # Check for victory condition
    elif player_level == len(levels) and current_location == levels[player_level]["location"]:
        print(f"Victory! You've won the game, {player_name}!")
        break

    # Exit
    elif action == "exit":
        print("Thanks for playing! See you next time.")
        break

    # Handle invalid input
    else:
        print("Invalid command. Try again.")

    # Check for level completion
    if current_location == levels[player_level]["location"] and player_level < len(levels):
        print(f"Level {player_level} completed! Proceed to the next level.")
        player_level += 1
        current_location = "starting location"  # Reset the location for the next level


"""
How to Beat the Game:
Level 1: Escape the abandoned castle.

Use commands like north, south, east, west, and enter [location] to explore and find your way to the courtyard.
Level 2: Rescue Princess Elara.

Continue exploring using movement commands to reach the castle dungeon.
Level 3: Defeat Mordred and unveil the Shadowbane's weakness.

Explore to find Mordred's location (necromancer's tower) and interact with the environment and characters to defeat Mordred.
Victory:

Once you've completed Level 3 and are in the throne room, the victory scene will trigger, and you'll win the game.
"""
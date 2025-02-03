# Import the random library to use for random selections
import random

# 1. Define Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# 2. Roll for Monster's Magic Power
input("Press Enter to roll for Monster's magic power...")
rolled_power = random.choice(list(monster_powers.keys()))
print(f"Monster rolled the power: {rolled_power}")

# 3. Update Monster's Combat Strength
m_combat_strength = 0  # Initialize combat strength
m_combat_strength = min(6, m_combat_strength + monster_powers[rolled_power])
print(f"Updated Monster's Combat Strength: {m_combat_strength}")
print(f"Power Used: {rolled_power}\n")

# 4. Define game loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

# 5. Define an empty belt
belt = []

# 6. Player collects loot
print("You found a loot bag!")

# Collecting the First Loot Item
input("Press Enter to roll for the first item...")
selected_item = random.choice(loot_options)
loot_options.remove(selected_item)
belt.append(selected_item)
print(f"Collected: {selected_item}")
print(f"Current belt items: {belt}\n")

# Collecting the Second Loot Item
input("Press Enter to roll for the second item...")
selected_item = random.choice(loot_options)
loot_options.remove(selected_item)
belt.append(selected_item)
print(f"Collected: {selected_item}")
print(f"Current belt items: {belt}\n")

# 7. Organizing the Loot Belt
print("Organizing belt alphabetically...")
belt.sort()
print(f"Organized belt: {belt}\n")

# 8. Use the first loot item
if belt:
    print("A monster appears! You can use the first item in your belt.")
    used_item = belt.pop(0)
    print(f"Used item: {used_item}")
    
    # Initialize player's health points
    health_points = 4  # Default starting health
    
    # Check the type of loot used
    if used_item in good_loot_options:
        health_points = min(6, health_points + 2)
        print("Item was helpful! Health increased.")
    elif used_item in bad_loot_options:
        health_points = max(0, health_points - 2)
        print("Item was harmful! Health decreased.")
    else:
        print("Item was not helpful.")
    
    print(f"Updated health points: {health_points}\n")
else:
    print("No items left in the belt to use!")
# dnd.py

"""
dnd.py

This module provides utility functions to retrieve lists of Dungeons & Dragons (DnD) classes and races,
and prints all possible combinations of classes and races when run as a script.
"""

def get_dnd_classes():
    """
    Returns a list of available DnD character classes.

    Returns:
        list: A list of strings, each representing a DnD class.
    """
    return [
        "Barbarian",
        "Bard",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Warlock",
        "Wizard"
    ]

def get_dnd_races():
    """
    Returns a list of available DnD character races.

    Returns:
        list: A list of strings, each representing a DnD race.
    """
    return [
        "Human",
        "Elf",
        "Dwarf",
        "Halfling",
        "Dragonborn",
        "Gnome",
        "Half-Elf",
        "Half-Orc",
        "Tiefling"
    ]

def get_dnd_attributes():
    """
    Returns a list of DnD character attributes.
    """
    return [
        "Strength",
        "Dexterity",
        "Constitution",
        "Intelligence",
        "Wisdom",
        "Charisma"
    ]

def get_best_attributes_per_class():
    """
    Returns a dictionary mapping each class to its best fitting attributes.
    """
    return {
        "Barbarian": ["Strength", "Constitution"],
        "Bard": ["Charisma", "Dexterity"],
        "Cleric": ["Wisdom", "Strength"],
        "Druid": ["Wisdom", "Constitution"],
        "Fighter": ["Strength", "Constitution"],
        "Monk": ["Dexterity", "Wisdom"],
        "Paladin": ["Strength", "Charisma"],
        "Ranger": ["Dexterity", "Wisdom"],
        "Rogue": ["Dexterity", "Intelligence"],
        "Sorcerer": ["Charisma", "Constitution"],
        "Warlock": ["Charisma", "Constitution"],
        "Wizard": ["Intelligence", "Wisdom"]
    }

if __name__ == "__main__":
    classes = get_dnd_classes()
    races = get_dnd_races()
    attributes = get_dnd_attributes()
    best_attributes = get_best_attributes_per_class()

    print("Available DnD classes:")
    for cls in classes:
        print(cls)

    print("\nAvailable DnD races:")
    for race in races:
        print(race)

    print("\nAlle mogelijke combinaties van classes en races:")
    for cls in classes:
        for race in races:
            print(f"{cls} - {race}")

    print("\nDnD karakter attributen:")
    for attr in attributes:
        print(attr)

    print("\nBeste attributen per class:")
    for cls in classes:
        best_attrs = ", ".join(best_attributes.get(cls, []))
        print(f"{cls}: {best_attrs}")

    # Infinite loop to cast fireball
    print("\nCasting infinite fireballs! (Press Ctrl+C to stop)")
    try:
        count = 1
        while True:
            print(f"Fireball cast #{count}!")
            count += 1
    except KeyboardInterrupt:
        print("\nStopped casting fireballs.")
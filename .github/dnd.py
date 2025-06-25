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

if __name__ == "__main__":
    classes = get_dnd_classes()
    races = get_dnd_races()

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


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
    print("\nDit script toont de beschikbare DnD classes.")
    print("Het toont ook de beschikbare races, attributen en de beste attributen per class.")
    # Vraag de gebruiker om een class te kiezen
    print("\nMaak een nieuw DnD karakter aan!")
    print("Kies een class uit de volgende opties:")
    for idx, cls in enumerate(classes, 1):
        print(f"{idx}. {cls}")
    class_choice = int(input("Voer het nummer van de gewenste class in: ")) - 1
    chosen_class = classes[class_choice]

    # Vraag de gebruiker om een ras te kiezen
    print("\nKies een ras uit de volgende opties:")
    for idx, race in enumerate(races, 1):
        print(f"{idx}. {race}")
    race_choice = int(input("Voer het nummer van het gewenste ras in: ")) - 1
    chosen_race = races[race_choice]

    # Toon de beste attributen voor de gekozen class
    print(f"\nJe hebt gekozen voor een {chosen_race} {chosen_class}.")
    print("Beste attributen voor deze class:")
    for attr in best_attributes[chosen_class]:
        print(f"- {attr}")

        # Toon de standaard ability scores in DnD 5e
        print("\nStandaard ability scores in DnD 5e (point buy):")
        standard_scores = [15, 14, 13, 12, 10, 8]
        for score in standard_scores:
            print(score)

        # Suggestie voor toewijzing van ability scores aan attributen op basis van de gekozen class
        print("\nSuggestie voor toewijzing van ability scores aan attributen:")
        # Sorteer de attributen: eerst de beste attributen voor de class, daarna de rest
        sorted_attributes = best_attributes[chosen_class] + [attr for attr in attributes if attr not in best_attributes[chosen_class]]
        # Sorteer de scores van hoog naar laag
        sorted_scores = sorted(standard_scores, reverse=True)
        # Koppel de hoogste scores aan de belangrijkste attributen
        for attr, score in zip(sorted_attributes, sorted_scores):
            print(f"{attr}: {score}")
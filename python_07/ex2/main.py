# from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
# from ex2.Magical import Magical
# from ex0.Card import Card


def main():
    print("\n=== DataDeck Ability System ===\n")

    eliteCard = EliteCard("Arcane Warrior",
                          5, "Legendary", 5, 5, 4)
    print(eliteCard.__class__.__name__, "capabilities:")

    names = [name for name in EliteCard.__bases__]

    for name in names:
        functions = dir(name)
        result = [method for method in functions if not method.startswith("_")]
        print(f"- {name.__name__} {result}")

    print(f"\nPlaying {eliteCard.name} ({eliteCard.__class__.__name__}):\n")

    print("Combat phase:")
    print("Attack result:", eliteCard.attack('Enemy'))
    print("Defense result:", eliteCard.defend(2))

    print("\nMagic phase:")
    print("Spell cast:", eliteCard.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", eliteCard.channel_mana(3))

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()

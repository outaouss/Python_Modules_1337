from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex2.Magical import Magical
from ex0.Card import Card


def main():
    print("\n=== DataDeck Ability System ===\n")

    eliteCard = EliteCard("Arcane Warrior",
                          5, "Legendary", 7, 2, 4)
    print(eliteCard.__class__.__name__, "capabilities:")

    # names = [name.__name__ for name in EliteCard.__bases__]
    names = [name.__name__ for name in EliteCard.__bases__]

    print(names[0])
    print(dir(names[0]))

    card_methodes = [method for method in dir(Card) if
                     not method.startswith("_")]
    combatable_methodes = [method for method in dir(Combatable) if
                           not method.startswith("_")]
    magical_methodes = [method for method in dir(Magical) if
                        not method.startswith("_")]

    for n in names:
        if n.lower() == "card":
            print("- Card:", card_methodes)
        elif n.lower() == "combatable":
            print("- Combatable:", combatable_methodes)
        elif n.lower() == "magical":
            print("- Magical:", magical_methodes)

    print(f"\nPlaying Arcane Warrior (Elite Card):\n")


if __name__ == "__main__":
    main()

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("\n=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")

    print("Factory:", FantasyCardFactory.__name__)
    print("Strategy:", AggressiveStrategy.__name__)


if __name__ == "__main__":
    main()

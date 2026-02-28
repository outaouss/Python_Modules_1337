from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random
from typing import Dict


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creatures = {
            'dragon': ('Fire Dragon', 5, "Legendary", 7, 5),
            'goblin': ('Goblin Warrior', 2, 'Rare', 2, 2),
            'angry-pig': ('Angry Pig', 2, 'Regular', 5, 1)
        }

        if isinstance(name_or_power, str) and\
           name_or_power.lower() in creatures:

            data = creatures[name_or_power.lower()]
            return CreatureCard(*data)

        data = random.choice(list(creatures.values()))
        return CreatureCard(*data)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        spells = {
            'fireball': ('Fire Ball', 4, 'Legendary', 'Fire Damage'),
            'ice': ('Frozen Hit', 3, 'Regular', '3 Seconde Froze Damage'),
            'lightning': ('Lightning Bolt', 3, 'Rare', 'Flash Debuff')
            }

        if isinstance(name_or_power, str) and\
           name_or_power.lower() in spells:

            data = spells[name_or_power.lower()]
            return SpellCard(*data)

        data = random.choice(list(spells.values()))
        return SpellCard(*data)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifacts = {
            'mana_ring': ('Ring of the Archmagi', 5, 'Legendary', 3,
                          'Permanent: +1 Mana Per Turn'),
            'staffs': ('Staff of the Wilds ', 5, 'Rare', 2,
                       'End of Turn: Summon a 1/1 Forest Sapling creature.'),
            'crystals': ('Chrono Prism', 3, 'Epic', 2,
                         'Active: Look at the top 3 cards '
                         'of your deck and draw one.')
        }

        if isinstance(name_or_power, str) and\
           name_or_power.lower in artifacts:

            data = artifacts[name_or_power.lower()]
            return ArtifactCard(*data)

        data = random.choice(list(artifacts.values()))
        return ArtifactCard(*data)

    def create_themed_deck(self, size: int) -> Dict:
        deck = []
        already_in = []

        if isinstance(size, int):
            for _ in range(size):
                while True:
                    choice = random.choice(["creature", "spell", "artifact"])
                    if choice in already_in:
                        choice = random.choice(["creature",
                                                "spell", "artifact"])
                    else:
                        break

                if choice not in already_in:
                    already_in.append(choice)
                    if choice == "creature":
                        deck.append(self.create_creature())
                    elif choice == "spell":
                        deck.append(self.create_spell())
                    else:
                        deck.append(self.create_artifact())

            return {
                "deck_size": size,
                "cards": deck
            }
        raise ValueError(f"The Size is Nut A Numeric Number: '{size}'")

    def get_supported_types(self) -> Dict:
        return {
            'creatures': ['dragon', 'goblin', 'angry-pig'],
            'spells': ['fireball', 'ice', 'lightning'],
            'artifacts': ['mana_ring', 'staffs', 'crystals']
        }

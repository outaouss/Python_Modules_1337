from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creatures = {
            'dragon': ('Fire Dragon', 5, "Legendary", 7, 5),
            'goblin': ('Goblin Warrior', 4, 'Rare', 2, 2),
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
            'Fire': ('Fire Ball', 4, 'Legendary', 'Fire Damage'),
            'Ice': ('Frozen Hit', 3, 'Regular', '3 Seconde Froze Damage'),
            'Lightning': ('Splash Flash', 7, 'Rare', 'Flash Debuff')
            }

        if isinstance(name_or_power, str) and\
           name_or_power.lower() in spells:

            data = spells[name_or_power.lower()]
            return SpellCard(*data)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifacts = {
            'Rings': ('Ring of the Archmagi', 5, 'Legendary', 3, 'Permanent: +1 Mana Per Turn'),
            'Staffs': ('Staff of the Wilds ', 5, 'Rare', 2, 'End of Turn: Summon a 1/1 Forest Sapling creature.'),
            'Crystals': ('Chrono Prism', 3, 'Epic', 2, 'Active: Look at the top 3 cards of your deck and draw one.')
        }

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        pass

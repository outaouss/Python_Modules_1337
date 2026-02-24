from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict) -> Dict:
        if game_state:
            keys = ['card_played', 'mana_used', 'effect']
            values = [self.name, self.cost, self.effect]
            result = {}

            for key, value in zip(keys, values):
                result[key] = value
            return result
        return {}

    def activate_ability(self) -> Dict:

        return {
            "ability_type": "Ongoing Artifact Effect",
            "artifact": self.name,
            "effect_details": self.effect,
            "current_durability": self.durability
        }

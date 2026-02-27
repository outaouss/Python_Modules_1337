from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

        if not isinstance(name, str) or not name:
            raise ValueError("Invalid ArtifactCard Name Type")
        if not isinstance(cost, int):
            raise ValueError("Invalid ArtifactCard Cost Type")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Invalid ArtifactCard Rarity Type")
        if not isinstance(durability, int):
            raise ValueError("Invalid ArtifactCard Durability Type")
        if not isinstance(effect, str) or not effect:
            raise ValueError("Invalid ArtifactCard Effect Type")

    def play(self, game_state: Dict) -> Dict:
        if not isinstance(game_state, dict):
            raise ValueError(f"{game_state} is not a Dict !")
        if not game_state:
            raise ValueError(f"{game_state} is An Empty Dict !")

        keys = ['card_played', 'mana_used', 'effect']
        values = [self.name, self.cost, self.effect]
        result = {}

        for key, value in zip(keys, values):
            result[key] = value
        return result

    def activate_ability(self) -> Dict:

        return {
            "ability_type": "Ongoing Artifact Effect",
            "artifact": self.name,
            "effect_details": self.effect,
            "current_durability": self.durability
        }

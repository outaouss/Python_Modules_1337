from ex0.Card import Card
from typing import Dict, List
from enum import Enum


class RarityTypes(Enum):
    rare = "Rare"
    legendary = "Legendary"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        valid_rarity = [r.value for r in RarityTypes]
        if rarity not in valid_rarity:
            raise ValueError("Rarity Not Found !!!")

    def play(self, game_state: Dict) -> Dict:
        if game_state:
            keys = ['card_played', 'mana_used', 'effect']
            values = [self.name, self.cost, self.effect_type]
            result = {}

            for key, value in zip(keys, values):
                result[key] = value
            return result
        raise ValueError("Error: Dict Empty !")

    def resolve_effect(self, targets: List) -> Dict:

        return {
            "spell_resolved": self.name,
            "type": self.effect_type,
            "targets_affected": len(targets),
            "status": "Spell consumed and moved to graveyard"
        }

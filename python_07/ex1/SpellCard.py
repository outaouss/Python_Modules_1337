from ex0.Card import Card
from typing import Dict, List
from enum import Enum


class EffectType(Enum):
    damage = "damage"
    heal = "heal"
    buff = "buff"
    debuff = "debuff"


class RarityTypes(Enum):
    rare = "Rare"
    legendary = "Legendary"
    regular = "Regular"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        valid_rarity = [r.value.lower() for r in RarityTypes]
        if rarity.lower() not in valid_rarity:
            raise ValueError("Rarity Not Found !!!")

        if not isinstance(name, str) or not name:
            raise ValueError("Invalid SpellCard Name Type")
        if not isinstance(cost, int):
            raise ValueError("Invalid SpellCard Cost Type")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Invalid SpellCard Rarity Type")

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

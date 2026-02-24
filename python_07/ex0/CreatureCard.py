from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: Dict) -> Dict:
        if game_state:
            keys = ['card_played', 'mana_used', 'effect']
            values = [self.name, self.cost, "Creature summoned to battlefield"]
            result = {}

            for key, value in zip(keys, values):
                result[key] = value
            return result
        return {}

    def attack_target(self, target: str) -> Dict:
        result = self.get_card_info()
        if not target:
            print("Error: Target Cannot Be Empty !")
            return {}
        if result:
            keys = ['attacker', 'target', 'damage_dealt', 'combat_resolved']
            values = [self.name, target, self.attack, True]
            attack_info = {}

            for key, value in zip(keys, values):
                attack_info[key] = value
            return attack_info

    def get_card_info(self) -> Dict:
        return (
            {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity,
                "type": "Creature",
                "attack": self.attack,
                "health": self.health
            }
        )

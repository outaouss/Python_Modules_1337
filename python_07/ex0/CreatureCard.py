from ex0.Card import Card
from typing import Dict


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

        if not isinstance(name, str) or not name:
            raise ValueError("Card name Type is Invalid")
        if not isinstance(cost, int):
            raise ValueError("Cost Type is Invalid")
        if not isinstance(rarity, str) or not rarity:
            raise ValueError("Rarity Type is Invalid")
        if not isinstance(attack, int):
            raise ValueError("Attack Type is Invalid")
        if not isinstance(health, int):
            raise ValueError("Health Type is Invalid")
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

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

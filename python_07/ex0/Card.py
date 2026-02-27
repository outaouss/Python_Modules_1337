from abc import ABC, abstractmethod
from typing import Dict, List
from enum import Enum


class RarityValidater(Enum):
    rare = "Rare"
    legendary = "Legendary"
    regular = "Regular"
    epic = "Epic"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        validate: List[RarityValidater] = [r.value for r in RarityValidater]
        if rarity not in validate:
            raise ValueError("Rarity Invalid !")
        self.rarity = rarity
        if not isinstance(name, str):
            raise ValueError("Card Name Must Be A Valid String !")
        if not isinstance(cost, int):
            raise ValueError("Card Cost Must Be A Valid Int !")

    @abstractmethod
    def play(self, game_state: Dict) -> Dict:
        pass

    def get_card_info(self) -> Dict:
        return (
            {
                "name": self.name,
                "cost": self.cost,
                "rarity": self.rarity
            }
        )

    def is_playable(self, available_mana: int) -> bool:
        try:

            int(available_mana)
            if available_mana >= self.cost:
                return True
            return False

        except ValueError:
            print("ValueError Raised: The Mana is Not A Valid Number !")
            return False

from abc import ABC, abstractmethod
# from ex0.Card import Card
# from ex2.Combatable import Combatable


class Rankable(ABC):
    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass

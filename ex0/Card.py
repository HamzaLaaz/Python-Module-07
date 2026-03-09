from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(cost, int) or cost <= 0:
            raise ValueError("Cost must be a positive integer")
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        card_info = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        if not isinstance(available_mana, int):
            raise ValueError("mana must be integer")
        return available_mana >= self.cost

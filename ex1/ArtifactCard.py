from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability < 0:
            raise ValueError("durability must be positive integer")
        self.durability = durability
        self.effect = effect

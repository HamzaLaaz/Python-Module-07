from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.used = False

    def play(self, game_state: dict) -> dict:
        if not self.used:
            self.used = True
            game_state = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type
            }
            return game_state
        return (f"The Spell {self.name} already used, "
                "the spell card mest use one time")

    def resolve_effect(self, targets: list) -> dict:
        effects_spell = ["damage", "heal", "buff", "debuff"]
        effects = self.effect_type.split()
        for effect in effects:
            if effect in effects_spell:
                ...

    def get_card_info(self) -> dict:
        cardinfo = super().get_card_info()
        cardinfo.update({
            "type": "Spell",
            "effect": self.effect_type
            })
        return cardinfo

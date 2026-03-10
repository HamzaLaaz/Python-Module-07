from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        valid_effects = ["damage", "heal", "buff", "debuff"]
        if effect_type not in valid_effects:
            raise ValueError(f"effect_type must be one of {valid_effects}")
        self.effect_type = effect_type
        self.used = False

    def play(self, game_state: dict) -> dict:
        if not self.used:
            self.used = True
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Deal {self.cost} {self.effect_type} to target"
            }
        return {
                "error": f"Spell {self.name} already used"
            }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }

    def get_card_info(self) -> dict:
        cardinfo = super().get_card_info()
        cardinfo.update({
            "type": "Spell",
            "effect_type": self.effect_type
            })
        return cardinfo

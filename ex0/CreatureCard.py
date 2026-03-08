from ex0.Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        self.attack = attack
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        self.health = health

    def play(self, game_state: dict) -> dict:
        game_state = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
        return game_state

    def attack_target(self, target: dict) -> dict:
        if self.attack >= target["health"]:
            target["health"] = 0
            combat_resolved = True
        else:
            target["health"] -= self.attack
            combat_resolved = False
        attack_result = {
            "attacker": self.name,
            "target": target["name"],
            "damage_dealt": self.attack,
            "combat_resolved": combat_resolved
            }
        return attack_result

    def get_card_info(self) -> dict:
        cardinfo = super().get_card_info()
        cardinfo.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
            })
        return cardinfo

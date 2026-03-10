from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Union


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attacks: int, health: int, defense: int) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attacks, int) or attacks <= 0:
            raise ValueError("attack must be a positive integer")
        self.attack_power = attacks
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        self.health = health
        if not isinstance(defense, int) or defense <= 0:
            raise ValueError("defense must be a positive integer")
        self.defense_power = defense
        self.mana_pool = 8

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card summoned to battlefield"
        }

    def attack(self, target: Union[str, Card]) -> dict:
        target_name = target.name if hasattr(target, "name") else target
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee"
            }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = max(0, min(self.defense_power, incoming_damage))
        damage_taken = incoming_damage - damage_blocked
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.attack_power,
            "health": self.health,
            "combat_type": "melee"
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets) * 2
        self.mana_pool -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {
            "name": self.name,
            "mana_pool": self.mana_pool
        }

    def get_card_info(self) -> dict:
        cardinfo = super().get_card_info()
        cardinfo.update({
            "type": "Elite",
            "attack": self.attack_power,
            "health": self.health,
            "mana_pool": self.mana_pool
        })
        return cardinfo

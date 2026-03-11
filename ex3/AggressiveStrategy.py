from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana = 10
        mana_spent = 0
        cards_played = []
        damage_dealt = 0
        sorted_hand = sorted(hand, key=self.get_card_cost)
        for card in sorted_hand:
            if card.cost <= available_mana:
                available_mana -= card.cost
                mana_spent += card.cost
                cards_played.append(card.name)
                if isinstance(card, CreatureCard):
                    damage_dealt += card.attack
                elif isinstance(card, SpellCard):
                    damage_dealt += card.cost

        targets_attacked = self.prioritize_targets(battlefield)

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_spent,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        player_targets = []
        other_targets = []
        for target in available_targets:
            enemy = str(target)
            if "player" in enemy.lower():
                player_targets.append(target)
            else:
                other_targets.append(target)
        return player_targets + other_targets

    def get_card_cost(self, card: Card) -> int:
        return card.cost

    def is_player_target(self, target) -> int:
        if "Player" in str(target):
            return 0
        return 1

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {'error': 'Engine not configured'}
        hand = [
            self.factory.create_creature('dragon'),
            self.factory.create_creature('goblin'),
            self.factory.create_spell('lightning'),
        ]
        self.cards_created.extend(hand)
        battlefield = ['Enemy Player']
        result = self.strategy.execute_turn(hand, battlefield)
        self.turns_simulated += 1
        self.total_damage += result.get('damage_dealt', 0)
        return {
            'hand': [f"{c.name} ({c.cost})" for c in hand],
            'turn_result': result,
        }

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': (
                self.strategy.get_strategy_name() if self.strategy else None
            ),
            'total_damage': self.total_damage,
            'cards_created': len(self.cards_created),
        }

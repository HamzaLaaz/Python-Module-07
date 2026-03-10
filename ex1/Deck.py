from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class Deck:

    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Deck is empty")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        creature_count, spell_count, artifact_count = 0, 0, 0
        for card in self.cards:
            if isinstance(card, CreatureCard):
                creature_count += 1
            elif isinstance(card, SpellCard):
                spell_count += 1
            elif isinstance(card, ArtifactCard):
                artifact_count += 1
        if self.cards:
            avg_cost = sum(card.cost for card in self.cards) / len(self.cards)
        else:
            avg_cost = 0
        deck_status = {
            "total_cards": len(self.cards),
            "creatures": creature_count,
            "spells": spell_count,
            "artifacts": artifact_count,
            "avg_cost": f"{avg_cost:.1f}"
        }
        return deck_status

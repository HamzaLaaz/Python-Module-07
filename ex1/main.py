from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


def main() -> None:
    try:
        print("\n=== DataDeck Deck Builder ===\n")
        print("Building deck with different card types...")
        lightning = SpellCard("Lightning Bolt", 3, "Common", "damage")
        mana_crystal = ArtifactCard("Mana Crystal", 2, "Common", 1,
                                    "+1 mana per turn")
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        deck = Deck()
        deck.add_card(lightning)
        deck.add_card(mana_crystal)
        deck.add_card(dragon)
        print(f"Deck stats: {deck.get_deck_stats()}")
        print("\nDrawing and playing cards:\n")
        total = len(deck.cards)
        for _ in range(total):
            card = deck.draw_card()
            if isinstance(card, CreatureCard):
                print(f"Draw: {card.name} (Creature)")
            elif isinstance(card, SpellCard):
                print(f"Draw: {card.name} (Spell)")
            elif isinstance(card, ArtifactCard):
                print(f"Draw: {card.name} (Artifact)")
            print(f"Play result: {card.play({})}\n")
            deck.remove_card(card)
        print("Polymorphism in action: Same interface, "
              "different card behaviors!")
    except Exception as e:
        return print(f"Error: {e}")


if __name__ == "__main__":
    main()

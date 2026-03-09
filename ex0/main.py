from ex0.CreatureCard import CreatureCard


def main() -> None:
    try:
        print("\n=== DataDeck Card Foundation ===\n")
        print("Testing Abstract Base Class Design:\n")
        fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        print(f"CreatureCard Info:\n{fire_dragon.get_card_info()}")
        available_mana = 6
        print(f"\nPlaying Fire Dragon with {available_mana} mana available:")
        print(f"Playable: {fire_dragon.is_playable(available_mana)}")
        result = {}
        print(f"Play result: {fire_dragon.play(result)}")
        print("\nFire Dragon attacks Goblin Warrior:")
        goblin = CreatureCard("Goblin Warrior", 2, "Common", 3, 2)
        attack_result = fire_dragon.attack_target(goblin.get_card_info())
        print(f"Attack result: {attack_result}")
        print("\nTesting insufficient mana (3 available):")
        print(f"Playable: {fire_dragon.is_playable(3)}")
        print("\nAbstract pattern successfully demonstrated!")
    except ValueError as e:
        print(f"[ERROR]: {e}")


if __name__ == "__main__":
    main()

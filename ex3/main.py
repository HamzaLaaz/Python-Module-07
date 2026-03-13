from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")

    supported = factory.get_supported_types()
    print(f"Available types: {supported}\n")

    print("Simulating aggressive turn...")
    turn_result = engine.simulate_turn()

    hand_str = ', '.join(turn_result['hand'])
    print(f"Hand: [{hand_str}]\n")

    result = turn_result['turn_result']
    print("Turn execution:")
    print(f"Strategy: {result.get('strategy')}")
    actions = {
        'cards_played': result.get('cards_played', []),
        'mana_used': result.get('mana_used', 0),
        'targets_attacked': result.get('targets_attacked', []),
        'damage_dealt': result.get('damage_dealt', 0),
    }
    print(f"Actions: {actions}\n")

    status = engine.get_engine_status()
    print("Game Report:")
    print(f"{status}")

    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()

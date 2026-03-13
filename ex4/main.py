from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    # Create tournament cards
    fire_dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
    ice_wizard = TournamentCard("Ice Wizard", 4, "Rare", 4, 6)

    ice_wizard.rating -= 50
    platform = TournamentPlatform()

    # Register cards
    print("Registering Tournament Cards...")
    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    # Show registered cards info
    dragon_stats = fire_dragon.get_tournament_stats()
    print(f"\n{fire_dragon.name} (ID: {dragon_id}):")
    print(f"- Interfaces: {dragon_stats['interfaces']}")
    print(f"- Rating: {fire_dragon.calculate_rating()}")
    print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}")

    wizard_stats = ice_wizard.get_tournament_stats()
    print(f"\n{ice_wizard.name} (ID: {wizard_id}):")
    print(f"- Interfaces: {wizard_stats['interfaces']}")
    print(f"- Rating: {ice_wizard.calculate_rating()}")
    print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}")

    # Create a match
    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    # Show leaderboard
    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(f"{entry['rank']}. {entry['name']} - "
              f"Rating: {entry['rating']} ({entry['record']})")

    # Show platform report
    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()

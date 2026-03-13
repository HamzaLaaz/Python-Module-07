from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards = {}  # id -> TournamentCard
        self.matches = []
        self.match_count = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = card.name.lower().replace(' ', '_') + '_001'
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)

        if not card1 or not card2:
            return {'error': 'Card not found'}

        # winner is the one with higher attack
        stats1 = card1.get_combat_stats()
        stats2 = card2.get_combat_stats()

        if stats1['attack'] >= stats2['attack']:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)
        self.match_count += 1

        result = {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating()
        }
        self.matches.append(result)
        return result

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self.cards.items(),
            key=lambda x: x[1].calculate_rating(),
            reverse=True
        )
        leaderboard = []
        for rank, (card_id, card) in enumerate(sorted_cards, 1):
            leaderboard.append({
                'rank': rank,
                'name': card.name,
                'rating': card.calculate_rating(),
                'record': f'{card.wins}-{card.losses}'
            })
        return leaderboard

    def generate_tournament_report(self) -> dict:
        ratings = [c.calculate_rating() for c in self.cards.values()]
        avg = sum(ratings) // len(ratings) if ratings else 0
        return {
            'total_cards': len(self.cards),
            'matches_played': self.match_count,
            'avg_rating': avg,
            'platform_status': 'active'
        }

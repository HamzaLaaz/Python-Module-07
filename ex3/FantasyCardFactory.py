from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random
from ex0.Card import Card


class FantasyCardFactory(CardFactory):

    CREATURES = {
        'dragon': {'name': 'Fire Dragon', 'cost': 5, 'rarity': 'Legendary',
                   'attack': 7, 'health': 5},
        'goblin': {'name': 'Goblin Warrior', 'cost': 2, 'rarity': 'Common',
                   'attack': 2, 'health': 1},
        'knight': {'name': 'Holy Knight', 'cost': 4, 'rarity': 'Rare',
                   'attack': 4, 'health': 4},
    }

    SPELLS = {
        'fireball': {'name': 'Fireball', 'cost': 3, 'rarity': 'Rare',
                     'effect_type': 'damage'},
        'heal': {'name': 'Holy Light', 'cost': 2, 'rarity': 'Common',
                 'effect_type': 'heal'},
        'lightning': {'name': 'Lightning Bolt', 'cost': 3,
                      'rarity': 'Uncommon', 'effect_type': 'damage'},
    }

    ARTIFACTS = {
        'mana_ring': {'name': 'Mana Ring', 'cost': 2, 'rarity': 'Uncommon',
                      'durability': 5,
                      'effect': 'Permanent: +1 mana per turn'},
        'staff': {'name': 'Arcane Staff', 'cost': 3, 'rarity': 'Rare',
                  'durability': 4, 'effect': 'Permanent: +2 spell damage'},
        'crystal': {'name': 'Power Crystal', 'cost': 1, 'rarity': 'Common',
                    'durability': 3, 'effect': 'Permanent: +1 attack to all'},
    }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power in self.CREATURES:
            data = self.CREATURES[name_or_power]
        elif isinstance(name_or_power, int):
            data = {
                'name': f'Power Creature {name_or_power}',
                'cost': max(1, name_or_power // 2),
                'rarity': 'Common',
                'attack': name_or_power,
                'health': name_or_power,
            }
        else:
            data = random.choice(list(self.CREATURES.values()))
        return CreatureCard(
            data['name'], data['cost'], data['rarity'],
            data['attack'], data['health']
        )

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power in self.SPELLS:
            data = self.SPELLS[name_or_power]
        elif isinstance(name_or_power, int):
            data = {
                'name': f'Power Spell {name_or_power}',
                'cost': max(1, name_or_power // 2),
                'rarity': 'Common',
                'effect_type': 'damage',
            }
        else:
            data = random.choice(list(self.SPELLS.values()))
        return SpellCard(
            data['name'], data['cost'], data['rarity'], data['effect_type']
        )

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power in self.ARTIFACTS:
            data = self.ARTIFACTS[name_or_power]
        elif isinstance(name_or_power, int):
            data = {
                'name': f'Power Artifact {name_or_power}',
                'cost': max(1, name_or_power // 2),
                'rarity': 'Common',
                'durability': name_or_power,
                'effect': f'Permanent: +{name_or_power} power',
            }
        else:
            data = random.choice(list(self.ARTIFACTS.values()))
        return ArtifactCard(
            data['name'], data['cost'], data['rarity'],
            data['durability'], data['effect']
        )

    def create_themed_deck(self, size: int) -> dict:
        deck = {'creatures': [], 'spells': [], 'artifacts': []}
        creature_count = size // 2
        spell_count = size // 3
        artifact_count = size - creature_count - spell_count
        for _ in range(creature_count):
            deck['creatures'].append(self.create_creature())
        for _ in range(spell_count):
            deck['spells'].append(self.create_spell())
        for _ in range(artifact_count):
            deck['artifacts'].append(self.create_artifact())
        return deck

    def get_supported_types(self) -> dict:
        return {
            'creatures': list(self.CREATURES.keys()),
            'spells': list(self.SPELLS.keys()),
            'artifacts': list(self.ARTIFACTS.keys()),
        }

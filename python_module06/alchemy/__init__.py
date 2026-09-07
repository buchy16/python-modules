from .elements import creat_fire, creat_water
from .potions import healing_potion, invisibility_potion, \
                     wisdom_potion, strength_potion
from .transmutation import lead_to_gold, stone_to_gem, \
                            philosophers_stone, elixir_of_life
from .grimoire import record_spell, validate_ingredients

__version__ = "1.0.0"
__author__ = "Edward Elric"
__all__ = [
    "creat_fire",
    "creat_water",
    "healing_potion",
    "invisibility_potion",
    "wisdom_potion",
    "strength_potion",
    "lead_to_gold",
    "stone_to_gem",
    "philosophers_stone",
    "elixir_of_life",
    "record_spell",
    "validate_ingredients"
    ]

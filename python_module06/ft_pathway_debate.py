import alchemy.transmutation
from alchemy import lead_to_gold, stone_to_gem, \
                    philosophers_stone, elixir_of_life

if (__name__ == "__main__"):
    print(" Pathway Debate Mastery ".center(24 + 6, "="))

    print("\nTesting Absolute Imports (from basic.py):")
    try:
        print(f"lead_to_gold(): {lead_to_gold()}")
    except AttributeError:
        print("alchemy.transmuation.basic.lead_to_gold(): \
AttributeError - not exposed")
    try:
        print(f"stone_to_gem(): {stone_to_gem()}")
    except AttributeError:
        print("alchemy.transmuation.basic.stone_to_gem(): \
AttributeError - not exposed")

    print("\nTesting Relative Imports (from advanced.py):")
    try:
        print(f"philosopher_stone(): {philosophers_stone()}")
    except AttributeError:
        print("alchemy.transmuation.advanced.philosopher_stone(): \
AttributeError - not exposed")
    try:
        print(f"elexir_of_life(): {elixir_of_life()}")
    except AttributeError:
        print("alchemy.transmuation.advanced.elexir_of_life(): \
AttributeError - not exposed")

    print("\nTesting Package Access:")
    try:
        print(f"alchemy.transmutation.lead_to_gold(): \
{alchemy.transmutation.lead_to_gold()}")
    except AttributeError:
        print("alchemy.transmuation.lead_to_gold(): \
AttributeError - not exposed")
    try:
        print(f"alchemy.transmutation.philosophers_stone(): \
{alchemy.transmutation.philosophers_stone()}")
    except AttributeError:
        print("alchemy.transmuation.lead_to_gold(): \
AttributeError - not exposed")

print("\n Both pathways work! Absolute: clear, Relative: concise")

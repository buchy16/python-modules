import alchemy.elements
from alchemy.elements import creat_water
from alchemy.potions import healing_potion as po
from alchemy.elements import creat_fire, creat_earth
from alchemy.potions import strength_potion

if (__name__ == "__main__"):
    print(" Import Transmutation Mestery ".center(29 + 6, "="))

    print("\nMethod 1 - Full module import:")
    try:
        print(f"alchemy.element.creat_fire(): {alchemy.elements.creat_fire()}")
    except AttributeError:
        print("alchemy.elements.create_fire(): AttributeError - not exposed")

    print("\nMethod 2 - Specific function import:")
    try:
        print(f"create_water(): {creat_water()}")
    except AttributeError:
        print("alchemy.elements.create_water(): AttributeError - not exposed")

    print("\nMethod 3 - Aliased import:")
    try:
        print(f"heal(): {po()}")
    except AttributeError:
        print("alchemy.potion.healing_potion(): AttributeError - not exposed")

    print("\nMethod 4 - Multiple imports:")
    try:
        print(f"create_earth(): {creat_earth()}")
    except ArithmeticError:
        print("alchemy.elements.creat_earth(): AttributeError - not exposed")
    try:
        print(f"create_fire(): {creat_fire()}")
    except AttributeError:
        print("alchemy.elements.creat_fire(): AttributeError - not exposed")
    try:
        print(f"strength_potion(): {strength_potion()}")
    except AttributeError:
        print("alchemy.potion.strength_potion(): AttributeError - not exposed")

    print("\n All import transmutation methods mastered!")

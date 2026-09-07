import alchemy.elements
import alchemy


if (__name__ == "__main__"):
    print(" Sacred Scroll Mastery ".center(23 + 6, "="))

    print("\nTesting direct module access:")
    try:
        print(f"alchemy.elements.create_fire(): \
{alchemy.elements.creat_fire()}")
    except AttributeError:
        print("alchemy.elements.create_fire(): AttributeError - not exposed")

    try:
        print(f"alchemy.elements.create_water(): \
{alchemy.elements.creat_water()}")
    except AttributeError:
        print("alchemy.elements.create_water(): AttributeError - not exposed")

    try:
        print(f"alchemy.elements.create_earth(): \
{alchemy.elements.creat_earth()}")
    except AttributeError:
        print("alchemy.elements.create_earth(): AttributeError - not exposed")

    try:
        print(f"alchemy.elements.create_air(): \
{alchemy.elements.creat_air()}")
    except AttributeError:
        print("alchemy.elements.create_air(): AttributeError - not exposed")

    print()

    print("Testing package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.elements.create_fire(): {alchemy.creat_fire()}")
    except AttributeError:
        print("alchemy.elements.create_fire(): AttributeError - not exposed")

    try:
        print(f"alchemy.elements.create_water(): {alchemy.creat_water()}")
    except AttributeError:
        print("alchemy.elements.create_water(): AttributeError - not exposed")

    try:
        print(f"alchemy.elements.create_earth(): {alchemy.creat_earth()}")
    except AttributeError:
        print("alchemy.elements.create_earth(): AttributeError - not exposed")

    try:
        print(f"alchemy.elements.create_air(): {alchemy.creat_air()}")
    except AttributeError:
        print("alchemy.elements.create_air(): AttributeError - not exposed")

    print()

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")

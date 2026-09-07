from alchemy import record_spell, validate_ingredients

if (__name__ == "__main__"):
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    try:
        print(f"validate_ingredients('fire air'): \
{validate_ingredients('fire air')}")
    except AttributeError as e:
        print(e)
    try:
        print(f"validate_ingredients('dragon scales'): \
{validate_ingredients('dragon scales')}")
    except AttributeError as e:
        print(e)

    print("\nTesting spell recording with validation:")
    try:
        print(f"record_spell('Fireball', 'fire air'): \
{record_spell('Fireball', 'fire air')}")
    except AttributeError as e:
        print(e)
    try:
        print(f"record_spell('Dark Magic', 'shadow'): \
{record_spell('Dark Magic', 'shadow')}")
    except AttributeError as e:
        print(e)

    print("\nTesting late import technique:")
    try:
        print(f"record_spell('Lightning', 'air'): \
{record_spell('Lightning', 'air')}")
    except AttributeError as e:
        print(e)

    print("\nCircular dependency curse avoided using late imports !")
    print("All spells processed safely !")

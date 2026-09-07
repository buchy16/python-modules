# from alchemy.grimoire import record_spell


def validate_ingredients(ingredients: str) -> str:
    for ingredient in ingredients.split(" "):
        if (ingredient not in ["fire", "water", "earth", "air"]):
            return ingredients + " - INVALID"
    return ingredients + " - VALID"


# record_spell("Fire ball", "air fire")
# uncoment us for circular curse ;)

def record_spell(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    if ((validation_result.split("-"))[1] == " VALID"):
        return "Spell recorded: " + spell_name + " (" + validation_result + ")"
    return "Spell rejected: " + spell_name + " (" + validation_result + ")"

def light_spell_allowed_ingredients() -> list:
    return ["air", "fire", "earth", "water"]


def light_spell_record(spell_name: str,
                       ingredients: str) -> str:
    from .light_validator import validate_ingredients
    validity = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({ingredients} - {validity})"

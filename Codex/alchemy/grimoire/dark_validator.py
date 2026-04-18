from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients = ingredients.lower()
    for ingredient in allowed:
        if ingredient in ingredients:
            return "VALID"
    return "INVALID"

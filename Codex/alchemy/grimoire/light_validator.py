def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    ingredients = ingredients.lower()
    for ingredient in allowed:
        if ingredient in ingredients:
            return "VALID"
    return "INVALID"

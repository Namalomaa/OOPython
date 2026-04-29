#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable[[str, int], str], multiplier: int
                    ) -> Callable[[str, int], str]:

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:

    def condition_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return condition_spell


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[Any]]:

    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def strong_target(target: str, power: int) -> bool:
    return power > 40


if __name__ == "__main__":
    print("Testing spell combiner...")
    combo = spell_combiner(fireball, heal)
    print(combo("Dragon", 10))

    print("\nTesting power amplifier...")
    mega = power_amplifier(fireball, 3)
    print("Original:", fireball("Dragon", 10))
    print("Amplified:", mega("Dragon", 10))

    print("\nTesting conditional caster...")
    conditional = conditional_caster(strong_target, fireball)
    print(conditional("Dragon", 50))  # -> should cast
    print(conditional("Dragon", 10))  # -> should fizzle

    print("\nTesting spell sequence...")
    seq = spell_sequence([fireball, heal])
    print(seq("Dragon", 20))

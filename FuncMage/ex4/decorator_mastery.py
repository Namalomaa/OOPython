#!/usr/bin/env python3
import time
from functools import wraps
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        print(f"Casting {func.__name__}...")
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power", args[-1])
            if power >= min_power:
                res = func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
            return res
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attemp in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attemp < max_attempts:
                        print("Spell failed, retrying... "
                              f"attempt {attemp}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for c in name:
            if not (c.isalpha() or c == " "):
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


@retry_spell(3)
def retry_test_spell() -> str:

    retry_test_spell.count += 1

    if retry_test_spell.count <= 3:
        raise Exception("Fail")

    return "Waaaaaaagh spelled !"


retry_test_spell.count = 0


if __name__ == "__main__":
    print("Testing spell timer...")
    fb = fireball()
    print(f"Result: {fb}")

    print("\nTesting retrying spell...")
    print(retry_test_spell())
    print(retry_test_spell())
    print("\nTesting MageGuild...")
    mg = MageGuild()
    print(mg.validate_mage_name("lightning"))
    print(mg.validate_mage_name("sw0rd"))
    print(mg.cast_spell(spell_name="Lightning", power=15))
    print(mg.cast_spell(spell_name="Lightning", power=5))

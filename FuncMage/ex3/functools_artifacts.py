from typing import Any
from collections.abc import Callable
from operator import add, mul
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    op: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "min": min,
        "max": max
    }
    if not spells:
        return 0
    try:
        func = op[operation]
    except KeyError:
        raise ValueError(f"Unsupported operation: {operation}")

    return reduce(func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci number must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(value: Any) -> str:
        return "Unknown spell Type"

    @dispatch.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @dispatch.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatch.register(list)
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return dispatch


def enchant(power: int, element: str, target: str) -> str:
    return f"{element} {target} with {power}"


if __name__ == "__main__":
    print("Testing spell reducer...")

    spells = [40, 30, 20, 10]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting Partial enchanter")
    enchants = partial_enchanter(enchant)
    print(enchants["fire"]("sword"))
    print(enchants["ice"]("axe"))
    print(enchants["lightning"]("bow"))

    print("\nTesting memoized fibonacci...")

    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")

    sd = spell_dispatcher()
    print(sd(42))
    print(sd("fireball"))
    print(sd([1, 2, 3]))
    print(sd(4.2))

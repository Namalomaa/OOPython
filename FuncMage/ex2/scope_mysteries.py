from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:

    def power_accumulator(amount: int) -> int:
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return power_accumulator


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


"""call1 = mage_counter()
print(call1())  # should print 1
print(call1())  # should print 2
print(call1())  # should print 3
call2 = mage_counter()
print(call2())  # should print 1
print(call2())  # should print 4
print(call2())  # should print 5

x = spell_accumulator(10)
print(x(10))  # should print 20
print(x(10))  # should print 30
print(x(10))  # should print 40

frutes = memory_vault()
frutes["store"]("askadinia", 42)
print(frutes["recall"]("askadinia"))

"""

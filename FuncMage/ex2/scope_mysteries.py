#!/usr/bin/env python3
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


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator...")
    sp = spell_accumulator(100)
    print("Base 100, add 20:", sp(20))
    print("Base 100, add 30:", sp(30))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    secrets = memory_vault()
    print("Store 'secret' = 42")
    secrets["store"]("secret", 42)
    print("Recall 'secret':", secrets["recall"]("secret"))
    print("Recall 'unknown':",  secrets["recall"]("unknown"))

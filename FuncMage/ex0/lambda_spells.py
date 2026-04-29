#!/usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]
                    ) -> list[dict[str, Any]]:
    return list(sorted(artifacts, key=lambda x: x["power"], reverse=True))


def power_filter(mages: list[dict[str, Any]], min_power: int
                 ) -> list[dict[str, Any]]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    st = list(map(lambda x: "* " + x + " *", spells))
    return st


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, float]:
    stat = dict()
    stat["max_power"] = max(mages, key=lambda x: x["power"])["power"]
    stat["min_power"] = min(mages, key=lambda x: x["power"])["power"]
    stat["avg_power"] = sum(mage["power"] for mage in mages) / len(mages)
    return stat


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92,  "type": "weapon"}
    ]

    sorted_artifacts = artifact_sorter(artifacts)

    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']}"
          f" ({sorted_artifacts[1]['power']} power)")

    print("\nTesting power filter...")
    test_mages = [
        {'name': 'Storm', 'power': 95},
        {'name': 'Phoenix', 'power': 100},
        {'name': 'Morgan', 'power': 49}
    ]
    strong_mages = power_filter(test_mages, 50)
    print(f"Mages with power >= 50: {[m['name'] for m in strong_mages]}")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]

    transformed = spell_transformer(spells)

    print(" ".join(transformed))
    print("\nTesting mage stats...")
    stats = mage_stats(test_mages)
    print(f"Max: {stats['max_power']}, Min: {stats['min_power']}, "
          f"Avg: {stats['avg_power']:.2f}")
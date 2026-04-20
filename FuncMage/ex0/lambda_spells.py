#!/usr/bin/env python3
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    st = list(map(lambda x: "* " + x +" *", spells))
    return " ".join(st)

def mage_stats(mages: list[dict]) -> dict:
    stat = dict()
    stat["max_power"] = max(mages, key=lambda x: x["power"])["power"]
    stat["min_power"] = min(mages, key=lambda x: x["power"])["power"]
    stat["avg_power"] = sum(mage["power"] for mage in mages) / len(mages)
    return stat

if __name__ == "__main__":
    print("Testing artifact sorter...")

    artifacts = [
        {"name": "Crystal Orb", "power": 85},
        {"name": "Fire Staff", "power": 92}
    ]

    sorted_artifacts = artifact_sorter(artifacts)

    print(f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)")

    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]

    transformed = spell_transformer(spells)

    print("".join(transformed))
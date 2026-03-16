#!/usr/bin/env python3
import sys


def parse_inventory_data() -> dict:
    inventory = {}
    for arg in sys.argv[1:]:
        colon = 0
        while arg[colon] != ":":
            colon += 1
        item = arg[:colon]
        count = int(arg[colon + 1:])
        inventory[item] = count
    return inventory


def sort_dict(inventory: dict) -> list:
    items = []
    for pair in inventory.items():
        items += [pair]
    i = 0
    n = len(items)
    while i < n:
        max_index = i
        j = i + 1
        while j < n:
            if items[j][1] > items[max_index][1]:
                max_index = j
            j += 1
        temp = items[i]
        items[i] = items[max_index]
        items[max_index] = temp
        i += 1
    return items


def main() -> None:
    print("=== Inventory System Analysis===\n")

    inventory = parse_inventory_data()

    total_items = 0
    for count in inventory.values():
        total_items += count
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    print()

    print("=== Current Inventory ===")
    items = sort_dict(inventory)
    i = 0
    while i < len(items):
        item = items[i][0]
        count = items[i][1]
        percent = (count / total_items) * 100
        unit = "unit" if count == 1 else "units"
        print(f"{item}: {count} {unit} ({percent:.1f}%)")
        i += 1
    print()

    print("=== Inventory Statistics ===")
    most_abundent = None
    least_abundent = None
    for item, count in inventory.items():
        if most_abundent is None or count > inventory[most_abundent]:
            most_abundent = item
        if least_abundent is None or count < inventory[least_abundent]:
            least_abundent = item

    unit = "units" if inventory[most_abundent] != 1 else "unit"
    print(f"Most abundent: {most_abundent} ", end="")
    print(f"({inventory[most_abundent]} {unit})")
    unit = "units" if inventory[least_abundent] != 1 else "unit"
    print(f"Least abundent: {least_abundent} ", end="")
    print(f"({inventory[least_abundent]} {unit})")
    print()

    print("=== Item Categories ===")
    moderate = {}
    scarce = {}
    for item in inventory.items():
        if item[1] >= 5:
            moderate[item[0]] = item[1]
        else:
            scarce[item[0]] = item[1]
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print()

    print("=== Management Suggestions ===")
    restock = [item for item, count in inventory.items() if count < 2]
    print(f"• Restock needed: {restock}")
    print()

    print("=== Dictionary Properties Demo ===")
    keys = [key for key in inventory.keys()]
    values = [value for value in inventory.values()]
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values: {values}")
    print(f"Sample lookup - ’sword’ in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()

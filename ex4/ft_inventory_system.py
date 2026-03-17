#!/usr/bin/env python3
import sys

def is_digit(s: str) -> bool:
    if s == "":
        return False
    for char in s:
        if char < "0" or char > "9":
            return False
    return True


def my_int(str_int: str) -> int:
    digits = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
        "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
    }

    result = 0
    for dig in str_int:
        if dig not in digits:
            raise ValueError("Invalid digit")
        result = result * 10 + digits[dig]

    return result


def parse_inventory_data() -> dict | None:
    inventory = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print("Invalid input. Usage: python3 ft_inventory_system.py"
                    " item1:quantity1 item2:quantity2 ...")
            return
        colon = 0
        while arg[colon] != ":":
            colon += 1
        item = arg[:colon]
        if item == "":
            print("Invalid input. Usage: python3 ft_inventory_system.py"
                    " item1:quantity1 item2:quantity2 ...")
            return
        if not is_digit(arg[colon + 1:]):
            print("Invalid input. Usage: python3 ft_inventory_system.py"
                    " item1:quantity1 item2:quantity2 ...")
            return
        count = my_int(arg[colon + 1:])
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
    if len(sys.argv) == 1:
        print("No data provided. Usage: python3 ft_inventory_system.py"
              " item1:quantity1 item2:quantity2 ...")
        return

    print("=== Inventory System Analysis===")
    inventory = parse_inventory_data()
    if inventory is None:
        return
    print()
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
        if total_items:
            percent = (count / total_items) * 100
        else:
            percent = 0
        unit = "unit" if count == 1 else "units"
        print(f"{item}: {count} {unit} ({percent:.1f}%)")
        i += 1
    print()

    print("=== Inventory Statistics ===")
    most_abundant = None
    least_abundant = None
    for item, count in inventory.items():
        if most_abundant is None or count > inventory[most_abundant]:
            most_abundant = item
        if least_abundant is None or count < inventory[least_abundant]:
            least_abundant = item

    unit = "units" if inventory[most_abundant] != 1 else "unit"
    print(f"Most abundant: {most_abundant} ", end="")
    print(f"({inventory[most_abundant]} {unit})")
    unit = "units" if inventory[least_abundant] != 1 else "unit"
    print(f"Least abundant: {least_abundant} ", end="")
    print(f"({inventory[least_abundant]} {unit})")
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
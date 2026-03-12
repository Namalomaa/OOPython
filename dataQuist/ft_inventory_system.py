#!/usr/bin/env python3

def main():
    print("=== Inventory System ===\n")

    inventory = {
        "potion": 5,
        "armor": 3,
        "shield": 2,
        "sword": 1,
        "helmet": 1
    }
    total_items = 0
    for count in inventory.values():
        total_items += count
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")
    print()
    print("=== Current Inventory ===")
    

    print("=== Inventory Statistics ===")



if __name__ == "__main__":
    main()
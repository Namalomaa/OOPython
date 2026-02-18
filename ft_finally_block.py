def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    plants = ["tomato", "lettuce", "carrots"]
    plants2 = ["tomatow", None]
    print("Testing normal watering...")
    try:
        water_plants(plants)
    except ValueError as e:
        print(e)
    print("\nTesting with error...")
    try:
        water_plants(plants2)
    except ValueError as e:
        print(e)
    finally:
        print("\nCleanup always happens, even with errors!")

def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():

    print("=== Garden Watering System ===\n")
    plants = ["tomato", "lettuce", "carrots"]
    plants2 = ["tomatow", None]
    print("Testing normal watering...")
    try:
        water_plants(plants)
        print("Watering completed successfully!")
    except ValueError as e:
        print(e)
    print("\nTesting with error...")
    try:
        water_plants(plants2)
    except ValueError as e:
        print(e)
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

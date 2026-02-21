def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None | str:
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")

    if not (1 <= water_level <= 10):
        if water_level > 10:
            raise ValueError(f"Error: Water level {water_level} "
                             "is too high (max 10)")
        else:
            raise ValueError(f"Error: Water level {water_level} "
                             "is too low (min 1)")
    if not (2 <= sunlight_hours <= 12):
        if sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                             " is too high (max 12)")
        else:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours}"
                             " is too low (min 2)")
    msg = f"Plant ’{plant_name}’ is healthy!"
    print(msg)
    return msg


def test_plant_checks() -> None:
    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(e)
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(e)
    print("\nTesting bad water level...")
    try:
        check_plant_health("Tulip", 15, 5)
    except ValueError as e:
        print(e)
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("carrot", 5, 0)
    except ValueError as e:
        print(e)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    print()
    test_plant_checks()

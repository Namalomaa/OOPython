class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_all(plant: str, plant_status: str, water_level: int) -> None:
    print("Testing catching all garden errors...")
    check_plant(plant, plant_status)
    check_water(water_level)


def check_plant(plant: str, plant_status: str) -> None:
    print("Testing PlantError...")
    if plant_status == "wilting":
        raise PlantError(f"The {plant} plant is {plant_status}!")


def check_water(water_level: int) -> None:
    print("Testing WaterError...")
    if water_level <= 0:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    try:
        check_plant("tomato", "wilting")
    except PlantError as e:
        print(f"caught a PlantError: {e}")
    print()
    try:
        check_water(-5)
    except WaterError as e:
        print(f"caught a WaterError: {e}")
    print()
    try:
        check_all("tomato", "wilting", -5)
    except GardenError as e:
        print(f"caught a garden error: {e}")
    print("\nAll custom error types work correctly!")

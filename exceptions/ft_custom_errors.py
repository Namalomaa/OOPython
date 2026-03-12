class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant: str, plant_status: str) -> None:
    if plant_status == "wilting":
        raise PlantError(f"The {plant} plant is {plant_status}!")


def check_water(water_level: int) -> None:
    if water_level <= 0:
        raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant("tomato", "wilting")
    except PlantError as e:
        print(f"caught a PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        check_water(-5)
    except WaterError as e:
        print(f"caught a WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato", "wilting")
    except GardenError as e:
        print(f"caught a garden error: {e}")
    try:
        check_water(-4)
    except GardenError as e:
        print(f"caught a garden error: {e}")
    print("\nAll custom error types work correctly!")

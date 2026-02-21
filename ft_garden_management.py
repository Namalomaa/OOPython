class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    def __init__(self) -> None:
        self.plants = {}

    def add_plant(self, name: str, water: int, sun: int) -> None:
        if not name:
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        try:
            water = int(water)
        except ValueError:
            raise GardenError("Water level must be an int")
        try:
            sun = int(sun)
        except ValueError:
            raise GardenError("Sunlight hours must be an int")
        self.plants[name] = {
            "water": water,
            "sun": sun
        }
        print(f"Added {name} successfully")

    def check_plant_health(self, name: str) -> None:

        if name not in self.plants:
            raise PlantError(f"Error '{name}' does not exist")

        plant = self.plants[name]
        water_level = plant["water"]
        sunlight_hours = plant["sun"]

        if not (1 <= water_level <= 10):
            if water_level > 10:
                raise WaterError(f"Error checking {name}: Water level"
                                 f" {water_level} is too high (max 10)")
            else:
                raise WaterError(f"Error checking {name}: Water level"
                                 f" {water_level} is too low (min 1)")
        if not (2 <= sunlight_hours <= 12):
            if sunlight_hours > 12:
                raise PlantError(f"Error checking {name}: Sunlight hours"
                                 f" {sunlight_hours} is too high (max 12)")
            else:
                raise PlantError(f"Error checking {name}: Sunlight hours"
                                 f" {sunlight_hours} is too low (min 2)")
        print(f"{name}: healthy(water: {water_level}, sun: {sunlight_hours})")

    def water_plants(self) -> None:
        try:
            print("Opening watering system")
            if not self.plants:
                raise WaterError("No plants to water")
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_tank(tank_level: int) -> None:
        if tank_level <= 0:
            raise GardenError("Not enough water in tank")
        else:
            print("tank level is Fine!")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    g = GardenManager()
    garden1 = [
        {"name": "tomato", "water": 5, "sun": 8},
        {"name": "lettuce", "water": 15, "sun": 6},
        {"name": "", "water": 3, "sun": 4}
    ]
    print("Adding plants to garden...")

    for plant in garden1:
        try:
            g.add_plant(**plant)
        except GardenError as e:
            print(e)
    print("\nWatering plants...")
    g.water_plants()
    print("\nChecking plant health...")
    for plant in g.plants:
        try:
            g.check_plant_health(plant)
        except GardenError as e:
            print(e)

    print("\nTesting Error Recovery...")
    try:
        GardenManager.check_tank(0)
    except GardenError as e:
        print(f"caught GardenError: {e}")

    print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()

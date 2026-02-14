
class Plant:
    counter = 0

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        Plant.counter += 1

    def get_type(self):
        return "regular"

    def grow(self) -> None:
        self.height += 1
        print(f"- {self.name} grew 1cm")

    def display_basic_info(self) -> None:
        print(f"{self.name}: {self.height}cm", end="")

    def display(self) -> None:
        print()


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def get_type(self):
        return "flowering"

    def bloom(self) -> None:
        self.is_blooming = True

    def display(self):
        self.display_basic_info()
        print(f", {self.color} flowers ({self.is_blooming})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def get_type(self):
        return "prize"

    def display(self):
        self.display_basic_info()
        print(f", prize points: {self.points}")


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        self.total_plants = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants += [plant]
        self.total_plants += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden: ")
        for plant in self.plants:
            plant.display()


class GardenManager:
    total_gardens = 0

    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden: Garden):
        self.gardens += [garden]
        GardenManager.total_gardens += 1

    def garden_network(cls) -> None:

        print("Garden Network Created")
        return cls()

    garden_network = classmethod(garden_network)

    class GardenStats:

        def count_types(plants: list[Plant]):
            reg = 0
            flower = 0
            prize = 0

            for p in plants:
                plant_type = p.get_type()

                if plant_type == "regular":
                    reg += 1
                elif plant_type == "flowering":
                    flower += 1
                elif plant_type == "prize":
                    prize += 1

            return reg, flower, prize

        count_types = staticmethod(count_types)

        def validate_height(height: int) -> bool:
            return height > 0
        validate_height = staticmethod(validate_height)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()
    p1 = Plant("Oak", 101)
    f1 = FloweringPlant("Rose", 26, "red")
    f1.bloom()
    p1 = PrizeFlower("Sunflower", 51, "yellow", 10)
    owner1 = Garden("Alice")
    owner1.add_plant(p1)
    owner1.add_plant(f1)
    owner1.add_plant(p1)
    print()
    owner1.grow_all()
    print()
    owner1.report()
    print()
    

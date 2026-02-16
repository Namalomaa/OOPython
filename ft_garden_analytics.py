#!/usr/bin/env python3

class Plant:
    counter = 0

    def set_name(self, name: str) -> None:
        self._name = name

    def set_height(self, height: int) -> None:
        self._height = height

    def __init__(self, name: str, height: int) -> None:
        self.set_name(name)
        self.set_height(height)
        Plant.counter += 1

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> int:
        return self._height

    def get_type(self) -> str:
        return "regular"

    def get_score(self) -> int:
        return self._height

    def grow(self) -> None:
        self._height += 1
        print(f"{self._name} grew 1cm")

    def display_basic_info(self) -> None:
        print(f"- {self._name}: {self._height}cm", end="")

    def display(self) -> None:
        self.display_basic_info()
        print()


class FloweringPlant(Plant):

    def set_color(self, name: str) -> None:
        self._color = name

    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.set_color(color)
        self.is_blooming = False

    def get_color(self) -> str:
        return self._color

    def get_type(self) -> str:
        return "flowering"

    def bloom(self) -> None:
        self.is_blooming = True

    def display_f(self) -> None:
        self.display_basic_info()
        if self.is_blooming:
            blm = "blooming"
        else:
            blm = "wilting"
        print(f", {self._color} flowers ({blm})", end="")

    def display(self) -> None:
        self.display_f()
        print()


class PrizeFlower(FloweringPlant):

    def set_points(self, points: int) -> None:
        self._points = points

    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        super().__init__(name, height, color)
        self.set_points(points)

    def get_points(self) -> int:
        return self._points

    def get_type(self) -> str:
        return "prize"

    def get_score(self) -> int:
        return self._height + self._points

    def display(self) -> None:
        super().display_f()
        print(f", prize points: {self._points}")


class Garden:

    def set_plants(self, plants: list[Plant]) -> None:
        self._plants = plants

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._plants = []
        self.total_growth = 0
        self.total_plants = 0

    def get_plants(self) -> list[Plant]:
        return self._plants

    def add_plant(self, plant: Plant) -> None:
        self._plants += [plant]
        self.total_plants += 1
        print(f"Added {plant.get_name()} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self._plants:
            plant.grow()
            self.total_growth += 1

    def report(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden: ")
        for plant in self._plants:
            plant.display()
        print()
        print(f"Plants added: {self.total_plants},", end="")
        print(f" Total growth: {self.total_growth}cm")

        reg, flower, prize = GardenManager.GardenStats.count_types(
            self.get_plants())
        print(f"Plant types: {reg} regular, {flower}", end="")
        print(f" flowering, {prize} prize flowers")


class GardenManager:
    total_gardens = 0

    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens += [garden]
        GardenManager.total_gardens += 1

    def garden_network(cls) -> None:
        print("Garden Network Created")
        return cls()


    garden_network = classmethod(garden_network)

    class GardenStats:

        def count_types(plants: list[Plant]) -> tuple[int, int, int]:
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

        def calculate_score(plants: list[Plant]) -> int:
            total = 0
            for p in plants:
                total += p.get_score()
            return total


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    p1 = Plant("Oak Tree", 100)
    f1 = FloweringPlant("Rose", 25, "red")
    f1.bloom()
    pr1 = PrizeFlower("Sunflower", 50, "yellow", 10)
    pr1.bloom()

    owner1 = Garden("Alice")
    owner1.add_plant(p1)
    owner1.add_plant(f1)
    owner1.add_plant(pr1)

    owner2 = Garden("Bob")
    owner2.add_plant(Plant("Olive", 92))

    print()

    manager = GardenManager.garden_network()
    manager.add_garden(owner1)
    manager.add_garden(owner2)

    owner1.grow_all()
    print()
    owner1.report()
    print()

    print("Height validation test:",
          GardenManager.GardenStats.validate_height(p1.get_height()))

    score1 = GardenManager.GardenStats.calculate_score(owner1.get_plants())
    score2 = GardenManager.GardenStats.calculate_score(owner2.get_plants())

    print(f"Garden scores - Alice: {score1}, Bob: {score2}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")

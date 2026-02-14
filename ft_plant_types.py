class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display_basic_info(self) -> None:
        print(f"{self.name} ({self.__class__.__name__}):", end="")
        print(f" {self.height}cm, {self.age} days", end=", ")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")

    def display(self) -> None:
        self.display_basic_info()
        print(f"{self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int, shade: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.shade} square meters of shade")

    def display(self) -> None:
        self.display_basic_info()
        print(f"{self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display(self) -> None:
        self.display_basic_info()
        print(f"{self.harvest_season} harvest")
        print(f"{self.name} is {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    f1 = Flower("Rose", 25, 30, "red")
    f2 = Flower("Tulip", 17, 26, "Pink")

    t1 = Tree("Oak", 500, 1825, 50, 78)
    t2 = Tree("Olive", 350, 2190, 45, 70)

    v1 = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    v2 = Vegetable("Okra", 20, 32, "summer", "rich in Potassium")

    f1.display()
    f1.bloom()
    print()
    t1.display()
    t1.produce_shade()
    print()
    v1.display()

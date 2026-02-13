class Plant:

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.day = 1

    def display(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 1

    def grow_older(self) -> None:
        self.age += 1
        self.day += 1

    def current_status(self) -> None:
        print(f"=== Day {self.day} ===")
        self.display()
        dif = self.day - 1
        if self.day >= 7:
            print(f"Growth this week: +{dif}cm")


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p1.current_status()
    for i in range(6):
        p1.grow()
        p1.grow_older()

    p1.current_status()

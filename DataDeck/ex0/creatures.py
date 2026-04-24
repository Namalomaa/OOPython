from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, n: str, t: str) -> None:
        self.c_name = n
        self.c_type = t

    @abstractmethod
    def attack(self):
        pass

    def describe(self) -> str:
        return f"{self.c_name} is a {self.c_type} type Creature"


class Flameling(Creature):

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self):
        return "Flameling uses Ember!"


class Pyrodon(Creature):

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self):
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):

    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self):
        return "Aquabub uses Water Gun!"


class Torragon(Creature):

    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self):
        return "Torragon uses Hydro Pump!"

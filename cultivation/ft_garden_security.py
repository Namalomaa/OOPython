#!/usr/bin/env python3

class SecurePlant:

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height{value}cm [REJECTED]")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def __init__(self, name, height, age):
        self._name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {name}")
        self.set_height(height)
        self.set_age(age)

    def current_plant(self) -> None:
        print(f"Current plant: {self._name} ({self._height}cm,", end="")
        print(f" {self._age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 25, 30)
    print()
    p1.set_height(-5)
    print()
    p1.current_plant()

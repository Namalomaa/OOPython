#!/usr/bin/env python3
import math


def calculate_distance(point1: tuple[int, int, int],
                       point2: tuple[int, int, int]) -> float:
    return math.sqrt((point2[0] - point1[0]) ** 2 +
                     (point2[1] - point1[1]) ** 2 +
                     (point2[2] - point1[2]) ** 2)


def parse_coordinates(coordinates: str) -> tuple[int, int, int]:
    n_coor = coordinates.split(",")
    x = int(n_coor[0])
    y = int(n_coor[1])
    z = int(n_coor[2])
    return (x, y, z)


def main():
    print("=== Game Coordinate System ===\n")
    origin = (0, 0, 0)
    position = (10, 20, 5)
    print("Position created:", position)
    print(f"Distance between {origin} and {position}: "
          f"{calculate_distance(origin, position):.2f}")
    print()
    coord = "3,4,0"
    print(f'Parsing coordinates: "{coord}"')
    p1 = parse_coordinates(coord)
    d1 = calculate_distance(origin, p1)
    print("Parsed coordinates:", p1)
    print(f"Distance between {origin} and {p1}: {d1}\n")

    invalid_coord = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_coord}"')

    try:
        parse_coordinates(invalid_coord)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__} Args: {e.args}\n")

    print("Unpacking demonstration:")
    x, y, z = p1
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()

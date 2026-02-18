def garden_operations(error: str) -> None:
    if error == "ValueError":
        int("fourty two")
    elif error == "ZeroDivisionError":
        print(7 / 0)
    elif error == "FileNotFoundError":
        f = open("missing.txt", "r")
        f.close()
    elif error == "KeyError":
        plants = {
            "flower": 15,
            "tree": 115
        }
        print(plants["rose"])


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    try:
        print("Testing ValueError...")
        garden_operations("ValueError")
    except ValueError as e:
        print("Caught ValueError:", e)
    print()
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
    print()
    try:
        print("Testing FileNotFoundError...")
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
    print()
    try:
        print("Testing KeyError...")
        garden_operations("KeyError")
    except KeyError as e:
        print("Caught KeyError:", e)
    print()
    try:
        print("Testing multiple errors together...")
        garden_operations("ZeroDivisionError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
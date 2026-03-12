def check_temperature(temp_str: str) -> int | None:
    try:
        print(f"Testing temperature: {temp_str}")
        temp = int(temp_str)
        if temp <= 40 and temp >= 0:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
    except ValueError:
        print(f"Error: ’{temp_str}’ is not a valid number")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print()
    check_temperature("25")
    print()
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")
    print()
    print("All tests completed - program didn’t crash!")


if __name__ == "__main__":
    test_temperature_input()

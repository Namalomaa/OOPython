#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    try:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1], "r")
        print("---\n")
        print(file.read())
        print("\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")

    


if __name__ == "__main__":
    main()

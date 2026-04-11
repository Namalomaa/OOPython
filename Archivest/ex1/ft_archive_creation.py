#!/usr/bin/env python3
import sys


def transform(content: str) -> None:
    print("Transform data: ")
    print("---\n")
    new = ""
    for c in content:
        if c == "\n":
            new += "#\n"
        else:
            new += c
    new += "#\n"
    print(new)
    print("\n---")
    n_file = input("Enter new file name (or empty): ")
    if not n_file:
        print("Not saving data.")
        return
    else:
        f = open(n_file, "w")
        print(f"Saving data to '{n_file}'")
        f.write(new)
        f.close()
        print(f"Data saved in file '{n_file}'.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    try:
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{sys.argv[1]}'")
        file = open(sys.argv[1], "r")
        print("---\n")
        content = file.read()
        print(content)
        print("\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    print()
    transform(content)
    


if __name__ == "__main__":
    main()

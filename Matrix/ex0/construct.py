import sys
import os


def detect_env() -> bool:
    return (hasattr(sys, 'real_prefix') or 
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


def display_env_info():
    print(f"Current Python: {sys.executable}")
    print(f"Python prefix: {sys.prefix}")

    if detect_env():
        print("SUCCESS: You're in an isolated environment!")
        import site
        print(f"Package path: {site.getsitepackages()[0]}")
    else:
        print("WARNING: Global environment detected!")
        print("Instructions: python -m venv matrix_env")


if __name__ == "__main__":
    display_env_info()

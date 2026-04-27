import sys
import os

def detect_env() -> bool:
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


def display_env_info():

    if detect_env():
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.prefix}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        import site
        print(f"Package path: {site.getsitepackages()[0]}")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.environ.get("VERTUAL_ENV")} detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    display_env_info()

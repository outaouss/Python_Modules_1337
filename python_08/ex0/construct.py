import sys
import os


def is_virtual_env() -> bool:

    has_dif = sys.prefix != sys.base_prefix

    return has_dif


def main() -> None:
    if not is_virtual_env():
        print("No virtual environment detected.")
        print("Instructions to set up your environment:")
        print("  1. Create: python3 -m venv matrix_env")
        print("  2. Activate: source matrix_env/bin/activate")
    else:
        print("Virtual environment detected!")

        venv_path = os.environ.get('VIRTUAL_ENV', sys.prefix)
        print(f"Environment Path: {venv_path}")
        print(f"Python Executable: {sys.executable}")


if __name__ == "__main__":
    main()

import sys
import os


def is_virtual_env() -> bool:
    """
    Detects if the script is running inside a Python Virtual Environment.

    Logic:
    When Python starts, it sets 'sys.base_prefix' to the global
    installation path.
    If a venv is active, 'sys.prefix' is changed to the venv's local directory.
    If they are different, we are isolated from the global system.
    """

    # Compare the current execution prefix with the base system prefix
    has_dif = sys.prefix != sys.base_prefix

    return has_dif


def main() -> None:
    # Check if the environment detection logic
    # returns False (Plugged in to Global)

    if not is_virtual_env():
        print("\nMATRIX STATUS: You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        # Provide instructions on how to create and enter
        # the 'Construct' (venv)
        print("To enter the construct, run:")
        print("python3 -m venv --without-pip matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")
        print("\nThen run this program again.")

    else:
        # The prefixes were different, meaning the user is in the 'Construct'
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print("Current Python:", sys.executable)

        # Extract the name of the folder where the venv lives
        venv_name = os.path.basename(sys.prefix)
        print("Virtual Environment:", venv_name)

        # Retrieve the path from the environment
        # variable set by the 'activate' script
        env_path = os.environ.get('VIRTUAL_ENV')
        print("Environment Path:", env_path)

        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print("\nPackage installation path:")
        # Show where packages will actually be stored to prove isolation
        check = sys.path

        for p in check:
            if "site-packages" in p:
                print(p)
                break


if __name__ == "__main__":
    main()

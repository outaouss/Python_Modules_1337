def garden_operations() -> None:
    '''Simulates various common Python errors to
    demonstrate exception handling'''
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        1 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError as r:
        print(f"Caught FileNotFoundError: No such file '{r.filename}'\n")

    try:
        print("Testing KeyError...")
        x = {"vegetable": "potato"}
        print(x["missing\\_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")

    try:
        print("\nTesting multiple errors together...")
        1 / 0
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    '''Entry point for the error types demo'''
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

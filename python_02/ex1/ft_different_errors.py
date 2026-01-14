def garden_operations():
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
        print(x["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")

    try:
        print("\nTesting multiple errors together...")
        1 / 0
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


test_error_types()

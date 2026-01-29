def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    '''Validates plant conditions and raises
    ValueError if limits are exceeded'''
    if plant_name == "" or plant_name is None:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Demonstrates raising and catching errors for plant health."""
    print("=== Garden Plant Health Checker ===\n")

    tests_conditions = [
        ("Good Values", ("tomato", 5, 5)),
        ("Empty plant name", ("", 5, 5)),
        ("Bad water level", ("tomato", 15, 6)),
        ("Bad sunlight hours", ("tomato", 5, 0)),
    ]

    for test, (name, water, sun) in tests_conditions:
        print(f"Testing {test}...")
        try:
            result = check_plant_health(name, water, sun)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")
        print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    try:
        test_plant_checks()
    except Exception as e:
        print(e)

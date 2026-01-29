def check_temperature(temp_str: str = None) -> None:
    print(f"Testing temperature: {temp_str}")
    try:
        if temp_str is None:
            raise ValueError("No Temperature Input Provided")

        temp = int(temp_str)

        if temp > 40:
            raise ValueError(f"{temp}°C is too hot (max 40°C)")
        elif temp < 0:
            raise ValueError(f"{temp}°C is too cold (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!\n")

    except ValueError as e:
        print(e)


def test_temperature_input() -> None:
    '''This function used to Run a series of test cases
    to verify the temperature checker logic'''

    print("=== Garden Temperature Checker ===\n")

    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")

    print("All tests completed - program didn't crash!")


# Get -- >
if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(e)

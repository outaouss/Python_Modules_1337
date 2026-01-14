def check_temperature(temp_str):
    print(f"Testing temperature: {temp_str}")

    try:
        temp = int(temp_str)
        if (temp >= 0 and temp <= 40):
            print(f"Temperature {temp}°C is perfect for plants!\n")
            return temp
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        else:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
    except ValueError:
        print(f"Error: {temp_str} is not a valid number\n")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    print()
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


test_temperature_input()

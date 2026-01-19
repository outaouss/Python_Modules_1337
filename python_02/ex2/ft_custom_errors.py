class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def wilting_checker(value: int) -> bool:
    return value < 0


def water_checker(level: int) -> bool:
    return level <= 0


def plant_health(wilting: int) -> None:
    '''Checks the health status of a plant based on a wilting factor'''
    if wilting_checker(wilting):
        raise PlantError("The tomato plant is wilting!")
    else:
        print("The tomato plant is in good health!")


def water_level(tank_validation: int) -> None:
    '''Validates the current water level in the garden tank'''
    if water_checker(tank_validation):
        raise WaterError("Not enough water in the tank!")
    else:
        print("There is enough water in the tank!")


if __name__ == "__main__":
    health_val = -15  # you can change it to check the catch error
    water_level_val = -15  # you can change it to check the catch error

    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        plant_health(health_val)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        water_level(water_level_val)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    for test, condition in [(plant_health, health_val),
                            (water_level, water_level_val)]:
        try:
            test(condition)
        except GardenError as e:
            print(f"Caught a garden error: {e}")
    print("\n All custom error types work correctly!")

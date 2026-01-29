class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def wilting_checker(value: int) -> bool:
    '''Methode That Return True or False For The Plant Wilting Check'''
    return value < 0


def water_checker(level: int) -> bool:
    '''Methode That Return True or False For The Storage of Water'''
    return level <= 0


def plant_health(wilting: int, name: str) -> None:
    '''Checks the health status of a plant based on a wilting factor'''
    if wilting_checker(wilting):
        raise PlantError(f"The {name} plant is wilting!")
    else:
        print(f"The {name} plant is in good health!")


def water_level(tank_validation: int, name: str) -> None:
    '''Validates the current water level in the garden tank'''
    if water_checker(tank_validation):
        raise WaterError(f"Not enough water in the {name}!")
    else:
        print(f"There is enough water in the {name}!")


if __name__ == "__main__":
    try:
        health_val = -15  # you can change it to check the catch error
        water_level_val = -15  # you can change it to check the catch error

        plant_name = "tomato"
        storage = "tank"

        print("=== Custom Garden Errors Demo ===")

        print("\nTesting PlantError...")
        try:
            plant_health(health_val, plant_name)
        except PlantError as e:
            print(f"Caught PlantError: {e}")

        print("\nTesting WaterError...")
        try:
            water_level(water_level_val, storage)
        except WaterError as e:
            print(f"Caught WaterError: {e}")

        print("\nTesting catching all garden errors...")
        for test, condition, name in [(plant_health, health_val, plant_name),
                                      (water_level, water_level_val, storage)]:
            try:
                test(condition, name)
            except GardenError as e:
                print(f"Caught a garden error: {e}")
        print("\nAll custom error types work correctly!")
    except Exception as e:
        print(e)

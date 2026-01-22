
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plant_list = []

    def water_checker(level: int) -> bool:
        return level <= 0
    water_checker = staticmethod(water_checker)

    def water_level(tank_validation: int) -> None:
        '''Validates the current water level in the garden tank'''
        if GardenManager.water_checker(tank_validation):
            raise WaterError("Not enough water in the tank!")
        else:
            print("There is enough water in the tank!")
    water_level = staticmethod(water_level)

    def add_plant(self, plant: list = None) -> None:
        try:
            if not plant:
                raise ValueError("no plant given")
            if plant[0] == "" or plant[0] is None:
                raise ValueError("Plant name cannot be empty!")
            else:
                self.plant_list += [plant]
                print(f"Added {plant[0]} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plant_list:
                if (plant[0] is None or plant[0] == ""
                        or type(plant[0]) is not str):
                    raise ValueError("Cannot water None - invalid plant!")
                print("Watering ", plant[0], "- success")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        try:
            for plant in self.plant_list:
                if plant[1] < 1:
                    raise ValueError(f"Water level {plant[1]} "
                                     f"is too low (min 1)")
                elif plant[1] > 10:
                    raise ValueError(f"Water level {plant[1]} "
                                     f"is too high (max 10)")

                if plant[2] < 2:
                    raise ValueError(f"Sunlight hours {plant[2]} "
                                     f"is too low (min 2)")
                elif plant[2] > 12:
                    raise ValueError(f"Sunlight hours {plant[2]} "
                                     f"is too high (max 12)")

                print(f"{plant[0]}: healthy (water: {plant[1]}, "
                      f"sun: {plant[2]})")
        except ValueError as e:
            print(f"Error checking {plant[0]}: {e}")


def test_garden_management():
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    plants = [
        ["tomato", 5, 8],
        ["lettuce", 15, 8],
        ["", 5, 8],
    ]
    print("Adding plants to garden...")
    for plant in plants:
        manager.add_plant()
    print()

    print("Watering plants...")
    manager.water_plants(plant)
    print()

    print("Checking plant health...")
    manager.check_plant_health()
    print()

    print("Testing erorr recovery...")
    try:
        GardenManager.water_level(-5)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    finally:
        print("System recovered and continuing...")
    print("\nGarden managemant system test complete!")


if __name__ == "__main__":
    test_garden_management()

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plant_list = []

    def add_plants(self, plant: str) -> None:
        try:
            if plant == "" or plant is None or type(plant) is not str:
                raise ValueError("Plant name cannot be empty!")
            else:
                self.plant_list += [plant]
                print(f"Added {plant} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plant_list:
                if plant is None or plant == "" or type(plant) is not str:
                    raise ValueError("Cannot water None - invalid plant!")
                print("Watering ", plant, "- success")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> None:
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")

        print(f"{plant_name}: healthy (water: {water_level}, "
              f"sun: {sunlight_hours})")


def test_garden_management():
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    plants = [
        "tomato",
        "lettuce",
        "",
    ]
    print("Adding plants to garden...")
    for plant in plants:
        manager.add_plants(plant)
    print()

    print("Watering plants...")
    manager.water_plants()
    print()

    print("Checking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    try:
        manager.check_plant_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")
    print()

    print("Testing erorr recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden managemant system test complete!")


if __name__ == "__main__":
    test_garden_management()

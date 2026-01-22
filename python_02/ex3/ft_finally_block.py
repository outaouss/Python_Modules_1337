def water_plants(plant_list: list):
    '''Waters plants and ensures the system closes using a finally block'''
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or type(plant) is not str:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            elif plant == "":
                raise ValueError("Cannot water None - invalid plant!")
            print("Watering ", plant)
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    '''Demonstrates watering system success and failure cases'''
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    plants = [
        "tomato",
        "lettuce",
        "carrots",
    ]
    water_plants(plants)
    print("\nTesting with error...")
    plants_with_errors = [
        "tomato",
        None,
    ]
    water_plants(plants_with_errors)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

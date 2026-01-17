class Plant:
    '''Blueprint for a basic garden plant'''
    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age


# A list containing instances of the Plant class
plant_data = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 15, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120),
]


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    for p in plant_data:
        print(f"Created: {p.name} ({p.starting_height}cm, "
              f"{p.starting_age} days)")

    print(f"\nTotal plants created: {len(plant_data)}")

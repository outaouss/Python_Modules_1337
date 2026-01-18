class Plant:
    '''Blueprint for a basic garden plant'''
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


plant_data = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120),
]

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    for pot in plant_data:
        print(f"{pot.name}: {pot.height}cm, {pot.age} days old")

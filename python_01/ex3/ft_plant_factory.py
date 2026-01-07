class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


plant_data = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 90),
    Plant("Oak", 200, 365),
    Plant("Fern", 15, 120),
]

print("=== Plant Factory Output ===")

for p in plant_data:
    print(f"Created: {p.name} ({p.height}cm, {p.age} days)")

print(f"\nTotal plants created: {len(plant_data)}")

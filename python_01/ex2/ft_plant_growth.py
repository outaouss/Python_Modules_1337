class Plant:
    def __init__(self, name, height, age_old):
        self.name = name
        self.height = height
        self.age_old = age_old

    def grow(self):
        self.height += 1

    def age(self):
        self.age_old += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age_old} days old"


Plant_1 = Plant("Rose", 25, 30)

start_height = Plant_1.height

print("=== Day 1 ===")
print(Plant_1.get_info())

# You Can Add The Number of Days u want To Simulate :)
days_to_simulate = 6

for _ in range(days_to_simulate):
    Plant_1.grow()
    Plant_1.age()

print(f"=== Day {days_to_simulate + 1} ===")
print(Plant_1.get_info())

total_height = Plant_1.height - start_height
print(f"Growth this week: +{total_height}cm")

class Plant:
    '''Blueprint for a basic garden plant'''
    def __init__(self, name, height, age_old):
        self.name = name
        self.height = height
        self.age_old = age_old

    def grow(self):
        '''This Methode Created to Make A Plant Growing By [ x ]'''
        self.height += 1  # x

    def age(self):
        '''This Methode Created to Upgrade The Age of A Plant By [ x ]'''
        self.age_old += 1  # x

    def get_info(self):
        '''Methode of Getting A Plant Info'''
        return f"{self.name}: {self.height}cm, {self.age_old} days old"


if __name__ == "__main__":
    Plant_1 = Plant("Rose", 25, 30)

    start_height = Plant_1.height

    print("=== Day 1 ===")
    print(Plant_1.get_info())

    days_to_simulate = 6  # You Can Use Any Number of Days To Simulate

    for _ in range(days_to_simulate):
        Plant_1.grow()
        Plant_1.age()

    print(f"=== Day {days_to_simulate + 1} ===")
    print(Plant_1.get_info())

    total_height = Plant_1.height - start_height
    print(f"Growth this week: +{total_height}cm")

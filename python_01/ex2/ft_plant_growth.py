class Plant:
    '''Blueprint for a basic garden plant'''
    def __init__(self, name: str, height: int, age_attr: int) -> None:
        self.name = name
        self.height = height
        self.age_attr = age_attr

    def grow(self) -> None:
        '''This Methode Created to Make A Plant Growing By [ x ]'''
        self.height += 1  # x

    def age(self) -> None:
        '''This Methode Created to Upgrade The Age of A Plant By [ x ]'''
        self.age_attr += 1  # x

    def get_info(self) -> None:
        '''Methode of Getting A Plant Info'''
        return f"{self.name}: {self.height}cm, {self.age_attr} days old"


if __name__ == "__main__":
    Plant_1 = Plant("Rose", 25, 30)

    start_height = Plant_1.height

    print("=== Day 1 ===")
    print(Plant_1.get_info())

    days_to_simulate = 6  # You Can Use Any Number of Days To Simulate

    for i in range(days_to_simulate):
        Plant_1.grow()
        Plant_1.age()

    print(f"=== Day {days_to_simulate + 1} ===")
    print(Plant_1.get_info())

    total_height = Plant_1.height - start_height
    print(f"Growth this week: +{total_height}cm")

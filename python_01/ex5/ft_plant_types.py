class Plant:
    '''Blueprint for a basic garden plant'''
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    '''Blueprint for a basic garden FLower'''
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        '''Method print the blooming text'''
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    '''Blueprint for a basic garden Tree'''
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        '''Method Used To Calculate The Trunk Diameter'''
        shade = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    '''Blueprint for a basic garden plant.'''
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def status(self):
        '''Method to check the nutrition of a vegetable'''
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

# |--> Flower Farm <--|

    flower = [
        Flower("Rose", 25, 30, "red"),
        Flower("Sunflower", 150, 45, "yellow"),
        Flower("oussama", 155, 60, "blue"),
    ]
    for f in flower:
        print(f"{f.name} ({Flower.__name__}): {f.height}cm, "
              f"{f.age} days, {f.color} color")
        f.bloom()
    print()

# |--> Tree Farm <--|

    tree = [
        Tree("Oak", 500, 1825, 50),
        Tree("Maple", 600, 2500, 60),
    ]
    for t in tree:
        print(f"{t.name} ({Tree.__name__}): {t.height}cm, "
              f"{t.age} days, {t.trunk_diameter}cm diameter")
        t.produce_shade()
    print()

# |--> Vegetable Farm <--|

    vegetable = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 15, 60, "Autumn", "vitamin A"),
    ]
    for v in vegetable:
        print(f"{v.name} ({Vegetable.__name__}): {v.height}cm, "
              f"{v.age} days, {v.harvest_season} harvest")
        v.status()

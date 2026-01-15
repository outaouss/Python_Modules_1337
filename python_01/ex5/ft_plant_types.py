class Plant:
    '''Class For Plant'''
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    '''Class For Flower'''
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        '''Method print the blooming text'''
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    '''Class For Tree'''
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        '''Method Calculate the trunk diameter'''
        shade = int(self.trunk_diameter * 1.56)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    '''Class For Vegetable'''
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def status(self):
        '''Method to check the nutrition of a vegetable'''
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    flower = Flower("Rose", 25, 30, "red")
    flower_2 = Flower("Sunflower", 150, 45, "yellow")
    tree = Tree("Oak", 500, 1825, 50)
    tree_2 = Tree("Maple", 600, 2500, 60)
    vegetable = Vegetable("Tomato", 80, 90, "Summer", "vitamin C") 
    vegetable_2 = Vegetable("Carrot", 15, 60, "Autumn", "vitamin A")

    print(f"{flower.name} ({Flower.__name__}): {flower.height}cm, "
          f"{flower.age} days, {flower.color} color")
    flower.bloom()
    print(f"{flower_2.name} ({Flower.__name__}): {flower_2.height}cm, "
          f"{flower_2.age} days, {flower_2.color} color")
    flower_2.bloom()
    print()

    print(f"{tree.name} ({Tree.__name__}): {tree.height}cm, "
          f"{tree.age} days, {tree.trunk_diameter}cm diameter")
    tree.produce_shade()
    print(f"{tree_2.name} ({Tree.__name__}): {tree_2.height}cm, "
          f"{tree_2.age} days, {tree_2.trunk_diameter}cm diameter")
    tree_2.produce_shade()
    print()

    print(f"{vegetable.name} ({Vegetable.__name__}): {vegetable.height}cm, "
          f"{vegetable.age} days, {vegetable.harvest_season} harvest")
    vegetable.status()
    print(f"{vegetable_2.name} ({Vegetable.__name__}): "
          f"{vegetable_2.height}cm, "
          f"{vegetable_2.age} days, {vegetable_2.harvest_season} harvest")
    vegetable_2.status()

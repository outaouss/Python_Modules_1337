class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age
        print(f"Plant Created: {self.name}")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            print(f"\nInvalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            print(f"\nInvalid operations attempted: "
                  f"age {value} days [REJECTED]")  # Splited Line :)
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {self.__age} days [OK]")

    def display_status(self):
        print(f"\nCurrent plant: {self.name} "  # Splited Line :)
              f"({self.__height}cm, {self.__age} days)")


print("=== Garden Security System ===")

my_plant = SecurePlant("Rose", -6, 25)

my_plant.height = 25
my_plant.age = 30

my_plant.height = -5

my_plant.display_status()

class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant Created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self.__height

    def set_height(self, value):
        if value < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def get_age(self):
        return self.__age

    def set_age(self, value):
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

my_plant = SecurePlant("Rose", 25, 30)

# my_plant.set_height(25)
# my_plant.set_age(30)

my_plant.set_height(-5)

my_plant.display_status()

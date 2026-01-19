class SecurePlant:
    '''Blueprint for a secure garden plant'''
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = None
        self._age = None
        print(f"Plant Created: {self.name}")
        self.set_height(height, 0)
        self.set_age(age, 0)

    def get_height(self) -> int:
        '''This is A Methode To Get The Height of A Plant'''
        return self._height

    def set_height(self, value: int, flag: int) -> None:
        '''This is A Methode To Set A Value to The Height if Valid'''
        if value < 0:
            print(f"\nInvalid operation attempted: "
                  f"height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            if flag == 1:
                print(f"Height updated: {value}cm [OK]")

    def get_age(self) -> int:
        '''This is A Methode To Get The Age of A Plant'''
        return self._age

    def set_age(self, value: int, flag: int) -> None:
        '''This is A Methode To Set A Value to The Age if Valid'''
        if value < 0:
            print(f"\nInvalid operations attempted: "
                  f"age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            if flag == 1:
                print(f"Age updated: {self._age} days [OK]")

    def display_status(self) -> None:
        '''This Methode Used to Display The Infos of A Plant By Getting The
            Height And The Age of It'''

        if self._age is None or self._height is None:
            pass
        else:
            print(f"\nCurrent plant: {self.name} "
                  f"({self.get_height()}cm, {self.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    my_plant = SecurePlant("Rose", 15, 56)
    my_plant.set_height(25, 1)
    my_plant.set_age(30, 1)
    my_plant.set_height(-5, 1)
    my_plant.display_status()

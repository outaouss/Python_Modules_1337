class Plant:
    '''Base class for all vegetation in the garden.'''
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.category = "regular"


class FloweringPlant(Plant):
    '''A plant produces colored flowers, inheriting from the base Plant.'''
    def __init__(self, name: str, height: int, flower_color: str) -> None:
        super().__init__(name, height)
        self.flower_color = flower_color
        self.category = "FloweringPlant"


class PrizeFlower(FloweringPlant):
    '''A high-value flowering plant used for scoring in garden competitions.'''
    def __init__(self, name: str, height: int,
                 flower_color: str, prize_points: int) -> None:
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points
        self.category = "PrizeFlower"


class GardenManager:
    '''Class responsible for Tracks all gardens and shared stats'''
    total_gardens = 0
    global_growth = 0

    def __init__(self, name: str) -> None:
        '''Sets manager name and starts an empty plant list.'''
        self.name = name
        self.growth_amm = 1
        self.plant_list = []
        GardenManager.total_gardens += 1

    class GardenStats:
        '''Nested helper for plant data and validation.'''
        def validation_height(height: int) -> bool:
            '''Static method to ensure plant height is a non-negative value.'''
            return height >= 0
        validation_height = staticmethod(validation_height)

        def get_length(ft_list: list) -> int:
            '''Methode To Calculate The Length of A List'''
            count: int = 0
            for _ in ft_list:
                count += 1
            return count
        get_length = staticmethod(get_length)

        def generate_report(plant_list: list) -> None:
            '''Counts types and calculates total heights.'''
            total_height = 0
            plant_count = 0
            flower_count = 0
            prize_count = 0
            # --> [ Val ] <-- Responsible For Growth Validation
            val = GardenManager.global_growth
            for plant in plant_list:
                if plant.category == "PrizeFlower":
                    prize_count += 1
                elif plant.category == "FloweringPlant":
                    flower_count += 1
                elif plant.category == "regular":
                    plant_count += 1
                total_height += plant.height

            # Variable to Store the length methode
            length = GardenManager.GardenStats.get_length

            print(f"\nPlant added: {length(plant_list)}, "
                  f"Total growth: {GardenManager.global_growth}cm")
            print(f"Plant types: {plant_count} regular, "
                  f"{flower_count} flowering, {prize_count} prize flowers")
            print(f"\nHeight validation test: "
                  f"{GardenManager.GardenStats.validation_height(val)}")
        generate_report = staticmethod(generate_report)

    def add_plant(self, plant: Plant, flag: int) -> None:
        '''Validates height then adds plant to inventory.'''
        if GardenManager.GardenStats.validation_height(plant.height):
            self.plant_list += [plant]
            if flag == 0:
                print(f"Added {plant.name} to {self.name}'s garden")
        else:
            print("Invalid height, plant rejected")

    def grow_plants(self) -> None:
        '''Increases every plant's height by a set amount.'''
        growth_ammount = 1

        print(f"{self.name} is helping all plants grow...")
        for plant in self.plant_list:
            plant.height += growth_ammount
            GardenManager.global_growth += growth_ammount
            print(f"{plant.name} grew {growth_ammount}cm")

    def display_report(self) -> None:
        '''Lists individual plants and triggers the summary.'''
        print(f"== {self.name}'s Garden Report ==")
        print("Plants in garden:")
        for plant in self.plant_list:
            if plant.category == "PrizeFlower":
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.flower_color} flowers (blooming), "
                      f"Prize points: {plant.prize_points}")
            elif plant.category == "FloweringPlant":
                print(f"- {plant.name}: {plant.height}cm,"
                      f" {plant.flower_color} (blooming)")
            elif plant.category == "regular":
                print(f"- {plant.name}: {plant.height}cm")
        GardenManager.GardenStats.generate_report(self.plant_list)

    def get_score(self) -> int:
        '''Sums heights plus any extra prize points.'''
        total = 0
        for plant in self.plant_list:
            total += plant.height
            if plant.category == "PrizeFlower":
                total += plant.prize_points
        return total

    def create_garden_network(cls, managers: list) -> None:
        '''Combines scores from all managers in the system'''
        scores_string = ""
        i = 0

        for m in managers:
            entry = f"{m.name}: {m.get_score()}"
            scores_string += entry
            if i < GardenManager.GardenStats.get_length(managers) - 1:
                scores_string += ", "
            i += 1

        print(f"Garden scores - {scores_string}")
        print(f"Total gardens managed: {cls.total_gardens}")
    create_garden_network = classmethod(create_garden_network)


if __name__ == "__main__":
    # Managers
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    # Plants
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 40)
    _ = PrizeFlower("Sunflower", 50, "yellow", 42)

    # System Demo
    print("=== Garden Management System Demo ===")

    print()
    alice.add_plant(oak, 0)
    alice.add_plant(rose, 0)
    alice.add_plant(sunflower, 0)
    bob.add_plant(_, 1)

    print()
    alice.grow_plants()

    print()
    alice.display_report()
    GardenManager.create_garden_network([alice, bob])

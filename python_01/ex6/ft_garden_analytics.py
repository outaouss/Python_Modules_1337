class Plant:
    '''Base class for all vegetation in the garden.'''
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    '''A plant produces colored flowers, inheriting from the base Plant.'''
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color


class PrizeFlower(FloweringPlant):
    '''A high-value flowering plant used for scoring in garden competitions.'''
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points


class GardenManager:
    '''Class responsible for Tracks all gardens and shared stats'''
    total_gardens = 0

    def __init__(self, name):
        '''Sets manager name and starts an empty plant list.'''
        self.name = name
        self.plant_list = []
        GardenManager.total_gardens += 1

    class GardenStats:
        '''Nested helper for plant data and validation.'''
        @staticmethod
        def validation_height(height):
            '''Static method to ensure plant height is a non-negative value.'''
            return height >= 0

        @staticmethod
        def generate_report(plant_list):
            '''Counts types and calculates total heights.'''
            total_height = 0
            plant_count = 0
            flower_count = 0
            prize_count = 0
            for plant in plant_list:
                if isinstance(plant, PrizeFlower):
                    prize_count += 1
                elif isinstance(plant, FloweringPlant):
                    flower_count += 1
                elif isinstance(plant, Plant):
                    plant_count += 1
                total_height += plant.height
            print(f"\nPlant added: {len(plant_list)}, "
                  f"Total growth: {len(plant_list)}cm")
            print(f"Plant types: {plant_count} regular, "
                  f"{flower_count} flowering, {prize_count} prize flowers")
            print(f"\nHeight validation test: "
                  f"{GardenManager.GardenStats.validation_height(10)}")

    def add_plant(self, plant):
        '''Validates height then adds plant to inventory.'''
        if GardenManager.GardenStats.validation_height(plant.height):
            self.plant_list.append(plant)
            print(f"Added {plant.name} to {self.name}'s garden")
        else:
            print("Invalid height, plant rejected")

    def grow_plants(self):
        '''Increases every plant's height by a set amount.'''
        growth_ammount = 1  # Enter Any Ammount You Want !!!

        print(f"{self.name} is helping all plants grow...")
        for plant in self.plant_list:
            plant.height += growth_ammount
            print(f"{plant.name} grew {growth_ammount}cm")

    def display_report(self):
        '''Lists individual plants and triggers the summary.'''
        print(f"== {self.name}'s Garden Report ==")
        print("Plants in garden:")
        for plant in self.plant_list:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.flower_color} flowers (blooming), "
                      f"Prize points: {plant.prize_points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm,"
                      f" {plant.flower_color} (blooming)")
            elif isinstance(plant, Plant):
                print(f"- {plant.name}: {plant.height}cm")
        GardenManager.GardenStats.generate_report(self.plant_list)

    def get_score(self):
        '''Sums heights plus any extra prize points.'''
        total = 0
        for plant in self.plant_list:
            total += plant.height
            if isinstance(plant, PrizeFlower):
                total += plant.prize_points
        return total

    @classmethod
    def create_garden_network(cls, managers):
        '''Combines scores from all managers in the system.'''
        score_entries = []
        for manager in managers:
            current_score = manager.get_score()
            score_entries.append(f"{manager.name}: {current_score}")        
        scores_string = ", ".join(score_entries)
        print(f"Garden scores - {scores_string}")
        print(f"Total gardens managed: {cls.total_gardens}")


if __name__ == "__main__":
    # Managers
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    # Plants
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 40)

    # System Demo
    print("=== Garden Management System Demo ===")

    print()
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    print()
    alice.grow_plants()

    print()
    alice.display_report()
    GardenManager.create_garden_network([alice, bob])

class GardenManager:
    total_gardens = 0
    def __init__(self, name):
        self.name = name
        self.plant_list = []
        GardenManager.total_gardens += 1
    
    class GardenStats:
        @staticmethod
        def validation_height(height):
            return height >= 0
        @staticmethod
        def generate_report(plant_list):
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
            print(f"\nPlant added: {len(plant_list)}, Total growth: {len(plant_list)}cm")
            print(f"Plant types: {plant_count} regular, {flower_count} flowering, {prize_count} prize flowers")
            print(f"\nHeight validation test: {GardenManager.GardenStats.validation_height(10)}")
    
    def grow_plants(self):
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plant_list:
            plant.height += 1
            print(f"{plant.name} grew 1cm")
    
    def display_report(self):
        print(f"== {self.name}'s Garden Report ==")
        print("Plants in garden:")
        for plant in self.plant_list:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.flower_color} flowers (blooming), Prize points: {plant.prize_points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.flower_color} (blooming)")
            elif isinstance(plant, Plant):
                print(f"- {plant.name}: {plant.height}cm")
        GardenManager.GardenStats.generate_report(self.plant_list)
    
    def add_plant(self, plant):
        if GardenManager.GardenStats.validation_height(plant.height):
            self.plant_list.append(plant)
            print(f"Added {plant.name} to {self.name}'s garden")
        else:
            print("Invalid height, plant rejected")
    
    @classmethod
    def create_garden_network(cls):
        print(f"Total gardens managed: {cls.total_gardens}")
    
    def calculate_score(self):
        total_score = 0
        for plant in self.plant_list:
            total_score += plant.height
            if isinstance(plant, PrizeFlower):
                total_score += plant.prize_points
        print(f"Garden scores - {self.name}: {total_score}")

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

alice = GardenManager("Alice")
bob = GardenManager("Bob")

oak = Plant("Oak Tree", 100)
rose = FloweringPlant("Rose", 25, "red")
sunflower = PrizeFlower("Sunflower", 50, "yellow", 40)

print("=== Garden Management System Demo ===")
print()
alice.add_plant(oak)
alice.add_plant(rose)
alice.add_plant(sunflower)
print()
alice.grow_plants()
print()
alice.display_report()
alice.calculate_score()
GardenManager.create_garden_network()
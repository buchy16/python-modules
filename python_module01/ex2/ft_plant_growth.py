class Plant():
    """a plant class with 4 methods
    init(), grow(), add_age(), get_info()
    """
    def __init__(self, name: str, height: int, age: int):
        """initiat initializes a new Plant type object

        Args:
            name (str): plant name
            height (int): plant height
            age (int): plant age
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def grow(self):
        """add one to the height of the plant
        """
        self.height += 1

    def add_age(self):
        """add one to the age of the plant
        """
        self.age += 1

    def get_info(self):
        """display the name, height and age of the plant
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if (__name__ == "__main__"):
    plant = Plant("Rose", 25, 30)
    plant2 = Plant("violet", 25, 12)
    i = 1
    age_start1 = plant.age
    age_start2 = plant2.age
    print("=== Day 1 ===")
    plant.get_info()
    plant2.get_info()
    while (i < 7):
        plant.grow()
        plant.add_age()
        plant2.grow()
        plant2.add_age()
        i += 1
    print("=== Day 7 ===")
    plant.get_info()
    print(f"Growth this week: +{plant.age - age_start1}cm")
    plant2.get_info()
    print(f"Growth this week: +{plant2.age - age_start2}cm")

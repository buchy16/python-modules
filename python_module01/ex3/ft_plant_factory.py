class Plant():
    """a plant class with 4 methods
    init(), grow(), add_age(), get_info()
    """
    total_plant = 0

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
        Plant.total_plant += 1
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

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
    print("=== Plant Factory Output ===")
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("oak", 200, 365)
    plant3 = Plant("cactus", 5, 90)
    plant4 = Plant("sunflower", 80, 45)
    plant5 = Plant("violet", 25, 12)
    print(f"\n Total plants created: {Plant.total_plant}")

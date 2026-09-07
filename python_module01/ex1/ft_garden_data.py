class Plant():
    """a plant class with 1 method
    init()
    """
    def __init__(self, name: str, height: int, age: int):
        """initiat initializes a new Plant type object

        Args:
            name (str): plant name
            height (int): plant height
            age (int): planr age
        """
        self.name = name.capitalize()
        self.height = height
        self.age = age


if (__name__ == "__main__"):
    plant1 = Plant("rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    plant4 = Plant("violet", 25, 12)
    print("=== Garden Plant Registery ===")
    print(f"{plant1.name}: {plant1.height}cm, {plant1.age} days old")
    print(f"{plant2.name}: {plant2.height}cm, {plant2.age} days old")
    print(f"{plant3.name}: {plant3.height}cm, {plant3.age} days old")
    print(f"{plant4.name}: {plant4.height}cm, {plant4.age} days old")

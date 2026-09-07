class SecurePlant():
    """a secured (because of the use of property) plant class with 11 methods
    init(), grow(), add_age(), get_info(), get_height()
    set_height(), get_age(), set_age(), get_total(), set_total(), get_class()
    total_plant is SecurePlant variable that count the number of plant
    object created
    """
    __total_plant = 0

    def get_total() -> int:
        """return the amount of plant created

        Returns:
            int: the amount of plant created
        """
        return (SecurePlant.__total_plant)

    def set_total(value: int) -> None:
        """set the value of total_plant to 'value'

        Args:
            value (int): value to put in total_plant
        """
        SecurePlant.__total_plant = value + SecurePlant.get_total()

    def __init__(self, name: str, height: int, age: int) -> None:
        """initiat a new SecurePlant type object

        Args:
            name (str): plant name
            height (int): plant height
            age (int): plant age
        """
        if (height < 0):
            print(f"Invalide height input: height {height} [REJECTED]")
        elif (age < 0):
            print(f"Invalide age input: age {age} [REJECTED]")
        else:
            self.name = name
            self.height = height
            self.age = age
            SecurePlant.set_total(SecurePlant.get_total() + 1)
            print(f"Plant created: {name}")

    @property
    def height(self) -> int:
        """creat a new property named height

        Returns:
            int: plant height
        """
        return (self.__height)

    @height.setter
    def height(self, new_height: int) -> None:
        """Operator Overloading for the property height
        set the height of plant to 'new_height', in case of non valid
        argument, an error will be returned

        Args:
            new_height (int): new height to attribute to the plant
        """
        if (new_height < 0):
            print(f"Invalide operation attempted: height {new_height}",
                  "[REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = new_height
            print(f"Height updated: {new_height}cm [OK]")

    @property
    def age(self) -> int:
        """creat a new property named age

        Returns:
            int: plant age
        """
        return (self.__age)

    @age.setter
    def age(self, new_age: int) -> None:
        """Operator Overloading for the property age
        set the age of plant to 'new_age', in case of non valid
        argument, an error will be returned

        Args:
            new_age (int): new age to attribute to the plant
        """
        if (new_age < 0):
            print(f"Invalide operation attempted: age {new_age}",
                  "[REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = new_age
            print(f"Age updated: {new_age} days [OK]")

    @property
    def name(self) -> str:
        """creat a new property named name

        Returns:
            str: The name of the plant
        """
        return (self.__name)

    @name.setter
    def name(self, new_name: str) -> None:
        """Operator Overloading for the property name
        set the name of plant to 'new_name', in case of non valid
        argument, an error will be returned

        Args:
            new_name (str): new name to attribute to the plant
        """
        self.__name = new_name.capitalize()

    def get_height(self) -> int:
        """return the height of the plant using the new height property

        Returns:
            int: plant height
        """
        return (self.height)

    def set_height(self, new_height: int) -> None:
        """set the height of the plant to 'new_height
        using the new height property

        Args:
            new_height (int): new height to attribute to the plant
        """
        self.height = new_height

    def get_age(self) -> int:
        """return the age of the plant using the new age property

        Returns:
            int: plant age
        """
        return (self.age)

    def set_age(self, new_age: int) -> None:
        """set the age of the plant to 'new_age
        using the new age property

        Args:
            new_age (int): new age to attribute to the plant
        """
        self.age = new_age

    def get_name(self) -> str:
        """return the age of the plant using the new age property

        Returns:
            str: plant name
        """
        return (self.name)

    def grow(self) -> None:
        """add one to the height of the plant
        using the height property
        """
        self.height = self.height + 1

    def add_age(self) -> None:
        """add one to the age of the plant
        using the age property
        """
        self.age = self.age + 1

    def get_class(self) -> str:
        """Return the class of the object

        Returns:
            str: the class of the object
        """
        return ("plant")

    def get_info(self) -> None:
        """display the name, height and age of the plant
        and the special attribute of subclasses
        """
        if (self.get_class() == "plant"):
            print(f"{self.name} (Plant): {self.height}cm,",
                  f"{self.age} days")
        elif (self.get_class() == "flower"):
            print(f"{self.name} (Flower): {self.height}cm,",
                  f"{self.age} days, {self.color} color")
        elif (self.get_class() == "tree"):
            print(f"{self.name} (Tree): {self.height}cm,",
                  f"{self.age} days, {self.trunk_diameter}cm diameter")
        elif (self.get_class() == "vegetable"):
            print(f"{self.name} (Vegetable): {self.height}cm,",
                  f"{self.age} days, {self.harvest_season} harvest")
            print(f"{self.name} is rich in vitamin {self.nutritional_value}")


class Flower(SecurePlant):
    """A secured Flower subclass that contain 2
    methodes, get_class(), bloom()

    Args:
        SecurePlant (class): the SecuredPlant class (Parent class)
    """
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """initiat a new Flower type object (child of SecurePlant)

        Args:
            name (str): flower name
            height (int): flower height
            age (int): flower age
            color (str): flower color
        """
        super().__init__(name, height, age)
        self.color = color

    @property
    def color(self) -> str:
        """creat a new property named color

        Returns:
            str: the color of the flower
        """
        return (self.__color)

    @color.setter
    def color(self, new_color: str) -> None:
        """Operator Overloading for the property color
        set the color of plant to 'new_color'

        Args:
            new_color (str): new color to attribut to the flower
        """
        self.__color = new_color

    def get_class(self) -> str:
        """Return the class of the object

        Returns:
            str: the class of the object
        """
        return ("flower")

    def bloom(self) -> None:
        """display the name of the flower followed by
        'is blooming beautifully !'
        """
        print(f"{self.name} is blooming beautifully !")


class Tree(SecurePlant):
    """A secured Tree subclass that contain 2
    methodes, get_class(), produce_shade()

    Args:
        SecurePlant (class): the SecuredPlant class (Parent class)
    """
    def __init__(self, name: str, height: int,
                 age: int, diameter: int) -> None:
        """initiat a new Tree type object (child of SecurePlant)

        Args:
            name (str): tree name
            height (int): tree height
            age (int): tree age
            diameter (int): tree diameter
        """
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    @property
    def trunk_diameter(self) -> str:
        """creat a new property named color

        Returns:
            str: the diameter of the tree
        """
        return (self.__trunk_diameter)

    @trunk_diameter.setter
    def trunk_diameter(self, new_diameter: int) -> None:
        """Operator Overloading for the property diameter
        set the diameter of tree to 'new_diameter'

        Args:
            new_diameter (int): new diameter to attribut to the tree
        """
        self.__trunk_diameter = new_diameter

    def get_class(self) -> str:
        """Return the class of the object

        Returns:
            str: the class of the object
        """
        return ("tree")

    def produce_shade(self) -> None:
        """display the name of the tree followed by
        'provides 78 square meters of shade'
        """
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(SecurePlant):
    """A secured Vegetable subclass that contain 1
    methodes, get_class()

    Args:
        SecurePlant (class): the SecuredPlant class (Parent class)
    """
    def __init__(self, name: str, height: int, age: int,
                 season: str, vitamin: str) -> None:
        """initiat a new Vegetable type object (child of SecurePlant)

        Args:
            name (str): vegetable name
            height (int): vegetable height
            age (int): vegetable age
            season (str): vegatble harvest season
            vitamin (str): vagetable nutritional value
        """
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = vitamin

    @property
    def harvest_season(self) -> str:
        """creat a new property named harvest_season

        Returns:
            str: the harvest season of the vegetable
        """
        return (self.__harvest_season)

    @harvest_season.setter
    def harvest_season(self, new_season: str) -> None:
        """Operator Overloading for the property harvest_season
        set the harvest_season of vegetable to 'new_season'

        Args:
            new_season (str): new harvest_season to attribut to the vegetable
        """
        self.__harvest_season = new_season

    @property
    def nutritional_value(self) -> str:
        """creat a new property named nutritional value

        Returns:
            str: the nutritional value of the vegetable
        """
        return (self.__nutritional_value)

    @nutritional_value.setter
    def nutritional_value(self, vitamin: str) -> None:
        """Operator Overloading for the property nutritional_value
        set the nutritional_value of vegetable to 'viatmin'

        Args:
            vitamin (str): new nutritional_value to attribut to the vegetable
        """
        self.__nutritional_value = vitamin

    def get_class(self) -> str:
        """Return the class of the object

        Returns:
            str: the class of the object
        """
        return ("vegetable")


if (__name__ == "__main__"):
    # plant = SecurePlant("Chlorophytum", 25, 60)
    flower = Flower("Violette", 15, 30, "purple")
    tree = Tree("oak", 500, 1825, 50)
    vegetable = Vegetable("Tomato", 80, 90, "summer", "C")
    # plant.get_info()
    flower.get_info()
    flower.bloom()
    tree.get_info()
    tree.produce_shade()
    vegetable.get_info()

class SecurePlant():
    """a secured (because of the use of property) plant class with 10 methods
    init(), grow(), add_age(), get_info(), get_height()
    set_height(), get_age(), set_age(), get_total(), set_total()
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
        """initiat initializes a new SecurePlant type object

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
            print(f"Invalide operation attempted: height {new_height}cm",
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
            print(f"Invalide operation attempted: age {new_age} days",
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

    def get_info(self) -> None:
        """display the name, height and age of the plant
        """
        print(f"Current plant: {self.name} ({self.height}cm,",
              f"{self.age} days)")


if (__name__ == "__main__"):
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 20, 25)
    # plant.get_info()
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.get_info()
    # plant.grow()
    # plant.add_age()
    # plant.get_info()
    # plant.__age = 0
    # plant.get_info()
    # print(SecurePlant.get_total())
    plant.height = 45

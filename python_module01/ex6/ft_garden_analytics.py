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
        """initializes a new SecurePlant type object

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
        """display the name, height of the plant
        and the special attribute of subclasses
        """
        if (isinstance(self, PrizeFlower)):
            print(f"- {self.name}: {self.height}cm, {self.color}",
                  f"flowers ({self.state}), Prize points: {self.prize_point}")
        elif (isinstance(self, FloweringPlant)):
            print(f"- {self.name}: {self.height}cm, {self.color}",
                  f"flowers ({self.state})")
        elif (isinstance(self, SecurePlant)):
            print(f"- {self.name}: {self.height}cm")


class FloweringPlant(SecurePlant):
    """A secured Flower subclass

    Args:
        SecurePlant (class): the SecuredPlant class (Parent class)
    """
    def __init__(self, name: str, height: int, age: int, color: str,
                 plant_state: str) -> None:
        """initializes a new FloweringPlant type object (child of SecurePlant)

        Args:
            name (str): flower name
            height (int): flower height
            age (int): flower age
            color (str): flower color
            plant_state (str): flower state
        """
        super().__init__(name, height, age)
        self.color = color
        self.state = plant_state

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

    @property
    def state(self) -> str:
        """creat a new property named state

        Returns:
            str: the state of the flower
        """
        return (self.__state)

    @state.setter
    def state(self, plant_state: str):
        """Operator Overloading for the property state
        set the state of plant to '[plant_state]'

        Args:
            plant_state (str): new state to attribut to the flower
        """
        self.__state = plant_state


class PrizeFlower(FloweringPlant):
    """A secured Flower subclass

    Args:
        FloweringPlant (class): the FlowerringPlant class (Parent class)
    """
    def __init__(self, name, height, age, color, plant_state, prize):
        """initializes a new PrizeFlower type object (child of FloweringPlant)

        Args:
            name (_type_): flower name
            height (_type_): flower height
            age (_type_): flower age
            color (_type_): flower color
            plant_state (_type_): flower state
            prize (_type_): flower prize
        """
        super().__init__(name, height, age, color, plant_state)
        self.prize_point = prize

    @property
    def prize_point(self) -> int:
        """creat a new property named 'prize_point'

        Returns:
            int: the prize of the plant
        """
        return (self.__prize_point)

    @prize_point.setter
    def prize_point(self, prize: int) -> None:
        """Operator Overloading for the property prize_point
        set the prize_point of plant to 'prize'

        Args:
            prize (int): new prize to attribut to the flower
        """
        self.__prize_point = prize


class GardenManager():
    """A garden class that gather plant of an owner, and and offers
    several garden management methods. This class has 4 methods,
    add_to_garden(), grow_plant(), grow_all(), garden_info()
    There is also an other class directly linked with the object created
    on the class, go check that class for more informations
    """
    class GardenStats():
        """_summary_
        A garden summary class to keep a trace of the garden evolution
        This class has 6 methods, garden_evolution_summary(),
        plant_type_count(),plant_score(), garden_score(), height_validation(),

        """
        total_garden = 0

        def __init__(self, garden: object) -> None:
            """initializes a new GardenSate type object
            cm_tracker will be used to count how much the plant grewup since
            they have been added to the garden
            regular_count is the number of regular plant on the garden
            flowering_count is the number of flowering flower on the garden
            prize_flower is the number of prize flower on the garden

            Args:
                garden (object): a garden from the class GardenManager
            """
            self.garden = garden
            self.cm_tracker = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_flowers = 0
            GardenManager.GardenStats.total_garden += 1

        @property
        def garden(self) -> object:
            """creat a new property named 'garden'

            Returns:
                object: the garden object (from the GardenManager class)
            """
            return (self.__garden)

        @garden.setter
        def garden(self, new_garden: object) -> None:
            """Operator Overloading for the property garden
            set the garden of plant to 'new_garden'

            Args:
                new_garden (object): new garden to attribut to the
                garden_summary
            """
            self.__garden = new_garden

        @property
        def cm_tracker(self) -> int:
            """creat a new property named 'cm_tracker'

            Returns:
                int: the total cm gained
            """
            return (self.__cm_tracker)

        @cm_tracker.setter
        def cm_tracker(self, number: int) -> None:
            """Operator Overloading for the property cm_tracker
            set the cm_tracker of plant to 'number'

            Args:
                number (int): new number to attribut to the
                cm_tracker
            """
            self.__cm_tracker = number

        def add_cm(self, number: int) -> None:
            """A method that will add 'number' to the attribut
            cm_tracker

            Args:
                number (int): number of cm we want to add
            """
            self.cm_tracker += number

        def garden_evolution_summary(self):
            """a method that display the evolution of the garden
            evolution include number of plants added, total growth
            and plant type (and their number)
            """
            print(f"Plants added: {len(self.garden.garden_content)},",
                  f"Total growth: {self.cm_tracker}cm")
            print(f"Pant types: {self.regular_count} regular, "
                  f"{self.flowering_count} flowering, "
                  f"{self.prize_flowers} prize flowers")

        def plant_type_count(self, plant: SecurePlant) -> None:
            """A method that will increase the right number of plant type
            using the parameter given

            Args:
                plant (SecurePlant): the plant added on the garden
            """
            if (isinstance(plant, PrizeFlower)):
                self.prize_flowers += 1
            elif (isinstance(plant, FloweringPlant)):
                self.flowering_count += 1
            elif (isinstance(plant, SecurePlant)):
                self.regular_count += 1

        @staticmethod
        def plant_score(plant: SecurePlant) -> int:
            """A static methode used to return the correct
            value of a plant

            Args:
                plant (SecurePlant): the plant to assess

            Returns:
                int: the value of the plant
            """
            if (isinstance(plant, PrizeFlower)):
                return (20 * plant.prize_point)
            if (isinstance(plant, FloweringPlant)):
                return (10)
            if (isinstance(plant, SecurePlant)):
                return (8)

        def garden_score(self) -> int:
            """A method that will calculate the score of the garden
            based on the value of each plant on the farden

            Returns:
                int: the score
            """
            result = 0
            for plant in self.garden.garden_content.values():
                result += GardenManager.GardenStats.plant_score(plant)
            return (result)

        def height_validation(self) -> bool:
            """A method to check if all the plant on the garden
            as a height greater than 20

            Returns:
                bool: the result of the comparison
            """
            for plant in self.garden.garden_content.values():
                if (plant.height < 20):
                    return (False)
            return (True)

    def __init__(self, owner: str) -> None:
        """initializes a new GardenManager type object
        that represent a garden composed of different type of
        flower (stored on a dictionary)
        stats is the GardenStats of the garden, used to keep a trace of
        his evolution
        Args:
            owner (str): _description_
        """
        self.owner = owner
        self.garden_content = {}
        self.stats = GardenManager.GardenStats(self)

    @property
    def owner(self) -> str:
        """creat a new proprty named 'owner'

        Returns:
            str: the name of the owner
        """
        return (self.__owner)

    @owner.setter
    def owner(self, name: str) -> None:
        """Operator Overloading for the property owner
            set the owner of plant to 'name'

        Args:
            name (str): the name to attribut to the owner of the garden
        """
        self.__owner = name.capitalize()

    @property
    def garden_content(self) -> dict:
        """creat a new propety named 'grden_content'
        that will contain all the plant in the garden

        Returns:
            dict: a dictionary that contain multiple plant
        """
        return (self.__garden_content)

    @garden_content.setter
    def garden_content(self, content: dict) -> None:
        """Operator Overloading for the property garden_content
        set the garden_content of plant to 'content'

        Args:
            content (dict): an empty dictionary
        """
        self.__garden_content = content

    @classmethod
    def create_garden_network(cls, owner_list: list) -> list:
        """A class method that will creat multiple garden using
        a list of owner name, the garden content will be empty
        at the beginning

        Args:
            owner_list (list): a list of owner name (name are string)

        Returns:
            list: a list of garden object
        """
        lst = []
        for owner in owner_list:
            lst += [cls(owner)]
        return (lst)

    def add_to_garden(self, plant: SecurePlant) -> None:
        """A method that will add the plant parameter on the
        garden of the owner

        Args:
            plant (SecurePlant): plant to add to the garden
        """
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.garden_content[plant.name] = plant
        self.stats.plant_type_count(plant)

    def grow_plant(self, plant_name: str) -> None:
        """A method that will make a plant grow
        by using its name to find it in the dictionary

        Args:
            plant_name (str): the name of the plant we want to grow
        """
        plant: SecurePlant
        plant = (self.garden_content)[plant_name]
        plant.grow()
        self.stats.add_cm(1)
        print(f"{plant.name} grew 1 cm")

    def grow_all(self):
        """A method that will make all plant grow by using the
        'grow_plant' method
        """
        print(f"{self.owner} is helping all plants grow...")
        plant: SecurePlant
        for plant in self.garden_content.values():
            self.grow_plant(plant.name)

    def garden_info(self) -> None:
        """Display some infos about the garden
        """
        print("Plants in garden:")
        for plant in self.garden_content.values():
            plant.get_info()


def fc_grow_all(garden: GardenManager) -> None:
    """Like the grow_all method but in a function

    Args:
        garden (GardenManager): the garden we want to help growing
    """
    garden.grow_all()


if (__name__ == "__main__"):
    Bob: GardenManager
    Alice: GardenManager
    Bob, Alice = GardenManager.create_garden_network(["Bob", "Alice"])

    # Bob.add_to_garden(SecurePlant("birchwood", 90, 1065))

    print("=== Garden Management System Demo === \n")
    Alice.add_to_garden(SecurePlant("Oak Tree", 100, 1074))
    Alice.add_to_garden(FloweringPlant("Rose", 25, 15, "red", "blooming"))
    Alice.add_to_garden(PrizeFlower("Sunflower", 50, 15, "yellow",
                                    "blooming", 10))
    print("")
    # Alice.grow_plant("Oak tree")
    Alice.grow_all()
    print("\n ===Alice's Garden Report ===")
    Alice.garden_info()
    print("")
    Alice.stats.garden_evolution_summary()
    print("")
    print(f"Height validation test: {Alice.stats.height_validation()}")
    print(f"Garden scores - {Alice.owner}: {Alice.stats.garden_score()}, ",
          f"{Bob.owner}: {Bob.stats.garden_score()}")
    print(f"Total gardens managed: {GardenManager.GardenStats.total_garden}")
    # Bob

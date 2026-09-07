import sys
import math


def creat_coo() -> tuple:
    """A function that will creat a tuple of coordinates
    with a list of number

    Returns:
        tuple: coordinates returned
    """
    try:
        for i in range(1, len(sys.argv)):
            sys.argv[i] = int(sys.argv[i])
        coo = (sys.argv[1], sys.argv[2], sys.argv[3])
        print(f"Position created: ({coo[0]}, {coo[1]}, {coo[2]})")
        return coo
    except ValueError as e:
        print(e)
        return (0, 0, 0)


def parse_coo() -> tuple:
    """A function that will creat a tuple of coordinates
    with a string, the string need to use a specific
    format like "x,y,z", if this pattern is not respected
    an error will be raised but the programme will not stop

    Returns:
        tuple: coordinates returned
    """
    try:
        lst = sys.argv[1].split(",")
        if (len(lst) < 3):
            raise Exception(f"Error details - Type: CoordinateError:\
(not enought coordinate, {len(lst)} were given insted of 3)")
        if (len(lst) > 3):
            raise Exception(f"Error details - Type: CoordinateError:\
(too much coordinate, {len(lst)} were given insted of 3)")
    except Exception as e:
        print(f"Error parsing coordinates: invalide number of\
 coordinates\n{e}")
        return (0, 0, 0)

    try:
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        coo = (lst[0], lst[1], lst[2])
        print(f"Parsed position: {coo}")
        return coo
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Typ: ValueError, Args: ({e},)")
        return (0, 0, 0)


def print_distance(coo1: tuple, coo2: tuple) -> None:
    """A function that calculate the distance betwen 2 point

    Args:
        coo1 (tuple): first tuple of coordinates
        coo2 (tuple): second tuple of coordinates
    """
    resultat = math.sqrt(math.pow(coo2[0] - coo1[0], 2) +
                         math.pow(coo2[1] - coo1[1], 2) +
                         math.pow(coo2[2] - coo1[2], 2))
    print(f"Distance between {coo1} and {coo2}: {round(resultat, 2)}")


def unpack(coo: tuple) -> None:
    """It's a weird function that shows twice the coordinates
    of "coo" ?

    Args:
        coo (tuple): a tuple of coordinates
    """
    print("\nUnpacking demonstration:")
    x, y, z = coo
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if (__name__ == "__main__"):
    print("=== Game Coordinate System ===\n")
    origine = (0, 0, 0)
    try:
        if (len(sys.argv) == 4):
            dummy = creat_coo()
        elif (len(sys.argv) == 2):
            dummy = parse_coo()
        print_distance(origine, dummy)
        unpack(dummy)
    except Exception:
        print("Arguments error")

import sys


def interpretor() -> None:
    """A simple interpretor that will iterate through
    argv, if no arguments was given, an error will be raised
    and the programme will continue

    """
    print("======= Command Quest =======")
    print("Programe name: ft_command_quest.py")
    lenght = len(sys.argv)
    try:
        if (lenght <= 1):
            raise Exception("No Arguments provided !")
        print(f"Argument recived: {lenght - 1}")
        for i in range(1, lenght):
            print(f"Argument {i}: {sys.argv[i]}")
    except Exception as e:
        print(e)
    finally:
        print(f"Total arguments: {lenght}")


if (__name__ == "__main__"):
    interpretor()

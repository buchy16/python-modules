import sys


def convertion(argument: str, data: list) -> None:
    """A function that will add the given arguments in the database passed
    if the argument is not a digit, an error will be raisede programme will
    insult you but the he will not stop

    Args:
        argument (str): a digit but in a string, represent a score
        data (list): list of scores
    """
    try:
        level = int(argument)
        data.append(level)
    except ValueError:
        print(f"STUPID MONKEY, '{argument}' IS NOT A NUMBER\n🦍\n")


def Player_score_analytiacs() -> None:
    """A function that will creat a list of score with argv and then
    display some stats, if the list is empty, an error will be raised
    but the programme will not stop

    """
    data = []
    try:
        for level in sys.argv[1:]:
            convertion(level, data)

        if (len(data) == 0):
            raise Exception("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")

        print(f"Scores processed: {data}")
        print(f"🙋Total players : {len(data)}")
        print(f"🚀Total score : {sum(data)}")
        print(f"📊Average score : {sum(data) / len(data)}")
        print(f"📈Hight score : {max(data)}")
        print(f"📉Low score : {min(data)}")
        print(f"📋Score range : {max(data) - min(data)}")
    except Exception as e:
        print(e)


if (__name__ == "__main__"):
    print("=== Player Score Analytiacs ===")
    Player_score_analytiacs()

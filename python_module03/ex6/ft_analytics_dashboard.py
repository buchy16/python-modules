achievment_data = ["first_kill",  # 0
                   "level_10",  # 1
                   "boss_slayer",  # 2
                   "collector",  # 3
                   "treasur_hunter",  # 4
                   "adventurer",  # 5
                   "traitor",  # 6
                   "cheater",  # 7
                   "kill_theme_all",  # 8
                   "fisher_man",  # 9
                   "hunter_expert",  # 10
                   "luckiest_player",  # 11
                   "veteran",  # 12
                   "huntEvent_winner",  # 13
                   "storm_bbeaurai"  # 14
                   ]


Alice = {
    "name": "alice",
    "score": 2300,
    "achievment": [achievment_data[0],
                   achievment_data[1],
                   achievment_data[2],
                   achievment_data[3],
                   achievment_data[4],
                   ],
    "region": "north"
}

Bob = {
    "name": "bob",
    "score": 1800,
    "achievment": [achievment_data[0],
                   achievment_data[1],
                   achievment_data[2],
                   ],
    "region": "east"
}

Charlie = {
    "name": "charlie",
    "score": 2150,
    "achievment": [achievment_data[0],
                   achievment_data[1],
                   achievment_data[2],
                   achievment_data[5],
                   achievment_data[9],
                   achievment_data[10],
                   achievment_data[11],
                   ],
    "region": "central"
}

Diana = {
    "name": "diana",
    "score": 2050,
    "achievment": [],
    "region": "south"
}

Dummy = {
    "name": "dummy",
    "score": 1050,
    "achievment": [achievment_data[0],
                   achievment_data[1],
                   achievment_data[2],
                   achievment_data[6],
                   achievment_data[12],
                   achievment_data[7]
                   ],
    "region": "est"
}

Jhon = {
    "name": "john doe",
    "score": 500,
    "achievment": [achievment_data[0],
                   achievment_data[1],
                   achievment_data[2],
                   achievment_data[13],
                   achievment_data[14],
                   achievment_data[8]
                   ],
    "region": "hell"
}

Players = [Alice, Bob, Charlie, Diana, Dummy, Jhon]


def list_comprehension(Players: list) -> None:
    """A function that will generate multiple list to display
    the highest score, all scores doubled and the most active
    players

    Args:
        Players (list): List of all players on the server
    """
    High_scorers_lst = sorted([player["name"] for player in Players
                               if player["score"] >= 2000])
    Scores_doubled = [player["score"] * 2 for player in Players]
    Active_players = sorted([player["name"] for player in Players
                             if len(player["achievment"]) > 0])
    print(f"High scorers (>2000): {High_scorers_lst}")
    print(f"Scores doubled: {Scores_doubled}")
    print(f"Active players: {Active_players}")


def count_categorie(Players: list, categorie: str) -> int:
    """A function that will return how many player had a score on the
    given categorie

    Args:
        Players (list): List of all players on the server
        categorie (str): categorie of score (Hight, medium, low)

    Returns:
        int: _description_
    """
    count = 0
    if (categorie == "hight"):
        for player in Players:
            if (player["score"] >= 2000):
                count += 1
    elif (categorie == "medium"):
        for player in Players:
            if (player["score"] >= 1000 and player["score"] < 2000):
                count += 1
    else:
        for player in Players:
            if (player["score"] < 1000):
                count += 1
    return count


def dict_comprehension(Players: list) -> None:
    """A function that will generate multiple dictionary to
    display some infos like player score, score categorie and
    the amount of achievement of each player

    Args:
        Players (list): List of all players on the server
    """
    player_scores = {player["name"]: player["score"] for player in Players}
    score_categories = {categorie: count_categorie(Players, categorie)
                        for categorie in ['hight', 'medium', 'low']}
    achievment_count = {player["name"]: len(player["achievment"])
                        for player in Players}

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievment counts: {achievment_count}")


def set_comprehension(Players: list) -> None:
    """A function that will generate set to display some infos like
    all the player rgistered, the commun achievments to all players and
    all the regions where the players are

    Args:
        Players (list): List of all players on the server
    """
    unique_players = {player["name"] for player in Players}
    unique_achievment = set.intersection(*({achievment for achievment in
                                           player["achievment"]}
                                           for player in Players
                                           if len(player["achievment"]) > 0))
    active_region = {player["region"] for player in Players}

    print(f"Unique players: {unique_players}")
    print(f"Unique achievments: {unique_achievment}")
    print(f"Active region: {active_region}")


def best_player(Players: list) -> dict:
    """A function that will return the best player based on his score
    and the number of achievement he had

    Args:
        Players (list): List of all players on the server

    Returns:
        dict: best player
    """
    best_player = Players[0]
    best_score = best_player["score"] + (len(best_player["achievment"]) * 50)

    for player in Players:
        score = (player["score"] + (len(player["achievment"]) * 50))
        if (score > best_score):
            best_player = player
            best_score = score
    return best_player


def combined_analysis(Players: list) -> None:
    """A function that will display some genarl info

    Args:
        Players (list): List of all player on the server
    """
    total_unique_achievment = len(set.union(*({achievment for achievment in
                                            player["achievment"]}
                                            for player in Players if
                                            len(player["achievment"]) > 0)))
    score_lst = [player["score"] for player in Players]
    top_performer = best_player(Players)

    print(f"Total players: {len(Players)}")
    print(f"Total unique achievements: {total_unique_achievment}")
    print(f"Average score: {sum(score_lst) / len(score_lst)}")
    print(f"Top performer: {top_performer["name"]} ({top_performer["score"]} \
points, {len(top_performer["achievment"])} achievements)")


if (__name__ == "__main__"):
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Exemples ===")
    list_comprehension(Players)

    print("\n=== Dict Comprehension Exemples ===")
    dict_comprehension(Players)

    print("\n=== Set Comprehension Exemples ===")
    set_comprehension(Players)

    print("\n=== Combined Analysis ===")
    combined_analysis(Players)

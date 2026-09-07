if (__name__ == "__main__"):
    Rare_achievments = {"first_kill", "level_10"}

    print("=== Achivevment Tracker System ===\n")

    Alice = set(["fisrt_kill", "level_10", "treasure_hunter", "speed_demon"])
    Bob = set(["fisrt_kill", "level_10", "boss_slayer", "collector"])
    Charlie = set(["level_10", "treasure_hunter", "boss_slayer", "speed_demon",
                  "perfectionist"])

    print(f"Player alice achivements: {Alice}")
    print(f"Player bob achivements: {Bob}")
    print(f"Player charlie achivements: {Charlie}")

    print("\n=== Achivement Analytics ===")
    print(f"All unique achievments: {Alice.union(Bob, Charlie)}")
    print(f"Total unique achievments: {len(Alice.union(Bob, Charlie))}\n")

    print(f"common to all players: {Alice.intersection(Bob, Charlie)}")
    print(f"Rare achievements (1 player) {Rare_achievments}")

    print(f"\nAlice vs Bob common: {Alice.intersection(Bob)}")
    print(f"Alice unique: {Alice.difference(Bob)}")
    print(f"Bob unique: {Bob.difference(Alice)}")

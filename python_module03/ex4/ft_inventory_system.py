item_data_base = {
    "sword": {"name": "sword", "category": "weapon", "rarity": "rare",
              "price": 500},
    "potion": {"name": "potion", "category": "consumable", "rarity": "common",
               "price": 50},
    "shield": {"name": "shield", "category": "armor", "rarity": "uncommon",
               "price": 200},
    "magic_ring": {"name": "magic_ring", "category": "magic_asset",
                   "rarity": "rare", "price": 800},
    "viking_ax": {"name": "viking_ax", "category": "weapon", "rarity": "rare",
                  "price": 500}
    }

Alice = {
    "slot_1": [item_data_base["sword"], 1],
    "slot_2": [item_data_base["potion"], 5],
    "slot_3": [item_data_base["shield"], 1]
    }

Bob = {
    "slot_1": [item_data_base["viking_ax"], 1],
    "slot_2": [item_data_base["magic_ring"], 2]
    }

Unamed_player000 = {
    "slot_1": [item_data_base["sword"], 50],
    "slot_2": [item_data_base["magic_ring"], 64],
    "slot_3": [item_data_base["potion"], 100]
    }

Players = {
    "Alice": [Alice, "Alice"],
    "Bob": [Bob, "Bob"],
}

Players_Beta_server = {
    "Alice": [Alice, "Alice"],
    "Bob": [Bob, "Bob"],
    "Unamed_player000": [Unamed_player000, "Unamed_player000"]
}


def search_item(Player: dict, item_name: str) -> list:
    """This function help searching an item not by the slot
    where he is but by his name

    Args:
        Player (dict): Player's inventory
        item_name (str): name of the item we search

    Returns:
        list: the list that contain the item and his quantity
    """
    for item in Player.values():
        if (item[0]['name'] == item_name):
            return (item)
    return (None)


def get_inventory(Player: dict) -> None:
    """A function that display the inventory of a Player

    Args:
        Player (dict): Player's inventory
    """
    for slot in Player.values():
        print(f"{slot[0]['name']} ({slot[0]['category']}, \
{slot[0]['rarity']}): {slot[1]}x @ {slot[0]['price']} gold each = \
{slot[1] * slot[0]['price']} gold")


def inventory_value(Player: dict) -> int:
    """calculat the total value of all the items in
    the player's inventory

    Args:
        Player (dict): Player's inventory

    Returns:
        int: total value of the inventory
    """
    total_gold_value = 0
    for slot in Player.values():
        total_gold_value += slot[0]['price'] * slot[1]
    return total_gold_value


def total_inventory_items(Player: dict) -> int:
    """Return the number of items in the inventory

    Args:
        Player (dict): Player's inventory

    Returns:
        int: the number of items in the inventory
    """
    total_item = 0
    for slot in Player.values():
        total_item += slot[1]
    return total_item


def total_items_type(Player: dict) -> None:
    """Display the number of items in the inventory
    sorted by category

    Args:
        Player (dict): Player's inventory
    """
    string = ""
    for slot in Player.values():
        string += f" {slot[0]['category']}({slot[1]}),"
    print(f"Categories:{string}")


def transaction(Player1: dict, Player2: dict, item_slot: str,
                quantity: int) -> None:
    """A function that will operate transaction betwen 2 players

    Args:
        Player1 (dict): Player1's inventory
        Player2 (dict): Player2's inventory
        item_slot (str): slot where the item is stord
                        (it's the key of the dict Player...)
        quantity (int): how many items you want to share
    """
    if (quantity <= search_item(Player1, Player1[item_slot][0]['name'])[1]):
        if (search_item(Player2, Player1[item_slot][0]['name']) is None):
            Player2.update({"slot_" + str(len(Player2) + 1):
                            [item_data_base[Player1[item_slot][0]['name']],
                            quantity]})
        else:
            search_item(Player2)[1] += quantity

        Player1[item_slot][1] -= quantity
        if (Player1[item_slot][1] <= 0):
            del Player1[item_slot]
        print("Transaction successful !")
    else:
        print("Transaction fail !")


def return_rarest_item(player: dict) -> str:
    """A function that will return the rarest item in the player's
    inventory, the rarity is based on the rarity attribut and the price

    Args:
        player (dict): Player's inventory

    Returns:
        str: item name
    """
    rareste_item = None
    for item in player.values():
        if (rareste_item is None or item[0]["rarity"] == "rare"):
            if (rareste_item is None or item[0]["price"] >
                    rareste_item["price"]):
                rareste_item = item[0]
    return rareste_item["name"]


def players_stats(players: dict) -> None:
    """A function that will display stats info
    about all players'inventory

    Args:
        players (dict): All players on the server
    """
    most_valuable = ["Dummy", 0]
    most_items = ["Dummy", 0]
    string = ""
    for player in players.values():
        if (inventory_value(player[0]) > most_valuable[1]):
            most_valuable = [player[1], inventory_value(player[0])]
        if (total_inventory_items(player[0]) > most_items[1]):
            most_items = [player[1], total_inventory_items(player[0])]
        string += f" {return_rarest_item(player[0])},"

    print(f"Most valuable player: {most_valuable[0]} ({most_valuable[1]} \
gold)")
    print(f"Most items: {most_items[0]} ({most_items[1]} items)")
    print(f"Rarest items:{string}")


if (__name__ == "__main__"):
    print("=== Player Inventory System ===\n")
    print("=== Alice's Inventory ===")
    get_inventory(Players["Alice"][0])
    print("")
    print(f'Inventory value: {inventory_value(Players["Alice"][0])} gold')
    print(f"Item count: {total_inventory_items(Players['Alice'][0])} items")
    total_items_type(Players["Alice"][0])

    # print("\n=== Bob's Inventory ===")
    # get_inventory(Players["Bob"][0])
    # print("")
    # print(f'Inventory value: {inventory_value(Players["Bob"][0])} gold')
    # print(f"Item count: {total_inventory_items(Players['Bob'][0])} items")
    # total_items_type(Players["Bob"][0])

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    transaction(Players["Alice"][0], Players["Bob"][0], "slot_2", 2)

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {search_item(Players['Alice'][0], 'potion')[1]}")
    print(f"Bob potions: {search_item(Players['Bob'][0], 'potion')[1]}")

    print("\n=== Inventory Analytics ===")
    players_stats(Players)


shop = {
    # > ITEM NAME | STAT | VAL | PRICE
    "Sword": ['ATK', 100, 200],
    "Shield": ['DEF', 50, 120]
}

player = {
    "ATK": 20,
    "DEF": 10,
    "GOLD": 1000
}

def playerDetail():
    print(f"""
    |---------- Player Status ------------|
            ATK     -       {player["ATK"]}
            DEF     -       {player['DEF']}
            GOLD    -       {player["GOLD"]}g
    |-------------------------------------| 
 """)
def menu():
    print(""" 
        |--------------- Menu --------------|
                1 - Show Player Status
                2 - Buy in shop
        |-----------------------------------| 
        |     'quit'   to    exit           |
        -------------------------------------
    """)

def buy():
    print("======= Shop Item =========")
    ice = 1
    for item, details in shop.items():
        print(f"{ice} | {item}: {details}")
        ice = ice + 1
    print("============================")
    buy_item = input("Enter item NAME to buy: ")
    stat_name = shop[buy_item][0]
    stat_value = shop[buy_item][1]
    price = (shop[buy_item][2])
    # print(stat_name)
    # print(stat_value)
    # print(price)
    if (int(player["GOLD"]) > price):
         new_player_gold = player["GOLD"] - price
         player["GOLD"] = new_player_gold
    else:
         print("Insufficient Gold")

    if stat_name == "ATK":
        player_atk = int(player["ATK"]) + stat_value
        player["ATK"] = player_atk
    elif stat_name == "DEF":
        player_def = int(player["DEF"]) + stat_value
        player["DEF"] = player_def
    else:
        print("not ATK not DEF")
    print("======= SUCCESS: NEW PLAYER DETAIL ===========")
    playerDetail()
    print("==============================================")



while True:
    menu()
    action = input('Action: ')

    if action == '1':
        playerDetail()
    elif action == '2':
        buy()
    elif action == 'quit':
        break
    else:
        print("Invalid input")
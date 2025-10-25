
shop = {
    # > ITEM NAME | STAT | VAL | PRICE
    "Sword": ['ATK', 100, 200],
    "Shield": ['DEF', 50, 120],
    "Knife": ['ATK', 50, 100],
    "Helmet": ['DEF', 100, 200]
}

player = {
    "ATK": 20,
    "DEF": 10,
    "GOLD": 1000,
    "BAG": []
}

def playerDetail():
    print(f"""
        |---------- Player Status ------------|
                ATK     -       {player["ATK"]}
                DEF     -       {player['DEF']}
                GOLD    -       {player["GOLD"]}g
        |-------------------------------------| 
 """)
    
def playerBag():
    print("        |------------------ Bag --------------------|")
    if len(player["BAG"]) != 0:
        for i, item in enumerate(player["BAG"], start=1):
            print(f"                {i} | {item[0]} +{item[2]} {item[1]}  -   {item[3]}")
        print("        |--------------------------------------|")
    else:
        print("              No bag item yet")
        print("         ----------------------------------")

def menu():
    print(""" 
        |--------------- Menu --------------|
                1 - Show Player Status
                2 - Buy in shop
                3 - Show bag
                4 - Equip Item
        |-----------------------------------| 
        |     'quit'   to    exit           |
        -------------------------------------
    """)

def equipItem():
    print("         |--- Select which item to equip ---|")
    if len(player["BAG"]) != 0:
        for i, item in enumerate(player["BAG"], start=1):
            print(f"                {i} | {item[0]} +{item[2]} {item[1]}   -   {item[3]}")
        print("        |---------------------------------|")

        toEquip = int(input("Item number to equip: "))

        # > validate range
        if (toEquip > len(player["BAG"])):
            print("Exceed range input")
        else:
            item = player["BAG"][toEquip - 1]
            itemStatName = item[1]
            itemStatValue = item[2]
            itemStatus = item[3]

            if (itemStatus == "Unequipped"):
                if (itemStatName == "ATK"):
                    player["ATK"] = player["ATK"] + itemStatValue

                    # > update the item to be "equipped"
                    item[3] = 'Equipped'
                    print("         |--------- Success! Item Equiped ---------|")
                    playerDetail()  
                elif (itemStatName == "DEF"):
                    player["DEF"] = player["DEF"] + itemStatValue

                    item[3] = 'Equipped'

                    print("         |--------- Success! Item Equiped ---------|")
                    playerDetail()
                else:
                    print("may mali sa ginawa ko")
            else:
                print("     ! >>>>>>>>>>>>>> Item Already Equipped <<<<<<<<<<<<<<<<<")

    else:
        print("              No bag item yet")
        print("         ----------------------------------")

def buy():
    print("======= Shop Item =========")
    for item, details in shop.items():
        print(f"{item}: {details}")
    print("============================")
    buy_item = input("Enter item NAME to buy: ")
    try:
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

        # ? if stat_name == "ATK":
        #     player_atk = int(player["ATK"]) + stat_value
        #     player["ATK"] = player_atk
        # elif stat_name == "DEF":
        #     player_def = int(player["DEF"]) + stat_value
        #     player["DEF"] = player_def
        # else:
        #     print("not ATK not DEF")

        # ? Add to bag
        player["BAG"].append([buy_item, stat_name, stat_value, 'Unequipped'])
        print("\n\n======= SUCCESS: NEW PLAYER DETAIL ===========")
        playerDetail()
        print("==============================================")
    except:
        print("\n! >>>>>>>> Item does not exist <<<<<<<<<<<< !")



while True:
    menu()
    action = input('Action: ')

    if action == '1':
        playerDetail()
    elif action == '2':
        buy()
    elif action == '3':
        playerBag()
    elif action == '4':
        equipItem()
    elif action == 'quit':
        break
    else:
        print("Invalid input")

print("Bye!")
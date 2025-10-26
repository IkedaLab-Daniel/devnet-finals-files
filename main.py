from random import randint

shop = {
    # > ITEM NAME | STAT | VAL | PRICE
    "Sword": ['ATK', 100, 200],
    "Shield": ['DEF', 50, 120],
    "Knife": ['ATK', 50, 100],
    "Helmet": ['DEF', 100, 200],
    "Potion": ['HP', 20, 50]
}

player = {
    "ATK": 20,
    "DEF": 10,
    "GOLD": 1000,
    "BAG": [],
    "HEALTH": 100
}

def playerDetail():
    print(f"""
        |---------- Player Status ------------|
                ATK     -       {player["ATK"]}
                DEF     -       {player['DEF']}
                GOLD    -       {player["GOLD"]}g
                HP      -       {player['HEALTH']}
        |-------------------------------------| 
 """)
    
def afterEquip(status, value):
    if status == "ATK":
        print(f"""
        |---------- Player Status ------------|
                ATK     -       {player["ATK"]} (+{value})
                DEF     -       {player['DEF']}
                GOLD    -       {player["GOLD"]}g
                HP      -       {player['HEALTH']}
        |-------------------------------------| 
    """)
    elif status == "DEF":
        print(f"""
        |---------- Player Status ------------|
                ATK     -       {player["ATK"]}
                DEF     -       {player['DEF']} (+{value})
                GOLD    -       {player["GOLD"]}g
                HP      -       {player['HEALTH']}
        |-------------------------------------| 
 """)
    elif status == "HP":
        print(f"""
        |---------- Player Status ------------|
                ATK     -       {player["ATK"]}
                DEF     -       {player['DEF']}
                GOLD    -       {player["GOLD"]}g
                HP      -       {player['HEALTH']} (+{value})
        |-------------------------------------| 
 """)
    else:
        print("------- May nagawa akong mali sa afterEquip() ---------")
            
    
def playerBag():
    print("        |------------------ Bag --------------------|")
    if len(player["BAG"]) != 0:
        for i, item in enumerate(player["BAG"], start=1):
            print(f"                {i} | {item[0]} +{item[2]} {item[1]}  -   {item[3]}")
        print("        |--------------------------------------|")

    prompt = (input("Do you want to equip an item? [y/n]: "))
    
    if prompt == "y":
        print("\n")
        equipItem()
        
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
                5 - Explore
        |-----------------------------------| 
        |     'quit'   to    exit           |
        -------------------------------------
    """)

def equipItem():
    print("         |------- Select which item to equip --------|")
    if len(player["BAG"]) != 0:
        for i, item in enumerate(player["BAG"], start=1):
            print(f"                {i} | {item[0]} +{item[2]} {item[1]}   -   {item[3]}")
        print("        |------------------------------------------|")
        try:
            toEquip = int(input("Item number to equip: "))
        except:
            print(" ! --- Number input only --- !")

        # > validate range
        if (toEquip > len(player["BAG"])):
            print("Exceed range input")
        else:
            item = player["BAG"][toEquip - 1]
            itemStatName = item[1]
            itemStatValue = item[2]
            itemStatus = item[3]

            if (itemStatus == "Unequipped" and itemStatus != "Used"):
                if (itemStatName == "ATK"):
                    player["ATK"] = player["ATK"] + itemStatValue

                    # > update the item to be "equipped"
                    item[3] = 'Equipped'
                    print("         |--------- Success! Item Equiped ---------|")
                    afterEquip('ATK', itemStatValue)
                elif (itemStatName == "DEF"):
                    player["DEF"] = player["DEF"] + itemStatValue

                    item[3] = 'Equipped'

                    print("         |--------- Success! Item Equiped ---------|")
                    afterEquip('DEF', itemStatValue)
                elif (itemStatName == "HP"):
                    player["HEALTH"] = player["HEALTH"] + itemStatValue

                    item[3] = 'Used'

                    print("         |--------- Success! Item Equiped ---------|")
                    afterEquip('HP', itemStatValue)
                else:
                    print("may mali sa ginawa ko")
            else:
                print("     ! >>>>>>>>>>>>>> Item Already Equipped/Used <<<<<<<<<<<<<<<<<")

    else:
        print("              No bag item yet")
        print("         ----------------------------------")

def buy():
    print("======= Shop Item =========\n")
    for item, details in shop.items():
        print(f"{item}: +{details[1]}{details[0]} | {details[2]}g")
    print("\n============================")
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
        print("\n==============================================")
        print("|         Success! Added to your bag!        |")
        print("==============================================\n")
    except:
        print("\n! >>>>>>>> Item does not exist <<<<<<<<<<<< !")

def explore():
    event = randint(1, 4)
    
    if event == 1:
        pass
    elif event == 2:
        pass
    elif event == 3:
        pass
    else:
        pass

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
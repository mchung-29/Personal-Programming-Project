## Personal Programming Project -- Martin Chung
import random, time, pygame, os, platform
from colorist import ColorRGB, BgColorRGB, rgb, bg_rgb
from time import sleep

def main(): 
    players_data, namelist, playercount = startup()
    game(players_data, namelist, playercount)

def startup(): ##setup before game starts
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5) ## change volume if needed but I doubt it
    clear_screen()
    lobbybgm()
    intro()
    playercount = get_pnum()
    players_data, namelist = var_assign(playercount)
    gamebgm()
    return players_data, namelist, playercount

def intro(): ##prints the game title
    slow_print("Welcome user, to")
    gold("""████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░""")
    time.sleep(0.1)
    gold("""░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝""")
    time.sleep(0.5)
    green("""
███╗░░░███╗░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░██╗░░░░░██╗░░░██╗
████╗░████║██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░╚██╗░██╔╝
██╔████╔██║██║░░██║██╔██╗██║██║░░██║██████╔╝██║░░██║██║░░░░░░╚████╔╝░""")
    time.sleep(0.1)
    green("""██║╚██╔╝██║██║░░██║██║╚████║██║░░██║██╔═══╝░██║░░██║██║░░░░░░░╚██╔╝░░
██║░╚═╝░██║╚█████╔╝██║░╚███║╚█████╔╝██║░░░░░╚█████╔╝███████╗░░░██║░░░
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░░░░░╚════╝░╚══════╝░░░╚═╝░░░
""")
    slow_print(" " * 21 + "<PRESS ENTER TO PLAY>")
    input()

def lobbybgm():  ## backgound music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.load("FE2Lobby.mp3")
    pygame.mixer.music.play(loops=-1) ## loops forever (-1)

def gamebgm():
    pygame.mixer.music.load("playlist.mp3")
    pygame.mixer.music.play(loops=-1)

def get_pnum(): ## gets number of players
    clear_screen()
    valid = False
    while valid == False:
        try:
            gold("How many people will be playing? (Max 5)")
            pnum = int(input())
        except ValueError:
            clear_screen()
            red("""Please enter a number below or equal to 5.
____________________________________________________\n""")
        else:
            if pnum <= 1:
                red("You can't play monopoly by yourself in multiplayer!")
            elif pnum <= 5:
                valid = True
            else:
                red("""Please enter a number below or equal to 5.
____________________________________________________\n""")
    return pnum

def var_assign(playercount): ## character and name selection
    players_data = []
    namelist = []
    rem_op = [1, 2, 3, 4, 5, 6]
    player_icons = ["🚢🟦", "🐈🟧", "🎩🟨","🐕🟩","🚙🟥","🐎🟪"]
    for i in range(playercount):
        clear_screen()
        icon_valid = False
        namevalid = False
        blue(f"What is your name, player {i+1}?")
        while namevalid == False:
            name = input()
            if len(name) > 20:
                red("Your name cannot be longer than 20 characters!")
            elif not name.isspace() and not name == "":
                namelist.append(name)
                namevalid = True
            else:
                red("Your name cannot be empty or solely contain spaces!")
        while icon_valid == False:
            green("\n---ICON AND COLOR SELECTION---")
            slow_print("Choose a number to select your icon.")
            for indx in range(len(rem_op)):
                print(f"{rem_op[indx]}: {player_icons[indx]}")
            try:
                gold(f"{name}, enter your selection:")
                char = int(input())
                if char in rem_op:
                    curr_indx = rem_op.index(char)
                    chosen_num = rem_op.pop(curr_indx)
                    chosen_set = player_icons.pop(curr_indx)
                    pdata = {
                        "name" : name,
                        "money" : 1500,
                        "position" : 0,
                        "icon" : chosen_set[0],
                        "color" : chosen_set[1],
                        "jail" : False,
                        "jail_cards" : 0,
                        "jail_turns" : 0,
                        "trains" : 0
                    }
                    players_data.append(pdata)
                    icon_valid = True
                else:
                    clear_screen()
                    red(f"\n {char} is already taken or not available.\nAvailable:{rem_op}")
            except ValueError:
                red(f"Please pick a number from the list.")
    clear_screen()
    pygame.mixer.music.fadeout(5000)
    slow_print("Selection Complete.") 
    time.sleep(1)
    slow_print("Let the game begin!")
    time.sleep(1)
    clear_screen()
    return players_data, namelist




def game(players_data, playerlist, playercount):
    board_data = board_dinit()
    bankrupt = []
    game_running = True     ## will change when I implement checking for no remaining players
    while game_running == True:
        for i in range(playercount):
            curr_pdata = players_data[i]
            curr_pname = playerlist[i]
            turn(curr_pname, playercount, curr_pdata, board_data, players_data)
            check_bankrupt(curr_pdata)
            check_win(playerlist, curr_pname)

def turn(curr_pname, playercount, curr_pdata, board_data, players_data): ##process of a turn
    doubles_count = 0
    turn_active = True
    while turn_active == True:
        clear_screen()
        printboard(curr_pdata, board_data, players_data)
        print_money(players_data, playercount)
        if curr_pdata["jail"] == True:
            jail_turn(curr_pdata, board_data, players_data)
            break
        your_turn(curr_pname, curr_pdata)
        is_doubles, roll_total = roll()
        if is_doubles == True:
            doubles_count += 1
            if doubles_count == 3:
                orange("You are SPEEDING! Go to jail.")
                prison(curr_pdata)
                break
            else:
                gold("You get to roll again!")
        move(roll_total, curr_pdata, board_data, players_data)
        if is_doubles == False:
            turn_active = False

def print_money(players_data, playercount):
    text = ""
    for i in range(playercount):
        pname = players_data[i]["name"]
        money = str(players_data[i]["money"])
        text += f"{pname}: {money}$    "
    text += "\n"
    yellow(text.center(104))

def your_turn(curr_pname, curr_pdata):
    if curr_pdata["color"] == "🟦":
        blue(f"{curr_pname} ({curr_pdata["icon"]} {curr_pdata["color"]}), it's your turn!")
    elif curr_pdata["color"] == "🟧":
        orange(f"{curr_pname} ({curr_pdata["icon"]} {curr_pdata["color"]}), it's your turn!")
    elif curr_pdata["color"] == "🟨":
        yellow(f"{curr_pname} ({curr_pdata["icon"]} {curr_pdata["color"]}), it's your turn!")
    elif curr_pdata["color"] == "🟩":
        green(f"{curr_pname} ({curr_pdata["icon"]} {curr_pdata["color"]}), it's your turn!")
    elif curr_pdata["color"] == "🟥":
        red(f"{curr_pname} ({curr_pdata["icon"]} {curr_pdata["color"]}), it's your turn!")
    else:
        purple(f"{curr_pname} ({curr_pdata["icon"]} {curr_pdata["color"]}), it's your turn!")

def roll(): ## getting numbers from rolling 2 dice
    magenta("Press enter to roll your dice.")
    input()
    sound("dice.mp3")
    slow_print("Rolling...")
    time.sleep(0.3)
    roll_num = random.randint(1,6)
    roll_num2 = random.randint(1,6)
    roll_total = roll_num + roll_num2
    purple(f"You rolled a {roll_num} and a {roll_num2}!")
    time.sleep(0.5)
    if roll_num == roll_num2:
        green("🄳 🄾 🅄 🄱 🄻 🄴 🅂 !")
        is_doubles = True
    else:
        is_doubles = False
    return is_doubles, roll_total

def prison(curr_pdata): ##sends someone to prison instantly
    sound("prisonsfx.mp3")
    red("Go to Jail. Go directly to jail, do not pass Go, do not collect 200$")
    time.sleep(1)
    slow_print("You are now in prison. You can either roll for doubles or use a jail free card if you have any.")
    time.sleep(1)
    curr_pdata["position"] = 10
    curr_pdata["jail"] = True

def jail_turn(curr_pdata, board_data, players_data):
    slow_print(f"{curr_pdata["name"]}, it's your JAIL turn!")
    if curr_pdata["jail_cards"] > 0:
        gold(f"You have {curr_pdata["jail_cards"]} Get out of jail free card(s).")
        blue("You can type 'use' to use a card. Otherwise, roll doubles py pressing enter.")
        choice = input().lower()
        clear_screen()
        printboard()
        if choice == "use":
            curr_pdata["jail_cards"] -= 1
            curr_pdata["jail"] = False
            curr_pdata["jail_turns"] = 0
            green("Card used! You are free to move next turn! Press enter to proceed.")
            input()
            return
    ## if no card:
    is_doubles, roll_total = roll()
    if is_doubles == True:
        green("Freedom! You rolled doubles!")
        curr_pdata["jail"] = False
        curr_pdata["jail_turns"] = 0
        move(roll_total, curr_pdata, board_data, players_data)
    else:
        curr_pdata["jail_turns"] += 1
        red(f"No doubles. You have spent {curr_pdata["jail_turns"]}/3 turns in jail.")
        if curr_pdata["jail_turns"] < 3:
            blue("Press enter to proceed.")
            input()
        else:
            red("You have spent 3 turns in jail. Paying 50$ to leave.")
            curr_pdata["money"] -= 50
            curr_pdata["jail"] = False
            curr_pdata["jail_turns"] = 0
            move(roll_total, curr_pdata, board_data, players_data)


def move(roll_total, curr_pdata, board_data, players_data): ## moves someone to a tile on the board
    old_pos = curr_pdata["position"]
    new_pos = (old_pos + roll_total) % 40
    curr_pdata["position"] = new_pos
    curr_tile = board_data[new_pos]
    tile_name = curr_tile["name"]
    tile_type = curr_tile["type"]
    if curr_pdata["position"] < old_pos and roll_total > 0:
        sound("money.mp3")
        green("You passed GO! Collected 200$.")
        pass_go(curr_pdata)
    blue(f"You are now on {tile_name}! Press enter to proceed.")
    input()
    if tile_type == "property" or tile_type == "railroad" or tile_type == "utility":
        utilcard = False
        prop_tile(roll_total, curr_pdata, curr_tile, players_data, board_data, utilcard)
    elif tile_type == "tax":
        orange(f"Tax square! Paying {curr_tile["price"]}$. Press enter to proceed.")
        input()
        curr_pdata["money"] -= curr_tile["price"]
    elif tile_type == "card":
        card_tile(curr_pdata, curr_tile, players_data, board_data, roll_total)
    else:
        special_tile(curr_pdata, curr_tile)

def prop_tile(roll_total, curr_pdata, curr_tile, players_data, board_data, utilcard): ## what happens when you land on a property tile
    owned = check_owned(curr_tile)
    if owned == True:
        if curr_tile["owner"] == curr_pdata["name"]:
            if curr_tile["type"] == "property":
                buy_house(curr_pdata, curr_tile)
        else:
            trespassing(roll_total, curr_pdata, curr_tile, players_data, board_data, utilcard)
    else:
        buy_prop(curr_pdata, curr_tile)

def buy_prop(curr_pdata, curr_tile): ## allows the player to buy the tile if its unowned
    if curr_pdata["money"] >= curr_tile["price"]:
        purple(f"Would you like to buy {curr_tile["name"]}?\nType 'buy' if you would like to purchase this tile.")
        choice = input().lower()
        if choice == "buy":
            curr_pdata["money"] -= curr_tile["price"]
            curr_tile["owner"] = curr_pdata["name"]
            sound("money.mp3")
            green(f"Success! You now own {curr_tile["name"]}!")
            if curr_tile["type"] == "railroad":
                curr_pdata["trains"] += 1
        else:
            orange("Property not bought.")
        light_blue("Press enter to proceed.")
        input()

def buy_house(curr_pdata, curr_tile):
    curr_houses = curr_tile["houses"]
    next_rent = curr_tile["rent_levs"][curr_houses + 1]
    if curr_houses >= 5:
        red("This property already has a hotel! You can't buy any more upgrades.")
        time.sleep(1)
    price = curr_tile["house_price"]
    if curr_pdata["money"] >= price:
        if curr_houses == 4:
            nextup = "hotel"
        else:
            nextup = "house"
        slow_print(f"Would you like to build a {nextup} for {price}$?")
        yellow(f"Your upgrade: {curr_tile["rent"]}$ --> {next_rent}$")
        slow_print(f"Type 'buy' if you would like to purchase a {nextup}.")
        choice = input().lower()
        if choice == "buy":
            curr_pdata["money"] -= price
            curr_tile["rent"] = curr_tile["rent_levs"][curr_tile["houses"]]
            curr_tile["houses"] += 1
            green(f"Success! You now have {curr_tile["houses"]} house(s) on this property.")
            time.sleep(2)

def check_owned(curr_tile): ## checks if a property tile is owned
    if curr_tile["owner"] == None:
        return False
    else:
        return True

def trespassing(roll_total, curr_pdata, curr_tile, players_data, board_data, utilcard): ## deducts money when they land on an owned tile
    fee = curr_tile["rent"]
    owner = curr_tile["owner"]
    red("!!Trespassing!!")
    if curr_tile["type"] == "utility":
        if util_check(board_data, curr_pdata) == True or utilcard == True:
            fee = roll_total * 10
        else:
            fee = roll_total * 4
    elif curr_tile["type"] == "property" and curr_tile["houses"] == 0:
        if full_set(curr_pdata, curr_tile, board_data) == True:
            fee *= 2
            orange("Full set bonus! Rent is doubled because the owner has the full set and has no houses on this tile!")
    slow_print(f"This property belongs to {owner}!")
    red(f"You must pay {fee}$ in rent.")
    curr_pdata["money"] -= fee
    for player in players_data:
        if player["name"] == owner:
            player["money"] += fee
            sound("money.mp3")
            gold(f"{owner} recieved {fee}$ from {curr_pdata["name"]} for trespassing!")
    blue("Press enter to proceed.")
    input()

def util_check(board_data, curr_pdata):
    if board_data[12]["owner"] == curr_pdata["name"] and board_data[28]["owner"] == curr_pdata["name"]:
        return True
    else:
        return False


def full_set(curr_pdata, curr_tile, board_data):
    if "color" not in curr_tile:
        return False
    tile_color = curr_tile["color"]
    color_set = []
    for tile in board_data:
        if "color" in tile:
            if tile["color"] == tile_color:
                color_set.append(tile)
    for i in color_set:
        if i["owner"] != curr_pdata["name"]:
            return False
    return True

def card_tile(curr_pdata, curr_tile, players_data, board_data, roll_total): ## determines what card they pull and if its from a comm chest or chance
    sound("card.mp3")
    if "Community Chest" in curr_tile["name"]:
        comm_chest(curr_pdata, players_data, board_data)
    else:
        chance(curr_pdata, curr_tile, players_data, board_data, roll_total)

def chance(curr_pdata, curr_tile, players_data, board_data, roll_total):
    card = random.randint(1, 6)
    position = curr_pdata["position"]
    slow_print("You drew a card from the chance deck...")
    if card == 1:
        yellow("Advance to GO! Collect 200$.")
        pass_go(curr_pdata)
        position = 0
        return
    elif card == 2:
        red("Advance to Bidoof Valley. Collect 200$ if you pass GO.")
        distance = (24 - curr_pdata["position"]) % 40
        move(distance, curr_pdata, board_data, players_data)
        return
    elif card == 3:
        blue("Advance to Hallfair.")
        curr_pdata["position"] = 37
        curr_tile = board_data[37]
        utilcard = False
        prop_tile(roll_total, curr_pdata, curr_tile, players_data, board_data, utilcard)
        return
    elif card == 4:
        orange("Advance to Paul Mall. Collect 200$ if you pass GO.")
        distance = (16 - curr_pdata["position"] + 40) % 40
        move(distance, curr_pdata, board_data, players_data)
        return
    elif card == 5 or card == 6:
        curr_position = curr_pdata["position"]
        if curr_position >= 0 and curr_position <= 10:
            near_ts = 5
        elif curr_position >= 11 and curr_position <= 20:
            near_ts = 15
        elif curr_position >= 21 and curr_position <= 30:
            near_ts = 25
        else:
            near_ts = 35
        orange("Advance to the nearest train station. If it is owned, pay double the rent!")
        curr_pdata["position"] = near_ts
        curr_tile = board_data[near_ts]
        utilcard = False
        prop_tile(roll_total, curr_pdata, curr_tile, players_data, board_data, utilcard)
        return
    elif card == 7:
        if curr_position >= 0 and curr_position < 20:
            near_ut = 12
        else:
            near_ut = 38
        yellow("Advance to the nearest utility. If owned, you must pay 10x your roll amount in $.")
        curr_pdata["position"] = near_ut
        curr_tile = board_data[near_ut]
        utilcard = True
        prop_tile(roll_total, curr_pdata, curr_tile, players_data, board_data, utilcard)
        return
    elif card == 8:
        gold("Bank pays you a dividend of 50$.")
        curr_pdata["money"] += 50
    elif card == 9:
        gold("You get a get out of jail free card!")
        curr_pdata["jail_cards"] += 1
    elif card == 10:
        orange("Go back 3 spaces!")
        distance = -3
        move(distance, curr_pdata, board_data, players_data)
    elif card == 11:
        prison(curr_pdata)
    elif card == 12: 
        red("Make general repairs on all your property. For each house pay 25$. For each hotel pay 100$")
        bill = 0
        for tile in board_data:
            if tile["owner"] == curr_pdata["name"]:
                if "houses" in tile:
                    house_num = tile["houses"]
                    if house_num == 5:
                        bill += 100
                    elif house_num > 0:
                        bill += (25 * house_num)
        curr_pdata["money"] -= bill
        red(f"You paid {bill}$ in repair fees!")
    elif card == 13:
        yellow("Speeding fine! Pay 15$.")
        curr_pdata["money"] -= 15
    elif card == 14:
        yellow("Take a trip to Tjiu Station. Collect $200 if you pass GO.")
        distance = (5 - curr_pdata["position"]) % 40
        move(distance, curr_pdata, board_data, players_data)
        return
    elif card == 15:
        gold("You have been elected Chairman of the Board. Pay each player 50$.")
        for player in players_data:
            if player != curr_pdata["name"]:
                slow_print(f"{curr_pdata["name"]} gave 50$!")
                player["money"] += 50
                curr_pdata["money"] -= 50
        red(f"You paid {(len(players_data) - 1) * 50} in total...")
    else:
        green("Your building loan matures. Collect 150$!")
        curr_pdata["money"] += 150
    time.sleep(3)

def comm_chest(curr_pdata, players_data, board_data):
    card = random.randint(1, 16)
    position = curr_pdata["position"]
    slow_print("You drew a card from the chance deck...")
    if card == 1:
        yellow("Advance to GO! Collect 200$.")
        pass_go(curr_pdata)
        position = 0
        return
    elif card == 2:
        magenta("Your video game 'Lankybox neighbourhood roleplay' was a success! Collect 200$.")
    elif card == 3:
        red("Doctor's Fee. Pay 50$.")
        curr_pdata["money"] -= 50
    elif card == 4:
        green("From sale of stock you get $50.")
        curr_pdata["money"] += 50
    elif card == 5:
        gold("You get a get out of jail free card!")
        curr_pdata["jail_cards"] += 1
    elif card == 6:
        prison(curr_pdata)
    elif card == 7:
        green("Holiday fund matures. Recieve 100$.")
        curr_pdata["money"] += 100
    elif card == 8:
        green("Income tax refund. Collect 20$.")
        curr_pdata["money"] += 20
    elif card == 9:
        magenta("It's your birthday! Collect 10$ from every player.")
        for player in players_data:
            if player["name"] != curr_pdata["name"]:
                slow_print(f"{player["name"]} gave 10$!")
                player["money"] -= 10
                curr_pdata["money"] += 10
        magenta(f"You recieved {(len(players_data) - 1) * 10}$ from everyone!")
    elif card == 10:
        blue("Holiday fund matures. Recieve 100$.")
        curr_pdata["money"] += 100
    elif card == 11:
        blue("Hospital fees. Pay 100$.")
        curr_pdata["money"] -= 100
    elif card == 12:
        orange("School fees. Pay 50$.")
        curr_pdata["money"] -= 50
    elif card == 13:
        green("Recieve 25$ of consulancy fees.")
        curr_pdata["money"] += 25
    elif card == 14:
        red("You are assessed for street repairs. Pay 40$ per house. 115$ per hotel.")
        bill = 0
        for tile in board_data:
            if tile["owner"] == curr_pdata["name"]:
                if "houses" in tile:
                    house_num = tile["houses"]
                    if house_num == 5:
                        bill += 115
                    elif house_num > 0:
                        bill += (40 * house_num)
        curr_pdata["money"] -= bill
        red(f"You paid {bill}$ in repair fees!")
    elif card == 15:
        purple("You win second prize in a beauty contest. Collect 10$.")
        curr_pdata["money"] += 10
    else:
        gold("You inherit 100$!")
        curr_pdata["money"] += 100
    time.sleep(3)

def pass_go(curr_pdata):
    curr_pdata["money"] += 200

def special_tile(curr_pdata, curr_tile): ## other tiles like free parking, go to jail and just visiting
    if curr_tile["name"] == "Go to JAIL":
        prison(curr_pdata)
    else:
        return

def check_win(playerlist, curr_pname): ##WIP
    if len(playerlist) == 1:
        yellow(f"CONGRATULATIONS, {curr_pname}! You are the winner of this monopoly game!!!")
        exit()

def check_bankrupt(curr_pdata):
    if curr_pdata["money"] < 0:
        red(f"{curr_pdata["name"]} went bankrupt!!")

def updateboard(curr_pdata, board_data, players_data, board):
    if curr_pdata["position"] == 10 and curr_pdata["jail"] == False:
        if board[4267] == " ":
            board[4267] = curr_pdata["icon"]
            board[4268] = ""
    else:
        board[4267] = " "
        board[4268] = " "
    if curr_pdata["position"] <= 9 and curr_pdata["position"] > 0:
        pass
def printboard(curr_pdata, board_data, players_data): ## keep in mind that there are 104 chars per line, 10 spaces wide per large square, 8 per small, 10 wide for side tiles
    #updateboard(curr_pdata, board_data, players_data, board) #🚢🟦 🐈🟧 🎩🟨 🐕🟩 🚙🟥 🐎🟪.   6th and 7th char for replacement for free parking 
    board = """
_______________________________________________________________________________________________________
|   Free   | Rathore| Chance |   Fu   | Bidoof | Farnham| Dream  |  Fox   |  Water |Fairplay|  Go to   |
|  Parking |  Park  |   ❓   |   St.  | Valley | 🚂 Sta.| Island |   St.  | Works💧|  Ave.  |   JAIL   |
|          |        |        |        |        |        |        |        |        |        |          |
|    🚗    |  220$  |        |  220$  |  240$  |  200$  |  260$  |  260$  |  150$  |  280$  |   🚔🚨   |
|__________|________|________|________|________|________|________|________|________|________|__________|
| Anthian  |                                                                                | Stickmin |
|    St.   |                                                                                |   Ave.   |
|   200$   |                                                                                |   300$   |
|__________|                                                                                |__________|
|  Snowdin |                                                                                | Solstice |
|   180$   |                                                                                |    Rd.   |
|          |                                                                                |   300$   |
|__________|                                      ●●●●                                      |__________|
|   Comm.  |                                      ●●●●                                      |  Comm.   |
|   Chest  |                                ●●●●●●●●●●●●●●●●                                |  Chest   |
|    🧰    |                             ●●●●●●●●●●●●●●●●●●●●●●●                            |    🧰    |
|__________|                          ●●●●●●●●●   ●●●●                                      |__________|
| Paul Mall|                         ●●●●         ●●●●                                      |  Stardew |
|   180$   |                        ●●●●●         ●●●●                                      |  Valley  |
|          |                        ●●●●●         ●●●●                                      |   320$   |
|__________|                         ●●●●         ●●●●                                      |__________|
| Dumfries |                          ●●●●●●●●●●●●●●●●●●●●●●●                               | McCreery |
| 🚂 Sta.  |                              ●●●●●●●●●●●●●●●●●●●●●●                            |  🚂 Sta. |
|   200$   |                                      ●●●●      ●●●●                            |   200$   |
|__________|                                      ●●●●      ●●●●●                           |__________|
|Alvin Ave.|                                      ●●●●      ●●●●●                           |  Chance  |
|   160$   |                       ●●●●           ●●●●      ●●●●●                           |    ❓    |
|          |                       ●●●●●●        ●●●●●●●●●●●●●●●                            |          |
|__________|                       ●●●●●●●●●●●●●●●●●●●●●●●●●●                               |__________|
|Lanky Lane|                           ●●●●●●●●●●●●●●●●●●                                   | Hallfair |
|   140$   |                                      ●●●●                                      |   400$   |
|          |                                      ●●●●                                      |          |
|__________|                                                                                |__________|
| Electric |                                                                                |Luxury Tax|
|  Comp.💡 |                                                                                | 💍(-100) |
|   150$   |                                                                                |          |
|__________|                                                                                |__________|
|  Box St. |                                                                                |  Langley |
|   140$   |                                                                                |   Inc.   |
|          |                                                                                |   400$   |
|__________|________________________________________________________________________________|__________|
|   |      |  Green |  Yoyle | Chance |  Baron |  Tjiu  | Income |  Birch |  Comm. |  Paper |          |
|   | JAIL |  Lake  |  Hotel |   ❓   |   Rd.  | 🚂 Sta.|  Tax   |  Ave.  | Chest  |   St.  |    GO!   |
|   |______|        |        |        |        |        |        |        |        |        |          |
| Visiting |  120$  |  100$  |        |  100$  |  200$  | (-200) |   60$  |   🧰   |   60$  |  (+200)  |
|__________|________|________|________|________|________|________|________|________|________|__________|
"""
    print(board)
def board_dinit():
    tile_data = [
    {"id": 0, "name": "GO", "type": "special", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 1, "name": "Paper Street", "type": "property", "price": 60, "color": "brown", "rent": 2, "house_price": 50, "rent_levs": [2, 10, 30, 90, 160, 250], "owner": None, "houses": 0},
    {"id": 2, "name": "Community Chest (South)", "type": "card", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 3, "name": "Birch Avenue", "type": "property", "price": 60, "color": "brown", "rent": 4, "house_price": 50, "rent_levs": [4, 20, 60, 180, 320, 450], "owner": None, "houses": 0},
    {"id": 4, "name": "Income Tax", "type": "tax", "price": 200, "rent": 0, "owner": None, "houses": 0},
    {"id": 5, "name": "Tjiu Station", "type": "railroad", "price": 200, "rent": 25, "owner": None, "houses": 0},
    {"id": 6, "name": "Baron Road", "type": "property", "price": 100, "color": "light_blue", "rent": 6, "house_price": 50, "rent_levs": [6, 30, 90, 270, 400, 550], "owner": None, "houses": 0},
    {"id": 7, "name": "Chance (South)", "type": "card", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 8, "name": "Yoyle Hotel", "type": "property", "price": 100, "color": "light_blue", "rent": 6, "house_price": 50, "rent_levs": [6, 30, 90, 270, 400, 550], "owner": None, "houses": 0},
    {"id": 9, "name": "Green Lake", "type": "property", "price": 120, "color": "light_blue", "rent": 8, "house_price": 50, "rent_levs": [8, 40, 100, 300, 450, 600], "owner": None, "houses": 0},
    {"id": 10, "name": "Just visiting", "type": "special", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 11, "name": "Box Street", "type": "property", "price": 140, "color": "pink", "rent": 10, "house_price": 100, "rent_levs": [10, 50, 150, 450, 625, 750], "owner": None, "houses": 0},
    {"id": 12, "name": "Electric Company", "type": "utility", "price": 150, "rent": 0, "owner": None, "houses": 0},
    {"id": 13, "name": "Lanky Lane", "type": "property", "price": 140, "color": "pink", "rent": 10, "house_price": 100, "rent_levs": [10, 50, 150, 450, 625, 750], "owner": None, "houses": 0},
    {"id": 14, "name": "Alvin Avenue", "type": "property", "price": 160, "color": "pink", "rent": 12, "house_price": 100, "rent_levs": [12, 60, 180, 500, 700, 900], "owner": None, "houses": 0},
    {"id": 15, "name": "Dumfries Station", "type": "railroad", "price": 200, "rent": 25, "owner": None, "houses": 0},
    {"id": 16, "name": "Paul Mall", "type": "property", "price": 180, "color": "orange", "rent": 14, "house_price": 100, "rent_levs": [14, 70, 200, 550, 750, 950], "owner": None, "houses": 0},
    {"id": 17, "name": "Community Chest (West)", "type": "card", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 18, "name": "Snowdin", "type": "property", "price": 180, "color": "orange", "rent": 14, "house_price": 100, "rent_levs": [14, 70, 200, 550, 750, 950], "owner": None, "houses": 0},
    {"id": 19, "name": "Anthian Street", "type": "property", "price": 200, "color": "orange", "rent": 16, "house_price": 100, "rent_levs": [16, 80, 220, 600, 800, 1000], "owner": None, "houses": 0},
    {"id": 20, "name": "Free Parking", "type": "special", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 21, "name": "Rathore Park", "type": "property", "price": 220, "color": "red", "rent": 18, "house_price": 150, "rent_levs": [18, 90, 250, 700, 875, 1050], "owner": None, "houses": 0},
    {"id": 22, "name": "Chance (North)", "type": "card", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 23, "name": "Fu Street", "type": "property", "price": 220, "color": "red", "rent": 18, "house_price": 150, "rent_levs": [18, 90, 250, 700, 875, 1050], "owner": None, "houses": 0},
    {"id": 24, "name": "Bidoof Valley", "type": "property", "price": 240, "color": "red", "rent": 20, "house_price": 150, "rent_levs": [20, 100, 300, 750, 925, 1100], "owner": None, "houses": 0},
    {"id": 25, "name": "Farnham Station", "type": "railroad", "price": 200, "rent": 25, "owner": None, "houses": 0},
    {"id": 26, "name": "Dream Island", "type": "property", "price": 260, "color": "yellow", "rent": 22, "house_price": 150, "rent_levs": [22, 110, 330, 800, 975, 1150], "owner": None, "houses": 0},
    {"id": 27, "name": "Fox Street", "type": "property", "price": 260, "color": "yellow", "rent": 22, "house_price": 150, "rent_levs": [22, 110, 330, 800, 975, 1150], "owner": None, "houses": 0},
    {"id": 28, "name": "Water Works", "type": "utility", "price": 150, "rent": 0, "owner": None, "houses": 0},
    {"id": 29, "name": "Fairplay Avenue", "type": "property", "price": 280, "color": "yellow", "rent": 24, "house_price": 150, "rent_levs": [24, 120, 360, 850, 1025, 1200], "owner": None, "houses": 0},
    {"id": 30, "name": "Go to JAIL", "type": "special", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 31, "name": "Stickmin Avenue", "type": "property", "price": 300, "color": "green", "rent": 26, "house_price": 200, "rent_levs": [26, 130, 390, 900, 1100, 1275], "owner": None, "houses": 0},
    {"id": 32, "name": "Solstice Road", "type": "property", "price": 300, "color": "green", "rent": 26, "house_price": 200, "rent_levs": [26, 130, 390, 900, 1100, 1275], "owner": None, "houses": 0},
    {"id": 33, "name": "Community Chest (East)", "type": "card", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 34, "name": "Stardew Valley", "type": "property", "price": 320, "color": "green", "rent": 28, "house_price": 200, "rent_levs": [28, 150, 450, 1000, 1200, 1400], "owner": None, "houses": 0},
    {"id": 35, "name": "McCreery Station", "type": "railroad", "price": 200, "rent": 25, "owner": None, "houses": 0},
    {"id": 36, "name": "Chance (East)", "type": "card", "price": 0, "rent": 0, "owner": None, "houses": 0},
    {"id": 37, "name": "Hallfair", "type": "property", "price": 350, "color": "dark_blue", "rent": 35, "house_price": 200, "rent_levs": [35, 175, 500, 1100, 1300, 1500], "owner": None, "houses": 0},
    {"id": 38, "name": "Luxury Tax", "type": "tax", "price": 100, "rent": 0, "owner": None, "houses": 0},
    {"id": 39, "name": "Langley Incorporated", "type": "property", "price": 400, "color": "dark_blue", "rent": 50, "house_price": 200, "rent_levs": [50, 200, 600, 1400, 1700, 2000], "owner": None, "houses": 0}
]
    return tile_data
    
## Text and sound
def slow_print(text): ##slow typing effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)
    print()

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")
    print("")

def sound(sfx):
    pygame.mixer.Sound(sfx).play()

## colors
def gold(string):
    rgb(string, 255, 204, 0)

def lime(string):
    rgb(string, 170, 255, 0)

def orange(string):
    rgb(string, 247, 144, 10)

def red(string):
    rgb(string, 255, 0, 0)

def blue(string):
    rgb(string, 0, 119, 188)

def light_blue(string):
    rgb(string, 138, 183, 255)

def yellow(string):
    rgb(string, 245, 205, 47)

def magenta(string):
    rgb(string, 207, 41, 168)

def green(string):
    rgb(string, 29, 219, 73)

def purple(string):
    rgb(string, 148, 3, 252)

main()
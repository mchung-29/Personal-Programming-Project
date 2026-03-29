## Personal Programming Project -- Martin Chung
import random, time, pygame, os, platform
from colorist import ColorRGB, BgColorRGB, rgb, bg_rgb
from time import sleep

def main(): 
    players_data, namelist, playercount = startup()
    game(players_data, namelist, playercount)

def startup(): ##setup before game starts
    clear_screen()
    #bgm() 
    intro()
    game_style = bot_player()
    if game_style == "multiplayer":
        playercount = get_pnum()
    elif game_style == "bots":
        playercount = 1
        bots = 3
    players_data, namelist = var_assign(playercount)
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
    slow_print("                     <PRESS ENTER TO PLAY>")
    input()

def bgm():  ## backgound music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.8) ## change volume if needed but I doubt it
    pygame.mixer.music.load("playlist.mp3")
    pygame.mixer.music.play(loops=-1) ## loops forever (-1)

def bot_player(): ##asks the player if they want to play multiplayer on one screen or vs bots
    clear_screen()
    lock = True
    while lock == True:
        orange("Would you like to play multiplayer or vs bots?")
        game_style = input().lower()
        if game_style == "multiplayer" or game_style == "bots":
            lock = False
        else:
            clear_screen()
            red("""Please enter either 'multiplayer' or 'bots'.\n____________________________________________________\n""")
    return game_style

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
            green("\n---ICON AND COLOUR SELECTION---")
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
                        "properties" : [],
                        "jail" : True,
                        "jail_cards" : 1,
                        "jail_turns" : 0,
                        "own_train_stats" : 0
                    }
                    players_data.append(pdata)
                    icon_valid = True
                else:
                    clear_screen()
                    red(f"\n {char} is already taken or not available.\nAvailable:{rem_op}")
            except ValueError:
                red(f"Please pick a number from the list.")
    clear_screen()
    slow_print("Selection Complete.") 
    time.sleep(1)
    slow_print("Let the game begin!")
    time.sleep(1)
    clear_screen()
    return players_data, namelist




def game(players_data, playerlist, playercount):
    board_data = board_dinit()
    game_running = True     ## will change when I implement checking for no remaining players
    while game_running == True:
        for i in range(playercount):
            curr_pdata = players_data[i]
            curr_pname = playerlist[i]
            turn(curr_pname, playercount, curr_pdata, board_data)
            check_win(playerlist)

def turn(curr_pname, playercount, curr_pdata, board_data): ##process of a turn
    doubles_count = 0
    turn_active = True
    while turn_active == True:
        clear_screen()
        printboard()
        if curr_pdata["jail"] == True:
            jail_turn(curr_pdata, board_data)
            break
        your_turn(curr_pname)
        is_doubles, roll_sum = roll()
        if is_doubles == True:
            doubles_count += 1
            if doubles_count == 3:
                orange("You are SPEEDING! Go to jail.")
                prison(curr_pdata)
                break
        move(roll_sum, curr_pdata, board_data)
        check_bankrupt(curr_pdata)
        if is_doubles == False:
            turn_active = False

def your_turn(curr_pname):
    lime(f"{curr_pname}, it's your turn!")

def roll(): ## getting numbers from rolling 2 dice
    magenta("Press enter to roll your dice.")
    input()
    slow_print("Rolling...")
    time.sleep(0.3)
    roll_num = random.randint(1,6)
    roll_num2 = random.randint(1,6)
    roll_total = roll_num + roll_num2
    green(f"You rolled a {roll_num} and a {roll_num2}!")
    time.sleep(1)
    if roll_num == roll_num2:
        green("🄳 🄾 🅄 🄱 🄻 🄴 🅂 !")
        is_doubles = True
    else:
        is_doubles = False
    return is_doubles, roll_total

def prison(curr_pdata): ##sends someone to prison instantly
    red("You do not pass GO or collect 200$.")
    time.sleep(1)
    slow_print("You are now in prison. You can either roll for doubles or use a jail free card if you have any.")
    time.sleep(1)
    curr_pdata["position"] = 10
    curr_pdata["jail"] = True

def jail_turn(curr_pdata, board_data):
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
            green("Card used! You are free to move!")
            turn()
            return
    ## if no card:
    is_doubles, roll_total = roll()
    if is_doubles == True:
        green("Freedom! You rolled doubles!")
        curr_pdata["jail"] = False
        curr_pdata["jail_turns"] = 0
        move(roll_total, curr_pdata, board_data)
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
            move(roll_total, curr_pdata, board_data)


def move(roll_sum, curr_pdata, board_data): ## moves someone to a tile on the board
    old_pos = curr_pdata["position"]
    new_pos = (old_pos + roll_sum) % 40
    curr_pdata["position"] = new_pos
    curr_tile = board_data[new_pos]
    tile_name = curr_tile["name"]
    blue(f"You are now on {tile_name}! Press enter to proceed.")
    input()
    if curr_pdata["position"] < old_pos:
        print("You passed GO! Collect 200$")
        curr_pdata["money"] += 200

def prop_tile(): ## what happens when you land on a property tile
    owned = check_owned()
    if owned == True:
        pass
    else:
        buy_option()

def buy_option():
    pass

def check_owned(): ## checks if a property tile is owned
    pass

def botactions():
    pass

def check_win(playerlist):
    if len(playerlist) == 1:
        win = True
        return win
    else:
        pass
    pass

def check_bankrupt(players_data):
    pass

def printboard():
    green("""
_______________________________________________________________________________________________________
|   Free   | Rathore| Chance |   Fu   | Bidoof | Farnham| Dream  |  Fox   |  Water |Fairplay|  Go to   |
|  Parking |  Park  |   ❓   |   St.  | Valley | 🚂 Sta.| Island |   St.  | Works💧|  Ave.  |   JAIL   |
|    🚗    |        |        |        |        |        |        |        |        |        |   🚔🚨   |
|          |  220$  |        |  220$  |  240$  |  200$  |  260$  |  260$  |  150$  |  280$  |          |
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
|   Paul   |                         ●●●●         ●●●●                                      |  Stardew |
|   Mall   |                        ●●●●●         ●●●●                                      |  Valley  |
|   180$   |                        ●●●●●         ●●●●                                      |   320$   |
|__________|                         ●●●●         ●●●●                                      |__________|
| Dumfries |                          ●●●●●●●●●●●●●●●●●●●●●●●                               | McCreery |
| 🚂 Sta.  |                              ●●●●●●●●●●●●●●●●●●●●●●                            |  🚂 Sta. |
|   200$   |                                      ●●●●      ●●●●                            |   200$   |
|__________|                                      ●●●●      ●●●●●                           |__________|
|   Alvin  |                                      ●●●●      ●●●●●                           |  Chance  |
|   Ave.   |                       ●●●●           ●●●●      ●●●●●                           |    ❓    |
|   160$   |                       ●●●●●●        ●●●●●●●●●●●●●●●                            |          |
|__________|                       ●●●●●●●●●●●●●●●●●●●●●●●●●●                               |__________|
|   Lanky  |                           ●●●●●●●●●●●●●●●●●●                                   | Hallfair |
|   Lane.  |                                      ●●●●                                      |   400$   |
|   140$   |                                      ●●●●                                      |          |
|__________|                                                                                |__________|
| Electric |                                                                                |Luxury Tax|
|  Comp.💡 |                                                                                | 💍(-100) |
|   150$   |                                                                                |          |
|__________|                                                                                |__________|
|   Box    |                                                                                |  Langley |
|   St.    |                                                                                |   Inc.   |
|   140$   |                                                                                |   400$   |
|__________|________________________________________________________________________________|__________|
|   |      |  Green |  Yoyle | Chance |  Baron |  Tjiu  | Income |  Birch |  Comm. |  Paper |          |
|   | JAIL |  Lake  |  Hotel |   ❓   |   Rd.  | 🚂 Sta.|  Tax   |  Ave.  | Chest  |   St.  |    GO    |
|   |______|        |        |        |        |        |        |        |        |        |  (+200)  |
| Visiting |  120$  |  100$  |        |  100$  |  200$  | (-200) |   60$  |   🧰   |   60$  |          |
|__________|________|________|________|________|________|________|________|________|________|__________|
""")

def board_dinit():
    tile_data = [
    {"id": 0, "name": "GO", "type": "special", "owner": None, "houses": 0},
    {"id": 1, "name": "Paper Street", "type": "property", "price": 60, "owner": None, "houses": 0},
    {"id": 2, "name": "Community Chest (South)", "type": "card", "owner": None, "houses": 0},
    {"id": 3, "name": "Birch Avenue", "type": "property", "price": 60, "owner": None, "houses": 0},
    {"id": 4, "name": "Income Tax", "type": "tax", "price": 200, "owner": None, "houses": 0},
    {"id": 5, "name": "Tjiu Station", "type": "property", "price": 200, "owner": None, "houses": 0},
    {"id": 6, "name": "Baron Road", "type": "property", "price": 100, "owner": None, "houses": 0},
    {"id": 7, "name": "Chance (South)", "type": "card", "owner": None, "houses": 0},
    {"id": 8, "name": "Yoyle Hotel", "type": "property", "price": 100, "owner": None, "houses": 0},
    {"id": 9, "name": "Green Lake", "type": "property", "price": 120, "owner": None, "houses": 0},
    {"id": 10, "name": "Just visiting", "type": "special", "owner": None, "houses": 0},
    {"id": 11, "name": "Box Street", "type": "property", "price": 140, "owner": None, "houses": 0},
    {"id": 12, "name": "Electric Company", "type": "utility", "price": 150, "owner": None, "houses": 0},
    {"id": 13, "name": "Lanky Lane", "type": "property", "price": 140, "owner": None, "houses": 0},
    {"id": 14, "name": "Alvin Avenue", "type": "property", "price": 160, "owner": None, "houses": 0},
    {"id": 15, "name": "Dumfries Station", "type": "property", "price": 200, "owner": None, "houses": 0},
    {"id": 16, "name": "Paul Mall", "type": "property", "price": 180, "owner": None, "houses": 0},
    {"id": 17, "name": "Community Chest (West)", "type": "card", "owner": None, "houses": 0},
    {"id": 18, "name": "Snowdin", "type": "property", "price": 180, "owner": None, "houses": 0},
    {"id": 19, "name": "Anthian Street", "type": "property", "price": 200, "owner": None, "houses": 0},
    {"id": 20, "name": "Free Parking", "type": "special", "owner": None, "houses": 0},
    {"id": 21, "name": "Rathore Park", "type": "property", "price": 220, "owner": None, "houses": 0},
    {"id": 22, "name": "Chance (North)", "type": "card", "owner": None, "houses": 0},
    {"id": 23, "name": "Fu Street", "type": "property", "price": 220, "owner": None, "houses": 0},
    {"id": 24, "name": "Bidoof Valley", "type": "property", "price": 240, "owner": None, "houses": 0},
    {"id": 25, "name": "Fanham Station", "type": "property", "price": 200, "owner": None, "houses": 0},
    {"id": 26, "name": "Dream Island", "type": "property", "price": 260, "owner": None, "houses": 0},
    {"id": 27, "name": "Fox Street", "type": "property", "price": 260, "owner": None, "houses": 0},
    {"id": 28, "name": "Water Works", "type": "utility", "price": 150, "owner": None, "houses": 0},
    {"id": 29, "name": "Fairplay Avenue", "type": "property", "price": 280, "owner": None, "houses": 0},
    {"id": 30, "name": "Go to JAIL", "type": "special", "owner": None, "houses": 0},
    {"id": 31, "name": "Stickmin Avenue", "type": "property", "price": 300, "owner": None, "houses": 0},
    {"id": 32, "name": "Solstice Road", "type": "property", "price": 300, "owner": None, "houses": 0},
    {"id": 33, "name": "Community Chest (East)", "type": "card", "owner": None, "houses": 0},
    {"id": 34, "name": "Stardew Valley", "type": "property", "price": 320, "owner": None, "houses": 0},
    {"id": 35, "name": "McCreery Station", "type": "property", "price": 200, "owner": None, "houses": 0},
    {"id": 36, "name": "Chance (East)", "type": "card", "owner": None, "houses": 0},
    {"id": 37, "name": "Hallfair", "type": "property", "price": 350, "owner": None, "houses": 0},
    {"id": 38, "name": "Luxury Tax", "type": "tax", "price": None, "owner": None, "houses": 0},
    {"id": 39, "name": "Langley Incorporated", "type": "property", "price": 400, "owner": None, "houses": 0}
]
    return tile_data
    
## Text-related stuff
def slow_print(text): ##slow typing effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)
    print()

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")
    print("")
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
    rgb(string, 50, 75, 168)

def light_blue(string):
    rgb(string, 138, 183, 255)

def yellow(string):
    rgb(string, 50, 75, 138)

def magenta(string):
    rgb(string, 207, 41, 168)

def green(string):
    rgb(string, 29, 219, 73)

##main()
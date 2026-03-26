## Personal Programming Project -- Martin Chung
import random, time, pygame, os, platform
from colorist import ColorRGB, BgColorRGB, rgb, bg_rgb
from time import sleep

def main(): 
    startup()
    turn()

def slow_print(text): ##slow typing effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def startup(): ##setup before game starts
    clear_screen()
    bgm() 
    intro()
    game_style = bot_player()
    if game_style == "multiplayer":
        players = get_pnum()
    elif game_style == "bots":
        players = 1
        bots = 3
    var_assign(players)

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")
    print("\n")

def intro(): ##prints the game title
    slow_print("Welcome user, to")
    gold("""████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝""")
    time.sleep(0.5)
    green("""
███╗░░░███╗░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░██╗░░░░░██╗░░░██╗
████╗░████║██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░╚██╗░██╔╝
██╔████╔██║██║░░██║██╔██╗██║██║░░██║██████╔╝██║░░██║██║░░░░░░╚████╔╝░
██║╚██╔╝██║██║░░██║██║╚████║██║░░██║██╔═══╝░██║░░██║██║░░░░░░░╚██╔╝░░
██║░╚═╝░██║╚█████╔╝██║░╚███║╚█████╔╝██║░░░░░╚█████╔╝███████╗░░░██║░░░
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░░░░░╚════╝░╚══════╝░░░╚═╝░░░
""")
    slow_print("                     <PRESS ENTER TO PLAY>")
    input()

def bgm():  ## backgound music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1) ## change volume if needed but I doubt it
    pygame.mixer.music.load("playlist.mp3")
    pygame.mixer.music.play(loops=-1) ## loops forever (-1)

def bot_player(): ##asks the player if they want to play multiplayer on one screen or vs bots
    lock = True
    while lock == True:
        game_style = input("Would you like to play multiplayer or vs bots?  ").lower()
        if game_style == "multiplayer" or game_style == "bots":
            lock = False
        else:
            clear_screen()
            red("""Please enter either 'multiplayer' or 'bots'.\n____________________________________________________\n""")
    return game_style

def get_pnum(): ## gets number of players
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
            if pnum <= 5:
                valid = True
            else:
                clear_screen()
                red("""Please enter a number below or equal to 5.
____________________________________________________\n""")
    return pnum

def var_assign(players):
    players_data = []
    rem_op = [1, 2, 3, 4, 5, 6]
    player_icons = ["🚢🟦", "🐈🟧", "🎩🟨","🐕🟩","🚙🟥","🐎🟪"]
    for i in range(players):
        clear_screen()
        valid = False
        while valid == False:
            green("---ICON AND COLOUR SELECTION---")
            gold("Choose a number to select your icon.")
            for indx in range(len(rem_op)):
                print(f"{rem_op[indx]}: {player_icons[indx]}")
            try:
                gold(f"Player {i+1}, enter your selection:")
                char = int(input())
                if char in rem_op:
                    curr_indx = rem_op.index(char)
                    chosen_num = rem_op.pop(curr_indx)
                    chosen_set = player_icons.pop(curr_indx)
                    pdata = {
                        "money" : 1500,
                        "position" : 0,
                        "icon" : chosen_set[0],
                        "color" : chosen_set[1],
                        "properties" : [],
                        "jail" : False,
                        "jail_card" : True,
                        "own_tr_stat" : 0
                    }
                    valid = True
                else:
                    red(f"\n {char} is already taken.\nAvailable:{rem_op}")
            except ValueError:
                red(f"Please pick a number from the list.")
    blue("SELECTION COMPLETE.")
    return players_data

def turn(): ##process of a turn
    roll()
    move()

def roll(): ## getting numbers from rolling 2 dice
    roll_num = random.randint(1,6)
    roll_num2 = random.randint(1,6)

def prison(): ##sends someone to prison instantly
    pass

def move(): ## moves someone to a tile on the board
    pass

def prop_tile(): ## what happens when you land on a property tile
    check_owned()

def check_owned(): ## checks if a property tile is owned
    pass
def botactions():
    pass
## colours
def gold(string):
    rgb(string, 255, 204, 0)

def lime(string):
    rgb(string, 170, 255, 0)

def orange(string):
    rgb(string, 247, 144, 10)

def red(string):
    rgb(string, 255, 0, 0)

def blue(string):
    rgb(string, 50, 75, 138)

def light_blue(string):
    rgb(string, 138, 183, 255)

def yellow(string):
    rgb(string, 50, 75, 138)

def magenta(string):
    rgb(string, 207, 41, 168)

def green(string):
    rgb(string, 29, 219, 73)
main()
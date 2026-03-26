## Personal Programming Project -- Martin Chung
import random, time, pygame, threading
from colorist import ColorRGB, BgColorRGB, rgb, bg_rgb  
from time import sleep

def main(): 
    startup()
    turn()

def startup(): ##setup before game starts
    bgm()
    intro()
    money_assign()
    game_style = bot_player()
    if game_style == "multiplayer":
        players = get_pnum()
        return players
    elif game_style == "bots":
        bots = 3
        return bots
def gold(string):
    rgb(string, 255, 204, 0)

def green(string):
    rgb(string, 170, 255, 0)

def intro(): ##prints the game title
    gold("Welcome user, to")
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

def bgm():  ## backgound music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1) ## change volume if needed but I doubt it
    pygame.mixer.music.load("playlist.mp3")
    pygame.mixer.music.play(loops=-1) ## loops forever (-1)

def bot_player(): ##asks the player if they want to play multiplayer on one screen or vs bots
    lock = True
    while lock == True:
        game_style = input("Would you like to play multiplayer or vs bots?\n").lower()
        if game_style == "multiplayer" or game_style == "bots":
            lock = False
        else:
            rgb("""Please enter either 'multiplayer' or 'bots'.\n____________________________________________________\n""", 255, 0, 0)
    return game_style

def get_pnum(): ## gets number of players
    valid = False
    while valid == False:
        try: 
            rgb("How many people will be playing? (Max 5)", 255, 204, 0)
            pnum = int(input())
        except ValueError:
            rgb("""Please enter a number below or equal to 5.
____________________________________________________\n""", 255, 0, 0)
        else:
            if pnum <= 5:
                valid = True
            else:
                rgb("""Please enter a number below or equal to 5.
____________________________________________________\n""", 255, 0, 0)
    return pnum

def money_assign():
    p1m = p2m = p3m = p4m = 1500
    print(p3m)
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
main()
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
    players = get_pnum()

def intro(): ##prints the game title
    rgb("""Welcome user, to
████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝""", 255, 204, 0), rgb("""
███╗░░░███╗░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░██╗░░░░░██╗░░░██╗
████╗░████║██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗██║░░░░░╚██╗░██╔╝
██╔████╔██║██║░░██║██╔██╗██║██║░░██║██████╔╝██║░░██║██║░░░░░░╚████╔╝░
██║╚██╔╝██║██║░░██║██║╚████║██║░░██║██╔═══╝░██║░░██║██║░░░░░░░╚██╔╝░░
██║░╚═╝░██║╚█████╔╝██║░╚███║╚█████╔╝██║░░░░░╚█████╔╝███████╗░░░██║░░░
╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░░░░░╚════╝░╚══════╝░░░╚═╝░░░
""", 170, 255, 0)

def bgm():  ## backgound music
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1) ## change volume if needed but I doubt it
    pygame.mixer.music.load("playlist.mp3")
    pygame.mixer.music.play()

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

main()
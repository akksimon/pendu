# config: utf-8

import sys, os, platform
from includes.pendu import *
import player_list as playerlist
from includes.from_file_to_game import *
from includes.show_hanged import *


players = get_player_list()
playerlist.print_player_list(players)
players = playerlist.create_player(players)
print("Apres ajout du joueur on relis le fichier")
playerlist.print_player_list(players)

distrib = platform.system()
playing = bool(show_menu())

# Boucle principale du jeu ...

while playing:
    secret_word = get_secret_word()
    pendu(secret_word)
    if distrib == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    playing = bool(show_menu())
sys.exit("\n\t*** See you soon ! ***\n")


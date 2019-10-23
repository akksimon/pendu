# config: utf-8

import sys, os, platform
from includes.pendu import *
import player_list as playerlist

players = [{"nom": "simon", "score": 22}, {"nom": "mohammed", "score": 23}, {"nom": "romane", "score": 1000}]

playerlist.create_player(players)
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

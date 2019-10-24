# config: utf-8

import sys, os, platform
from includes.pendu import *
import player_list as playerlist
from includes.from_file_to_game import *
from includes.show_hanged import *
import copy

#playing = bool(show_menu())

# Boucle principale du jeu ...



while True:
    playerlist.menu()
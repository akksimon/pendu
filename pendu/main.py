# config: utf-8

import sys, os, platform
from includes.pendu import *


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

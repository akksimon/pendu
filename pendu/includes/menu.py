# config: utf-8

import player
import sys

def main_menu():
    
    # - Menu principal du jeu -

    print("\t\n\t\t===  Main menu ===\n\t")
    print("\t|  (1) : Créer nouveau joueur\n\t|  (2) : Afficher liste des joueurs\n\t|  (3) : Lancer une partie\n\t|  (4) : Quitter")
    choice = input("\nVotre choix --> ")
    if choice == "1":
        player.create_player()
        main_menu()
    elif choice == "2":
        player.print_player_list()
        main_menu()
    elif choice == "3":
        player.check_player()
    elif choice == "4":
        sys.exit("\n\n\t\t=== See you soon ===\n\n")
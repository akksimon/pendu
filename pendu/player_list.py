# config: utf-8

import copy, json
from includes.from_file_to_game import *

import sys, os, platform
from includes.pendu import *
import player_list as playerlist
from includes.from_file_to_game import *
from includes.show_hanged import *
import copy

def print_player_list():
    players = get_player_list()
    # Affichage de la liste des joueurs
    print("\t\t\n\n===  Liste des joueurs  ===\n")

    for i, v in players.items():
        print(i, " => ", v)
    print("_______________________________________________________")

def create_player():

    players = get_player_list()
    newplayer = input("veuiller choisir un nom de joueur : ")
    if newplayer in players:
        print("Joueur déjà existant...")
        create_player()

    else:
        players[newplayer]={'score': []}
        put_new_player(players)
        print("Bienvenue ", newplayer)


    # players_list = copy.deepcopy(players)
    # Vérification de la présence du joueur
    # for i in players_list.keys():
    #     if (newplayer == i):
    #         print("Joueur déjà existant...")
    #         create_player()
    # players[newplayer] = {"score":[]}
    # put_new_player(players)
    # print("Bienvenue ", newplayer)


def check_player():

    players = get_player_list()
    player = input("Nom du joueur : ")
    #players_list = copy.deepcopy(players)
    # Vérification de la présence du joueur
    for i in players.keys():
        if (player == i):
            go_pendu(player)
    print("Le joueur n'existe pas, veuillez créer un joueur")
    create_player()



def go_pendu(player):
    distrib = platform.system()
    playing = bool(show_menu(player))
    while playing:
        secret_word = get_secret_word()
        pendu(secret_word)
        if distrib == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        playing = bool(show_menu(player))
    menu()

def menu():
    print("\t\t\n===  Main menu ===\n")
    print("\t(1) : Créer nouveau joueur\n\t(2) : Afficher liste des joueurs\n\t(3) : Lancer une partie\n\t(4) : Quitter")
    choice = input("\nVotre choix : ")
    if choice == "1":
        playerlist.create_player()
        menu()
    elif choice == "2":
        playerlist.print_player_list()
        menu()
    elif choice == "3":
        playerlist.check_player()
    elif choice == "4":
        sys.exit("ciao bize")

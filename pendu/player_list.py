# config: utf-8

import copy, json
from includes.from_file_to_game import *

def print_player_list(players):
    # Affichage de la liste des joueurs
    print("\t\t\n\n===  Liste des joueurs  ===\n")

    for i, v in players.items():
        print(i, " => ", v)
    print("_______________________________________________________")

def create_player(players):
    newplayer = input("veuiller saisir un nom : ")

    players_list = copy.deepcopy(players)
    # Vérification de la présence du joueur
    for i in players_list.keys():
        if (newplayer == i):
            print("Joueur déjà existant...")
            create_player(players)
    players[newplayer] = {"score":[]}
    put_new_player(players)
# config: utf-8

from includes.pendu import *

def print_player_list():

    # - Affichage de la liste des joueurs -

    print("\t\t\n\n===  Liste des joueurs  ===\n")
    players = get_player_list()
    for i, v in players.items():
        print(i, " --> ", v)
    print("_______________________________________________________")

def create_player():

    # - Création d'un nouveau joueur après vérification qu'il n'existe pas -

    players = get_player_list()
    newplayer = input("\n\tVeuiller choisir un nom de joueur --> ")
    if newplayer in players:
        print("\n\tJoueur déjà existant...")
        create_player()

    else:
        players[newplayer]={'score': []}
        put_new_player(players)
        print("\n\t*** Bienvenue ", newplayer.capitalize(), " ! ***")


def check_player():

    # - Vérification de l'existance du joueur dans le fichier 'playerliste.json' -

    players = get_player_list()
    player = input("\n\n\tNom du joueur --> ")

    for i in players.keys():
        if (player == i):
            go_pendu(player)
    print("\n\tDésolé, le joueur n'existe pas, veuillez créer un nouveau joueur")
    create_player()



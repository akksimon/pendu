# config: utf-8

import random, json, sys


""" Module de récupération de données via fichiers '.txt' ou '.json' (Liste des mots à deviner + Liste des joueurs + scores )
"""

def get_secret_word():

    # - Récupération aléatoire du mot à deviner dans le fichier 'listemystere' -
    
    try:
        # Ouverture du fichier 'listemystere' en lecture seule
        with open("listemystere.txt", "r") as file:
            words_list = file.readlines()
    except:
        sys.exit("Erreur : le fichier 'listemystere' est introuvable...")

    secret_word = random.choice(words_list)
    secret_word = secret_word.rstrip('\n')
    secret_word = secret_word.upper()

    # On retourne le mot mystere choisi aléatoirement dans la liste de mots du fichier
    return secret_word


def get_player_list():

    # Récupération de la liste des joueurs dans le fichier 'playerlist.json - 
    
    try:
        # Ouverture du fichier ' .... ' en lecture seule
        with open('playerlist.json', 'r') as file:
            return json.load(file)
    except:
        sys.exit("Erreur de chargement de la liste des joueurs")


def put_new_player(newplayer):

    # Ajout d'un nouveau joueur à la liste 'playerlist.json -
    
    try:
        # Ouverture du fichier en lecture / écriture pour l'ajout du nouveau joueur 'newplayer'
        with open("playerlist.json", "w") as file:
            json.dump(newplayer, file)
    except:
        sys.exit("Erreur d'ajout du nouveau joueur à la liste")



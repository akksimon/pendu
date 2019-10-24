# config: utf-8

import random, json

def get_secret_word():
    """ Récupération aléatoire du mot à deviner dans le fichier 'listemystere'
    """
    try:
        # Ouverture du fichier 'listemystere' en lecture seule
        with open("listemystere.txt", "r") as file:
            words_list = file.readlines()
    except:
        sys.exit("Erreur : le fichier 'listemystere' est introuvable...")

    secret_word = random.choice(words_list)
    secret_word = secret_word.rstrip('\n')
    secret_word = secret_word.upper()

    return secret_word

def get_player_list():
    """ Récupération de la liste des joueurs dans le fichier 'playerlist.json
    """
    try:
        # Ouverture du fichier ' .... ' en lecture seule
        with open('playerlist.json', 'r') as file:
            return json.load(file)
    except:
        sys.exit("Erreur de chargement de la liste des joueurs")

def put_new_player(newplayerlist):
    """ Ajout d'un nouveau joueur à la liste 'playerlist.json
    """
    try:
        # Ouverture du fichier en lecture / écriture
        with open("playerlist.json", "w") as file:
            json.dump(newplayerlist, file)
    except:
        sys.exit("Erreur d'ajout du nouveau joueur à la liste")

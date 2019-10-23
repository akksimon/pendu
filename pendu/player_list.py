# config: utf-8

def print_player_list():
    print("\t\t\n\n===  Liste des joueurs  ===\n")
    players = [{"nom": "simon", "score": 22}, {"nom": "mohammed", "score": 23}, {"nom": "romane", "score": 1000}]
    players.append({"nom":"zozo", "score":0})

    for i in players:
        print("[", i["nom"], "]", "\tscore ==>\t", i["score"])

    print("_______________________________________________________")

def create_player():
    newplayer = input("veuiller saisir un nom")
    for i in players:
        if (newplayer in i["nom"]):
            print ("joueur existant")
            create_player()
        else:
            players.append({"nom":newplayer, "score":0})
            print("bienvenue")
# config: utf-8

def print_player_list(players):
    print("\t\t\n\n===  Liste des joueurs  ===\n")
    players.append({"nom":"zozo", "score":0})

    for i in players:
        print("[", i["nom"], "]", "\tscore ==>\t", i["score"])

    print("_______________________________________________________")

def create_player(players):
    newplayer = input("veuiller saisir un nom")
    for i in players:
        if (newplayer in i["nom"]):
            print ("joueur existant")
            create_player(players)
        else:
            players.append({"nom":newplayer, "score":0})
            print("bienvenue")
            break
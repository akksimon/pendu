# config: utf-8

def print_player_list():
    players = [{"nom": "simon", "score": 22}, {"nom": "mohammed", "score": 23}, {"nom": "romane", "score": 1000}]
    players.append({"nom":"zozo", "score":0})

    for i in players:
        print(i["nom"], i["score"])
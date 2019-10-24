# config: utf-8

import random, time, os, platform, sys
from includes.menu import *
from includes.show_hanged import *
from includes.check_letter import *
from includes.from_file_to_game import *

""" Module principal pour le jeu du Pendu.
"""


def pendu(secret_word):
	"""Fonction principale du jeu
	"""
	# Définition des variables pour le fonctionnement du jeu

	player_word = []
	alive = 0
	count = 0
	distrib = platform.system()

	# '- - - - - - - -'
	for i in secret_word:
		player_word.append("-")
	secret_word = list(secret_word)			# Repassage en liste pour faciliter le parcours

	while player_word != secret_word and alive <= 9:
		show_hang(alive)
		print("\n\t\tQuel est le mot secret ? ", " ".join(player_word))
		letter = input("\t\tEntrez une lettre --> ")
		letter = letter.upper()
		if check_letter(secret_word, player_word, letter):
			print("\t> Yes !")
			player_word = add_letter(secret_word, player_word, letter)
		else:
			print("\t> Non pas de ", letter)
			alive += 1
		count += 1
		print("\t\tNombre d'essais restants :", 10 - int(alive), "\n")

	if alive < 9:
		print("\n\tBravo ! Vous avez gagné en {} coups !".format(count))

	else:
		if distrib == "Windows":
			os.system("cls")
		else:
			os.system("clear")
			print("\n\n\n\t\t***  ", end = ' ')
			message = "Game Over..."
			for i in message:
				print(i, end = '')
				#time.sleep(0.25)
			print("  ***\n\n")
			show_hang(10)

	time.sleep(4)

def go_pendu(player):
    
    # - Chargement + lancement du jeu [Récupération du mot mystère + lancement de la fonction 'pendu'] -

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
    main_menu()
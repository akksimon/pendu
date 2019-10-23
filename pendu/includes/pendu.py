# config: utf-8

import random, time, os, platform, sys

"""Module pour le jeu du Pendu.
"""

def show_hang(index = 0):
	hanged = (
			"\t\t                 \n\t\t                        \n\t\t                      \n\t\t                   \n\t\t_________________\n",
			"\t\t|                 \n\t\t|                \n\t\t|                  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|                \n\t\t|                  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|                  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|               |  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|\\\n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|\\\n\t\t|              /  \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|\\\n\t\t|              /\\\n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|                  \n\t\t|                 \n\t\t_____ SOON DEAD__\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|                  \n\t\t|                 \n\t\t_____ YOU DIED___\n",
	)
	#	count = 0
	#	for i in hanged:
	#	print(count)
	#	print(i)
	#	count += 1

	print(hanged[index])

def get_secret_word():
	""" Récupération aléatoire du mot à deviner dans le fichier 'listemystere'
	"""
	try:
		with open("listemystere.txt", "r") as file:
			words_list = file.readlines()
	except:
		sys.exit("Erreur : le fichier 'listemystere' est introuvable...")
            
	secret_word = random.choice(words_list)
	secret_word = secret_word.rstrip('\n')
	secret_word = secret_word.upper()

	return secret_word

def show_menu():
	"""Main menu
    """
	print("\n\n\t\t==========  Bienvenue sur le jeu du pendu !  ==========\n\n")
	print("\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|\\\n\t\t|              /\\\n\t\t_________________\n")
	return int(input("\t\t(1) : Jouer\n\t\t(0) : Quitter\n\n\t\tChoix : "))

def check_letter(secret_word, player_word, letter):
	"""Vérification de la présence de la lettre dans le mot mystère
        On check aussi que le mot n'a pas déjà été demandé
    """
	for i in range(len(secret_word)):
		j = secret_word[i]
		if secret_word[i] == letter and j not in player_word:
			return True
	return False

def add_letter(secret_word, player_word, letter):
	"""Mise à jour du mot du joueur avec la lettre nouvellement trouvée
    """
	for i in range(len(secret_word)):
		if secret_word[i] == letter:
			player_word[i] = letter
	return player_word

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
		letter = input("\t\tEntrez une lettre : ")
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

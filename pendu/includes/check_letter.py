# config: utf-8

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










# config: utf-8

def show_hang(index = 0):
    	
	# - Affichage du 'dessin du pendu' lors de la partie au fil des coups - 
	hanged = (
			"\t\t                 \n\t\t                        \n\t\t                      \n\t\t                   \n\t\t_________________\n",
			"\t\t|                 \n\t\t|                \n\t\t|                  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|                \n\t\t|                  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|                  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|               |  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|  \n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|\\\n\t\t|                 \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|\\\n\t\t|              / \n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|\\\n\t\t|              /\\\n\t\t_________________\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|                  \n\t\t|                 \n\t\t_____ SOON DEAD__\n",
			"\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|                  \n\t\t|                 \n\t\t_____ YOU DIED___\n",
	)
	print(hanged[index])

def show_menu(player):
	print("\n\n\t\t==========  Bienvenue ", player, "sur le jeu du pendu !  ==========\n\n")
	print(show_hang(8))
	return int(input("\t\t(1) : Jouer\n\t\t(0) : Retour menu principal\n\n\t\tChoix : "))


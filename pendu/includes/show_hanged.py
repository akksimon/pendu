# config: utf-8


def show_menu():
    """Main menu of the game
    """
    print("\n\n\t\t==========  Bienvenue sur le jeu du pendu !  ==========\n\n")
    print("\t\t|'''''''''''''''|\n\t\t|               O\n\t\t|              /|\\\n\t\t|              /\\\n\t\t_________________\n")
    return int(input("\t\t(1) : Jouer\n\t\t(0) : Quitter\n\n\t\tChoix : "))

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

tab = [[" "," "," "],[" "," "," "],[" "," "," "]]
memoX = []
memoO = []
velha = 0

def print_tab(): # Imprime o tabuleiro e coordenadas

	print("  0   1   2")
	print("0", tab[0][0], "|", tab[0][1], "|", tab[0][2])
	print(" ---+---+---")
	print("1", tab[1][0], "|", tab[1][1], "|", tab[1][2])
	print(" ---+---+---")
	print("2", tab[2][0], "|", tab[2][1], "|", tab[2][2])

def endgame():
	global velha
	print("Jogadas de X:\n", memoX)
	print("Jogadas de O:\n", memoO)

	a = int(input("\nDigite 1 para começar novamente ou 0 para sair: "))
	if(a == 1):
		for i in range(3):
			for j in range(3):
				tab[i][j] = " "

		del memoX[:]
		del memoO[:]
		velha = 0
		print_tab()
		jogadaX()
	else:
		exit()

def check_end(a):
		if(tab[0][0] == a and tab[0][1] == a and tab[0][2] == a):
			print("!!! Jogador %s é o vencedor !!! \n" % (a))
			endgame()
		elif(tab[1][0] == a and tab[1][1] == a and tab[1][2] == a):
			print("!!! Jogador %s é o vencedor !!! \n" % (a))
			endgame()
		elif(tab[2][0] == a and tab[2][1] == a and tab[2][2] == a):
			print("!!! Jogador %s é o vencedor !!! \n" % (a))
			endgame()
		elif(tab[0][0] == a and tab[1][0] == a and tab[2][0] == a):
			print("!!! Jogador %s é o vencedor !!! \n" % (a))
			endgame()
		elif(tab[0][1] == a and tab[1][1] == a and tab[2][1] == a):
			print("!!! Jogador %s é o vencedor !!! \n" % (a))
			endgame()
		elif(tab[0][2] == a and tab[1][2] == a and tab[2][2] == a):
			print("!!! Jogador %s é o vencedor !!! \n" % (a))
			endgame()
		elif(tab[0][0] == a and tab[1][1] == a and tab[2][2] == a):
			print("!!! Jogador %s é o vencedor !!! \n" % (a))	
			endgame()
		elif(tab[0][2] == a and tab[1][1] == a and tab[2][0] == a):
			print("!!! Jogador %s é o vencedor !!! \n" % (a))
			endgame()
		elif(velha >= 9):
			print("Deu velha :/")
			endgame()

def jogadaX(): #  Ação do Jogaor X
	global velha
	global memoX
	a = int(input("Jogador 1 - Escolha uma linha para X: "))
	b = int(input("Jogador 1 - Escolha uma coluna para X: "))
	if (a > 3 or a < 0 or b > 3 or b < 0):
		print("Coordenadas inválidas, jogue novamente.")
		jogadaX()
	elif (tab[a][b] == "O" or tab[a][b] == "X"):
		print("Campo já escolhido, escolha outro.")
		jogadaX()
	
	else:
		tab[a][b] = "X"
		memoX.extend([(a, b)]) #insere coordenada na lista de movimentos
		velha = velha+1 # verificador de velha
		print_tab()
		check_end("X")
		jogadaO()

def jogadaO(): # Ação do Jogador Os
	global velha
	global memoO
	a = int(input("Jogador 2 - Escolha uma linha para O: "))
	b = int(input("Jogador 2 - Escolha uma coluna para O: "))
	if (a > 3 or a < 0 or b > 3 or b < 0):
		print("Coordenadas inválidas, jogue novamente.")
		jogadaO()
	
	elif (tab[a][b] == "O" or tab[a][b] == "X"):
		print("Campo já escolhido, escolha outro.")
		jogadaO()
	
	else:
		tab[a][b] = "O"
		velha = velha+1
		memoO.extend([(a, b)])
		print_tab()
		check_end("O")
		jogadaX()

print("Jogo da velha")
print_tab()
jogadaX()

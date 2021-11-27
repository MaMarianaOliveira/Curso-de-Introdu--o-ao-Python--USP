def partida():

    n = int (input("	Quantas peças?: "))
    m = int (input("	Qual o limite de peças por jogada?: "))

    is_computer_turn = False

    if n % (m + 1) == 0:
        is_computer_turn = False
        print("		Você começa")
    elif n % (m + 1) != 0:
        is_computer_turn = True
        print("		Computador começa")
             
    
    while n > 0:
        
        if (is_computer_turn):
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("	Computador tirou", jogada, "peças")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("	Você tirou", jogada,"peças")
                
        n = n - jogada
            
        print("		Restam apenas", n,"peça(s) no tabuleiro")

    
    if is_computer_turn:
        print("		Você ganhou!")
        return 1
    else:
        print("		Computador ganhou!")
        return 0





def usuario_escolhe_jogada(n,m):

	

	jogada = 0
	
	while jogada == 0:
		jogada = int(input("		Quantas peças você irá tirar?"))
		if jogada > n or jogada < 1 or jogada > m :
			jogada = 0
			print("		Ops!Jogada inválida! Tente de novo!")
	return jogada

def computador_escolhe_jogada(n,m):

	
	if n <= m :
		return n 
	else:
		quantia = n % ( m+1)
		if quantia > 0 :
			return quantia

	return m 


def campeonato():

	usuario = 0 
	computador = 0
	rodada = 1
	qt_partida = 1
	
	
	while qt_partida < 4 :
		print("		**** Rodada ", rodada,"****")
		vencedor = partida()
		
		if vencedor == 1:
			usuario = usuario + 1
		else:
			computador = computador + 1 
		
		qt_partida = qt_partida + 1
		rodada = rodada + 1 


	print ("	Fim de Jogo! O computador ganhou!	")
	print("")
	print(" 	**** Final do campeonato! ****"	)
	print(" 	Placar final : Você {} x  {} Computador".format(usuario, computador))


tipo_jogo = 0 

while tipo_jogo == 0 :
	print ("		Bem vindo ao jogo NIM! Escolha:		")
	print("")
	print("		1 - Para jogar uma partida isolada!	")
	print("		2 - Para jogar um campeonato!	")

	tipo_jogo = int(input("		Qual é sua opção? 	"))
	print("")

	if tipo_jogo == 1 :
		print("		Você escolheu partida isolada!		")
		partida()
		break
	elif tipo_jogo == 2:
		print("		Você escolheu um campeonato!	")
		campeonato()
		break
	else:
		print("		Opção inválida!	")
		tipo_jogo = 0





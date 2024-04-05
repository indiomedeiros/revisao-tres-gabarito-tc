from random import randint #Importação de uma função nova para o código. Pesquise sobre ela!

def jogar ():
    
    opcao_de_continucacao = True
    while (opcao_de_continucacao == True):

        opcao = ["Pedra", "Papel", "Tesoura"]
        print("Escolha uma opcao para jogar: ")
        print("[0]", opcao[0])
        print("[1]", opcao[1])
        print("[2]", opcao[2])
        
        escolha_do_jogador = int(input("Digite sua escolha:"))
        escolha_do_computador = randint(0,2)

        if(escolha_do_jogador > 2 or escolha_do_jogador < 0):
            print("-==============================")
            print("Entrada inválida!")
            print("-==============================")

        else:
            print("JO")
            print("KEN")
            print("POOH!!!")

            print("-====================")
            print("O computador escolheu:", opcao[escolha_do_computador])
            print("O jogador escolheu:", opcao[escolha_do_jogador])
            print("-====================")
            
            if (escolha_do_computador  == 0):
                    if escolha_do_jogador == 0:
                        print("Empate!")
                    elif (escolha_do_jogador == 1):
                        print("Jogador venceu")
                    elif (escolha_do_jogador == 2):
                        print("Computador venceu")
                    else:
                        print("Operacao invalida")

            elif (escolha_do_computador  == 1):
                    if escolha_do_jogador == 0:
                        print("Computador venceu")
                    elif (escolha_do_jogador == 1):
                        print("Empate!")
                    elif (escolha_do_jogador == 2):
                        print("Jogador venceu")
                    else:
                        print("Operacao invalida")

            elif (escolha_do_computador == 2):
                    if (escolha_do_jogador == 0):
                        print("Jogador venceu")
                    elif (escolha_do_jogador == 1):
                        print("Computador venceu")
                    elif (escolha_do_jogador == 2):
                        print("Empate!")
                    else:
                        print("Operacao invalida")
            else:
                print("Operacao invalida")
                
            decisao = input("Deseja continuar jogando? [s/n]")
            if (decisao == "n"):
                print("Obrigado por jogar!")
                play = False
            else:
                print("-==============================")

jogar()


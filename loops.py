def contar_ate_vinte():
#Exemplo com for
#   for numero in range(21):
#     print(numero)

#Exemplo com while
  contador = 0
  while(contador < 21):
      print(contador)
      contador = contador + 1

contar_ate_vinte()

def contagem_ate_numero_digitado():
  numero_do_usuario = int(input("Digite um número: "))

#Exemplo com for
#   for i in range(numero_do_usuario + 1):
#     print(i)

#Exemplo com while
  contador = 0
  while(contador <= numero_do_usuario):
    print(contador)
    contador = contador + 1

contagem_ate_numero_digitado()

def criar_tauada_adicao():
    #Exemplo com for
    # for i in range(1, 11):
    #     soma = 2 + i
    #     print("2", "+" ,i, "=", soma)

    #Exemplo com while
    contador = 1
    while(contador < 11):
        soma = 2 + contador
        print("2", "+" ,contador, "=", soma)
        contador = contador + 1

criar_tauada_adicao()

def criar_tabuada_multiplicacao():
    numero_do_usuario = int(input("Digite um número inteiro: "))
   #Exemplo com for
    # for i in range(1, 11):
    #     multiplicacao = numero_do_usuario * i
    #     print(numero_do_usuario, "x" ,i, "=", multiplicacao)

    #Exemplo com while
    contador = 1
    while(contador < 11):
        multiplicacao = numero_do_usuario * contador
        print(numero_do_usuario, "x" ,contador, "=", multiplicacao)
        contador = contador + 1


criar_tabuada_multiplicacao()
   
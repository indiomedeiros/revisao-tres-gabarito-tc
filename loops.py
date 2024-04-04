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